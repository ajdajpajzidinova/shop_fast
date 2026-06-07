from fastapi import APIRouter, HTTPException, Depends
from shop_app.database.db import SessionLocal
from shop_app.database.models import Product
from shop_app.database.schema import ProductSchema, ProductCreateSchema
from sqlalchemy.orm import Session
from typing import List


product_router = APIRouter(prefix='/product', tags=['Product'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@product_router.post('/', response_model=ProductSchema)
async def create_product(product: ProductCreateSchema, db: Session = Depends(get_db)):
    product_db = Product(**product.dict())
    db.add(product_db)
    db.commit()
    db.refresh(product_db)
    return product_db


@product_router.get('/', response_model=List[ProductSchema])
async def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@product_router.get('/{product_id}/', response_model=ProductSchema)
async def detail_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(detail='Мындай продукт жок', status_code=404)
    return product


@product_router.put('/{product_id}/', response_model=dict)
async def update_product(product_id: int, product: ProductCreateSchema,
                         db: Session = Depends(get_db)):
    product_db = db.query(Product).filter(Product.id == product_id).first()
    if not product_db:
        raise HTTPException(detail='Мындай продукт жок', status_code=404)

    for key, value in product.dict().items():
        setattr(product_db, key, value)

    db.commit()
    db.refresh(product_db)
    return {'message': 'Продукт өзгөртүлдү'}


@product_router.delete('/{product_id}/', response_model=dict)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_db = db.query(Product).filter(Product.id == product_id).first()
    if not product_db:
        raise HTTPException(detail='Мындай продукт жок', status_code=404)

    db.delete(product_db)
    db.commit()
    return {'message': 'Продукт өчүрүлдү'}
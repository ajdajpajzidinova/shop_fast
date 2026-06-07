from fastapi import APIRouter, HTTPException, Depends
from shop_app.database.db import SessionLocal
from shop_app.database.models import SubCategory
from shop_app.database.schema import SubCategorySchema, SubCategoryCreateSchema
from sqlalchemy.orm import Session
from typing import List


subcategory_router = APIRouter(prefix='/subcategory', tags=['SubCategory'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@subcategory_router.post('/', response_model=SubCategorySchema)
async def create_subcategory(subcategory: SubCategoryCreateSchema, db: Session = Depends(get_db)):
    subcategory_db = SubCategory(**subcategory.dict())
    db.add(subcategory_db)
    db.commit()
    db.refresh(subcategory_db)
    return subcategory_db


@subcategory_router.get('/', response_model=List[SubCategorySchema])
async def list_subcategories(db: Session = Depends(get_db)):
    return db.query(SubCategory).all()


@subcategory_router.get('/{subcategory_id}/', response_model=SubCategorySchema)
async def detail_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory:
        raise HTTPException(detail='Мындай субкатегори жок', status_code=404)
    return subcategory


@subcategory_router.put('/{subcategory_id}/', response_model=dict)
async def update_subcategory(subcategory_id: int, subcategory: SubCategoryCreateSchema,
                             db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай субкатегори жок', status_code=404)

    for key, value in subcategory.dict().items():
        setattr(subcategory_db, key, value)

    db.commit()
    db.refresh(subcategory_db)
    return {'message': 'Субкатегори өзгөртүлдү'}


@subcategory_router.delete('/{subcategory_id}/', response_model=dict)
async def delete_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай субкатегори жок', status_code=404)

    db.delete(subcategory_db)
    db.commit()
    return {'message': 'Субкатегори өчүрүлдү'}
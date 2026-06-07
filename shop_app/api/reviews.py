from fastapi import APIRouter, HTTPException, Depends
from shop_app.database.db import SessionLocal
from shop_app.database.models import Review
from shop_app.database.schema import ReviewSchema, ReviewCreateSchema
from sqlalchemy.orm import Session
from typing import List


review_router = APIRouter(prefix='/review', tags=['Review'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@review_router.post('/', response_model=ReviewSchema)
async def create_review(review: ReviewCreateSchema, db: Session = Depends(get_db)):
    review_db = Review(**review.dict())
    db.add(review_db)
    db.commit()
    db.refresh(review_db)
    return review_db


@review_router.get('/', response_model=List[ReviewSchema])
async def list_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()


@review_router.get('/{review_id}/', response_model=ReviewSchema)
async def detail_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(detail='Мындай коммент жок', status_code=404)
    return review


@review_router.put('/{review_id}/', response_model=dict)
async def update_review(review_id: int, review: ReviewCreateSchema,
                        db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id).first()
    if not review_db:
        raise HTTPException(detail='Мындай коммент жок', status_code=404)

    for key, value in review.dict().items():
        setattr(review_db, key, value)

    db.commit()
    db.refresh(review_db)
    return {'message': 'коммент өзгөртүлдү'}


@review_router.delete('/{review_id}/', response_model=dict)
async def delete_review(review_id: int, db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id).first()
    if not review_db:
        raise HTTPException(detail='Мындай коммент жок', status_code=404)

    db.delete(review_db)
    db.commit()
    return {'message': 'коммент өчүрүлдү'}
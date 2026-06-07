from pydantic import BaseModel,EmailStr
from typing import Optional, List
from enum import Enum
from datetime import date, datetime


class StatusChoices(str, Enum):
    gold = 'gold'
    silver = 'silver'
    bronze = 'bronze'
    simple = 'simple'


class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int] = None
    phone_number: Optional[str] = None
    avatar: Optional[str] = None
    status: StatusChoices
    date_registered: date

    class Config:
        from_attributes = True


class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int] = None
    phone_number: Optional[str] = None
    avatar: Optional[str] = None
    status: StatusChoices = StatusChoices.simple
    password: str

class UserLoginSchema(BaseModel):
    username: str
    password: str

class CategoryOutSchema(BaseModel):
    id: int
    category_image: str
    category_name: str

    class Config:
        from_attributes = True


class CategoryInputSchema(BaseModel):
    category_image: str
    category_name: str


class SubCategorySchema(BaseModel):
    id: int
    subcategory_name: str
    category_id: int

    class Config:
        from_attributes = True


class SubCategoryCreateSchema(BaseModel):
    subcategory_name: str
    category_id: int


class ProductImageSchema(BaseModel):
    id: int
    image: str
    product_id: int

    class Config:
        from_attributes = True


class ProductImageCreateSchema(BaseModel):
    image: str
    product_id: int


class ProductSchema(BaseModel):
    id: int
    subcategory_id: int
    product_name: str
    price: int
    article_number: int
    description: str
    product_type: bool
    video: str
    created_date: date
    product_images: List[ProductImageSchema] = []

    class Config:
        from_attributes = True


class ProductCreateSchema(BaseModel):
    subcategory_id: int
    product_name: str
    price: int
    article_number: int
    description: str
    product_type: bool
    video: str


class ReviewSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    stars: int
    comment: str
    created_date: datetime

    class Config:
        from_attributes = True


class ReviewCreateSchema(BaseModel):
    user_id: int
    product_id: int
    stars: int
    comment: str
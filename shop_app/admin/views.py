from shop_app.database.models import UserProfile, Category, Product, Review, SubCategory, RefreshToken
from sqladmin import ModelView


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.first_name, UserProfile.last_name,
                   UserProfile.username, UserProfile.email, UserProfile.status,
                   UserProfile.date_registered]


class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [RefreshToken.id, RefreshToken.user_id,
                   RefreshToken.token, RefreshToken.created_date]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.category_name, Category.category_image]


class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.id, SubCategory.subcategory_name, SubCategory.category_id]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.product_name, Product.price,
                   Product.article_number, Product.product_type,
                   Product.subcategory_id, Product.created_date]


class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.user_id, Review.product_id,
                   Review.stars, Review.comment, Review.created_date]
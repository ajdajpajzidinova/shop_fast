from fastapi import FastAPI
from shop_app.api import  users, category , auth , products,subcategory,reviews
import uvicorn
from shop_app.admin.setup import setup_admin


shop_app = FastAPI(title='Store')
shop_app.include_router(users.users_router)
shop_app.include_router(category.category_router)
shop_app.include_router(products.product_router)
shop_app.include_router(subcategory.subcategory_router)
shop_app.include_router(reviews.review_router)
shop_app.include_router(auth.auth_router)
setup_admin(shop_app)

if __name__ == '__main__':
    uvicorn.run(shop_app, host='127.0.0.1', port=8001)
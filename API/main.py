from fastapi import FastAPI
import time
from functions_for_API import parser_for_goods, parser_for_categoties, get_data




app = FastAPI(timeout=5, title="API", description="This is API for using our web shop", version='0.2.0', docs_url='/')



@app.get("/api/get_categoties", tags=['main items'], description='Отримати категорії')
def get_categories():
    return parser_for_categoties()


@app.get("/api/get_goods_info", tags=['main items'], description='Отримати інформацію про товар в якійсь категорії')
def get_goods_info(text: str):
    return parser_for_goods(text)


@app.get("/api/get_good_info", tags=['main items'], description='Отримати інформацію про товар')
async def get_good_info(text: str):
    return await get_data(text)

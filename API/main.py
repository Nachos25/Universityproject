from fastapi import FastAPI
import time
import json
from redis import Redis
from functions_for_API import parser_for_goods, parser_for_categoties, get_data

redis = Redis(host="localhost", port=6379, db=1)


app = FastAPI(timeout=5, title="API", description="This is API for using our web shop", version='0.2.0', docs_url='/')



@app.get("/api/get_categoties", tags=['main items'], description='Отримати категорії')
def get_categories():
    cache_key = "categories"
    # redis.delete(cache_key)
    cached_data = redis.get(cache_key)
    if cached_data:
        information = cached_data
    else:
        information = parser_for_categoties()
        redis.setex(cache_key, 60*5, str(information))
    try:
        return json.loads(information.decode("utf-8").replace("'", "\""))
    except AttributeError:
        return information


@app.get("/api/get_goods_info", tags=['main items'], description='Отримати інформацію про товар в якійсь категорії')
def get_goods_info(text: str):
    return parser_for_goods(text)


@app.get("/api/get_good_info", tags=['main items'], description='Отримати інформацію про товар')
async def get_good_info(text: str):
    result = get_data(text)
    return result

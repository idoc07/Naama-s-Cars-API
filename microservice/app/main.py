from fastapi import FastAPI
from pydantic import BaseModel
from db_setup import get_message, insert


class GreetingModel(BaseModel):
    car_num: int
    car_type: str
    extended_info: str


app = FastAPI()


@app.get("/")
def health():
    return {"status": "working"}


@app.get("/get_message")
async def print_message():
    return {"message": get_message()}


@app.post('/send_greetings')
async def send_data(info: GreetingModel):
    print(info.car_num, info.car_type, info.extended_info)
    return {"text": insert(info.car_num, info.car_type, info.extended_info)}

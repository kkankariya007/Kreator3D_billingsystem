from fastapi import FastAPI,File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pymongo 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/add")
async def save(name:str,age:int,contact:int,email:str):
  client = pymongo.MongoClient("mongodb+srv://SaiHarshithTedla:1768%40Sh14035@cluster0.5ltvpng.mongodb.net/?retryWrites=true&w=majority")
  db = client.test

  # name="Kunal"
  # age=21
  # contact=8767046387
  # email="kk3288@gmail.com"

  Database = client["myFirstDatabase"]
  SampleTable = Database["Info"]

  person = {
    "name": name,
    "age":age,
    "contact": contact,
    "email":email
  }

  SampleTable.insert_one(person)
  return "Hogaya bhai"

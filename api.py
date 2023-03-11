from fastapi import FastAPI
import pymongo 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://SaiHarshithTedla:1768%40Sh14035@cluster0.5ltvpng.mongodb.net/?retryWrites=true&w=majority")
db = client.test

name="Kunal"
age=21
contact=8767046387
email="kk3288@gmail.com"

Database = client["myFirstDatabase"]
SampleTable = Database["Info"]



person = {
  "name": name,
  "age":age,
  "contact": contact,
  "email":email
}
SampleTable.insert_one(person)

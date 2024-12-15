from typing import Union, Optional


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import MongoDsn
from pymongo import mongo_client, MongoClient

app = FastAPI()

conn = MongoClient("mongodb+srv://eazdanrafin:rAcA2YU66mXRqxEO@fastapilearning.tuidz.mongodb.net")





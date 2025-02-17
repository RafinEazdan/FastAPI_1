from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Routes.note import note

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(note)

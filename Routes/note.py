from fastapi import  APIRouter
from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from  models.note import Note
from config.db import conn
from schema.note import noteEntity,notesEntity
from fastapi.responses import HTMLResponse

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"],
        })
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def create_item(request: Request, title:str = Form(...), desc:str = Form(...), important:bool = Form(...)):
    #
    form = await  request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict["important"] == "on" else False
    conn.notes.notes.insert_one(formDict)
    return {"Success": "Data inserted successfully"}

import uvicorn
from fastapi import FastAPI, Path, Body,Query,Request
from typing import List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    subjects: List[str] = []

class City(BaseModel):
    id:int
    country:List[str] = []
    code:int

@app.post("/students")
async def student_data(name:str=Body(...), marks:int=Body(...)):
    return {"name":name, "marks":marks}

@app.post("/students/{college}")
async def student_data(college:str,age:int, student:Student):
    reval={"college":college, "age":age, "student":student}
    return reval

@app.post("/student/details")
async def city_data(student:Student,city:City=Body(...)):
    return {"country":country, "code":code, "city":city}


@app.get("/")
async def index():
    return {"message": "Success! The API is working."}

#@app.get("/hello/{name}/{age}")
#async def hello(name:str=Path(..., min_length=3, max_length=10), age:int=Path(...,ge=1, le=100)):
 #   return{"name":name ,"age":age}

templates = Jinja2Templates(directory="templates")

@app.get("/about/{name}", response_class=HTMLResponse)
async def about(request: Request,name:str):
    return templates.TemplateResponse("about.html", {"request": request, "name":name})


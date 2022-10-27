from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
@app.get("/")
def read_root():
 html_content = "<h2> Hello, my name is Asanali!</h2>"
 return HTMLResponse(content=html_content)


from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
 return {"message": "Hello my name is Asanali"}

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
 return {"message": "Hello!"}
@app.get("/about")
def about():
 return {"message": "О сайте"}

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse
app = FastAPI()
@app.get("/text", response_class = PlainTextResponse)
def root_text():
 return "Hello World!"
@app.get("/html", response_class = HTMLResponse)
def root_html():
 return "<h2>Hello World!</h2>"

@app.get("/users/{name}-{age}")
def users(name, age):
 return {"user_name": name, "user_age": age}

from fastapi import FastAPI
app = FastAPI()
@app.get("/users/{name}")
def users(name):
 return {"user_name": name}

 from fastapi import FastAPI, Path
 app = FastAPI() \
       @ app.get("/users/{name}/{age}")

 def users(name: str = Path(min_length=3, max_length=20),
           age: int = Path(ge=18, lt=111)):
  return {"name": name, "age": age}

 from fastapi import FastAPI
 from fastapi.staticfiles import StaticFiles
 app = FastAPI()
 app.mount("/static", StaticFiles(directory="public"))

 from fastapi import FastAPI
 from fastapi.responses import FileResponse
 from pydantic import BaseModel
 class Person(BaseModel):
  name: str
  age: int

 app = FastAPI()

 @app.get("/")
 def root():
  return FileResponse("public/index.html")

 @app.post("/hello")
 def hello(people: list[Person]):
  return {"message": people}


 import uuid
 from fastapi import FastAPI, Body, status
 from fastapi.responses import JSONResponse, FileResponse
 class Person:
  def __init__(self, name, age):
   self.name = name

  self.age = age
  self.id = str(uuid.uuid4())

 people = [Person("Tom", 38), Person("Bob", 42), Person("Sam", 28)]

 def find_person(id):
  for person in people:
   if person.id == id:
    return person
  return None

 app = FastAPI()
 @app.get("/")
 async def main():
  return FileResponse("public/index.html")

 @app.get("/api/users")
 def get_people():
  return people

 @app.get("/api/users/{id}")
 def get_person(id):
  person = find_person(id)
  print(person)
  if person == None:
   return JSONResponse(
    status_code=status.HTTP_404_NOT_FOUND,
    content={"message": "Пользователь не найден"}
   )
  return person

 @app.post("/api/users")
 def create_person(data=Body()):
  person = Person(data["name"], data["age"])
  people.append(person)
  return person

 @app.put("/api/users")
 def edit_person(data=Body()):
  person = find_person(data["id"])
  if person == None:
   return JSONResponse(
    status_code=status.HTTP_404_NOT_FOUND,
    content={"message": "Пользователь не найден"}
   )

  person.age = data["age"]
  person.name = data["name"]
  return person

 @app.delete("/api/users/{id}")
 def delete_person(id):
  person = find_person(id)



 if person == None:
  return JSONResponse(
   status_code=status.HTTP_404_NOT_FOUND,
   content={"message": "Пользователь не найден"}
  )
 # если пользователь найден, удаляем его
 people.remove(person)
 return person
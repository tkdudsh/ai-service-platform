# /todo - get, post , put, delete

from fastapi import APIRouter


router= APIRouter() # fastapi 라우터 생성

class Todo(BaseModel):
    id:int

todo_list = []

#create
@router.post("/todo")
async def create_todo() -> dict:
    return {"message": "CREATE::TODO"}

#read
@router.get("/todo/all")
async def read_todo() -> dict:
    return {"message": "READ::TODO"}

@router.get("/todo/{id}")
async def read_todo(id:int  ) -> dict:
    for todo in todo_list:
        if todo.id==id:
            return {"todo":todo}
    return {"message": "READ::TODO"}

#Update
@router.put("/todo")
async def put_todo() -> dict:
    return {"message": "PUT::TODO"}

# Delete
@router.delete("/todo")
async def delete_todo() -> dict:
    return {"message": "DELETE::TODO"}

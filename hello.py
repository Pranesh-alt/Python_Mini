from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel


app=FastAPI(title="test")


students = {
    1: {
        "name": "pranesh",
        "age": 21,
        "track":"python"
    }
}


class NewArticle(BaseModel):
    title: str
    description: str
    author: str
    
    
class UpdateArticle(BaseModel):
    title: str
    description: str
    author: str

@app.get("/")
def index():
    return {"name": "First data"}



@app.get("/v1/articles")
def get_article():
    return {"data": []}


@app.get("/v1/articles/{id}")
def get_article_byid(id: str):
    print(id)
    return {"data": {id},
            "status":200}
 

@app.post("/v1/articles")
def create_article(new_article:NewArticle):
    print(new_article)
    return {"status" : 201}


@app.put("/v1/articles/{id}")
def update_article(update_article:UpdateArticle):
    print(update_article)
    return {"status" : 204}

@app.delete("/v1/articles/{id}")
def delete_article(id: str):
    print(id)
    return {"status" : 200}



# @app.get("/get-student/{student_id}")
# def student_id(student_id: int = Path(...,description="The ID of the student you want to view")): #None-Empty data
#     return students[student_id]


# @app.get("/get-by-name")
# def student_name(*,student_id: int,name: Optional[str]= None,test: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
        
#     return{"Data": "Not found"}
    

# @app.post("/create-student/{student_id}")
# def create_student(student_id: int,student: Student):
#     if student_id in students:
#         return {"Error": "Student exists"}
    
#     students[student_id] = student
#     return students[student_id]
    












# def main():
#     print("Hello from test!")


# if __name__ == "__main__":
#     main()
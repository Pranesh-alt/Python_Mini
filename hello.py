from fastapi import FastAPI
from pydantic import BaseModel

class NewArticle(BaseModel):
    title: str
    description:str
    author:str

app=FastAPI(title="hi")

@app.get("/")
def hello():
    return "hello"

@app.get("/v1/articles")
def get_articles():
    return {"data":[],"status":200}

data={1:"article 1",2:'article 2'}

@app.get("/v1/articles/{id}")
def get_article_by_id(id:int):
    return {"data":data[1],"status":200}


@app.post("/v1/articles")
def create_article(new_article: NewArticle):
    print(new_article)
    return {"status":201}

@app.put("/v1/articles")
def update_article(update_article: NewArticle):
    print(update_article)
    return {"status":204}
    
@app.delete("/v1/articles/{id}")
def delete_article(id:int):
    return {"status":200}

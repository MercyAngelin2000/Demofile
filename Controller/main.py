from fastapi import FastAPI,Depends,HTTPException,status
from Database.database import engine, get_db
from Model import model
from Schema.schema import create
from sqlalchemy.orm import Session

model.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"Hai":"Juju"}

@app.post("/post")
def postmethod(Post:create,db:Session=Depends(get_db)):
    data = model.sample(**Post.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@app.get("/get/{id}")
def getmethod(id:int,db:Session=Depends(get_db)):
    data=db.query(model.sample).filter(model.sample.id==id)
    value = data.first()
    if value:
        return value
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

@app.put("/update/{id}")
def putmethod(id:int,Post:create,db:Session=Depends(get_db)):
    data = db.query(model.sample).filter(model.sample.id==id)
    msg = data.first()
    if msg:
        data.update(Post.dict(),synchronize_session=False)
        db.commit()
        return data.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

@app.delete("/del/{id}")
def deletemethod(id:int,db:Session=Depends(get_db)):
    data=db.query(model.sample).filter(model.sample.id==id)
    msg = data.first()
    if msg:
        data.delete(synchronize_session=False)
        db.commit()
        return{"msg":"Success"}

from fastapi import Response,status,HTTPException,Depends,APIRouter
from .. import models,schema,utils
from ..database import get_db
from typing import List
from sqlalchemy.orm import Session
router = APIRouter(
    prefix='/users',
    tags=['Users']
)
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.UserOut)
def create_user(user: schema.UserCreate,db:Session=Depends(get_db)):
    #hash the password - user.password
    user.password = utils.hash(user.password)
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return  new_user
@router.get("/{id}",response_model=schema.UserOut)
def get_user(id:int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"No User found with id : {id}")
    else:
        return user
    

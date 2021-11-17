from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)

    class Config:
        schema_extra = {
            "Post-test" : {
                "title" : "Loreasum",
                "content" : "Ini adalah content"
            }
        }

class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "name" : "yasril",
                "email": "yasril@gmail.com",
                "password": "123456"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "email": "yasril@gmail.com",
                "password": "123456"
            }
        }
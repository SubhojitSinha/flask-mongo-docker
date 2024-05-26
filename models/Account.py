from models.BaseModel import BaseModel

class Account(BaseModel):
    def __init__(self):
        super().__init__('accounts')

class User(BaseModel):
    def __init__(self):
        super().__init__('Users')
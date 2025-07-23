from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PortfolioCreate(BaseModel):
    name: str

class Portfolio(BaseModel):
    id: int
    name: str
    user_id: int
    created_at: datetime
    updated_at: datetime
    user: Optional[User] = None

    class Config:
        orm_mode = True

class TradeCreate(BaseModel):
    symbol: str
    quantity: float
    price: float
    trade_type: str

class Trade(BaseModel):
    id: int
    portfolio_id: int
    symbol: str
    quantity: float
    price: float
    trade_type: str
    created_at: datetime
    updated_at: datetime
    portfolio: Optional[Portfolio] = None

    class Config:
        orm_mode = True

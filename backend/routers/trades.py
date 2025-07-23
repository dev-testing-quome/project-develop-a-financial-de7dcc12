from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import TradeCreate, Trade
from services import trade_service

router = APIRouter(prefix="/api/trades", tags=["Trades"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Trade, status_code=status.HTTP_201_CREATED)
def create_trade(trade: TradeCreate, db: Session = Depends(get_db)):
    return trade_service.create_trade(db, trade)

@router.get("/{{"trade_id:int}}", response_model=Trade)
def get_trade(trade_id: int, db: Session = Depends(get_db)):
    trade = trade_service.get_trade(db, trade_id)
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    return trade

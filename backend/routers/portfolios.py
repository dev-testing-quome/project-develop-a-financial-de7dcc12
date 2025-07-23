from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import PortfolioCreate, Portfolio
from services import portfolio_service

router = APIRouter(prefix="/api/portfolios", tags=["Portfolios"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Portfolio, status_code=status.HTTP_201_CREATED)
def create_portfolio(portfolio: PortfolioCreate, db: Session = Depends(get_db)):
    return portfolio_service.create_portfolio(db, portfolio)

@router.get("/{{"portfolio_id:int}}", response_model=Portfolio)
def get_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    portfolio = portfolio_service.get_portfolio(db, portfolio_id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio

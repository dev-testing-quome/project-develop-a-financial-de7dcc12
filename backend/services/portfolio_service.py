from sqlalchemy.orm import Session
from schemas import PortfolioCreate, Portfolio
from models import Portfolio as PortfolioModel

def create_portfolio(db: Session, portfolio: PortfolioCreate) -> Portfolio:
    db_portfolio = PortfolioModel(name=portfolio.name)
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return Portfolio.from_orm(db_portfolio)

def get_portfolio(db: Session, portfolio_id: int) -> Portfolio | None:
    db_portfolio = db.query(PortfolioModel).filter(PortfolioModel.id == portfolio_id).first()
    if db_portfolio:
        return Portfolio.from_orm(db_portfolio)
    return None

from sqlalchemy.orm import Session
from schemas import TradeCreate, Trade
from models import Trade as TradeModel

def create_trade(db: Session, trade: TradeCreate) -> Trade:
    db_trade = TradeModel(symbol=trade.symbol, quantity=trade.quantity, price=trade.price, trade_type=trade.trade_type)
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return Trade.from_orm(db_trade)

def get_trade(db: Session, trade_id: int) -> Trade | None:
    db_trade = db.query(TradeModel).filter(TradeModel.id == trade_id).first()
    if db_trade:
        return Trade.from_orm(db_trade)
    return None

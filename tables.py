from decimal import Decimal
from enum import Enum
from datetime import date
from typing import Optional

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class Operation(Base):
    __tablename__ = 'operations'

    id: int
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

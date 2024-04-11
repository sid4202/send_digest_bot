from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import BOOLEAN
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
import Subscription
import Base


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_subscriber = Column(BOOLEAN)
    superuser_password = Column(String)
    subscription_id = Column(Integer, ForeignKey('subscription.id'))

    subscription = relationship(Subscription.__name__)
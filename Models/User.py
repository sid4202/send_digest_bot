from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import BOOLEAN
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
import Subscription
import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    job_name = Column(String, nullable=True)
    password = Column(String)
    is_subscriber = Column(BOOLEAN)
    is_company_superuser = Column(BOOLEAN)
    is_employer = Column(BOOLEAN)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))

    subscription = relationship(Subscription.__name__)

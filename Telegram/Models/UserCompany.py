from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from Models import Base
class UserCompany(Base):
    __tablename__ = 'user_company'

    user_id = Column(Integer, ForeignKey('user.id'))
    company_id = Column(Integer, ForeignKey('company.id'))
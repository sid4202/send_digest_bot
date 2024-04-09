from sqlalchemy import Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy import BOOLEAN
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import Base
import DigestConfig


class Subscription(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    last_payment = Column(TIMESTAMP)
    expired_at = Column(TIMESTAMP)
    has_expired = Column(BOOLEAN)
    is_corporate = Column(BOOLEAN)
    digest_config_id = Column(Integer, ForeignKey('digest_config.id'))

    digest_config = relationship(DigestConfig.__name__)
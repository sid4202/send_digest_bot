from sqlalchemy import Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy import BOOLEAN
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import String

import Base

class DigestConfig(Base):
    schedule = Column(String)
    category = Column(String)
    channel_to_send = Column(String)
    sending_time = Column(TIMESTAMP)

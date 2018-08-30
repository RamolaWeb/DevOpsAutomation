from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Server(Base):
    """ This Class Store Detail of the Server"""
    __tablename__ = "Server"
    id = Column(Integer, autoincrement=True, primary_key=True)
    ip = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    dbUser = Column(Text, nullable=False)
    dbName = Column(Text, nullable=False)
    dbPass = Column(Text, nullable=False)
    sshUser = Column(Text, nullable=False)
    sshPass = Column(Text, nullable=False)


class User(Base):
    """ This Class Store the Detail of the User"""
    __tablename__ = "User"
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(Text, nullable=False)


engine = create_engine('mysql+pymysql://root:root@localhost:3306/automation')
Base.metadata.create_all(engine)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String)
    user_id = Column(String(20), ForeignKey('user.id'))

engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

# 插入数据
# session = DBSession()
# new_user =User(id='5', name='Bob')
# session.add(new_user)
# session.commit()
# session.close()

# session = DBSession()
# new_book = Book(id='1', name='Chinese', user_id='1')
# new_book2 = Book(id='2', name='Chinese', user_id='1')
# new_book3 = Book(id='3', name='Chinese', user_id='1')
# session.add(new_book)
# session.add(new_book2)
# session.add(new_book3)
# session.commit()
# session.close()

session = DBSession()
user = session.query(User).filter(User.id=='1').one()

print('name', user.name)
for book in user.books:
    print(book.name)

session.close()
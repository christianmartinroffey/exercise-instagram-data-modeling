import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    firstname = Column(String(250),  nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)

class Follower(Base):
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, foreignKey('User.id'))
    user_to_id = Column(Integer, foreignKey('User.id'))

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, unique=True, primary_key=True)
    user_id = Column(Integer, nullable=False))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, unique=True, primary_key=True)
    comment_text = Column(String, nullable=False)
    author_id = Column(Integer, foreignKey('User.id'))
    post_id = Column(Integer, foreignKey('Post.id'))

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, unique=True, primary_key=True)
    type = Column(Enum, nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, foreignKey('Post.id'))




# examples below

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
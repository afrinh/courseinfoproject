import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

 
Base = declarative_base()
 
 
class Questions(Base):
    __tablename__ = 'questions'
   
    id = Column(Integer, primary_key = True, autoincrement=True)
    question = Column(String(100))
    course_name=Column(String(100))
    cid= Column(Integer)

    def __init__(self,question,course_name,cid):
        # self.qid=qid
        self.question = question
        self.course_name = course_name
        self.cid = cid


    def insertion(self):
        session.add(self)
        session.commit()

class PQuestions(Base):
    __tablename__ = 'pquestions'
   
    id = Column(Integer, primary_key = True, autoincrement=True)
    pquestion = Column(String(100))

    def __init__(self,question):
        self.pquestion = pquestion


    def insertion(self):
        session.add(self)
        session.commit()

class CQuestions(Base):
    __tablename__ = 'cquestions'
   
    id = Column(Integer, primary_key = True, autoincrement=True)
    cquestion = Column(String(100))

    def __init__(self,cquestion):
        self.cquestion = cquestion


    def insertion(self):
        session.add(self)
        session.commit()

class JQuestions(Base):
    __tablename__ = 'jquestions'
   
    id = Column(Integer, primary_key = True, autoincrement=True)
    jquestion = Column(String(100))

    def __init__(self,jquestion):
        self.jquestion = jquestion


    def insertion(self):
        session.add(self)
        session.commit()

class DSQuestions(Base):
    __tablename__ = 'dsquestions'
   
    id = Column(Integer, primary_key = True, autoincrement=True)
    dsquestion = Column(String(100))

    def __init__(self,dsquestion):
        self.dsquestion = dsquestion


    def insertion(self):
        session.add(self)
        session.commit()

class DBMSQuestions(Base):
    __tablename__ = 'dbmsquestions'
   
    id = Column(Integer, primary_key = True, autoincrement=True)
    dbmsquestion = Column(String(100))

    def __init__(self,dbmsquestion):
        self.dbmsquestion = dbmsquestion


    def insertion(self):
        session.add(self)
        session.commit()

class User(Base):
    __tablename__ = 'user'
   
    user_id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String(30), unique=True)
    password=Column(String(20))

    def __init__(self,uid,n,pw):
        self.user_id=uid
        self.name = n 
        self.password= pw    

    def insertion(self):
        session.add(self)
        session.commit()

class Answers(Base):
    __tablename__ = 'answers'
   
    course_id = Column(Integer)
    ans_id = Column(Integer)
    answer = Column(String(100), primary_key = True)
    upvotes = Column(Integer)
    downvotes = Column(Integer)



    def __init__(self,course_id,ans_id,answer,upvotes,downvotes):
        self.course_id=course_id
        self.ans_id=ans_id
        self.answer = answer
        self.upvotes=upvotes
        self.downvotes=downvotes


    def insertion(self):
        session.add(self)
        session.commit()


engine = create_engine('sqlite:///questions.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session=Session()

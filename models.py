from sqlalchemy import *
from sqlalchemy.orm import *
import pymysql

engine = create_engine('mysql+pymysql://root:@localhost/foo', echo=True)
Base = declarative_base()
Session = sessionmaker(engine)

class Grade(Base):
    __tablename__ = 'Grade'

    id = Column(Integer(), primary_key=True)
    stage = Column(Integer())
    semesters = relationship('Semesters')
    modules = relationship('Modules')

    def __init__(self, stage):
        self.stage = stage

    def insert(self):
        Session.add(self)
        Session.commit()

    def delete(self):
        Session.delete(self)
        Session.commit(self)

    def update(self):
        Session.commit()

    def format(self):
        return {
            'id': self.id,
            'stage': self.stage
        }


class Semesters(Base):
    __tablename__ = 'Semesters'
    id = Column(Integer, primary_key=True)
    num = Column(Integer)
    grade_id = Column(Integer, ForeignKey('Grade.id'))
    modules = relationship('Modules')

    def __init__(self, num, grade_id):
        self.num = num
        self.grade_id = grade_id

    def insert(self):
        Session.add(self)
        Session.commit()

    def delete(self):
        Session.delete(self)
        Session.commit(self)

    def update(self):
        Session.commit()

    def format(self):
        return {
            'id': self.id,
            'grade_id': self.grade_id,
            'sem_num': self.num
        }


class Modules(Base):
    __tablename__ = 'Modules'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    grade_id = Column(Integer, ForeignKey('Grade.id'))
    semester_id = Column(Integer, ForeignKey('Semesters.id'))
    mcqs = relationship('Mcqs')

    def __init__(self, name, grade_id, semester_id):
        self.name = name
        self.grade_id = grade_id
        self.semester_id = semester_id

    def insert(self):
        Session.add(self)
        Session.commit()

    def delete(self):
        Session.delete(self)
        Session.commit(self)

    def update(self):
        Session.commit()

    def format(self):
        return {
            'id': self.id,
            'grade_id': self.grade_id,
            'sem_id': self.semester_id,
            'module': self.name
        }


class Mcqs(Base):
    __tablename__ = 'Mcqs'
    id = Column(Integer, primary_key=True)
    question = Column(String(255), nullable=False)
    choice_A = Column(String(255), nullable=False)
    choice_B = Column(String(255), nullable=False)
    choice_C = Column(String(255), nullable=False)
    choice_D = Column(String(255), nullable=False)
    choice_E = Column(String(255))
    answer = Column(String(255), nullable=False)
    module_id = Column(Integer, ForeignKey('Modules.id'))

    def __init__(self, question, choice_A, choice_B, choice_C, choice_D, choice_E, answer, module_id):
        self.question = question
        self.choice_A = choice_A
        self.choice_B = choice_B
        self.choice_C = choice_C
        self.choice_D = choice_D
        self.choice_E = choice_E
        self.answer = answer
        self.module_id = module_id

        def insert(self):
            Session.add(self)
            Session.commit()

        def delete(self):
            Session.delete(self)
            Session.commit(self)

        def update(self):
            Session.commit()

        def format(self):
            return {
                'id': self.id,
                'question': self.question,
                'choice_A': self.choice_A,
                'choice_B': self.choice_B,
                'choice_C': self.choice_C,
                'choice_D': self.choice_D,
                'choice_E': self.choice_E,
                'answer': self.answer,
                'module_id': self.module_id

            }




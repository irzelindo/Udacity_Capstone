'''
  This file contains all the database connection definition,
  and all the CRUD for category and question tables.
'''
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

DATABASE_PATH = "postgres://iahzcugahonalx:8698b8c2ad6c35ecda6052809f3a9449d2a67159609776cc0602087d702642e1@ec2-3-214-53-225.compute-1.amazonaws.com:5432/dai1c51jluqmkq"
db = SQLAlchemy()
# print(DATABASE_PATH)
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=DATABASE_PATH):
    ''' Database setup '''
    print(database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()



# Question


class Question(db.Model):
    ''' Question table definition '''
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category = Column(String)
    difficulty = Column(Integer)

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        ''' Insert data into Question table '''
        db.session.add(self)
        db.session.commit()

    def update(self):
        ''' Update data on Question table'''
        db.session.commit()

    def delete(self):
        ''' Delete data on Questino table'''
        db.session.delete(self)
        db.session.commit()

    def format(self):
        ''' Serialize Question table data for json object '''
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
        }


# Category


class Category(db.Model):
    ''' Category table definition '''
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    def format(self):
        ''' Serialize CAtegory table data for json object '''
        return {
            'id': self.id,
            'type': self.type
        }

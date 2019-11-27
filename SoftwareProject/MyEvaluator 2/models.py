from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from sqlalchemy.ext.declarative import declarative_base
from fill_db import add_to_db,delete_from_db


file_path = os.path.abspath(os.getcwd())+"\database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)



taking = db.Table('takers',
	db.Column('person_id',db.Integer,db.ForeignKey('person.person_id')),
	db.Column('subject_id',db.Integer,db.ForeignKey('subject.subject_id'))
	)
mystudents = db.Table('mystudents',
	db.Column('professor_id',db.Integer,db.ForeignKey('professor.professor_id')),
	db.Column('students_id',db.Integer,db.ForeignKey('student.student_id'))
	)
mygroups = db.Table('mygroups',
	db.Column('person_id',db.Integer,db.ForeignKey('person.person_id')),
	db.Column('group_id',db.Integer,db.ForeignKey('group.group_id'))
	)


submiters = db.Table('submiters',
	db.Column('form_id',db.Integer,db.ForeignKey('form.form_id')),
	db.Column('person_id',db.Integer,db.ForeignKey('person.person_id'))
	)

form_subject = db.Table('form_subject',
	db.Column('form_id',db.Integer,db.ForeignKey('form.form_id')),
	db.Column('subject_id',db.Integer,db.ForeignKey('subject.subject_id'))
	)

form_professor = db.Table('form_professor',
	db.Column('form_id',db.Integer,db.ForeignKey('form.form_id')),
	db.Column('professor_id',db.Integer,db.ForeignKey('professor.professor_id'))
	)

class Person(db.Model):
	name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	mail = db.Column(db.String(100))
	password = db.Column(db.String(100))
	person_id = db.Column(db.Integer,primary_key = True)
	subjects = db.relationship('Subject',secondary=taking,backref = db.backref('takers'),lazy = 'dynamic')
	groups = db.relationship('Group',secondary=mygroups,backref = db.backref('mygroups'),lazy = 'dynamic')
	__mapper_args__ = {"polymorphic_on": person_id}

	def add_person(self):
		db.session.add(self)
		db.session.commit()
		print("hhhh")

	def remove_person(self):
		db.session.delete(self)
		db.session.commit()
	

class Subject(db.Model):
	 subject_id= db.Column(db.Integer,primary_key = True)
	 subject_name = db.Column(db.String(100))
	 subject_forms = db.relationship('Form',secondary=form_subject,backref = db.backref('form_subject'),lazy = 'dynamic') 

class Professor(Person,db.Model):
	professor_id = db.Column(db.Integer,db.ForeignKey('person.person_id'),primary_key = True)
	students = db.relationship('Student',secondary = mystudents,backref= db.backref('mystudents'),lazy = 'dynamic')
	professor_forms = db.relationship('Form',secondary = form_professor,backref= db.backref('form_professor'),lazy = 'dynamic')
	


class Student (Person,db.Model):
	student_id =	db.Column(db.Integer,db.ForeignKey('person.person_id'),primary_key = True)
	

class Faculty(Person,db.Model):
	faculty_id = db.Column(db.Integer,db.ForeignKey('person.person_id'),primary_key = True)
	

class Answer(db.Model):
	answer_id = db.Column(db.Integer,primary_key = True)
	answer_content = db.Column(db.String(200))
	
	def add_answer():
		db.session.add(self)
		db.session.commit()
	def remove_answer(self):
		db.session.delete(self)
		db.session.commit()	

class Form(db.Model):
	form_id = db.Column(db.Integer,primary_key = True)
	well = db.Column(db.String(100))
	wrong = db.Column(db.String(100))
	improved = db.Column(db.String(100))
	submiters = db.relationship('Person',secondary=submiters,backref = db.backref('submiters'),lazy = 'dynamic')



	def add_form(self):
		db.session.add(self)
		db.session.commit()
	def remove_form():
		db.session.delete()
		db.session.commit()	

class Group(db.Model):
	group_id = db.Column(db.Integer,primary_key = True)
	group_name = db.Column(db.String(100))	



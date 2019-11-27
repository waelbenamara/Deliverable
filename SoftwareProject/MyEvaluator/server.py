from flask import Flask, request, render_template, send_from_directory,jsonify
import os
from scripts import*
from models import*
import sqlite3
import json
#app = Flask(__name__)

connection = sqlite3.connect("")
cursor = connection.cursor()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/",methods=['POST','GET'])
def main() :

	return "Server is Active"

@app.route("/login",methods=['POST','GET'])
def validate_mail() :
	id = 0
	data = request.get_json()
	print(data)
	email = data['email']
	password = data['password']
	if email == "admin" and password == "admin":
		response = '200'
		type ='Faculty'
		id = get_id(email)
	elif is_Student(email,password) :
		response = '200'
		type = 'Student'
		id = get_id(email)
	elif is_Professor(email,password) :
		response = '200'
		type = 'Professor'
		id = get_id(email)
	elif is_Faculty(email,password) :
		response = '200'
		type = 'Faculty'
		id = get_id(email)	
	else :
		response = '403'
		type = 'none'	

	return jsonify({"response": response,"type":type,"id" : id})

	
			
@app.route("/add_user",methods=['POST','GET'])
def add_user() :
	data = request.get_json()
	name = data['Name']
	lastname = data['LastName']
	email = data['Email']
	tupe = data['type']
	courses = data['coursesSelected']
	groups = data['groupsSelected']
	password = data['password']
	print(type(courses))
	if (tupe == 'Professor'):
		add_professor(name, lastname,email,courses,groups,password)
	elif (tupe == 'Student'):
		add_student(name, lastname,email,courses,groups,password)	
	else :
		add_faculty(name, lastname,email,courses,groups,password)	
	
	
	return "User added !"

@app.route("/get_courses",methods=['GET','POST'])
def get_courses() :

	courses = get_courses_faculty()
	print(courses)
	return jsonify({"courses":courses})

@app.route("/submit_answers",methods=['POST','GET'])
def submit_answers() :
	data = request.get_json()
	print(data)
	well = data['well']
	wrong = data['wrong']
	improved = data['improved']
	person = data['personid']
	course = data['course']
	submit_form(well,wrong,improved,course,person)
	return ""	


@app.route("/get_courses_for_student",methods=['POST','GET'])
def get_courses_for_student() :
	data = request.get_json()
	print(data)
	id = data['currentid']
	courses =get_courses_student(id)
	return jsonify({"courses":courses})	

@app.route("/get_form",methods=['POST','GET'])
def get_form() :
	data = request.get_json()
	professor_id = Professor.query.filter_by(last_name = data['professor']).first().person_id
	forms = get_forms_for_professor(professor_id)
	answers = []
	for x in forms :
		answer = x.well+"," + x.wrong + ","+x.improved+"."
		answers.append(answer)
		print(x)	
	return jsonify({"answers":answers})

@app.route("/get_professors",methods=['POST','GET'])
def get_professors() :
	professors = get_professors_faculty()
	print(professors)
	return 	jsonify({"professors":professors})



if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port=80,threaded = True)


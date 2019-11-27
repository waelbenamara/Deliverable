from models import*
from flask import jsonify

def add_professor(name, lastname,email,courses,groups,password):
	p = Professor(name = name , last_name = lastname, mail = email,password = password)
	p.add_person()
	for x in courses:
		print(x)
		sub = Subject(subject_name = x)
		sub.takers.append(p)
		db.session.commit()
	for y in groups:
		print(y)
		g = Group(group_name = y)
		g.mygroups.append(p)
		db.session.commit()	


def add_student(name, lastname,email,courses,groups,password):
	p = Student(name = name , last_name = lastname, mail = email,password = password)
	p.add_person()
	for x in courses:
		print(x)
		sub = Subject(subject_name = x)
		sub.takers.append(p)
		db.session.commit()
	for y in groups:
		print(y)
		g = Group(group_name = y)
		g.mygroups.append(p)
		db.session.commit()	

def add_faculty(name, lastname,email,courses,groups,password):
	p = Faculty(name = name , last_name = lastname, mail = email,password = password)
	p.add_person()
	for x in courses:
		print(x)
		sub = Subject(subject_name = x)
		sub.takers.append(p)
		db.session.commit()
	for y in groups:
		print(y)
		g = Group(group_name = y)
		g.mygroups.append(p)
		db.session.commit()		

def is_Professor(professor_mail,password):
	flag = False
	users = Professor.query.all()
	for x in users :
		if professor_mail == str(x.mail) and password == str(x.password) :
			print("its trueeee")
			flag = True
			break
		
		else :
			flag = False
	return flag

def is_Student(student_mail,password):
	flag = False
	users = Student.query.all()
	for x in users :
		print(x.mail)	
		print(x.password)
		if student_mail == x.mail and password == x.password :
			print("its trueeee")
			flag = True
			break
		
		else :
			flag = False
	return flag


def is_Faculty(faculty_mail,password):
	flag = False
	users = Faculty.query.all()
	for x in users :
		if faculty_mail == x.mail and password == x.password :
			flag = True
			break
		
		else :
			flag = False
	return flag			

def get_courses_faculty():
	courses = Subject.query.all()
	y = []
	for x in courses :
		y.append(x.subject_name)
	return y

def get_professors_faculty():
	professors = Professor.query.all()
	y = []
	for x in professors:
		y.append(x.last_name)
	return y			

def get_id(email):
	all_person = Person.query.all()
	for x in all_person :
		if (x.mail == email):
			return x.person_id


def get_courses_student(id):
	all_students = Student.query.all()
	y =[]
	for student in all_students :
		if id == student.student_id:
			for mycourses in student.subjects :
				y.append(mycourses.subject_name)
			break
	return y	

def submit_form(well,wrong,improved,course,id):
	form = Form(well = well , wrong = wrong , improved = improved)
	form.add_form()
	student = Person.query.get(id)
	form.submiters.append(student)
	subject = Subject.query.filter_by(subject_name = course).first()
	subject.subject_forms.append(form)
	profs = Professor.query.all()

	for x in profs :
		for y in x.subjects:
			if course == y.subject_name:
				x.professor_forms.append(form)
				break;
	db.session.commit()

def get_forms_for_professor(id):
	professor = Professor.query.get(id)
	forms = []
	for x in professor.professor_forms :
		print(x)
		forms.append(x)
	print(forms)	
	return forms







	

			







from models import *

db.create_all()

s1 = Student(name = "bechir")
s2 = Student(name = "hatem")
s3 = Student(name = "wael")

subj1 = Subject(subject_name = "cs101")
subj2 = Subject(subject_name = "cs102")

professor1 = Professor(name = "Nejib")

answer1 = Answer(answer_content = "The best professor")

s1.add_person()
s2.add_person()
s3.add_person()

db.session.add(subj1)
db.session.add(subj2)
db.session.add(answer1)



subj1.takers.append(s1)
subj1.takers.append(s2)





answer1.myanswers.append(s1)
answer1.myanswers.append(professor1)



db.session.commit()

for x in subj1.takers:
	print(x.name)
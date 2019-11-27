

def add_to_db(MyObject):
	db.session.add(MyObject)
	db.session.commit()

def delete_from_db(MyObject):
	db.session.delete(MyObject)
	db.session.commit()

# db_create.py

from datetime import date
from project import db
from project.models import Task, User


# create the database and db table
db.create_all()

# insert data
db.session.add(
    User("admin", "admin@admin.com", "admin", "admin")
)

db.session.add(
Task("Testing the admin", date(2016, 3, 13), 10, date(2015,8, 31), 1, 5))

db.session.add(
Task("Finish Flask tasks", date(2016, 3, 13), 10, date(2015,8, 31), 1, 5))

    
#db.session.add(Task("Finish Real Python", date(2015, 3, 13), 10, 1))

# commit the changes
db.session.commit()
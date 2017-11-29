from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    course1 = Course(course_number ='FINC314', title ='Investments', description = 'Learn how to analyze different investment opportunities.')
    course2 = Course(course_number = 'COMM212', title ='Oral Communication in Business', description = 'Learn how to effectively public speak in a business setting.')
    prof1 = Professor(name="Jay Coughenour", department = "Finance")
    prof2 = Professor(name="Allie Whitehouse", department = "Communcation")
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(prof1)
    db.session.add(prof2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()

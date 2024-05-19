from app import app, db
from app import City

with app.app_context():
    db.create_all()
    seattle = City(name='Seattle')
    db.session.add(seattle)
    db.session.commit()
    print("added sucssesfuly")

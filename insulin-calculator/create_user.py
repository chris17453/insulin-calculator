from app import app,db, User
from werkzeug.security import generate_password_hash

try:
    # Push an application context
    ctx = app.app_context()
    ctx.push()

    db.create_all()
    # Create new user
    hashed_password = generate_password_hash('ok', method='scrypt')
    new_user = User(username='chris', password=hashed_password)
    # Add new user to the database
    db.session.add(new_user)
    res=db.session.commit()
except  Exception as ex :
    print(ex)

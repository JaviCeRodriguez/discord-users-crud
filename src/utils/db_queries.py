import json
from sqlalchemy.orm import Session

from src.db.database import engine
from src.users import model, schemas

db = Session(bind=engine)

def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user
    """
    db_user = model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def populate_users():
    """
    Populate DB using json file in ./users.json
    """

    db = Session(bind=engine)
    users = get_users(db)
    if not users:
        print("No hay usuarios en la base de datos. Populando...")
        with open("src/utils/users.json") as f:
            users = json.load(f)
            for user in users:
                create_user(db, schemas.UserCreate(**user))
        db.commit()
        db.close()
        print("Tabla users populada con éxito!")


def get_users(db: Session):
    """
    Get all users
    """
    return db.query(model.User).all()


def get_user_by_discriminant(db: Session, discriminant: int):
    """
    Get user by discriminant
    """
    return db.query(model.User).filter(model.User.discriminant == discriminant).first()

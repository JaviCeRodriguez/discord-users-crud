from fastapi import FastAPI

from src.db.database import engine, SessionLocal
from src.users.routes import router as users_router
from src.users import model
from src.utils.db_queries import get_users, populate_users

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    """
    Populate users table if db not exists
    """
    print("Iniciando API 🧉")
    populate_users()


@app.on_event("shutdown")
async def shutdown():
    """
    Close DB connection
    """
    engine.dispose()


@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {"message": "Hola! Ve a http://127.0.0.1:8000/docs para ver la documentación de la API"}

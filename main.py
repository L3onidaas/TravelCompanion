from fastapi import FastAPI
from routers import users, places





app = FastAPI()
app.include_router(users.users_router)
app.include_router(places.places_router)









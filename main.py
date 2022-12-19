from fastapi import FastAPI

from user.api.route_user import router
from user.core.config import settings
from user.db.session import engine
from user.db.base_class import Base


def include_router(app):
    app.include_router(router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_application()

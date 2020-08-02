from suika.models.db import db
from sqlalchemy.sql import func


class Base(db.Model):
    __abstract__ = True

    date_created = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    date_modified = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    def add(self) -> None:
        db.session.add(self)
        self.commit()

    def commit(self) -> None:
        db.session.commit()

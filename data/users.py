from datetime import datetime

import sqlalchemy.orm as orm
import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    type = sa.Column(sa.String)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    password = sa.Column(sa.String, nullable=True, index=True)
    created_at = sa.Column(sa.DateTime, default=datetime.now, index=True)
    updated_at = sa.Column(sa.DateTime, index=True)

    # projects relationship
    projects = orm.relationship("Project")

    def __repr__(self):
        return '<User {}>'.format(self.user_id)

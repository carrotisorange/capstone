from datetime import datetime

import sqlalchemy.orm as orm
import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase
from data.projects import Project


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    user_id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    type = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True, nullable=True)
    password = sa.Column(sa.String, nullable=True, index=True)
    created_at = sa.Column(sa.DateTime, default=datetime.now, index=True)
    updated_at = sa.Column(sa.DateTime)

    # projects relationship
    projects = orm.relation("Project", order_by=[
        Project.created_at.desc(),
        Project.updated_at.desc()
    ], back_populates='projects')

    def __repr__(self):
        return '<User {}>'.format(self.user_id)

import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class ProjectUGC(SqlAlchemyBase):
    __tablename__ = 'project_ugcs'

    user_id = sa.Column(sa.Integer, primary_key=True)
    project_id = sa.Column(sa.Integer, primary_key=True)

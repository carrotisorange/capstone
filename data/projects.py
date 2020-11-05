from datetime import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.modelbase import SqlAlchemyBase


class Project(SqlAlchemyBase):
    __tablename__ = 'projects'

    project_id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at = sa.Column(sa.DateTime, default=datetime.now, index=True)
    updated_at = sa.Column(sa.DateTime)
    project_name = sa.Column(sa.String)
    category = sa.Column(sa.String)
    search_terms = sa.Column(sa.String)
    data_source = sa.Column(sa.String)


    @property
    def __repr__(self):
        return '<Project {}>'.format(self.project_id)

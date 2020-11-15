from datetime import datetime
import sqlalchemy as sa
from data.modelbase import SqlAlchemyBase


class Project(SqlAlchemyBase):
    __tablename__ = 'projects'

    project_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    project_name = sa.Column(sa.String)
    category = sa.Column(sa.String)
    search_terms = sa.Column(sa.String)
    data_source = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, default=datetime.now, index=True)
    updated_at = sa.Column(sa.DateTime, index=True)

    # project and user relationship
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.user_id"))

    def __repr__(self):
        return '<Project {}>'.format(self.project_id)

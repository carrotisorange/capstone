from datetime import datetime

import sqlalchemy.orm as orm
import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class ProjectUGC(SqlAlchemyBase):
    __tablename__ = 'project_ugcs'

    project_ugc_id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

    # project and user relationship
    project_id = sa.Column(sa.BigInteger, sa.ForeignKey("projects.project_id"))
    project = orm.relation("Project")

    # project and user relationship
    user_id = sa.Column(sa.BigInteger, sa.ForeignKey("users.user_id"))
    user = orm.relation("User")

    def __repr__(self):
        return '<ProjectUGC {}>'.format(self.project_ugc_id)

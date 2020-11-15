from typing import List
import sqlalchemy.orm as orm

import data.db_session as db_session
from data.users import User
from data.projects import Project


def get_all_projects():
    session = db_session.create_session()
    return session.query(Project).all()

    session.close()
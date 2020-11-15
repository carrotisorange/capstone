import os
from data.users import User
from data.projects import Project

import data.db_session as db_session


def main():
    init_db()
    while True:
        insert_a_user()


def insert_a_user():
    u = User()
    u.name = input("Name: ").strip()
    u.type = input("Type: ").strip()
    u.email = input("Email: ").strip()
    u.password = input("Password: ").strip()

    print("Release 1: ")

    p = Project()
    p.project_name = input("Project name: ").strip()
    p.category = input("Category: ").strip()
    p.search_terms = input("Search terms: ").strip()
    p.data_source = input("Data source: ").strip()
    u.projects.append(p)

    print("Release 2: ")

    p = Project()
    p.project_name = input("Project name: ").strip()
    p.category = input("Category: ").strip()
    p.search_terms = input("Search terms: ").strip()
    p.data_source = input("Data source: ").strip()
    u.projects.append(p)

    session = db_session.create_session()

    session.add(u)

    session.commit()


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'db.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()

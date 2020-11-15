import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class UGC(SqlAlchemyBase):
    __tablename__ = 'ugcs'

    ugc_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    content = sa.Column(sa.String)
    language = sa.Column(sa.String)
    like_count = sa.Column(sa.Integer)
    retweet_count = sa.Column(sa.Integer)
    author = sa.Column(sa.String)
    friend_count = sa.Column(sa.Integer)
    follower_count = sa.Column(sa.Integer)
    listed_count = sa.Column(sa.Integer)
    created_at = sa.Column(sa.DateTime)

    def __repr__(self):
        return '<UGC {}>'.format(self.ugc_id)

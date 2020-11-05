import sqlalchemy.orm as orm
import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase
from data.projects import Project


class UGC(SqlAlchemyBase):
    __tablename__ = 'ugcs'

    ugc_id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    screen_name = sa.Column(sa.String, nullable=True)
    text = sa.Column(sa.String)
    lang = sa.Column(sa.String)
    follower_count = sa.Column(sa.Interval)
    retweet_count = sa.Column(sa.Integer)
    reply_count = sa.Column(sa.Integer)
    like_count = sa.Column(sa.Integer)
    friend_count = sa.Column(sa.Integer)
    listed_count = sa.Column(sa.Integer)
    posted_at = sa.Column(sa.DateTime)

    def __repr__(self):
        return '<UGC {}>'.format(self.ugc_id)

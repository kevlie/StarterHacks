from datetime import datetime
from Learnify import p_db


class User(p_db.Model):
    user_id = p_db.Column(p_db.Integer, primary_key=True)
    username = p_db.Column(p_db.String(20), unique=True, nullable=False)
    playlist_id = p_db.Column(p_db.Integer, foreign_keys="Playlist.playlist_id")

    def __repr__(self):
        return f"User('{self.user_id}', '{self.username}', '{self.playlist_id}')"


class Playlist(p_db.Model):
    playlist_id = p_db.Column(p_db.Integer, primary_key=True)
    title = p_db.Column(p_db.String(100), nullable=False)
    date_posted = p_db.Column(p_db.DateTime, nullable=False, default=datetime.utcnow)
    links = p_db.Column(p_db.String(700), nullable=False)

    def __repr__(self):
        return f"Post('{self.playlist_id}', '{self.title}', '{self.date_posted}', '{self.links}')"

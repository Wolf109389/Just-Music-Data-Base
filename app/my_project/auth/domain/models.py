from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Стикувальна таблиця для M:M
playlist_tracks = db.Table(
    'playlist_tracks',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id', ondelete='CASCADE'), primary_key=True),
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.id', ondelete='CASCADE'), primary_key=True),
    db.Column('added_at', db.DateTime, server_default=db.func.current_timestamp())
)

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(80))
    bio = db.Column(db.Text)

    albums = db.relationship('Album', backref='artist', cascade='all, delete-orphan', lazy=True)

    def to_dto(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'bio': self.bio
        }

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    release_year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'), nullable=False)

    tracks = db.relationship('Track', backref='album', cascade='all, delete-orphan', lazy=True)

    def to_dto(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'artist_id': self.artist_id
        }

class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    file_path = db.Column(db.String(255))
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id', ondelete='CASCADE'), nullable=False)

    def to_dto(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'file_path': self.file_path,
            'album_id': self.album_id
        }

class Playlist(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    tracks = db.relationship('Track', secondary=playlist_tracks, backref='playlists', lazy='subquery')

    def to_dto(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
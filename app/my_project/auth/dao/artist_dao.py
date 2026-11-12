from app.my_project.auth.domain.models import db, Artist

class ArtistDAO:
    def get_all(self):
        return Artist.query.all()

    def get_by_id(self, artist_id):
        return Artist.query.get(artist_id)

    def create(self, data):
        artist = Artist(**data)
        db.session.add(artist)
        db.session.commit()
        return artist

    def update(self, artist_id, data):
        artist = self.get_by_id(artist_id)
        if artist:
            for key, value in data.items():
                setattr(artist, key, value)
            db.session.commit()
        return artist

    def delete(self, artist_id):
        artist = self.get_by_id(artist_id)
        if artist:
            db.session.delete(artist)
            db.session.commit()
            return True
        return False
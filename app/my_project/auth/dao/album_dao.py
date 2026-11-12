from app.my_project.auth.domain.models import db, Album

class AlbumDAO:
    def get_all(self):
        return Album.query.all()

    def get_by_id(self, album_id):
        return Album.query.get(album_id)

    def create(self, data):
        album = Album(**data)
        db.session.add(album)
        db.session.commit()
        return album

    def update(self, album_id, data):
        album = self.get_by_id(album_id)
        if album:
            for key, value in data.items():
                setattr(album, key, value)
            db.session.commit()
        return album

    def delete(self, album_id):
        album = self.get_by_id(album_id)
        if album:
            db.session.delete(album)
            db.session.commit()
            return True
        return False
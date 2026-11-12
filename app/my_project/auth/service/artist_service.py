from app.my_project.auth.dao.artist_dao import ArtistDAO

class ArtistService:
    def __init__(self):
        self.dao = ArtistDAO()

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, artist_id):
        return self.dao.get_by_id(artist_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, artist_id, data):
        return self.dao.update(artist_id, data)

    def delete(self, artist_id):
        return self.dao.delete(artist_id)
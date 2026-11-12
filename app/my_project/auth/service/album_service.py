from app.my_project.auth.dao.album_dao import AlbumDAO

class AlbumService:
    def __init__(self):
        self.dao = AlbumDAO()

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, album_id):
        return self.dao.get_by_id(album_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, album_id, data):
        return self.dao.update(album_id, data)

    def delete(self, album_id):
        return self.dao.delete(album_id)
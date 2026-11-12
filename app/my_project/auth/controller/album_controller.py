from flask import jsonify, request
from app.my_project.auth.service.album_service import AlbumService

class AlbumController:
    def __init__(self):
        self.service = AlbumService()

    def get_all(self):
        return jsonify([a.to_dto() for a in self.service.get_all()]), 200

    def get_by_id(self, album_id):
        album = self.service.get_by_id(album_id)
        if not album:
            return jsonify({'message': 'Album not found'}), 404
        return jsonify(album.to_dto()), 200

    def create(self):
        data = request.get_json()
        album = self.service.create(data)
        return jsonify(album.to_dto()), 201

    def update(self, album_id):
        data = request.get_json()
        album = self.service.update(album_id, data)
        if not album:
            return jsonify({'message': 'Album not found'}), 404
        return jsonify(album.to_dto()), 200

    def delete(self, album_id):
        success = self.service.delete(album_id)
        if not success:
            return jsonify({'message': 'Album not found'}), 404
        return jsonify({'message': 'Deleted successfully'}), 200
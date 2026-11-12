from flask import jsonify, request
from app.my_project.auth.service.artist_service import ArtistService

class ArtistController:
    def __init__(self):
        self.service = ArtistService()

    def get_all(self):
        return jsonify([a.to_dto() for a in self.service.get_all()]), 200

    def get_by_id(self, artist_id):
        artist = self.service.get_by_id(artist_id)
        if not artist:
            return jsonify({'message': 'Artist not found'}), 404
        return jsonify(artist.to_dto()), 200

    def create(self):
        data = request.get_json()
        artist = self.service.create(data)
        return jsonify(artist.to_dto()), 201

    def update(self, artist_id):
        data = request.get_json()
        artist = self.service.update(artist_id, data)
        if not artist:
            return jsonify({'message': 'Artist not found'}), 404
        return jsonify(artist.to_dto()), 200

    def delete(self, artist_id):
        success = self.service.delete(artist_id)
        if not success:
            return jsonify({'message': 'Artist not found'}), 404
        return jsonify({'message': 'Deleted successfully'}), 200
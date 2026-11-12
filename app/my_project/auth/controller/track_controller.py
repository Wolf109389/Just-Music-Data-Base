from flask import jsonify, request
from app.my_project.auth.service.track_service import TrackService

class TrackController:
    def __init__(self):
        self.service = TrackService()

    def get_all(self):
        tracks = self.service.get_all_tracks()
        return jsonify([t.to_dto() for t in tracks]), 200

    def get_by_id(self, track_id):
        track = self.service.get_track_by_id(track_id)
        if not track:
            return jsonify({'message': 'Track not found'}), 404
        return jsonify(track.to_dto()), 200

    def get_by_album(self, album_id):
        # M:1 запит
        tracks = self.service.get_tracks_by_album(album_id)
        return jsonify([t.to_dto() for t in tracks]), 200

    def create(self):
        data = request.get_json()
        track = self.service.create_track(data)
        return jsonify(track.to_dto()), 201

    def update(self, track_id):
        data = request.get_json()
        track = self.service.update_track(track_id, data)
        if not track:
            return jsonify({'message': 'Track not found'}), 404
        return jsonify(track.to_dto()), 200

    def delete(self, track_id):
        success = self.service.delete_track(track_id)
        if not success:
            return jsonify({'message': 'Track not found'}), 404
        return jsonify({'message': 'Deleted successfully'}), 200
from flask import jsonify, request
from app.my_project.auth.service.playlist_service import PlaylistService

class PlaylistController:
    def __init__(self):
        self.service = PlaylistService()

    def get_all(self):
        playlists = self.service.get_all_playlists()
        return jsonify([p.to_dto() for p in playlists]), 200

    def get_playlist_tracks(self, playlist_id):
        # M:M запит через стикувальну таблицю
        tracks = self.service.get_tracks_in_playlist(playlist_id)
        if tracks is None:
            return jsonify({'message': 'Playlist not found'}), 404
        return jsonify([t.to_dto() for t in tracks]), 200

    def create(self):
        data = request.get_json()
        playlist = self.service.create_playlist(data)
        return jsonify(playlist.to_dto()), 201

    def add_track(self, playlist_id, track_id):
        success = self.service.add_track_to_playlist(playlist_id, track_id)
        if not success:
            return jsonify({'message': 'Failed to add track'}), 400
        return jsonify({'message': 'Track added to playlist'}), 200
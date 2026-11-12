from app.my_project.auth.dao.playlist_dao import PlaylistDAO

class PlaylistService:
    def __init__(self):
        self.dao = PlaylistDAO()

    def get_all_playlists(self):
        return self.dao.get_all()

    def get_tracks_in_playlist(self, playlist_id):
        return self.dao.get_tracks_by_playlist_id(playlist_id)

    def create_playlist(self, data):
        return self.dao.create(data)

    def add_track_to_playlist(self, playlist_id, track_id):
        return self.dao.add_track_to_playlist(playlist_id, track_id)

    def delete_playlist(self, playlist_id):
        return self.dao.delete(playlist_id)
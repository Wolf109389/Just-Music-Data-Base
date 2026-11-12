from app.my_project.auth.domain.models import db, Playlist, Track

class PlaylistDAO:
    def get_all(self):
        return Playlist.query.all()

    def get_by_id(self, playlist_id):
        return Playlist.query.get(playlist_id)

    def get_tracks_by_playlist_id(self, playlist_id):
        # Реалізація вибірки зі стикувальної таблиці зв'язку M:M
        playlist = self.get_by_id(playlist_id)
        return playlist.tracks if playlist else None

    def add_track_to_playlist(self, playlist_id, track_id):
        playlist = self.get_by_id(playlist_id)
        track = Track.query.get(track_id)
        if playlist and track and track not in playlist.tracks:
            playlist.tracks.append(track)
            db.session.commit()
            return True
        return False

    def create(self, playlist_data):
        playlist = Playlist(**playlist_data)
        db.session.add(playlist)
        db.session.commit()
        return playlist

    def delete(self, playlist_id):
        playlist = self.get_by_id(playlist_id)
        if playlist:
            db.session.delete(playlist)
            db.session.commit()
            return True
        return False
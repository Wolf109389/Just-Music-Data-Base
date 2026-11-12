from app.my_project.auth.dao.track_dao import TrackDAO

class TrackService:
    def __init__(self):
        self.dao = TrackDAO()

    def get_all_tracks(self):
        return self.dao.get_all()

    def get_track_by_id(self, track_id):
        return self.dao.get_by_id(track_id)

    def get_tracks_by_album(self, album_id):
        return self.dao.get_by_album_id(album_id)

    def create_track(self, data):
        return self.dao.create(data)

    def update_track(self, track_id, data):
        return self.dao.update(track_id, data)

    def delete_track(self, track_id):
        return self.dao.delete(track_id)
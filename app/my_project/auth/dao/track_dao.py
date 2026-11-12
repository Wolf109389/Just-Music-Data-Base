from app.my_project.auth.domain.models import db, Track

class TrackDAO:
    def get_all(self):
        return Track.query.all()

    def get_by_id(self, track_id):
        return Track.query.get(track_id)

    def get_by_album_id(self, album_id):
        # Реалізація зв'язку M:1 (отримати всі треки конкретного альбому)
        return Track.query.filter_by(album_id=album_id).all()

    def create(self, track_data):
        track = Track(**track_data)
        db.session.add(track)
        db.session.commit()
        return track

    def update(self, track_id, track_data):
        track = self.get_by_id(track_id)
        if track:
            for key, value in track_data.items():
                setattr(track, key, value)
            db.session.commit()
        return track

    def delete(self, track_id):
        track = self.get_by_id(track_id)
        if track:
            db.session.delete(track)
            db.session.commit()
            return True
        return False
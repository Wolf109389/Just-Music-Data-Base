import os

from flask import Blueprint
from flask import send_from_directory, abort

from app.my_project.auth.controller.artist_controller import ArtistController
from app.my_project.auth.controller.album_controller import AlbumController
from app.my_project.auth.controller.track_controller import TrackController
from app.my_project.auth.controller.playlist_controller import PlaylistController

from app.my_project.auth.domain.models import Track

api_bp = Blueprint('api', __name__, url_prefix='/api')

artist_ctrl = ArtistController()
album_ctrl = AlbumController()
track_ctrl = TrackController()
playlist_ctrl = PlaylistController()

# --- Artists ---
api_bp.add_url_rule('/artists', endpoint='artist_get_all', view_func=artist_ctrl.get_all, methods=['GET'])
api_bp.add_url_rule('/artists/<int:artist_id>', endpoint='artist_get_by_id', view_func=artist_ctrl.get_by_id, methods=['GET'])
api_bp.add_url_rule('/artists', endpoint='artist_create', view_func=artist_ctrl.create, methods=['POST'])
api_bp.add_url_rule('/artists/<int:artist_id>', endpoint='artist_update', view_func=artist_ctrl.update, methods=['PUT'])
api_bp.add_url_rule('/artists/<int:artist_id>', endpoint='artist_delete', view_func=artist_ctrl.delete, methods=['DELETE'])

# --- Albums ---
api_bp.add_url_rule('/albums', endpoint='album_get_all', view_func=album_ctrl.get_all, methods=['GET'])
api_bp.add_url_rule('/albums/<int:album_id>', endpoint='album_get_by_id', view_func=album_ctrl.get_by_id, methods=['GET'])
api_bp.add_url_rule('/albums', endpoint='album_create', view_func=album_ctrl.create, methods=['POST'])
api_bp.add_url_rule('/albums/<int:album_id>', endpoint='album_update', view_func=album_ctrl.update, methods=['PUT'])
api_bp.add_url_rule('/albums/<int:album_id>', endpoint='album_delete', view_func=album_ctrl.delete, methods=['DELETE'])

# --- Tracks ---
api_bp.add_url_rule('/tracks', endpoint='track_get_all', view_func=track_ctrl.get_all, methods=['GET'])
api_bp.add_url_rule('/tracks/<int:track_id>', endpoint='track_get_by_id', view_func=track_ctrl.get_by_id, methods=['GET'])
api_bp.add_url_rule('/tracks', endpoint='track_create', view_func=track_ctrl.create, methods=['POST'])
api_bp.add_url_rule('/tracks/<int:track_id>', endpoint='track_update', view_func=track_ctrl.update, methods=['PUT'])
api_bp.add_url_rule('/tracks/<int:track_id>', endpoint='track_delete', view_func=track_ctrl.delete, methods=['DELETE'])

# --- Запит M:1 (усі треки обраного альбому) ---
api_bp.add_url_rule('/albums/<int:album_id>/tracks', endpoint='album_get_tracks', view_func=track_ctrl.get_by_album, methods=['GET'])

# --- Playlists & Зв'язок M:M ---
api_bp.add_url_rule('/playlists', endpoint='playlist_get_all', view_func=playlist_ctrl.get_all, methods=['GET'])
api_bp.add_url_rule('/playlists', endpoint='playlist_create', view_func=playlist_ctrl.create, methods=['POST'])
api_bp.add_url_rule('/playlists/<int:playlist_id>/tracks', endpoint='playlist_get_tracks', view_func=playlist_ctrl.get_playlist_tracks, methods=['GET'])
api_bp.add_url_rule('/playlists/<int:playlist_id>/tracks/<int:track_id>', endpoint='playlist_add_track', view_func=playlist_ctrl.add_track, methods=['POST'])

# Папка, де фізично лежать аудіофайли на сервері
AUDIO_FOLDER = os.path.join(os.getcwd(), 'static', 'music')

@api_bp.route('/stream/<int:track_id>', methods=['GET'])
@api_bp.route('/download/<int:track_id>', methods=['GET'])
def get_audio_file(track_id):
    track = Track.query.get(track_id)
    if not track or not track.file_path:
        abort(404)
        
    filename = os.path.basename(track.file_path)
    return send_from_directory(AUDIO_FOLDER, filename)

# Шлях веде до папки music_files у корені репозиторію Just-Music-Data-Base
MUSIC_DIR = os.path.join(os.getcwd(), 'music_files')

@api_bp.route('/tracks/<int:track_id>/audio', methods=['GET'])
def get_track_audio(track_id):
    track = Track.query.get(track_id)
    if not track or not track.file_path:
        abort(404, description="Track record not found in DB")

    filename = track.file_path
    full_path = os.path.join(MUSIC_DIR, filename)

    # Виводимо в консоль для діагностики:
    print(f"--> Шукаю файл за шляхом: {full_path}")

    if not os.path.isfile(full_path):
        abort(404, description=f"Audio file missing on server: {filename}")

    return send_from_directory(MUSIC_DIR, filename)
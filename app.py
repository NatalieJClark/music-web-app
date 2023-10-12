import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Routes ==
@app.route('/albums', methods=['POST'])
def post_albums():
    if has_invalid_album_parameters(request.form):
        return "You need to submit a title, release year and artist id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id']
    )
    repository.create(album)
    return '', 200

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return '\n'.join(
        f'{album}'
        for album in repository.all()
    )

def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form or \
        'artist_id' not in form

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


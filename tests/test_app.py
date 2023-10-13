"""
When I request GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)"

"""
When I request POST /albums
With title, release_year and artist_id arguments
Then that album is reflected in the list when I request GET /albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/albums", data={
        'title':'Voyage',
        'release_year': '2022',
        'artist_id': '2'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)\n" \
        "Album(13, Voyage, 2022, 2)"

"""
When I request POST /albums
With no data
I get a 400 status code and "You need to submit a title, release year and artist id"
And GET /albums gets an unaffected list
"""
def test_post_albums_wiith_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post('/albums')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit a title, release year and artist id"

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)"
    
"""
When I request GET /artists
I get a list of artists back
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
When I request POST /artists
With a name and genre
That artist is reflected in the list when I call GET /artists
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    post_response = web_client.post('/artists', data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"

"""
When I request POST /artists
With no data
I get a 400 status code and 'You need to submit a name and a genre'
And the GET /artists list is unaffected
"""
def test_post_artists_with_no_data(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    post_response = web_client.post('/artists')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == 'You need to submit a name and a genre'

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'
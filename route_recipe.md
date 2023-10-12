# Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
Body Parameters:
  title: string
  release_year: integer (string)
  artist_id: integer (string)

GET /albums
No parameters
  
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# POST /albums
# Parameters:
#   title=Voyage
#   release_year=2022
#   artist_id=2
# Expected response (200 OK):
#   (No content)
# GET /albums
# Expected response (200 OK):
"""
Album(1, 'Doolittle', 1989, 1),
Album(2, 'Surfer Rosa', 1988, 1),
Album(3, 'Waterloo', 1974, 2),
Album(4, 'Super Trouper', 1980, 2),
Album(5, 'Bossanova', 1990, 1),
Album(6, 'Lover', 2019, 3),
Album(7, 'Folklore', 2020, 3),
Album(8, 'I Put a Spell on You', 1965, 4),
Album(9, 'Baltimore', 1978, 4),
Album(10, 'Here Comes the Sun', 1971, 4),
Album(11, 'Fodder on My Wings', 1982, 4),
Album(12, 'Ring Ring', 1973, 2)
Album(13, 'Voyage', 2022, 2)
"""

# POST /albums
# Parameters:
# Expected response (400 Bad Request):
"""
You need to submit a title, release_year and artist_id
"""
# GET /albums
# Expected response (200 OK):
"""
Album(1, 'Doolittle', 1989, 1),
Album(2, 'Surfer Rosa', 1988, 1),
Album(3, 'Waterloo', 1974, 2),
Album(4, 'Super Trouper', 1980, 2),
Album(5, 'Bossanova', 1990, 1),
Album(6, 'Lover', 2019, 3),
Album(7, 'Folklore', 2020, 3),
Album(8, 'I Put a Spell on You', 1965, 4),
Album(9, 'Baltimore', 1978, 4),
Album(10, 'Here Comes the Sun', 1971, 4),
Album(11, 'Fodder on My Wings', 1982, 4),
Album(12, 'Ring Ring', 1973, 2)
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

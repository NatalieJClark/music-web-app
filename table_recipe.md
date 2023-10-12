# Single Table Design Recipe Template

## 1. Extract nouns from the user stories or specification

```python
# Request:
POST /albums
# With body parameters:
title=Voyage
release_year=2022
artist_id=2
# Expected response (200 OK)
(No content)
# Then subsequent request:
GET /albums
# Expected response (200 OK)
new album reflected
```

```python
# Request:
GET /artists
# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone


# Request:
POST /artists
# With body parameters:
name=Wild nothing
genre=Indie
# Expected response (200 OK)
(No content)
# Then subsequent request:
GET /artists
# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```
```
Nouns:

album, title, release year, artist, id
artist, name, genre
```

## 2. Infer the Table Name and Columns

| Record                | Properties                         |
| --------------------- | ---------------------------------- |
| album                 | id, title, release year, artist_id |
| artist                | id, name, genre                    |

Name of the table (always plural): `albums`

Column names: `id`, `title`, `release_year`, `artist_id`

Name of the table (always plural): `artists`

Column names: `id`, `name`, `genre`

## 3. Decide the column types

```
Table: albums
id: SERIAL
title: text
release_year: int
artist_id: int

Table: artists
id: SERIAL
name: text
genre: text
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: music_library.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_web_app < albums_table.sql
```
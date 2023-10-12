# Single Table Design Recipe Template

## 1. Extract nouns from the user stories or specification

```
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

Your test should assert that the new album is present in the list of records returned by GET /albums.
```

```
Nouns:

album, title, release year, artist, id
```

## 2. Infer the Table Name and Columns

| Record                | Properties                         |
| --------------------- | ---------------------------------- |
| album                 | id, title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `id`, `title`, `release_year`, `artist_id`

## 3. Decide the column types

```
Table: albums
id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_web_app < albums_table.sql
```
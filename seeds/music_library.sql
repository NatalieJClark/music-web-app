-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year, artist_id INT,
    artist_id INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Invisible Cities', 'Italo Calvino');
INSERT INTO albums (title, release_year, artist_id) VALUES ('The Man Who Was Thursday', 'GK Chesterton');
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bluets', 'Maggie Nelson');
INSERT INTO albums (title, release_year, artist_id) VALUES ('No Place on Earth', 'Christa Wolf');
INSERT INTO albums (title, release_year, artist_id) VALUES ('Nevada', 'Imogen Binnie');
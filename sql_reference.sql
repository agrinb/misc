-- Actors sorted alphabetically
SELECT actors.name FROM actors ORDER BY actors.name;

-- Visiting /actors/:id will show the details for a given actor.
-- This page should contain a list of movies that the actor has starred
-- in and what their role was. Each movie should link to the details
-- page for that movie.
SELECT movies.title, cast_members.character FROM movies
  JOIN cast_members ON movies.id = cast_members.movie_id
  WHERE cast_members.actor_id = 60;

-- Visiting /movies will show a table of movies, sorted alphabetically by title.
-- The table includes the movie title, the year it was released, the rating,
-- the genre, and the studio that produced it. Each movie title is a
-- link to the details page for that movie.
SELECT movies.title AS title, movies.year AS year, movies.rating AS rating, genres.name AS genre, studios.name AS studio FROM movies
  JOIN genres ON movies.genre_id = genres.id
  JOIN studios ON movies.studio_id = studios.id;

-- Visiting /movies/:id will show the details for the movie.
-- This page should contain information about the movie
-- (including genre and studio) as well as a list
-- of all of the actors and their roles. Each actor name
-- is a link to the details page for that actor.
SELECT genres.name, studios.name, actors.name, cast_members.character FROM movies
  JOIN genres ON movies.genre_id = genres.id
  JOIN studios ON movies.studio_id = studios.id
  JOIN cast_members ON movies.id = cast_members.movie_id
  JOIN actors ON actors.id = cast_members.actor_id
  WHERE movies.id = 'POTATO';

-- find movie details
SELECT movies.title AS title, genres.name AS genre, studios.name AS studio FROM movies
                JOIN genres ON movies.genre_id = genres.id
                JOIN studios ON movies.studio_id = studios.id
                WHERE movies.id = $1;


-- find character details
SELECT actors.id AS id, actors.name AS name, cast_members.character AS character
  FROM actors
  JOIN cast_members ON actors.id = cast_members.actor_id
  JOIN movies ON cast_members.movie_id = movies.id
  WHERE movies.id = $1;

SELECT genres.name AS genre FROM genres
JOIN movies ON movies.genre_id = genres.id WHERE movies.title LIKE '%Jumpout%';

"INSERT INTO movies (title, year, rating, genre_id, created_at) " +
    "VALUES ($1, $2, $3, $4, NOW())"

INSERT INTO movies (studio_id) VALUES (2) WHERE movies.title LIKE '%Jump%';

UPDATE movies SET studio_id = 2 WHERE movies.title LIKE '%Jump%';

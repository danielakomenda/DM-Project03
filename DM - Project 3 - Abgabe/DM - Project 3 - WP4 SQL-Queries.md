# Data Management – Project 3 – WP 4
## SQL-Queries to select specific data

### Subpart 1
```sql
-- Returns Value A.1
SELECT name FROM League;
-- > returns all name of the table League
 
-- Returns Value A.1 and A.2
SELECT name, country FROM League;
-- > returns all name and country of the table League
 
-- Returns Value A.2
SELECT country FROM League;
-- > returns all the country of the table League
```


### Subpart 2
```sql
-- Returns the A.1 and the numbers of instances in B
SELECT League.name, COUNT(*) AS num_games
FROM League, Game
WHERE Game.league_id=League.id
GROUP BY Game.league_id
ORDER BY num_games DESC
-- > returns the name of the league and the number of games that are played in this league
```


### Subpart 3
```sql
-- Returns the A.1 of all the values B.2 that match the given datetime
SELECT League.id
FROM League, Game
WHERE Game.league_id=League.id
AND Game.date = "2009-05-04 00:00:00";
-- > returns the league-id for all the games that took place at the datetime “2009-05-04 00:00:00”

-- Returns the A.1 of all the values B.2 that match the given date
SELECT League.id
FROM League, Game
WHERE Game.league_id=League.id
AND Game.date LIKE  "2009-05-04%";
-- > returns the league-id for all the games that took place at the date "2009-05-04"

-- Returns the A.2 of all the values B.2 that match the given date
SELECT League.name
FROM League, Game
WHERE Game.league_id=League.id
AND Game.date LIKE "2009-05-04%";
-- > returns the league-name for all the games that took place at the date "2009-05-04"
```


### Other interesting Queries
```sql
-- Returns A.1, B.1, B.2, B.3,  C.1-Home, C.1-Away
SELECT
League.name AS league,
Game.season,
Game.date, 
hometeam.long_name AS home_team,
home_team_goal, 
away_team_goal,
awayteam.long_name AS away_team

FROM Game, League
LEFT JOIN Team AS hometeam ON hometeam.id = Game.home_team_id
LEFT JOIN Team AS awayteam ON awayteam.id = Game.away_team_id
WHERE League.id=Game.league_id

-- > returns the league-name, the game-date, the home-team, the away-team, 
-- > the numbers of goals for the home-team, the number of goals for the away-team
-- > for all the games


-- Returns A.1, B.1, B.2, B.3,  C.1-Home, C.1-Away for a given B.2
SELECT
League.name AS league,
Game.season,
Game.date,
hometeam.long_name AS home_team,
home_team_goal, 
away_team_goal,
awayteam.long_name AS away_team

FROM Game, League
LEFT JOIN Team AS hometeam ON hometeam.id = Game.home_team_id
LEFT JOIN Team AS awayteam ON awayteam.id = Game.away_team_id
WHERE League.id=Game.league_id
AND Game.date LIKE "2008-08-09%"  -- > This value can be changed to another date

-- > returns the league-name, the game-date, the home-team, the away-team, 
-- > the numbers of goals for the home-team, the number of goals for the away-team
-- > for a game of a specific date
```
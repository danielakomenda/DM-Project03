# Data Management – Project 3 – WP 2
## Design your relational database


```sql
-- League-Table
CREATE TABLE League (
id INTEGER PRIMARY KEY AUTOINCREMENT,
country TEXT,
name TEXT UNIQUE);
 

-- Player-Table
CREATE TABLE Player (
id INTEGER UNIQUE PRIMARY KEY,
name TEXT,
birthday TEXT,
height INTEGER,
weight INTEGER
);

-- Team-Table
CREATE TABLE Team (
id INTEGER UNIQUE PRIMARY KEY,
long_name TEXT,
short_name TEXT
);
 
-- Game-Table
CREATE TABLE Game (
id INTEGER UNIQUE PRIMARY KEY,
season TEXT,
date TEXT,
home_team_goal INTEGER,
away_team_goal INTEGER,
league_id INTEGER,
home_team_id INTEGER,
away_team_id INTEGER,
home_player_1 INTEGER,
home_player_2 INTEGER,
home_player_3 INTEGER,
home_player_4 INTEGER,
home_player_5 INTEGER,
home_player_6 INTEGER,
home_player_7 INTEGER,
home_player_8 INTEGER,
home_player_9 INTEGER,
home_player_10 INTEGER,
home_player_11 INTEGER,
away_player_1 INTEGER,
away_player_2 INTEGER,
away_player_3 INTEGER,
away_player_4 INTEGER,
away_player_5 INTEGER,
away_player_6 INTEGER,
away_player_7 INTEGER,
away_player_8 INTEGER,
away_player_9 INTEGER,
away_player_10 INTEGER,
away_player_11 INTEGER,


FOREIGN KEY (league_id) REFERENCES League (id),
FOREIGN KEY (home_team_id) REFERENCES Team (id),
FOREIGN KEY (away_team_id) REFERENCES Team (id),
FOREIGN KEY (home_player_1) REFERENCES Player (id),
FOREIGN KEY (home_player_2) REFERENCES Player (id),
FOREIGN KEY (home_player_3) REFERENCES Player (id),
FOREIGN KEY (home_player_4) REFERENCES Player (id),
FOREIGN KEY (home_player_5) REFERENCES Player (id),
FOREIGN KEY (home_player_6) REFERENCES Player (id),
FOREIGN KEY (home_player_7) REFERENCES Player (id),
FOREIGN KEY (home_player_8) REFERENCES Player (id),
FOREIGN KEY (home_player_9) REFERENCES Player (id),
FOREIGN KEY (home_player_10) REFERENCES Player (id),
FOREIGN KEY (home_player_11) REFERENCES Player (id),
FOREIGN KEY (away_player_1) REFERENCES Player (id),
FOREIGN KEY (away_player_2) REFERENCES Player (id),
FOREIGN KEY (away_player_3) REFERENCES Player (id),
FOREIGN KEY (away_player_4) REFERENCES Player (id),
FOREIGN KEY (away_player_5) REFERENCES Player (id),
FOREIGN KEY (away_player_6) REFERENCES Player (id),
FOREIGN KEY (away_player_7) REFERENCES Player (id),
FOREIGN KEY (away_player_8) REFERENCES Player (id),
FOREIGN KEY (away_player_9) REFERENCES Player (id),
FOREIGN KEY (away_player_10) REFERENCES Player (id),
FOREIGN KEY (away_player_11) REFERENCES Player (id) 
);
```

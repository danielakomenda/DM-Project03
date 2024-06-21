# Data Management – Project 3 – WP 5
## Queries to export data from SQL and import data to Neo4j

### SQL-Query 1
```sql
SELECT id, long_name FROM Team

-- > Returns a list of all the teams with their ID and Name
```

### SQL-Query 2
```sql
SELECT DISTINCT
Player.name AS goal_keeper,
g1.home_team_id AS first_team, 
g2.home_team_id AS second_team
FROM Game g1, Game g2
LEFT JOIN Player ON Player.id = g1.home_player_1
WHERE g1.home_player_1 = g2.home_player_1
AND first_team < second_team

-- > Returns all team-pairs where the goalkeeper (player_1) played for both teams at some point
```


### Cypher-Query 1
```cypher
LOAD CSV WITH HEADERS FROM 'file:///teams.csv' AS row
WITH toInteger(row.id) as teamID, row.long_name as teamName
MERGE (t:Team {teamID: teamID})
SET t.teamID = teamID, t.teamName = teamName
RETURN count(t)
```

### Cypher-Query 2
```cypher
LOAD CSV WITH HEADERS FROM 'file:///team_link.csv' AS row
WITH row.goal_keeper as goalKeeper, toInteger(row.first_team) as firstTeam, toInteger(row.second_team) as secondTeam
MATCH(team1:Team {teamID:firstTeam})
MATCH(team2:Team {teamID:secondTeam})
MERGE (team1)-[:shared_goalkeeper {name:goalKeeper}]-(team2)
RETURN count(goalKeeper)
```


import datetime
from pathlib import Path

import pandas as pd
import sqlite3
import random


# The path probably has to be changed
path_to_db = Path(__file__).resolve().parents[1] / "football.sqlite"


def ask_again():
    incorrect = True
    while incorrect:
        answer = input("Wanna play again? Use 'y' or 'n' ")
        if answer == "n":
            return False
        elif answer == "y":
            return True
        else:
            print("Wrong input")
            incorrect = True


def run_quiz(dataframe):
    a = 0
    b = len(dataframe.index) - 1
    row = random.randint(a, b)

    goal_home = dataframe.loc[row, "home_team_goal"].item()
    goal_away = dataframe.loc[row, "away_team_goal"].item()

    print(
        f"The game took place on {dataframe.loc[row, 'date']}. "
        f"The teams were {dataframe.loc[row, 'home_team']} : {dataframe.loc[row, 'away_team']}"
    )

    guess = input("What is your result guess? ")
    print(f"The correct answer is {goal_home}:{goal_away}.")
    return check_answer(guess, goal_home, goal_away)


def check_answer(guess, goal_home, goal_away):
    run_points = 0
    guess = guess.split(":")

    guess_home = int(guess[0])
    guess_away = int(guess[1])

    message = f"You didn't guess correctly."

    if guess_home == goal_home and guess_away == goal_away:
        run_points = 3
        message = f"You guessed the result correctly."

    else:
        if (goal_home < goal_away and guess_home < guess_away) or (goal_home > goal_away and guess_home > guess_away):
            run_points = 1
            message = f"You guessed the winner correctly."
            
        if guess_home == goal_home:
            run_points += 1
            if run_points == 1:
                message = f"You guessed the amount of goals of the home team correctly."
            else:
                message += f" And you guessed the amount of goals of the home team correctly."

        elif guess_away == goal_away:
            run_points += 1
            if run_points == 1:
                message = f"You guessed the amount of goals of the away team correctly."
            else:   
                message += f" And you guessed the amount of goals of the away team correctly."
        
    message += f" You achieved {run_points} Points."

    print(message)
    return run_points


def add_to_db(input_name, input_points, input_runs, input_average):
    date = datetime.datetime.now(datetime.timezone.utc)

    input_data = [date, input_name, input_points, input_runs, input_average]
    cur = connection.cursor()




    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Bestlist (
            date           DATETIME,
            name           TEXT,
            total_points   INTEGER,
            num_of_games   INTEGER,
            average_points NUMERIC
        );"""
    )
    connection.commit()
    cur.execute(
        """
        INSERT INTO Bestlist (date, name, total_points, num_of_games, average_points) VALUES (?, ?, ?, ?, ?);""",
        input_data
    )
    connection.commit()
    connection.close()


connection = sqlite3.connect(path_to_db)

query = """SELECT
Game.date,
home_team_goal, 
away_team_goal,
hometeam.long_name AS home_team,
awayteam.long_name AS away_team

FROM Game, League
LEFT JOIN Team AS hometeam ON hometeam.id = Game.home_team_id
LEFT JOIN Team AS awayteam ON awayteam.id = Game.away_team_id
WHERE League.id=Game.league_id
"""


try:
    points = 0
    runs = 0
    df = pd.read_sql_query(query, connection)
    run = True
    while run:
        points += run_quiz(df)
        runs += 1
        print(f"You have now {points} Points for {runs} Runs. This is an average of {round(points/runs, 2)}")
        run = ask_again()

    name = input("What is your name? ")
    average = round(points/runs, 2)
    add_to_db(name, points, runs, average)


finally:
    connection.close()

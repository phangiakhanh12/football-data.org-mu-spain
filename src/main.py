import os
import requests

API_TOKEN = os.getenv("API_TOKEN")
HEADERS = {"X-Auth-Token": API_TOKEN}

LEAGUES = {
    "Premier League": "PL",
    "La Liga": "PD",
    "Serie A": "SA"
}

def get_recent_matches(league_code):
    url = f"https://api.football-data.org/v4/competitions/{league_code}/matches?status=FINISHED&limit=5"
    response = requests.get(url, headers=HEADERS)
    matches = response.json().get('matches', [])
    return matches

def get_top_scorers(league_code):
    url = f"https://api.football-data.org/v4/competitions/{league_code}/scorers?limit=3"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('scorers', [])

def display_league_info():
    for league_name, league_code in LEAGUES.items():
        print(f"\n=== {league_name} ===")
        
        # Recent Matches
        matches = get_recent_matches(league_code)
        print("\n📅 Recent Matches:")
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            score = match['score']['fullTime']
            print(f"{home_team} {score['home']} - {score['away']} {away_team}")

def display_top_scorers():
    for league_name, league_code in LEAGUES.items():
        print(f"\n=============== {league_name} ===============")
        scorers = get_top_scorers(league_code)
        if not scorers:
            print("No scorers data available.")
            continue
        for i, scorer in enumerate(scorers, start=1):
            player = scorer['player']['name']
            team = scorer['team']['name']
            goals = scorer['goals']
            print(f"{i}. {player} ({team}) - {goals} goals")

if __name__ == "__main__":
    display_league_info()
    display_top_scorers()

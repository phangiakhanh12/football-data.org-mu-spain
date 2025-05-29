import os
import requests

API_TOKEN = os.getenv("API_TOKEN")
HEADERS = {"X-Auth-Token": API_TOKEN}

LEAGUES = {
    "Premier League": "PL",
    "La Liga": "PD",
    "Serie A": "SA"
}

OUTPUT_FILE = "league_summary.txt"

def get_recent_matches(league_code):
    url = f"https://api.football-data.org/v4/competitions/{league_code}/matches?status=FINISHED&limit=5"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('matches', [])

def get_top_scorers(league_code):
    url = f"https://api.football-data.org/v4/competitions/{league_code}/scorers?limit=3"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('scorers', [])

def generate_summary():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for league_name, league_code in LEAGUES.items():
            file.write(f"\n=============== {league_name.upper()} ===============\n\n")

            # Recent Matches
            try:
                matches = get_recent_matches(league_code)
                file.write("📅 Recent Matches:\n")
                for match in matches:
                    home = match['homeTeam']['name']
                    away = match['awayTeam']['name']
                    score = match['score']['fullTime']
                    file.write(f"{home} {score['home']} - {score['away']} {away}\n")
            except Exception as e:
                file.write(f"Error fetching recent matches for {league_name}: {e}\n")

            # Top Scorers
            try:
                scorers = get_top_scorers(league_code)
                file.write("\n🔥 Top 3 Scorers:\n")
                for i, scorer in enumerate(scorers, start=1):
                    name = scorer['player']['name']
                    team = scorer['team']['name']
                    goals = scorer['goals']
                    file.write(f"{i}. {name} ({team}) - {goals} goals\n")
            except Exception as e:
                file.write(f"Error fetching top scorers for {league_name}: {e}\n")

if __name__ == "__main__":
    generate_summary()

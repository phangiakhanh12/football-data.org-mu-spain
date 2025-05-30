import os
import requests
from datetime import datetime

API_TOKEN = os.getenv("API_TOKEN")
HEADERS = {"X-Auth-Token": API_TOKEN}

LEAGUES = {
    "Premier League": "PL",
    "La Liga": "PD",
    "Serie A": "SA"
}

OUTPUT_FILE = "league_summary.txt"

def get_recent_matches(league_code):
    url = f"https://api.football-data.org/v4/competitions/{league_code}/matches?status=FINISHED"
    response = requests.get(url, headers=HEADERS)
    matches = response.json().get('matches', [])

    # Sort by match date (most recent first)
    matches.sort(key=lambda x: x['utcDate'], reverse=True)

    # Return only the 5 most recent
    return matches[:5]

def get_top_scorers(league_code):
    url = f"https://api.football-data.org/v4/competitions/{league_code}/scorers?limit=3"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('scorers', [])

def write_league_info_to_file():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for league_name, league_code in LEAGUES.items():
            file.write(f"\n=============== {league_name} ===============\n")
            
            # Recent Matches
            matches = get_recent_matches(league_code)
            file.write("\n📅 Recent Matches:\n")
            for match in matches:
                home_team = match['homeTeam']['name']
                away_team = match['awayTeam']['name']
                score = match['score']['fullTime']
                file.write(f"{home_team} {score['home']} - {score['away']} {away_team}\n")
            
            # # Top Scorers
            # file.write("\n🔥 Top Scorers:\n")
            # scorers = get_top_scorers(league_code)
            # if not scorers:
            #     file.write("No scorers data available.\n")
            # else:
            #     for i, scorer in enumerate(scorers, start=1):
            #         player = scorer['player']['name']
            #         team = scorer['team']['name']
            #         goals = scorer['goals']
            #         file.write(f"{i}. {player} ({team}) - {goals} goals\n")

        # 🕒 Add current time at the end
        current_time = datetime.now()
        file.write(f"\n⏱️  Data last updated at: {current_time.strftime('%H:%M:%S')}\n")

if __name__ == "__main__":
    write_league_info_to_file()


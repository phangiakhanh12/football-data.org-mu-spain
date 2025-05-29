import os
import requests
from datetime import datetime, timedelta

API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_TOKEN}

def get_next_match(team_id):
    url = f"{BASE_URL}/teams/{team_id}/matches?status=SCHEDULED&limit=1"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error fetching next match for team {team_id}: {response.status_code} - {response.text}")
        return "No upcoming matches (API error)"

    data = response.json()

    if not data.get("matches"):
        return "No upcoming matches"

    match = data["matches"][0]
    home_team = match["homeTeam"]["name"]
    away_team = match["awayTeam"]["name"]
    match_date = match["utcDate"]

    return f"{home_team} vs {away_team} on {match_date}"




def get_recent_match(team_id):
    url = f"{BASE_URL}/teams/{team_id}/matches?status=FINISHED&limit=1"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Error fetching recent match: {response.status_code}")
        return None
    
    data = response.json()
    matches = data.get("matches", [])
    return matches[0] if matches else None



def get_goal_scorers_and_ratings(match):
    home_team = match["homeTeam"]["name"]
    away_team = match["awayTeam"]["name"]
    score = f"{match['score']['fullTime']['home']} - {match['score']['fullTime']['away']}"
    match_info = f"{home_team} vs {away_team} | Final Score: {score}"

    # Ratings are not provided by Football-Data.org; mock for now
    top_players = [("Player A", 8.1), ("Player B", 7.9), ("Player C", 7.8)]
    scorers = ["Player A", "Player B"]  # Mock list

    return match_info, top_players, scorers

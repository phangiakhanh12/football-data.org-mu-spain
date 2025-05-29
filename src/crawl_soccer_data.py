from utils import get_next_match, get_recent_match, get_goal_scorers_and_ratings
import os

OUTPUT_DIR = "summaries"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TEAM_IDS = {
    "Manchester United": 66,
    "Spain National Team": 758
}

def generate_summary(team_name, team_id):
    print(f"\n📊 Generating summary for {team_name}...")

    next_match = get_next_match(team_id)
    recent_match = get_recent_match(team_id)

    if recent_match:
        match_info, top_players, scorers = get_goal_scorers_and_ratings(recent_match)
    else:
        match_info = "No recent match found."
        top_players = []
        scorers = []

    summary = f"""
==== {team_name} Weekly Summary ====

🗓️ Next Match:
{next_match}

⚽ Most Recent Match:
{match_info}

🔥 Top 3 Players:
{', '.join([f"{name} ({rating})" for name, rating in top_players])}

🥅 Goal Scorers:
{', '.join(scorers)}

===============================
"""
    with open(f"{OUTPUT_DIR}/{team_name.replace(' ', '_').lower()}_summary.txt", "w") as f:
        f.write(summary)
    print(summary)


if __name__ == "__main__":
    for team, team_id in TEAM_IDS.items():
        generate_summary(team, team_id)

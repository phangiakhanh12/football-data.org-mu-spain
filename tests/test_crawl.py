import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ["API_TOKEN"] = os.getenv("API_TOKEN", "dummy_token")  # fallback for test

from src.utils import get_next_match, get_recent_match, get_goal_scorers_and_ratings


def test_next_match():
    man_utd_id = 66
    result = get_next_match(man_utd_id)

    assert isinstance(result, str), f"Expected string but got {type(result)}"
    assert "vs" in result or "No upcoming matches" in result



def test_recent_match():
    man_utd_id = 66
    match = get_recent_match(man_utd_id)
    assert match is None or "homeTeam" in match

def test_goal_scorers_and_ratings():
    match = {
        "homeTeam": {"name": "Team A"},
        "awayTeam": {"name": "Team B"},
        "score": {"fullTime": {"home": 2, "away": 1}}
    }
    match_info, players, scorers = get_goal_scorers_and_ratings(match)
    assert "vs" in match_info
    assert len(players) == 3

from types import SimpleNamespace

from logic_utils import check_guess, start_new_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_guess_too_high_returns_lower_hint():
    # Bug regression: a guess above the secret must hint to go LOWER, not higher
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low_returns_higher_hint():
    # Bug regression: a guess below the secret must hint to go HIGHER, not lower
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_winning_guess_returns_correct_message():
    # A correct guess should report the Win outcome and the success message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_new_game_resets_attempts():
    # A game in progress with attempts should reset to 0
    state = SimpleNamespace(secret=42, attempts=5, score=80, status="lost", history=[10, 20])
    start_new_game(state, 1, 100)
    assert state.attempts == 0

def test_new_game_resets_score():
    # Score should reset to 0 on a new game
    state = SimpleNamespace(secret=42, attempts=5, score=80, status="lost", history=[10, 20])
    start_new_game(state, 1, 100)
    assert state.score == 0

def test_new_game_resets_status_to_playing():
    # A finished game ("won"/"lost") should return to "playing"
    state = SimpleNamespace(secret=42, attempts=5, score=80, status="won", history=[10, 20])
    start_new_game(state, 1, 100)
    assert state.status == "playing"

def test_new_game_clears_history():
    # Previous guesses should be wiped out
    state = SimpleNamespace(secret=42, attempts=5, score=80, status="lost", history=[10, 20, 30])
    start_new_game(state, 1, 100)
    assert state.history == []

def test_new_game_picks_secret_in_range():
    # The new secret should fall within the given [low, high] range
    state = SimpleNamespace(secret=0, attempts=5, score=80, status="lost", history=[10])
    start_new_game(state, 1, 20)
    assert 1 <= state.secret <= 20

# --- New Game: secret respects the selected difficulty range ---

# Difficulty -> (low, high), mirroring get_range_for_difficulty in app.py.
# Encoded locally because app.py runs Streamlit at import time and the
# logic_utils version of get_range_for_difficulty is not implemented yet.
DIFFICULTY_RANGES = {
    "Easy": (1, 20),
    "Normal": (1, 100),
    "Hard": (1, 50),
}

def test_new_game_easy_secret_in_range():
    # A new game on Easy must pick a secret inside the Easy range (1-20)
    low, high = DIFFICULTY_RANGES["Easy"]
    state = SimpleNamespace(secret=0, attempts=5, score=80, status="lost", history=[10])
    # Repeat: secret is random, so one draw could mask an out-of-range bug
    for _ in range(200):
        start_new_game(state, low, high)
        assert low <= state.secret <= high

def test_new_game_normal_secret_in_range():
    # A new game on Normal must pick a secret inside the Normal range (1-100)
    low, high = DIFFICULTY_RANGES["Normal"]
    state = SimpleNamespace(secret=0, attempts=5, score=80, status="lost", history=[10])
    for _ in range(200):
        start_new_game(state, low, high)
        assert low <= state.secret <= high

def test_new_game_hard_secret_in_range():
    # A new game on Hard must pick a secret inside the Hard range (1-50)
    low, high = DIFFICULTY_RANGES["Hard"]
    state = SimpleNamespace(secret=0, attempts=5, score=80, status="lost", history=[10])
    for _ in range(200):
        start_new_game(state, low, high)
        assert low <= state.secret <= high

def test_new_game_resets_attempts_to_zero():
    # Reset must set attempts to 0, regardless of the prior count (startup uses 1)
    state = SimpleNamespace(secret=42, attempts=1, score=80, status="playing", history=[])
    start_new_game(state, 1, 100)
    assert state.attempts == 0

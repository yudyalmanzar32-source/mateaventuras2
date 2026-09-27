from database.schema import init_db
from services.progress_service import log_attempt, get_student_stats

def test_progress_stats_without_users():
    init_db()
    # Log an attempt without requiring a user ID
    log_attempt(None, 1, "4", 1)
    stats = get_student_stats()
    assert stats['total'] >= 1
    assert stats['correct'] >= 1

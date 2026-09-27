from database.connection import get_db

def log_attempt(student_id, question_id, selected_answer, is_correct):
    conn = get_db()
    conn.execute("INSERT INTO attempts (student_id, question_id, selected_answer, is_correct) VALUES (?, ?, ?, ?)",
                 (student_id, question_id, selected_answer, is_correct))
    conn.commit()
    conn.close()

def get_student_stats(student_id=None):
    conn = get_db()
    if student_id is not None:
        stats = conn.execute('''SELECT COUNT(*) as total, SUM(is_correct) as correct 
                                FROM attempts WHERE student_id = ?''', (student_id,)).fetchone()
    else:
        stats = conn.execute('''SELECT COUNT(*) as total, SUM(is_correct) as correct 
                                FROM attempts''').fetchone()
    conn.close()
    return {'total': stats['total'] if stats['total'] else 0, 
            'correct': stats['correct'] if stats['correct'] else 0}


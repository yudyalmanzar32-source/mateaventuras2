from services.ai_generator import validate_ai_output
import json
def test_valid_ai_output():
    mock_json = json.dumps([{"question": "1+1", "options": ["1", "2", "3"], "correct_answer": "2"}])
    assert validate_ai_output(mock_json) == True

def test_invalid_ai_output():
    mock_json = json.dumps([{"question": "1+1", "options": ["1", "3", "4"], "correct_answer": "2"}])
    assert validate_ai_output(mock_json) == False

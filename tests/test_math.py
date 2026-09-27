from services.math_engine import validate_math_operation
def test_valid_operation():
    assert validate_math_operation("¿Cuánto es 2 + 2?", "4") == True

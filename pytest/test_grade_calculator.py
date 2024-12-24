import pytest

def grade_calculator(score):
    if (score > 100):
        return "Invalid"
    elif (score >= 70):
        return "Outstanding"
    elif (score >= 60):
        return "Good"
    elif (score >= 50):
        return "Satisfactory"
    elif (score >= 40):
        return "Sufficient"
    elif (score >= 30):
        return "Unsatisfactory"
    elif (score >= 0):
        return "Fail"
    else:
        return "Invalid"

@pytest.mark.parametrize("score,expected_outcome",[
    (100.1,"Invalid"),
    (100,"Outstanding"),
    (69,"Good"),
    (59,"Satisfactory"),
    (49,"Sufficient"),
    (39,"Unsatisfactory"),
    (29,"Fail"),
    (-1,"Invalid")
])
def test_grade_calculator(score,expected_outcome):
    assert grade_calculator(score) == expected_outcome

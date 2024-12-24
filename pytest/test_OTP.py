import pytest

def OTP_length_detection(OTP):
    OTP_length = len(str(OTP))

    if(OTP_length >= 7 or OTP_length <= 5):
        return "Invalid"
    else:
        return "Valid"

def OTP_format_detection(OTP):
    OTP_check = (str(OTP)).isdecimal()

    if(OTP_check):
        return "Valid"
    else:
        return "Invalid"

@pytest.mark.parametrize("OTP,expected_outcome",[
    ("A12B0","Invalid"),
    ("03461","Invalid"),
    ("01F36T","Valid"),
    ("005390","Valid"),
    ("AB471G3","Invalid"),
    ("0833589","Invalid")
])
def test_OTP_length(OTP,expected_outcome):
    assert OTP_length_detection(OTP) == expected_outcome

@pytest.mark.parametrize("OTP,expected_outcome",[
    ("A12B0","Invalid"),
    ("03461","Valid"),
    ("01F36T","Invalid"),
    ("005390","Valid"),
    ("AB471G3","Invalid"),
    ("0833589","Valid")
])
def test_OTP_format(OTP,expected_outcome):
    assert OTP_format_detection(OTP) == expected_outcome

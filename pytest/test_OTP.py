import pytest

def OTP_length_detection(OTP):
    OTP_length = len(str(OTP))

    if(OTP_length >= 7 or OTP_length <= 5):
        return "Invalid length"
    else:
        return "Valid length"

def OTP_format_detection(OTP):
    OTP_check = (str(OTP)).isdecimal()

    if(OTP_check):
        return "Valid format"
    else:
        return "Invalid format"

@pytest.mark.parametrize("OTP,expected_length_outcome,expected_format_outcome",[
    ("A12B0","Invalid length","Invalid format"),
    ("03461","Invalid length","Valid format"),
    ("01F36T","Valid length","Invalid format"),
    ("005390","Valid length","Valid format"),
    ("AB471G3","Invalid length","Invalid format"),
    ("0833589","Invalid length","Valid format")
])
def test_OTP_validation(OTP,expected_length_outcome,expected_format_outcome):
    assert OTP_length_detection(OTP) == expected_length_outcome
    assert OTP_format_detection(OTP) == expected_format_outcome
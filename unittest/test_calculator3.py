import pytest

from calculator import square

def test_positive():
    assert square(2) == 4, "Test failed: square(2) should be 4"
    assert square(3) == 9, "Test failed: square(3) should be 9"
    
def test_negative():
    assert square(-2) == 4, "Test failed: square(-2) should be 4"
    assert square(-3) == 9, "Test failed: square(-3) should be 9"
    
def test_zero():
    assert square(0) == 0, "Test failed: square(0) should be 0"
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")

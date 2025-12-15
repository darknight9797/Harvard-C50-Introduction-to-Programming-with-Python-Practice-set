from calculator import square

def test_square():
    assert square(2) == 4, "Test failed: square(2) should be 4"
    assert square(3) == 9, "Test failed: square(3) should be 9"
    assert square(-2) == 4, "Test failed: square(-2) should be 4"
    assert square(-3) == 9, "Test failed: square(-3) should be 9"
    assert square(0) == 0, "Test failed: square(0) should be 0"
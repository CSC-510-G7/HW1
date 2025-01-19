import pytest
from myfile import fib_slow, fib_fast

@pytest.mark.timeout(1)
def test_fib_fast():
    assert fib_fast(0) == 0
    assert fib_fast(1) == 1
    assert fib_fast(2) == 1
    assert fib_fast(3) == 2
    assert fib_fast(4) == 3
    assert fib_fast(100) == 354_224_848_179_261_915_075

@pytest.mark.timeout(1)
def test_fib_slow():
    assert fib_slow(0) == 0
    assert fib_slow(1) == 1
    assert fib_slow(2) == 1
    assert fib_slow(3) == 2
    assert fib_slow(4) == 3
    assert fib_slow(100) == 354_224_848_179_261_915_075

# To run tests/test_core.py and check that everything is working:
# 1. Install pytest (if not already installed):
#     pip install pytest
# 2. Navigate to the project root (the directory containing pyproject.toml).
# 3. Run pytest:
#     pytest -q
# The -q flag runs tests in “quiet” mode, showing only minimal output.

from p2c.core import build

def test_build_and_callable():
    a, b, c, p2c, jac = build(7, 3)
    assert a == 10
    assert b == 4
    assert c == 11
    assert p2c(2) == a * 4 + b * 2 + c
    assert jac(2) == 2 * a * 2 + b
    
    
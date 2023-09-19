import api.something.something as something


def test_something():
    assert something.Something.do_something(1) == 2
    assert something.Something.do_something(2) == 3
    assert something.Something.do_something(5) == 6
    assert something.Something.do_something(10) == 11


def test_something_else():
    assert something.Something.do_something_else(1, 1) == 1
    assert something.Something.do_something_else(1, 2) == 0
    assert something.Something.do_something_else(1000, 10) == 1990

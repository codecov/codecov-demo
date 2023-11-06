from api.something.something import Something


def test_something():
    st = Something()
    assert st.do_something(1) == 2
    assert st.do_something(2) == 3
    assert st.do_something(5) == 6
    assert st.do_something(10) == 11


def test_something_else():
    st = Something()
    assert st.do_something_else(1, 1) == 1
    assert st.do_something_else(1, 2) == 0
    assert st.do_something_else(1000, 10) == 1990

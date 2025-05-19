from table import table

def test_table_0():
    assert table(0) == [0,0,0,0,0,0,0,0,0,0,0] #[0] * 11

def test_table_1():
    assert table(1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list(range(11))

def test_table_3():
    assert table(3) == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

def test_table_100():
    assert table(100) == [i * 100 for i in range(11)]

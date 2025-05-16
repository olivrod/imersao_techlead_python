from functions_everywhere import shrink
from functions_everywhere import enlarge

def test_shrink_0():
    assert shrink('asdfghjkl') == 'asdfghjk'

def test_shrink_1():
    assert shrink('asd') == 'asd'

def test_enlarge_0():
    assert enlarge('asd') == 'asdZZZZZ'

def test_enlarge_1():
    assert enlarge('asdfghjk') == 'asdfghjk'
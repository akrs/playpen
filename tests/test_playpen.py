from playpen import eval_numeric


def test_simple_numeric_math():
    assert eval_numeric('3 * 4') == 12
    assert eval_numeric('3 + 4') == 7
    assert eval_numeric('3 ** 4') == 81
    assert eval_numeric('4 - 3') == 1
    assert eval_numeric('4 + -3') == 1


def test_numeric_variables():
    variables = {
        'x': 3,
        'y': 4
    }

    assert eval_numeric('x + y', variables=variables) == 7


def test_parens():
    assert eval_numeric('(1 + 2) * 3') == 9

def test_compare():
    assert eval_numeric('2 < 3') == True

from playpen import __version__, eval_numeric


def test_version():
    assert __version__ == '0.1.0'

def test_simple_numeric_math():
    assert eval_numeric('3 * 4') == 12
    assert eval_numeric('3 + 4') == 7
    assert eval_numeric('3 ** 4') == 81
    assert eval_numeric('4 - 3') == 1


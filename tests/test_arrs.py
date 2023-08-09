import pytest

from utils import arrs


@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, "test", 2),
    ([], -1, "test", "test")
])
def test_get(array, index, default, expected):
    """ Проверяем индексы в get """
    assert arrs.get(array, index, default) == expected


@pytest.mark.parametrize('coll, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([], 1, None, []),
    ([1], -1, None, [1]),
    ([1], -2, None, [1]),
])
def test_slice(coll, start, end, expected):
    """ Проверяем слайс my_slice """
    assert arrs.my_slice(coll, start, end) == expected


@pytest.mark.parametrize('array, index, default, raise_error', [
    (dict(), 1, None, KeyError),
    (dict(), None, None, TypeError),
    (set(), None, None, TypeError)
])
def test_get_raise(array, index, default, raise_error):
    """ Проверяем тип данных на входа в get в массив """
    with pytest.raises(raise_error):
        arrs.get(array, index, default)

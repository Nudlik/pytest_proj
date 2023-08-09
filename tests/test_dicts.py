import pytest

from utils.dicts import get_val


@pytest.mark.parametrize("d, key, default, expected", [
    ({"vcs": "mercurial"}, 'vcs', '', 'mercurial'),
    ({}, 'vcs', 'git', 'git'),
])
def test_dict(d, key, default, expected):
    """ Проверяем работу функции get_val """
    assert get_val(d, key, default) == expected


@pytest.mark.parametrize("coll, key, default", [
    ((), 'vcs', 'git'),
    ([], 'vcs', 'git'),
    (set(), None, None),
    (1, 2, (3, 4, 5, 6, 7))
])
def test_dict_type_error(coll, key, default):
    """ Проверяем работу функции get_val с типом ошибки TypeError """
    with pytest.raises(TypeError):
        get_val(coll, key, default)

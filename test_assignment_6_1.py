import pytest
import random

import assignment_6_1 as hw


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ('TARGET_1', True),
        ('TARGET_2', True),
        ('FOOTPATH', True),
        ('update_footpath', True),
        ('footpath_generator', True),
        ('get_direction', True),
    ]
)
def test_attributes(string, expected):
    assert hasattr(hw, string)


@pytest.mark.parametrize(
    ("path_len", "expected_path"),
    [
        (2, None),
        (-1, None),
        (3, ['home', 'X', 'pub']),
        (4, None),
        (5, ['home', '_', 'X', '_', 'pub']),
        (19, ['home', '_', '_', '_', '_', '_', '_', '_', '_', 'X', '_', '_', '_', '_', '_', '_', '_', '_', 'pub']),
    ]
)
def test_generator(path_len, expected_path):
    assert hw.footpath_generator(path_len) == expected_path


def test_generator_2():
    assert hw.footpath_generator() == ['home', '_', '_', '_', '_', 'X', '_', '_', '_', '_', 'pub']


@pytest.mark.parametrize(
    ("path", "old_pos", "new_pos", "expected_path"),
    [
        (['home', 'X', '_', '_', 'pub'], 1, 2, ['home', '_', 'X', '_', 'pub']),
        (['home', '_', '_', '_', '_', 'X', 'pub'], 5, 3, ['home', '_', '_', 'X', '_', '_', 'pub']),
    ]
)
def test_update(path, old_pos, new_pos, expected_path):
    assert hw.update_footpath(path, old_pos, new_pos) == expected_path


@pytest.mark.parametrize(
    ("seed", "p_home", "expected_direction"),
    [
        (1, 0.5, -1),
        (0, 0.5, 1),
        (0, 1, -1),
        (0, 0, 1),
    ]
)
def test_direction(seed, p_home, expected_direction):
    random.seed(seed)
    assert hw.get_direction(p_home) == expected_direction


@pytest.mark.parametrize(
    ("seed", "path_len", "max_step", "p_home", "expected_target"),
    [
        (20, 19, 25, 0.65, 'home'),
        (1, 19, 5, 0.7, 'darkness',),
        (2, 17, 30, 0.3, 'pub'),
        (0, 15, 3, 0.5, 'darkness'),
        (0, 4, 3, 1, None),
        (0, 3, 2, 1, 'home'),
        (1, 3, 2, 0, 'pub'),
    ]
)
def test_main(seed, path_len, max_step, p_home, expected_target):
    random.seed(seed)
    assert hw.main(path_len=path_len, max_step=max_step, p_home=p_home) == expected_target


def test_docstring():
    assert hw.main.__doc__
    assert hw.update_footpath.__doc__
    assert hw.footpath_generator.__doc__
    assert hw.get_direction.__doc__

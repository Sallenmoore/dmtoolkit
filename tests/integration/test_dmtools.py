import dmtools


def test_get_dndbeyond_character():
    assert dmtools.get_dndbeyond_character("68398459")


def test_get_monster():
    assert dmtools.get_monster("gnoll")


def test_get_item():
    assert dmtools.get_item("bag-of-tricks-tan")
    assert dmtools.get_item("dice-set")


def test_get_spell():
    assert dmtools.get_spell("animate-objects")


def test_search_monster():
    assert dmtools.search_monster("goblin")


def test_search_item():
    assert dmtools.search_item("fire")


def test_search_spell():
    assert dmtools.search_spell("ice")

import dmtools


def test_get_dndbeyond_character():
    assert dmtools.get_dndbeyond_character("68398459")


def test_get_monster():
    assert dmtools.get_monster("/api/monsters/gnoll")


def test_get_item():
    assert dmtools.get_item("/api/magic-items/bag-of-tricks")
    assert dmtools.get_item("/api/equipment/dice-set")


def test_get_rules():
    assert dmtools.get_rules("/api/rules/adventuring")


def test_get_feature():
    assert dmtools.get_feature("/api/feats/grappler")


def test_search_monster():
    assert dmtools.search_monster("goblin")


def test_search_item():
    assert dmtools.search_item("fire")


def test_search_rules():
    assert dmtools.search_rules("rest")


def test_search_feature():
    assert dmtools.search_feature("arcane-tradition")

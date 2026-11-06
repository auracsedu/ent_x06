import pytest

from problem_extra_01 import Inventory


def make():
    bag = Inventory()
    bag.add("포션", 3)
    bag.add("포션")
    bag.add("열쇠")
    return bag


def test_빈_가방():
    bag = Inventory()
    assert len(bag) == 0
    assert bag["포션"] == 0
    assert ("포션" in bag) is False
    assert list(bag) == []
    assert repr(bag) == "Inventory({})"
    assert bag.items == {}


def test_가방마다_items가_따로_있다():
    a = Inventory()
    b = Inventory()
    a.add("포션")
    assert len(b) == 0, "items = {} 를 클래스 몸통이 아니라 __init__ 안에 쓰세요"


def test_add와_len():
    bag = make()
    assert len(bag) == 5, f"len은 전체 개수(5)입니다. 종류 수가 아닙니다: {len(bag)}"
    assert bag.items == {"포션": 4, "열쇠": 1}
    assert bag.add("화살", 2) is None


def test_getitem():
    bag = make()
    assert bag["포션"] == 4
    assert bag["열쇠"] == 1
    assert bag["방패"] == 0, "없는 물건은 KeyError가 아니라 0"


def test_contains():
    bag = make()
    assert ("포션" in bag) is True
    assert ("방패" in bag) is False
    assert ("포션" not in bag) is False
    assert "__contains__" in vars(Inventory), "__contains__ 를 직접 만드세요 (__iter__로도 in이 되지만 이 문제의 요구입니다)"


def test_iter_이름을_정렬된_순서로():
    bag = make()
    bag.add("가위")
    assert list(bag) == ["가위", "열쇠", "포션"]
    assert [bag[name] for name in bag] == [1, 1, 4]
    assert sorted(bag) == list(bag)
    assert "__iter__" in vars(Inventory), "__iter__ 를 직접 만드세요"


def test_repr():
    bag = make()
    assert repr(bag) == "Inventory({'열쇠': 1, '포션': 4})", f"repr = {repr(bag)!r}"
    assert str(bag) == "Inventory({'열쇠': 1, '포션': 4})"


def test_setitem():
    bag = make()
    bag["포션"] = 1
    assert bag["포션"] == 1 and len(bag) == 2
    bag["방패"] = 2
    assert bag["방패"] == 2 and len(bag) == 4
    bag["열쇠"] = 0
    assert "열쇠" not in bag
    assert "열쇠" not in bag.items, "0개가 되면 items에서 이름을 지우세요"
    assert list(bag) == ["방패", "포션"]


def test_setitem_음수는_ValueError():
    bag = make()
    with pytest.raises(ValueError):
        bag["포션"] = -1
    assert bag["포션"] == 4, "실패한 대입이 가방을 바꿨습니다"


def test_add_두_가방을_합친_새_가방():
    a = Inventory()
    a.add("포션", 2)
    a.add("화살", 10)
    b = Inventory()
    b.add("포션", 1)
    b.add("열쇠")
    c = a + b
    assert isinstance(c, Inventory)
    assert (c["포션"], c["화살"], c["열쇠"], len(c)) == (3, 10, 1, 14)
    assert c is not a and c is not b
    assert (a["포션"], len(a), len(b)) == (2, 12, 2), "a, b는 바뀌지 않아야 합니다"
    assert c.items is not a.items, "a의 items 딕셔너리를 그대로 넘기지 말고 새로 만드세요"


def test_eq():
    a = Inventory()
    a.add("포션", 2)
    a.add("화살", 10)
    b = Inventory()
    b.add("포션", 1)
    b.add("열쇠")
    c = a + b
    assert (c == a + b) is True
    assert (a == b) is False
    assert (a != b) is True
    d = Inventory()
    d.add("화살", 10)
    d.add("포션", 2)
    assert (a == d) is True, "넣은 순서가 달라도 items가 같으면 같은 가방입니다"
    assert (a == {"포션": 2, "화살": 10}) is False
    assert (Inventory() == Inventory()) is True

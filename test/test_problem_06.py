from problem_06 import Character, Hero


def test_Hero는_Character를_상속한다():
    assert issubclass(Hero, Character), "class Hero(Character): 라고 쓰세요"
    h = Hero("용사", 100, 12)
    assert isinstance(h, Hero) and isinstance(h, Character)


def test_속성_다섯_개():
    h = Hero("용사", 100, 12)
    assert (h.name, h.hp, h.max_hp, h.attack, h.level) == ("용사", 100, 100, 12, 1)
    for attr in ("name", "hp", "max_hp", "attack", "level"):
        assert attr in vars(h), f"{attr}가 인스턴스 변수가 아닙니다. super().__init__(name, hp) 를 불렀는지 확인하세요"


def test_물려받은_메서드를_다시_쓰지_않았다():
    for name in ("is_alive", "take_damage", "heal"):
        assert name not in vars(Hero), f"{name}은 Character에 이미 있습니다. Hero에 다시 쓰지 말고 물려받으세요"


def test_물려받은_메서드가_그대로_동작한다():
    h = Hero("용사", 100, 12)
    h.take_damage(30)
    assert h.hp == 70
    h.heal(100)
    assert h.hp == 100
    h.take_damage(999)
    assert h.hp == 0 and h.is_alive() is False


def test_str은_부모_결과에_레벨을_붙인다():
    h = Hero("용사", 100, 12)
    assert str(h) == "용사(100/100) Lv.1", f"str(h) = {str(h)!r}"
    h.take_damage(30)
    assert str(h) == "용사(70/100) Lv.1"
    assert str(Character("슬라임", 20)) == "슬라임(20/20)", "Character는 고치지 마세요"


def test_strike_괴물을_공격():
    h = Hero("용사", 100, 12)
    c = Character("슬라임", 20)
    assert h.strike(c) is False
    assert c.hp == 8
    assert h.strike(c) is True
    assert c.hp == 0
    assert (h.level, h.attack) == (2, 14), "쓰러뜨리면 level +1, attack +2"
    assert str(h) == "용사(100/100) Lv.2"
    assert str(c) == "슬라임(0/20)"


def test_strike_이미_쓰러진_상대():
    h = Hero("용사", 100, 50)
    c = Character("슬라임", 20)
    assert h.strike(c) is True
    assert h.strike(c) is False, "이미 쓰러진 상대를 공격하면 False"
    assert (h.level, h.attack) == (2, 52), "이미 쓰러진 상대를 공격했는데 레벨이 또 올랐습니다"


def test_strike_영웅끼리():
    a = Hero("용사", 30, 10)
    b = Hero("도적", 25, 8)
    a.strike(b)
    b.strike(a)
    assert (a.hp, b.hp) == (22, 15)
    assert a.hp == 22, "공격한 쪽의 hp는 변하지 않습니다"


def test_target은_어떤_Character라도_된다():
    h = Hero("용사", 100, 12)
    targets = [Character("슬라임", 10), Hero("도적", 10, 1), Character("박쥐", 12)]
    results = [h.strike(t) for t in targets]
    assert results == [True, True, True], "target의 타입을 따지지 말고 take_damage / is_alive 만 쓰세요"
    assert h.level == 4

from problem_01 import Robot


def test_속성_네_개가_설정된다():
    r = Robot("알파", 10)
    assert r.name == "알파"
    assert r.battery == 10
    assert r.max_battery == 10, f"max_battery는 처음 battery와 같아야 합니다: {r.max_battery!r}"
    assert r.distance == 0, f"distance는 항상 0에서 시작합니다: {r.distance!r}"
    for attr in ("name", "battery", "max_battery", "distance"):
        assert attr in vars(r), f"{attr}가 인스턴스 변수가 아닙니다. __init__ 안에서 self.{attr} = ... 로 쓰세요"


def test_인스턴스마다_값이_따로_있다():
    a = Robot("알파", 10)
    b = Robot("베타", 20)
    a.battery = 0
    assert b.battery == 20, "a의 battery를 바꿨는데 b가 바뀌었습니다. self.battery 에 넣고 있는지 확인하세요"


def test_is_on():
    r = Robot("알파", 10)
    assert r.is_on() is True
    r.battery = 0
    assert r.is_on() is False, "battery가 0이면 꺼진 것입니다"


def test_move_성공():
    r = Robot("알파", 10)
    result = r.move(4)
    assert result is True, f"배터리가 충분하면 True여야 합니다: {result!r}"
    assert (r.battery, r.distance) == (6, 4), f"(battery, distance) = {(r.battery, r.distance)}, 기대값 (6, 4)"


def test_move_배터리를_딱_맞게_쓴다():
    r = Robot("알파", 10)
    assert r.move(10) is True
    assert (r.battery, r.distance) == (0, 10)
    assert r.is_on() is False


def test_move_실패하면_아무_일도_없다():
    r = Robot("알파", 10)
    r.move(4)
    result = r.move(7)
    assert result is False, f"6 < 7 이므로 False여야 합니다: {result!r}"
    assert (r.battery, r.distance) == (6, 4), "실패한 move가 battery나 distance를 바꿨습니다. 검사를 먼저 하세요"


def test_charge_최대치를_넘지_않는다():
    r = Robot("알파", 10)
    r.move(4)
    r.charge(2)
    assert r.battery == 8
    r.charge(100)
    assert r.battery == 10, f"max_battery(10)를 넘었습니다: {r.battery}"
    assert r.charge(1) is None, "charge는 값을 돌려주지 않습니다"


def test_give_성공():
    a = Robot("알파", 10)
    b = Robot("베타", 20)
    b.battery = 5
    result = a.give(b, 3)
    assert result is True
    assert (a.battery, b.battery) == (7, 8), f"(a, b) = {(a.battery, b.battery)}, 기대값 (7, 8)"


def test_give_상대의_최대치를_넘는_만큼은_사라진다():
    a = Robot("알파", 10)
    b = Robot("베타", 5)
    b.battery = 3
    assert a.give(b, 4) is True
    assert (a.battery, b.battery) == (6, 5), "other.charge(amount)를 부르면 최대치 규칙이 저절로 지켜집니다"


def test_give_실패하면_아무_일도_없다():
    a = Robot("알파", 10)
    b = Robot("베타", 20)
    b.battery = 5
    result = a.give(b, 100)
    assert result is False
    assert (a.battery, b.battery) == (10, 5), "실패한 give가 배터리를 바꿨습니다"


def test_give_자기_배터리를_전부_줄_수_있다():
    a = Robot("알파", 10)
    b = Robot("베타", 20)
    b.battery = 0
    assert a.give(b, 10) is True
    assert (a.battery, b.battery, a.is_on(), b.is_on()) == (0, 10, False, True)

from problem_03 import Garage, Robot


def make():
    g = Garage()
    a = Robot("알파", 10)
    b = Robot("베타", 4)
    c = Robot("감마", 10)
    g.add(a)
    g.add(b)
    g.add(c)
    return g, a, b, c


def test_빈_정비소():
    g = Garage()
    assert g.size() == 0
    assert g.on_robots() == []
    assert g.total_battery() == 0
    assert g.most_charged() is None
    assert g.move_all(3) == 0


def test_add와_size():
    g, a, b, c = make()
    assert g.size() == 3
    assert g.robots == [a, b, c], "robots 리스트에 넣은 순서대로 들어 있어야 합니다"


def test_정비소마다_리스트가_따로_있다():
    g, a, b, c = make()
    h = Garage()
    assert h.size() == 0, "다른 정비소가 비어 있지 않습니다. robots = [] 를 클래스 몸통이 아니라 __init__ 안에 쓰세요"
    assert g.robots is not h.robots


def test_total_battery():
    g, a, b, c = make()
    assert g.total_battery() == 24


def test_most_charged_같으면_먼저_넣은_로봇():
    g, a, b, c = make()
    assert g.most_charged() is a, "10으로 같을 때는 먼저 넣은 a여야 합니다. '더 큰' 경우에만 바꾸세요"
    c.battery = 11
    assert g.most_charged() is c
    assert isinstance(g.most_charged(), Robot), "로봇 객체 자체를 돌려줘야 합니다"


def test_on_robots():
    g, a, b, c = make()
    assert g.on_robots() == [a, b, c]
    b.battery = 0
    assert g.on_robots() == [a, c], "꺼진 로봇은 빼고, 순서는 넣은 순서"
    assert g.on_robots() is not g.robots, "새 리스트를 돌려주세요"
    assert g.size() == 3, "꺼져도 맡아 둔 로봇 수는 그대로입니다"


def test_charge_all은_로봇의_charge를_쓴다():
    g, a, b, c = make()
    a.battery, b.battery, c.battery = 5, 0, 9
    assert g.charge_all(3) is None
    assert (a.battery, b.battery, c.battery) == (8, 3, 10), "최대치를 넘었습니다. robot.charge(amount)를 부르면 저절로 지켜집니다"


def test_move_all은_움직인_수를_돌려준다():
    g, a, b, c = make()
    moved = g.move_all(5)
    assert moved == 2, f"b(4)는 5만큼 못 움직이므로 2여야 합니다: {moved!r}"
    assert (a.battery, b.battery, c.battery) == (5, 4, 5)
    assert (a.distance, b.distance, c.distance) == (5, 0, 5), "robot.move(steps)를 불러야 distance도 함께 바뀝니다"
    assert g.move_all(5) == 2
    assert g.move_all(5) == 0


def test_예시_흐름():
    g, a, b, c = make()
    assert g.move_all(5) == 2
    assert g.most_charged() is a
    b.battery = 0
    assert g.on_robots() == [a, c]
    g.charge_all(3)
    assert (a.battery, b.battery, c.battery) == (8, 3, 8)
    assert g.size() == 3

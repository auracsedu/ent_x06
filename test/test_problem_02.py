import pytest

from problem_02 import Part


@pytest.fixture(autouse=True)
def reset_count():
    assert "count" in vars(Part), "클래스 몸통에 count = 0 을 적으세요 (클래스 변수)"
    Part.count = 0
    yield
    Part.count = 0


def test_데코레이터가_붙어_있다():
    assert isinstance(vars(Part)["is_valid_price"], staticmethod), "is_valid_price 윗줄에 @staticmethod 를 붙이세요"
    assert isinstance(vars(Part)["from_string"], classmethod), "from_string 윗줄에 @classmethod 를 붙이세요"


def test_속성과_번호표():
    a = Part("모터", 1200)
    b = Part("바퀴", 300)
    assert (a.name, a.price) == ("모터", 1200)
    assert (a.id, b.id) == (1, 2), f"id는 1부터 만들어진 순서입니다: {(a.id, b.id)}"
    assert Part.count == 2, f"Part.count가 {Part.count}입니다. Part.count += 1 로 올리세요 (self.count 가 아닙니다)"
    assert "count" not in vars(a), "self.count += 1 을 쓰면 인스턴스 변수가 따로 생깁니다. Part.count 로 쓰세요"


def test_count는_모든_인스턴스가_공유한다():
    a = Part("모터", 1200)
    b = Part("바퀴", 300)
    c = Part("센서", 450)
    assert a.count == b.count == c.count == 3
    assert c.id == 3


@pytest.mark.parametrize(
    "price, expected",
    [(1200, True), (1, True), (0, False), (-5, False), ("1200", False), (3.5, False), (None, False)],
)
def test_is_valid_price(price, expected):
    assert Part.is_valid_price(price) is expected, f"is_valid_price({price!r})가 {expected}여야 합니다"


def test_정적_메서드는_인스턴스로도_부를_수_있다():
    p = Part("모터", 1200)
    assert p.is_valid_price(100) is True


def test_잘못된_가격은_ValueError():
    with pytest.raises(ValueError):
        Part("센서", 0)
    with pytest.raises(ValueError):
        Part("센서", "1200")


def test_실패한_생성은_count를_올리지_않는다():
    Part("모터", 1200)
    with pytest.raises(ValueError):
        Part("센서", -1)
    assert Part.count == 1, "ValueError가 난 생성이 count를 올렸습니다. 검사를 count 올리기 '앞'에 두세요"
    assert Part("바퀴", 300).id == 2


def test_from_string():
    p = Part.from_string("모터,1200")
    assert isinstance(p, Part)
    assert (p.name, p.price, p.id) == ("모터", 1200, 1)
    assert isinstance(p.price, int), "가격은 int로 바꿔야 합니다"


def test_from_string_공백_무시():
    p = Part.from_string(" 센서 , 450 ")
    assert (p.name, p.price) == ("센서", 450), f"조각 앞뒤 공백을 strip 하세요: {(p.name, p.price)!r}"


def test_from_string도_init을_거친다():
    Part("모터", 1200)
    Part("바퀴", 300)
    p = Part.from_string("센서, 450")
    assert (p.id, Part.count) == (3, 3), "from_string은 cls(name, price)로 만들어야 번호표가 이어집니다"
    with pytest.raises(ValueError):
        Part.from_string("고장, 0")

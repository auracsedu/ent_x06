import pytest

from problem_04 import Fraction


def nd(f):
    assert isinstance(f, Fraction), f"결과가 Fraction이 아닙니다: {f!r}"
    return (f.num, f.den)


# ---- (1) 출력 ----


@pytest.mark.parametrize(
    "num, den, s",
    [(6, 8, "3/4"), (1, 2, "1/2"), (-1, 2, "-1/2"), (3, -6, "-1/2"), (2, 1, "2"), (4, 2, "2"), (-4, 2, "-2"), (0, 7, "0")],
)
def test_str(num, den, s):
    f = Fraction(num, den)
    assert str(f) == s, f"str(Fraction({num}, {den}))이 {str(f)!r}, 기대값 {s!r}"


@pytest.mark.parametrize(
    "num, den, r",
    [(6, 8, "Fraction(3, 4)"), (-1, 2, "Fraction(-1, 2)"), (2, 1, "Fraction(2, 1)"), (4, 2, "Fraction(2, 1)"), (0, 7, "Fraction(0, 1)")],
)
def test_repr(num, den, r):
    f = Fraction(num, den)
    assert repr(f) == r, f"repr(Fraction({num}, {den}))이 {repr(f)!r}, 기대값 {r!r}. 분모가 1이어도 두 수를 씁니다"


def test_둘_다_문자열을_돌려준다():
    f = Fraction(1, 2)
    assert isinstance(f.__str__(), str), "__str__은 문자열을 return 해야 합니다 (print가 아닙니다)"
    assert isinstance(f.__repr__(), str), "__repr__은 문자열을 return 해야 합니다"


def test_print는_str을_쓴다(capsys):
    print(Fraction(6, 8))
    assert capsys.readouterr().out == "3/4\n"


def test_f문자열은_str을_쓴다():
    f = Fraction(6, 8)
    assert f"{f}" == "3/4"
    assert f"{f}!" == "3/4!"


def test_리스트_안에서는_repr을_쓴다():
    fs = [Fraction(1, 2), Fraction(4, 2)]
    assert str(fs) == "[Fraction(1, 2), Fraction(2, 1)]"
    assert repr(fs) == "[Fraction(1, 2), Fraction(2, 1)]"


def test_repr을_그대로_실행하면_같은_분수():
    f = Fraction(10, 4)
    g = eval(repr(f))
    assert (g.num, g.den) == (f.num, f.den)


# ---- (2) 같은지 비교 ----


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (2, 4), True), ((1, 2), (1, 3), False), ((0, 3), (0, 7), True), ((-1, 2), (1, -2), True), ((2, 1), (4, 2), True), ((1, 2), (-1, 2), False)],
)
def test_분수끼리_비교(a, b, expected):
    result = Fraction(*a) == Fraction(*b)
    assert result is expected, f"Fraction{a} == Fraction{b} 가 {result!r}, 기대값 {expected}"


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (2, 4), False), ((1, 2), (1, 3), True), ((2, 1), (4, 2), False)],
)
def test_같지_않다는_따로_만들지_않아도_된다(a, b, expected):
    result = Fraction(*a) != Fraction(*b)
    assert result is expected, f"Fraction{a} != Fraction{b} 가 {result!r}, 기대값 {expected}. != 는 __eq__의 결과를 뒤집어 계산됩니다"


@pytest.mark.parametrize("num, den, n, expected", [(4, 2, 2, True), (4, 2, 3, False), (1, 2, 0, False), (0, 5, 0, True), (-6, 3, -2, True), (1, 2, 1, False)])
def test_정수와_비교(num, den, n, expected):
    assert (Fraction(num, den) == n) is expected, f"Fraction({num}, {den}) == {n} 이 {expected}여야 합니다"
    assert (n == Fraction(num, den)) is expected, f"{n} == Fraction({num}, {den}) 도 {expected}여야 합니다 (파이썬이 뒤집어 불러 줍니다)"


def test_모르는_타입과는_False():
    f = Fraction(1, 2)
    assert (f == "1/2") is False
    assert (f == 0.5) is False, "float는 다루지 않습니다. NotImplemented를 돌려주면 False가 됩니다"
    assert (f == None) is False
    assert (f != "1/2") is True


def test_모르는_타입에는_NotImplemented를_돌려준다():
    f = Fraction(1, 2)
    assert f.__eq__("1/2") is NotImplemented, "모르는 타입이면 False가 아니라 NotImplemented 를 return 하세요"


def test_in과_count도_eq를_쓴다():
    fs = [Fraction(1, 2), Fraction(1, 3)]
    assert Fraction(2, 4) in fs
    assert Fraction(1, 4) not in fs
    assert fs.count(Fraction(2, 4)) == 1
    assert fs.index(Fraction(3, 9)) == 1


def test_자기_자신과_같다():
    f = Fraction(3, 7)
    assert (f == f) is True


# ---- (3) 사칙연산 ----




@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (1, 3), (5, 6)), ((1, 2), (1, 2), (1, 1)), ((1, 3), (-1, 3), (0, 1)), ((-1, 4), (1, 2), (1, 4)), ((2, 3), (5, 6), (3, 2))],
)
def test_add(a, b, expected):
    assert nd(Fraction(*a) + Fraction(*b)) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (1, 3), (1, 6)), ((1, 2), (1, 2), (0, 1)), ((1, 3), (1, 2), (-1, 6)), ((-1, 4), (1, 2), (-3, 4))],
)
def test_sub(a, b, expected):
    assert nd(Fraction(*a) - Fraction(*b)) == expected, "a/b - c/d = (ad - bc) / bd. 순서를 확인하세요"


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (1, 3), (1, 6)), ((2, 3), (3, 2), (1, 1)), ((0, 1), (5, 7), (0, 1)), ((-1, 2), (1, 2), (-1, 4)), ((3, 4), (-4, 3), (-1, 1))],
)
def test_mul(a, b, expected):
    assert nd(Fraction(*a) * Fraction(*b)) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (1, 3), (3, 2)), ((2, 3), (2, 3), (1, 1)), ((1, 2), (-1, 4), (-2, 1)), ((0, 1), (5, 7), (0, 1)), ((3, 4), (3, 1), (1, 4))],
)
def test_truediv(a, b, expected):
    assert nd(Fraction(*a) / Fraction(*b)) == expected, "a/b ÷ c/d = ad / bc"


def test_0으로_나누면_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 1)
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / 0


@pytest.mark.parametrize(
    "expr, expected",
    [
        (lambda a: a + 1, (3, 2)),
        (lambda a: a - 1, (-1, 2)),
        (lambda a: a * 4, (2, 1)),
        (lambda a: a / 2, (1, 4)),
        (lambda a: a + 0, (1, 2)),
        (lambda a: a * 0, (0, 1)),
    ],
)
def test_정수와_연산(expr, expected):
    assert nd(expr(Fraction(1, 2))) == expected, "int인 other는 Fraction(other)로 바꿔 계산하세요"


def test_원본은_바뀌지_않고_새_객체가_나온다():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    results = [a + b, a - b, a * b, a / b]
    for r in results:
        assert r is not a and r is not b, "self나 other를 돌려주지 말고 새 Fraction을 만드세요"
    assert (a.num, a.den) == (1, 2), "연산 뒤에 a가 바뀌었습니다. self를 건드리면 안 됩니다"
    assert (b.num, b.den) == (1, 3)


def test_결과는_정수_분자_분모():
    r = Fraction(1, 3) / Fraction(2, 5)
    assert isinstance(r.num, int) and isinstance(r.den, int), "분자·분모가 float가 되었습니다. / 대신 곱셈으로 계산하세요"


def test_이어서_계산하기():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    assert nd((a + b) * 6) == (5, 1)
    assert nd(a + b - a) == (1, 3)
    assert nd(a * b / a) == (1, 3)


def test_eq와_함께_쓰기():
    assert (Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)) is True
    assert (Fraction(1, 2) + Fraction(1, 2) == 1) is True
    assert (Fraction(1, 2) * 2 == 1) is True


# ---- (4) 크기 비교 ----




@pytest.mark.parametrize(
    "a, b, lt, le",
    [
        ((1, 2), (2, 3), True, True),
        ((2, 3), (1, 2), False, False),
        ((1, 2), (2, 4), False, True),
        ((-1, 2), (1, 3), True, True),
        ((-1, 2), (-2, 3), False, False),
        ((0, 1), (1, 100), True, True),
        ((7, 3), (7, 3), False, True),
    ],
)
def test_lt_le(a, b, lt, le):
    x, y = Fraction(*a), Fraction(*b)
    assert (x < y) is lt, f"Fraction{a} < Fraction{b} 가 {lt}여야 합니다"
    assert (x <= y) is le, f"Fraction{a} <= Fraction{b} 가 {le}여야 합니다"


@pytest.mark.parametrize(
    "a, b, gt, ge",
    [((2, 3), (1, 2), True, True), ((1, 2), (2, 3), False, False), ((1, 2), (2, 4), False, True)],
)
def test_gt_ge는_뒤집어서_동작한다(a, b, gt, ge):
    x, y = Fraction(*a), Fraction(*b)
    assert (x > y) is gt, "__gt__ 가 없으면 파이썬은 y < x 를 대신 계산합니다. __lt__ 를 확인하세요"
    assert (x >= y) is ge


@pytest.mark.parametrize(
    "num, den, n, lt, le",
    [(1, 2, 1, True, True), (3, 1, 3, False, True), (5, 2, 2, False, False), (-1, 2, 0, True, True)],
)
def test_정수와_크기_비교(num, den, n, lt, le):
    f = Fraction(num, den)
    assert (f < n) is lt
    assert (f <= n) is le


def test_sorted():
    fs = [Fraction(2, 3), Fraction(1, 2), Fraction(3, 4), Fraction(1, 6)]
    result = sorted(fs)
    assert [nd(f) for f in result] == [(1, 6), (1, 2), (2, 3), (3, 4)], f"sorted 결과: {result!r}"
    assert [nd(f) for f in fs] == [(2, 3), (1, 2), (3, 4), (1, 6)], "sorted는 원본을 바꾸지 않습니다"


def test_sorted_reverse_min_max():
    fs = [Fraction(2, 3), Fraction(1, 2), Fraction(3, 4), Fraction(1, 6)]
    assert nd(sorted(fs, reverse=True)[0]) == (3, 4)
    assert nd(min(fs)) == (1, 6)
    assert nd(max(fs)) == (3, 4)


def test_음수와_정수가_섞인_정렬():
    fs = [Fraction(1, 2), Fraction(-3, 2), Fraction(0), Fraction(5, 1), Fraction(-1, 3)]
    assert [nd(f) for f in sorted(fs)] == [(-3, 2), (-1, 3), (0, 1), (1, 2), (5, 1)]


def test_list_sort도_된다():
    fs = [Fraction(3, 4), Fraction(1, 4), Fraction(1, 2)]
    fs.sort()
    assert [nd(f) for f in fs] == [(1, 4), (1, 2), (3, 4)]


def test_비교_결과는_bool():
    assert Fraction(1, 2).__lt__(Fraction(2, 3)) is True
    assert Fraction(1, 2).__le__(Fraction(1, 3)) is False


def test_큰_수에서도_정확하다():
    a = Fraction(10**18 + 1, 10**18)
    b = Fraction(10**18 + 2, 10**18 + 1)
    assert (a < b) is False, "float로 바꾸면 두 값이 같아 보입니다. 통분해서 정수로 비교하세요"
    assert (b < a) is True

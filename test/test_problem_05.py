import pytest

from problem_05 import Polynomial


def co(p):
    assert isinstance(p, Polynomial), f"결과가 Polynomial이 아닙니다: {p!r}"
    return p.coeffs


@pytest.mark.parametrize(
    "coeffs, expected",
    [([1, 2, 3], [1, 2, 3]), ([1, 2, 3, 0, 0], [1, 2, 3]), ([0, 0], [0]), ([], [0]), ([0], [0]), ([0, 1], [0, 1]), ([5], [5])],
)
def test_init_최고차의_0을_지운다(coeffs, expected):
    assert Polynomial(coeffs).coeffs == expected, f"Polynomial({coeffs}).coeffs 가 {expected}여야 합니다"


def test_init은_리스트를_복사한다():
    src = [1, 2, 3, 0]
    p = Polynomial(src)
    assert p.coeffs is not src, "받은 리스트를 그대로 쓰지 말고 복사하세요"
    assert src == [1, 2, 3, 0], "받은 리스트가 바뀌었습니다"


@pytest.mark.parametrize("coeffs, d", [([1, 2, 3], 2), ([5], 0), ([0], 0), ([], 0), ([0, 0, 0, 7], 3), ([1, 1, 0], 1)])
def test_degree(coeffs, d):
    assert Polynomial(coeffs).degree() == d


@pytest.mark.parametrize("coeffs, x, expected", [([1, 2, 3], 0, 1), ([1, 2, 3], 1, 6), ([1, 2, 3], 2, 17), ([1, 2, 3], -1, 2), ([0], 100, 0), ([0, 0, 1], 5, 25), ([7], 3, 7)])
def test_call(coeffs, x, expected):
    p = Polynomial(coeffs)
    assert p(x) == expected, f"Polynomial({coeffs})({x}) = {p(x)}, 기대값 {expected}"


@pytest.mark.parametrize(
    "coeffs, s",
    [
        ([1, 2, 3], "3x^2 + 2x + 1"),
        ([0], "0"),
        ([5], "5"),
        ([-5], "-5"),
        ([0, 1], "x"),
        ([0, -1], "-x"),
        ([0, 0, 1], "x^2"),
        ([-1, 0, 2], "2x^2 - 1"),
        ([0, 1, -1], "-x^2 + x"),
        ([1, -1], "-x + 1"),
        ([1, 1], "x + 1"),
        ([3, 0, 0, -4], "-4x^3 + 3"),
        ([-2, -3, -1], "-x^2 - 3x - 2"),
        ([0, 0, 0, 0, 10], "10x^4"),
    ],
)
def test_str(coeffs, s):
    assert str(Polynomial(coeffs)) == s, f"str(Polynomial({coeffs})) = {str(Polynomial(coeffs))!r}, 기대값 {s!r}"


@pytest.mark.parametrize("coeffs, r", [([1, 2, 3], "Polynomial([1, 2, 3])"), ([0], "Polynomial([0])"), ([1, 2, 3, 0], "Polynomial([1, 2, 3])")])
def test_repr(coeffs, r):
    assert repr(Polynomial(coeffs)) == r


@pytest.mark.parametrize(
    "a, b, expected",
    [([1, 2, 3], [1, 1], [2, 3, 3]), ([1, 1], [1, 2, 3], [2, 3, 3]), ([1, 1], [-1, -1], [0]), ([1, 2, 3], [0, 0, -3], [1, 2]), ([0], [0], [0])],
)
def test_add(a, b, expected):
    assert co(Polynomial(a) + Polynomial(b)) == expected, "길이가 다른 쪽은 0으로 채워 더하세요. 결과의 뒤 0은 __init__이 지웁니다"


@pytest.mark.parametrize(
    "a, b, expected",
    [([1, 1], [1, 1], [1, 2, 1]), ([1, -1], [1, 1], [1, 0, -1]), ([1, 2, 3], [2], [2, 4, 6]), ([0], [1, 2, 3], [0]), ([0, 1], [0, 1], [0, 0, 1]), ([1, 2], [3, 4, 5], [3, 10, 13, 10])],
)
def test_mul(a, b, expected):
    assert co(Polynomial(a) * Polynomial(b)) == expected, "result[i + j] += p[i] * q[j]"


def test_정수와_연산():
    p = Polynomial([1, 2, 3])
    assert co(p + 10) == [11, 2, 3]
    assert co(p * 2) == [2, 4, 6]
    assert co(p * 0) == [0]
    assert co(p + 0) == [1, 2, 3]


@pytest.mark.parametrize(
    "expr, expected",
    [(lambda p: 10 + p, [11, 2, 3]), (lambda p: 0 + p, [1, 2, 3]), (lambda p: 2 * p, [2, 4, 6]), (lambda p: 0 * p, [0]), (lambda p: -1 * p, [-1, -2, -3])],
)
def test_정수가_왼쪽에_와도_된다(expr, expected):
    result = expr(Polynomial([1, 2, 3]))
    assert co(result) == expected, "정수 + 다항식 은 __radd__, 정수 * 다항식 은 __rmul__ 이 처리합니다. 결과는 다항식 + 정수 와 같습니다"


def test_원본은_바뀌지_않는다():
    p = Polynomial([1, 2, 3])
    q = Polynomial([1, 1])
    r = p + q
    s = p * q
    assert r is not p and s is not p
    assert p.coeffs == [1, 2, 3] and q.coeffs == [1, 1], "연산 뒤에 원본 계수가 바뀌었습니다"


def test_eq():
    assert (Polynomial([1, 2, 3]) == Polynomial([1, 2, 3, 0])) is True
    assert (Polynomial([1, 2, 3]) == Polynomial([1, 2])) is False
    assert (Polynomial([7]) == 7) is True
    assert (Polynomial([7, 1]) == 7) is False
    assert (Polynomial([0]) == 0) is True
    assert (Polynomial([1]) == "1") is False
    assert (Polynomial([1, 2]) != Polynomial([2, 1])) is True
    assert Polynomial([1]).__eq__("1") is NotImplemented


def test_이어서_계산하기():
    q = Polynomial([1, 1])
    assert (q * q)(3) == 16
    assert str(q * q) == "x^2 + 2x + 1"
    assert (q * q == Polynomial([1, 2, 1])) is True
    assert str((q * q) + Polynomial([-1, -2, -1])) == "0"
    assert str(Polynomial([1, -1]) * Polynomial([1, 1]) * Polynomial([1, 0, 1])) == "-x^4 + 1"
    assert str(3 * q * q) == "3x^2 + 6x + 3"
    assert str(1 + 2 * Polynomial([0, 1])) == "2x + 1"

"""
문제 5. 다항식 (__call__: 객체를 함수처럼, __radd__/__rmul__: 왼쪽 피연산자)

정수 계수 다항식을 나타내는 클래스 Polynomial을 작성하세요. 계수는 낮은 차수부터
리스트로 받습니다. Polynomial([1, 2, 3]) 은 1 + 2x + 3x² 입니다.

    Polynomial(coeffs)   계수 리스트를 "복사해서" 속성 coeffs 에 둡니다. 맨 뒤(최고차)의
                         0은 모두 지웁니다. 다 지워져 빈 리스트가 되면 [0] 으로 둡니다.
    degree()             차수. coeffs 길이 - 1. (영 다항식 [0]의 차수는 0으로 둡니다)
    p(x)                 __call__(self, x): x를 대입한 값
    p + q, 10 + p        __add__, __radd__: 합. other는 Polynomial 또는 int. 새 Polynomial
    p * q, 2 * p         __mul__, __rmul__: 곱. other는 Polynomial 또는 int. 새 Polynomial
    p == q               __eq__: 계수 리스트가 같으면 True. other가 int이면 상수
                         다항식과 비교. 그 밖의 타입은 NotImplemented
    repr(p)              "Polynomial([1, 2, 3])"
    str(p)               "3x^2 + 2x + 1" 꼴. 규칙은 아래.

str 규칙
    - 높은 차수부터 씁니다. 계수가 0인 항은 쓰지 않습니다.
    - 항은 "3x^2", "2x", "1" 꼴. 1차는 x^1 이 아니라 x, 0차는 수만 씁니다.
    - 계수 1은 쓰지 않습니다("x^2", "x"). 단 상수항은 "1"이라고 씁니다. 계수 -1은 "-x^2".
    - 항 사이는 " + " 또는 " - " 로 잇습니다. 음수 계수는 " - " 뒤에 절댓값을 씁니다.
      맨 앞 항이 음수면 "-" 를 바로 붙입니다.
    - 영 다항식은 "0" 입니다.

예시
    p = Polynomial([1, 2, 3])
    p.coeffs                 -> [1, 2, 3]
    p.degree()               -> 2
    p(0), p(1), p(2)         -> 1, 6, 17
    str(p)                   -> "3x^2 + 2x + 1"
    repr(p)                  -> "Polynomial([1, 2, 3])"

    Polynomial([1, 2, 3, 0, 0]).coeffs      -> [1, 2, 3]       # 최고차의 0은 지움
    Polynomial([0, 0]).coeffs               -> [0]
    Polynomial([]).degree()                 -> 0
    str(Polynomial([0]))                    -> "0"
    str(Polynomial([-1, 0, 2]))             -> "2x^2 - 1"
    str(Polynomial([0, -1]))                -> "-x"
    str(Polynomial([0, 1, -1]))             -> "-x^2 + x"
    str(Polynomial([5]))                    -> "5"
    str(Polynomial([0, 0, 1]))              -> "x^2"

    q = Polynomial([1, 1])                  # 1 + x
    p + q                    -> Polynomial([2, 3, 3])
    p + 10                   -> Polynomial([11, 2, 3])
    10 + p                   -> Polynomial([11, 2, 3])         # 정수가 왼쪽에 와도 됩니다
    q * q                    -> Polynomial([1, 2, 1])          # (1 + x)² = 1 + 2x + x²
    p * 2                    -> Polynomial([2, 4, 6])
    2 * p                    -> Polynomial([2, 4, 6])          # 이것도
    Polynomial([1, -1]) * Polynomial([1, 1])    -> Polynomial([1, 0, -1])   # (1-x)(1+x)
    Polynomial([1, 1]) + Polynomial([-1, -1])   -> Polynomial([0])         # 0은 [0]으로
    p == Polynomial([1, 2, 3, 0])               -> True
    Polynomial([7]) == 7                        -> True
    (q * q)(3)               -> 16
    str(3 * q * q)           -> "3x^2 + 6x + 3"

매직 메서드로 생각하는 법
    새로 나오는 것은 둘입니다.

    (1) __call__. p(2) 라고 쓰면 파이썬은 p.__call__(2) 를 부릅니다. 다항식은
    "함수"이기도 하니 함수처럼 부를 수 있게 하는 것이 자연스럽습니다.

    (2) 왼쪽 피연산자. p * 2 는 p.__mul__(2) 입니다. 그런데 2 * p 는 어떨까요?
    왼쪽이 int이므로 파이썬은 먼저 (2).__mul__(p) 를 부르는데, int는 Polynomial을
    몰라서 NotImplemented를 돌려줍니다. 그러면 파이썬은 오른쪽 피연산자에게 "뒤집은"
    메서드 p.__rmul__(2) 를 물어봅니다. r은 right(오른쪽에 있을 때)입니다. 덧셈과
    곱셈은 순서가 상관없으니 __radd__, __rmul__ 은 __add__, __mul__ 과 같은 일을
    하면 됩니다. 문제 4 (2)에서 2 == Fraction(4, 2) 가 된 것과 같은 원리입니다.
    (- 와 / 에도 __rsub__, __rtruediv__ 가 있는데 other - self 라서 순서를 조심해야
    합니다. 이번 문제에는 없습니다.)

    나머지(__add__, __mul__, __eq__, __repr__, __str__)는 문제 4에서 한 것과 같은
    원리이고, 이 문제의 진짜 일은 str 규칙처럼 "경우를 빠짐없이 나누는" 것입니다.

힌트
    - 복사는 list(...) 한 번이면 됩니다. 뒤의 0은 마지막 원소가 0인 동안 지우되,
      [0] 하나는 남겨야 합니다.
    - 값 계산은 enumerate 를 쓰면 차수와 계수가 같이 나옵니다.
    - 합: 긴 쪽 길이만큼 돌며 짧은 쪽은 0으로 칩니다. 뒤의 0 정리는 __init__이
      하므로 결과를 Polynomial(...) 에 넘기기만 하면 됩니다.
    - 곱: 결과 길이를 먼저 정해 0으로 채워 두고, i차 항과 j차 항의 곱은 i+j차에
      더합니다.
    - int인 other는 상수 다항식으로 바꿔 같은 코드를 씁니다.
    - str: 높은 차수부터 돌며 (부호, 절댓값, 차수) 를 보고 조각을 이어 붙이는 쪽이
      경우가 적습니다. "맨 앞 항"만 특별 취급하면 됩니다.
"""

from typing import List


class Polynomial:
    def __init__(self, coeffs: List[int]) -> None:
        raise NotImplementedError

    def degree(self) -> int:
        raise NotImplementedError

    def __call__(self, x: int) -> int:
        raise NotImplementedError

    def __add__(self, other) -> "Polynomial":
        raise NotImplementedError

    def __radd__(self, other) -> "Polynomial":
        raise NotImplementedError

    def __mul__(self, other) -> "Polynomial":
        raise NotImplementedError

    def __rmul__(self, other) -> "Polynomial":
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

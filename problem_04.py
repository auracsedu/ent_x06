"""
문제 4. 분수 (매직 메서드: 출력, 비교, 사칙연산, 크기 비교)

여기서부터는 이번 주 본 내용, 매직 메서드입니다. 소재는 지난주 도전 문제의
분수 Fraction입니다. 약분과 부호 정리를 하는 __init__은 완성되어 있습니다.
(지난주 extra 2를 풀었다면 그 코드와 같은 일을 합니다. 이번 주에는 __init__을
고칠 일이 없습니다.)

Fraction에 아래 메서드들을 추가하세요. 네 단계로 나누어 두었고 테스트도 같은
순서입니다. 한 단계씩 만들고 테스트하세요.

(1) 출력
    __str__(self)       "3/4" 꼴의 문자열. 분모가 1이면 "2" 처럼 정수만 씁니다.
                        (지난주 to_string과 같습니다.)
    __repr__(self)      "Fraction(3, 4)" 꼴의 문자열. 분모가 1이어도 "Fraction(2, 1)"
                        처럼 항상 두 수를 씁니다. 그대로 복사해 실행하면 같은 분수가
                        만들어지는 꼴입니다.

(2) 같은지 비교
    __eq__(self, other)
        other가 Fraction이면   두 분수가 같은 수일 때 True, 아니면 False.
                               (둘 다 기약분수이므로 분자와 분모를 각각 비교하면 됩니다)
        other가 int이면        분수가 그 정수와 같은 수일 때 True. 예: Fraction(4, 2) == 2
        그 밖의 타입이면       NotImplemented 를 돌려줍니다. (아래 설명)

(3) 사칙연산
    a + b     __add__(self, other)       합을 "새" Fraction으로
    a - b     __sub__(self, other)       차를 "새" Fraction으로
    a * b     __mul__(self, other)       곱을 "새" Fraction으로
    a / b     __truediv__(self, other)   나눗셈 결과를 "새" Fraction으로.
                                         b가 0이면 ZeroDivisionError.
    other는 Fraction 또는 int입니다. int는 분모 1인 분수로 보고 계산합니다.
    네 연산 모두 self와 other를 바꾸지 않습니다.

(4) 크기 비교
    a < b      __lt__(self, other)    a가 b보다 작으면 True
    a <= b     __le__(self, other)    a가 b보다 작거나 같으면 True
    other는 Fraction 또는 int입니다. 두 메서드만 만들면 >, >=, sorted(), min(),
    max() 가 모두 동작합니다. (아래 설명)

예시
    (1)
    f = Fraction(6, 8)
    str(f)                   -> "3/4"
    print(f)                 -> 3/4         # print는 str()을 부릅니다
    f"{f}"                   -> "3/4"       # f-문자열도 str()을 부릅니다
    repr(f)                  -> "Fraction(3, 4)"
    f                        -> Fraction(3, 4)      # 대화형 셸에서 그냥 이름만 치면 repr
    [Fraction(1, 2), Fraction(4, 2)]       -> [Fraction(1, 2), Fraction(2, 1)]
    str([Fraction(1, 2)])    -> "[Fraction(1, 2)]"  # 리스트 안에서는 repr이 쓰입니다
    str(Fraction(-4, 2))     -> "-2"

    (2)
    a = Fraction(1, 2)
    a == Fraction(2, 4)          -> True
    a != Fraction(1, 3)          -> True      # != 는 따로 만들지 않아도 됩니다
    Fraction(4, 2) == 2          -> True
    2 == Fraction(4, 2)          -> True      # 정수가 왼쪽에 와도 됩니다
    Fraction(1, 2) == 0.5        -> False     # float는 다루지 않습니다
    a == "1/2"                   -> False
    Fraction(2, 4) in [Fraction(1, 2), Fraction(1, 3)]    -> True   # in도 == 를 씁니다

    (3)
    b = Fraction(1, 3)
    a + b                    -> Fraction(5, 6)
    a - b                    -> Fraction(1, 6)
    a * b                    -> Fraction(1, 6)
    a / b                    -> Fraction(3, 2)
    a + 1                    -> Fraction(3, 2)
    a * 4                    -> Fraction(2, 1)
    a / 0                    -> ZeroDivisionError
    a                        -> Fraction(1, 2)       # a는 그대로
    (a + b) * 6              -> Fraction(5, 1)       # 결과도 Fraction이라 이어서 계산됩니다
    a + b == Fraction(5, 6)  -> True                 # (2)의 == 가 그대로 쓰입니다

    (4)
    a < b                    -> False
    a <= Fraction(2, 4)      -> True
    a > b                    -> True      # __gt__ 를 만들지 않았지만 됩니다
    a < 1                    -> True
    fs = [Fraction(2, 3), Fraction(1, 2), Fraction(3, 4), Fraction(1, 6)]
    sorted(fs)               -> [Fraction(1, 6), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
    min(fs), max(fs)         -> Fraction(1, 6), Fraction(3, 4)

매직 메서드로 생각하는 법
    지난주에 f.to_string() 이라고 "내가" 불렀습니다. 이번 주에는 그 메서드 이름을
    __str__ 로 바꾸기만 합니다. 그러면 str(f), print(f), f"{f}" 를 쓸 때 "파이썬이"
    f.__str__() 를 대신 불러 줍니다. 양쪽에 밑줄 두 개가 붙은 이런 메서드를
    매직 메서드(특수 메서드)라고 합니다. 내가 직접 부르는 일은 거의 없고, 파이썬
    문법(str(), print, +, ==, <, len(), [] …)이 뒤에서 부릅니다. 이번 주 문제는
    전부 "어느 문법이 어느 메서드를 부르는가"를 익히는 것입니다.

    (1) __str__과 __repr__은 둘 다 문자열을 돌려주지만 쓰이는 곳이 다릅니다.
        __str__    사람이 읽기 좋게.        print(f), str(f), f"{f}"
        __repr__   코드로 다시 만들 수 있게.  repr(f), 셸에서 f, 리스트/딕셔너리 안의 f
    __str__이 없으면 파이썬은 대신 __repr__을 씁니다. 그래서 __repr__ 하나만
    만들어도 print는 되지만, 그 반대는 아닙니다.

    (2) a == b 라고 쓰면 파이썬은 a.__eq__(b) 를 부릅니다. __eq__을 만들지 않은
    클래스는 "같은 객체인가(is)"로만 비교해서, 지난주 서술형 S4-(a)처럼 값이 같아도
    False가 나왔습니다. 이제 "무엇을 같다고 볼지"를 우리가 정합니다.
    other가 무엇인지 모르기 때문에 세 갈래가 있습니다. 모르는 타입이면
    NotImplemented 를 return 합니다(raise 아님!). "나는 이 비교를 모르겠다"는 뜻의
    특별한 값으로, 파이썬은 이걸 받으면 상대편(other.__eq__(self))에게 한 번 더
    물어보고, 그래도 안 되면 False로 정합니다. 2 == Fraction(4, 2) 가 True가 되는
    것도 같은 원리입니다. int의 __eq__이 Fraction을 몰라 NotImplemented를 돌려주면,
    파이썬이 Fraction의 __eq__을 뒤집어 불러 줍니다.
    a != b 는 a.__eq__(b) 의 결과를 뒤집어 계산되므로 따로 만들지 않습니다.

    (3) a + b 는 a.__add__(b) 입니다. 지난주에 a.add(b) 라고 만들었다면 이름만
    바꾸면 됩니다. 지난주와 같은 원칙: 수를 나타내는 객체의 연산은 자기를 바꾸지
    않고 Fraction(새 분자, 새 분모) 를 "만들어 돌려"줍니다. 약분은 __init__이
    하므로 분자·분모를 계산해 넘기기만 하면 결과는 저절로 기약분수입니다.

    (4) sorted(), min(), max()는 원소들을 < 로만 비교합니다. 그러니 __lt__ 하나를
    만들면 정렬이 됩니다. 어떤 기준으로 줄 세울지를 클래스가 스스로 아는 것입니다.
    a > b 를 만나면 파이썬은 먼저 a.__gt__(b) 를 찾고, 없으면 "b < a 와 같은
    뜻"이라며 b.__lt__(a) 를 뒤집어 부릅니다. >= 도 <= 를 뒤집어 씁니다. 그래서
    __lt__, __le__ 둘만 만들어도 네 비교가 전부 됩니다. ((2)의 2 == Fraction(4, 2)
    와 같은 원리입니다.) 단, 1 < Fraction(3, 2) 처럼 정수가 왼쪽에 오면 뒤집은 것은
    Fraction(3, 2) > 1, 즉 __gt__ 이므로 이번 문제에서는 지원하지 않습니다.

    연산자와 메서드 이름
        +  __add__    -  __sub__    *  __mul__    /  __truediv__
        // __floordiv__   % __mod__   ** __pow__          (이번 주에는 안 만듭니다)
        <  __lt__    <=  __le__    >  __gt__    >=  __ge__    ==  __eq__    !=  __ne__

힌트
    - (1) 둘 다 self만 받고 문자열을 "돌려줍니다"(return). print 하면 안 됩니다.
      __repr__에서는 분모가 1인지 따지지 않습니다. 항상 두 수.
    - (2) other가 어느 타입인지는 isinstance 로 갈라냅니다. 갈래는 셋입니다.
      비교 결과는 bool이어야 합니다.
    - (3) 네 메서드가 모두 "other가 int면 분수로 바꾸기"로 시작합니다. __init__의
      den 기본값이 1인 것을 쓰세요. 분자·분모는 통분해서 정수 곱셈·덧셈만으로
      만듭니다. / 를 쓰면 float가 됩니다.
      나눗셈은 계산하기 전에 0으로 나누는지 확인해 ZeroDivisionError 를 냅니다.
      그냥 두면 Fraction(x, 0) 에서 ValueError 가 먼저 납니다.
    - (4) 분모가 모두 양수라는 점을 쓰면 나눗셈(float) 없이 정수끼리 비교할 수
      있습니다. float로 비교하면 큰 수에서 틀립니다. __le__ 는 __lt__ 와 __eq__ 을
      조합해도 됩니다.
    - 테스트는 ==, !=, <, <= 의 결과를 is True / is False 로 확인합니다.
"""

import math


class Fraction:
    def __init__(self, num: int, den: int = 1) -> None:
        if den == 0:
            raise ValueError("분모는 0일 수 없습니다")
        if den < 0:
            num, den = -num, -den
        g = math.gcd(num, den)
        self.num = num // g
        self.den = den // g

    # (1) 출력
    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    # (2) 같은지 비교
    def __eq__(self, other) -> bool:
        raise NotImplementedError

    # (3) 사칙연산
    def __add__(self, other) -> "Fraction":
        raise NotImplementedError

    def __sub__(self, other) -> "Fraction":
        raise NotImplementedError

    def __mul__(self, other) -> "Fraction":
        raise NotImplementedError

    def __truediv__(self, other) -> "Fraction":
        raise NotImplementedError

    # (4) 크기 비교
    def __lt__(self, other) -> bool:
        raise NotImplementedError

    def __le__(self, other) -> bool:
        raise NotImplementedError

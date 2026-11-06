"""
문제 2. 부품 번호표 (복습: 클래스 변수, @classmethod, @staticmethod)

로봇 부품을 나타내는 클래스 Part를 작성하세요. 이름 name과 가격 price를 받습니다.

    Part.count            지금까지 만들어진 부품 수. 처음에는 0. (클래스 변수)
    p.name, p.price       받은 값 그대로
    p.id                  몇 번째로 만들어졌는지. 1부터.

    Part.is_valid_price(p)     가격이 규칙에 맞으면 True, 아니면 False. (정적 메서드)
                               규칙: int 타입이고 0보다 큼.
    Part(name, price)          price가 규칙에 맞지 않으면 ValueError. 이때 count는
                               오르지 않습니다.
    Part.from_string(s)        "모터, 1200" 꼴의 문자열로 부품을 만듭니다. (클래스 메서드)
                               쉼표로 나누고, 조각 앞뒤 공백은 무시하고, 가격은 int로
                               바꿉니다.

예시
    Part.count                     -> 0
    a = Part("모터", 1200)
    b = Part("바퀴", 300)
    a.id, b.id, Part.count         -> 1, 2, 2

    Part.is_valid_price(1200)      -> True
    Part.is_valid_price(0)         -> False
    Part.is_valid_price(-5)        -> False
    Part.is_valid_price("1200")    -> False     # 문자열은 가격이 아닙니다
    Part("센서", 0)                -> ValueError
    Part.count                     -> 2         # 실패한 생성은 세지 않습니다

    c = Part.from_string(" 센서 , 450 ")
    c.name, c.price, c.id          -> "센서", 450, 3

클래스로 생각하는 법 (복습)
    세 종류의 메서드를 한 클래스에서 다시 봅니다.
        인스턴스 메서드   self    (이번 문제에는 없음)
        클래스 메서드     cls     from_string: 부품이 아직 없는데 부품을 만드는 일
        정적 메서드       없음    is_valid_price: 어느 상태도 안 건드리는 규칙
    count는 "어느 한 부품"의 것이 아니라 Part 전체의 정보라서 클래스 변수입니다.
    바꿀 때는 Part.count += 1 이라고 클래스 이름으로 씁니다.

힌트
    - 골격의 def 윗줄에 데코레이터가 비어 있습니다. 알맞은 것을 붙이세요.
      골격에 count = 0 도 없습니다. 클래스 몸통에 직접 적습니다.
    - "int 타입인지"는 isinstance 로 확인합니다. 문자열 "1200" 을 0과 비교하면
      TypeError가 나므로 어느 검사를 먼저 할지 생각하세요.
    - "실패한 생성은 세지 않습니다"는 __init__ 안에서 어느 줄이 먼저 오는지의
      문제입니다.
    - from_string 은 지난주 문제 5의 from_string 과 같은 모양입니다.
"""


class Part:
    def __init__(self, name: str, price: int) -> None:
        raise NotImplementedError

    def is_valid_price(price) -> bool:
        raise NotImplementedError

    def from_string(cls, s: str) -> "Part":
        raise NotImplementedError

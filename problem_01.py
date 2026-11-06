"""
문제 1. 로봇과 배터리 (복습: 클래스, 인스턴스 메서드, 다른 객체 받기)

이번 주 앞부분은 지난주 복습입니다. 소재는 로봇 정비소입니다.

이름 name과 배터리 battery를 받아 로봇 한 대를 나타내는 클래스 Robot을 작성하세요.
만들어진 로봇은 다음 네 속성과 네 메서드를 가집니다.

    name           이름
    battery        현재 배터리 (처음에는 받은 battery)
    max_battery    최대 배터리 (처음 battery와 같음. 이후 변하지 않음)
    distance       지금까지 움직인 거리. 항상 0에서 시작. (매개변수로 받지 않습니다)

    is_on()               배터리가 0보다 크면 True, 아니면 False
    move(steps)           배터리가 steps 이상이면 배터리를 steps만큼 쓰고 distance를
                          steps만큼 늘린 뒤 True를 돌려줍니다. 배터리가 모자라면
                          아무 일도 하지 않고 False를 돌려줍니다.
    charge(amount)        배터리를 amount만큼 충전합니다. max_battery를 넘지 않습니다.
                          돌려주는 값은 없습니다.
    give(other, amount)   자기 배터리 amount만큼을 다른 로봇 other에게 줍니다.
                          자기 배터리가 amount보다 적으면 아무 일도 하지 않고 False.
                          아니면 자기 배터리를 amount만큼 빼고 other.charge(amount)를
                          부른 뒤 True. (other의 최대치를 넘는 만큼은 사라집니다)

예시
    r = Robot("알파", 10)
    r.name, r.battery, r.max_battery, r.distance    -> "알파", 10, 10, 0
    r.move(4)            -> True
    r.battery, r.distance                            -> 6, 4
    r.move(7)            -> False                    # 6 < 7, 아무 일도 없음
    r.battery, r.distance                            -> 6, 4
    r.charge(100)
    r.battery            -> 10                       # 최대치를 넘지 않음

    a = Robot("알파", 10)
    b = Robot("베타", 20)
    b.battery = 5                                    # b를 거의 다 썼다고 치면
    a.give(b, 3)         -> True
    a.battery, b.battery                             -> 7, 8
    a.give(b, 100)       -> False                    # 7 < 100
    a.battery, b.battery                             -> 7, 8

클래스로 생각하는 법 (복습)
    __init__ 안에서 self.속성 = 값 으로 네 속성을 붙입니다. max_battery와 distance는
    매개변수가 아니지만 __init__ 안에서 정합니다.
    give 안에는 객체가 둘(self, other) 있습니다. 누구의 배터리가 줄고 누구의
    charge를 부르는지 확인하세요. 충전의 "최대치를 넘지 않음" 규칙은 이미 charge에
    있으니 other.battery를 직접 고치지 말고 other.charge(amount)를 부릅니다.

힌트
    - "넘지 않음"은 min() 으로 한 줄에 쓸 수 있습니다.
    - move와 give는 조건을 먼저 검사해 모자라면 바로 False를 돌려주고, 상태를 바꾸는
      줄은 그 아래에 둡니다. 그래야 "아무 일도 하지 않고"가 저절로 지켜집니다.
    - 테스트가 is True / is False 로 확인하므로 진짜 bool을 돌려주세요.
"""


class Robot:
    def __init__(self, name: str, battery: int) -> None:
        raise NotImplementedError

    def is_on(self) -> bool:
        raise NotImplementedError

    def move(self, steps: int) -> bool:
        raise NotImplementedError

    def charge(self, amount: int) -> None:
        raise NotImplementedError

    def give(self, other: "Robot", amount: int) -> bool:
        raise NotImplementedError

"""
문제 3. 정비소 (복습: 객체를 담는 객체, 다른 객체에게 일 시키기)

로봇 여러 대를 맡아 두는 정비소 클래스 Garage를 작성하세요.
Robot은 완성되어 있습니다(문제 1의 답). 고치지 말고 그대로 쓰세요.

    Garage()              빈 정비소. 로봇들은 리스트 robots 에 들어갑니다.
    add(robot)            로봇을 맨 뒤에 넣습니다. 돌려주는 값은 없습니다.
    size()                맡아 둔 로봇 수
    on_robots()           켜져 있는(배터리 > 0) 로봇만 담은 새 리스트. 순서는 넣은 순서.
    total_battery()       모든 로봇의 배터리 합. 아무도 없으면 0.
    most_charged()        배터리가 가장 많은 로봇. 같으면 먼저 넣은 로봇. 없으면 None.
    charge_all(amount)    모든 로봇을 amount만큼 충전합니다. 돌려주는 값은 없습니다.
    move_all(steps)       모든 로봇에게 steps만큼 움직이라고 시키고, 실제로 움직인
                          로봇의 수를 돌려줍니다.

예시
    g = Garage()
    g.size()                 -> 0
    a = Robot("알파", 10)
    b = Robot("베타", 4)
    c = Robot("감마", 10)
    g.add(a); g.add(b); g.add(c)
    g.size()                 -> 3
    g.total_battery()        -> 24
    g.most_charged() is a    -> True       # 10으로 같지만 a를 먼저 넣음
    g.move_all(5)            -> 2          # b는 4 < 5 라서 못 움직임
    a.battery, b.battery, c.battery        -> 5, 4, 5
    g.most_charged() is a    -> True
    b.battery = 0
    g.on_robots()            -> [a, c]     # 같은 객체들이 그대로 들어 있습니다
    g.charge_all(3)
    a.battery, b.battery, c.battery        -> 8, 3, 8
    g.size()                 -> 3

    h = Garage()
    h.size()                 -> 0          # 다른 정비소는 비어 있어야 합니다

클래스로 생각하는 법 (복습)
    robots = [] 를 어디에 쓰는지가 핵심입니다. 클래스 몸통에 쓰면 모든 정비소가
    리스트 하나를 함께 씁니다. 정비소마다 따로 가지려면 __init__ 안에
    self.robots = [] 라고 씁니다. (지난주 서술형 S3)
    charge_all과 move_all은 배터리를 직접 계산하지 않습니다. 로봇을 하나씩 꺼내
    그 로봇의 charge, move를 부르면 규칙(최대치, 모자라면 안 움직임)이 저절로 지켜집니다.

힌트
    - most_charged: 빈 정비소를 먼저 처리합니다. 동점일 때 "먼저 넣은 로봇"이
      남으려면 비교에 > 와 >= 중 어느 쪽을 써야 하는지 생각하세요.
    - move_all: move가 돌려주는 값을 세기만 하면 됩니다.
"""

from typing import List, Optional


# ---- 아래 Robot은 완성된 코드입니다. 고치지 마세요. ----
class Robot:
    def __init__(self, name: str, battery: int) -> None:
        self.name = name
        self.battery = battery
        self.max_battery = battery
        self.distance = 0

    def is_on(self) -> bool:
        return self.battery > 0

    def move(self, steps: int) -> bool:
        if self.battery < steps:
            return False
        self.battery -= steps
        self.distance += steps
        return True

    def charge(self, amount: int) -> None:
        self.battery = min(self.max_battery, self.battery + amount)

    def give(self, other: "Robot", amount: int) -> bool:
        if self.battery < amount:
            return False
        self.battery -= amount
        other.charge(amount)
        return True


# ---- 여기서부터 작성하세요. ----
class Garage:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, robot: Robot) -> None:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError

    def on_robots(self) -> List[Robot]:
        raise NotImplementedError

    def total_battery(self) -> int:
        raise NotImplementedError

    def most_charged(self) -> Optional[Robot]:
        raise NotImplementedError

    def charge_all(self, amount: int) -> None:
        raise NotImplementedError

    def move_all(self, steps: int) -> int:
        raise NotImplementedError

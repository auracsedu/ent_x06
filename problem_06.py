"""
문제 6. 캐릭터와 영웅 (상속 맛보기: super(), 덮어쓰기)

지난주 Hero와 Monster는 name, hp, max_hp, is_alive, take_damage 를 똑같이 갖고
있었습니다. 같은 코드를 두 번 쓰지 않도록, 공통 부분을 Character 클래스에 모아
두었습니다(완성된 코드. 고치지 마세요). Character를 상속받는 Hero를 작성하세요.

    class Hero(Character):
        __init__(name, hp, attack)   Character의 __init__으로 name, hp, max_hp를
                                     설정한 뒤, attack과 level(1)을 추가합니다.
        strike(target)               지난주 규칙 그대로. target은 Character라면
                                     무엇이든(영웅, 괴물) 됩니다.
                                       - target.take_damage(self.attack)
                                       - 이번 공격으로 target이 쓰러졌으면 level +1,
                                         attack +2, True. 아니면 False.
                                       - 이미 쓰러진 target이면 아무 일 없이 False.
        __str__()                    Character의 __str__ 결과 뒤에 " Lv.레벨"을 붙입니다.
                                     예: "용사(100/100) Lv.1"

    is_alive, take_damage, heal 은 Character에 이미 있으므로 Hero에 다시 쓰지 않습니다.

예시
    c = Character("슬라임", 20)
    str(c)                       -> "슬라임(20/20)"
    h = Hero("용사", 100, 12)
    h.name, h.hp, h.max_hp, h.attack, h.level     -> "용사", 100, 100, 12, 1
    isinstance(h, Hero), isinstance(h, Character) -> True, True   # 영웅은 캐릭터이기도 합니다
    h.take_damage(30)                             # Character의 메서드를 그대로 씁니다
    str(h)                       -> "용사(70/100) Lv.1"
    h.strike(c)                  -> False         # c.hp 20 -> 8
    h.strike(c)                  -> True          # 쓰러짐. level 2, attack 14
    str(h)                       -> "용사(70/100) Lv.2"
    str(c)                       -> "슬라임(0/20)"

상속으로 생각하는 법
    class Hero(Character): 라고 쓰면 Hero는 Character의 모든 메서드를 물려받습니다.
    Hero 인스턴스에서 h.take_damage(30) 을 부르면 파이썬은 Hero에서 먼저 찾고, 없으면
    Character에서 찾습니다. 그래서 공통 메서드는 한 번만 씁니다.

    두 가지만 새로 배웁니다.
    (1) super().__init__(name, hp)
        부모의 __init__을 불러 공통 속성을 설정하게 맡기고, 그 뒤에 자기 것(attack,
        level)만 덧붙입니다. self.name = name 을 다시 쓰지 않습니다.
    (2) 덮어쓰기(override)
        __str__을 Hero에도 만들면 Hero 인스턴스에서는 Hero의 것이 쓰입니다. 부모의
        것을 버리는 대신 super().__str__() 로 부모 결과를 받아 뒤에 덧붙일 수 있습니다.

힌트
    - Hero의 __init__ 과 __str__ 은 둘 다 "부모 것을 부른 뒤 내 것을 덧붙이기"입니다.
      위 설명의 super() 두 가지를 그대로 씁니다.
    - strike는 지난주 문제 3의 코드와 같습니다. target의 타입은 신경 쓰지 않아도
      됩니다. Character라면 모두 is_alive, take_damage 를 갖고 있으니까요.
    - 테스트는 Hero 안에 is_alive, take_damage, heal 을 다시 정의하지 않았는지도
      확인합니다. 물려받은 것은 다시 쓰지 않습니다.
"""


# ---- 아래 Character는 완성된 코드입니다. 고치지 마세요. ----
class Character:
    def __init__(self, name: str, hp: int) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def heal(self, amount: int) -> None:
        if not self.is_alive():
            return
        self.hp = min(self.max_hp, self.hp + amount)

    def __str__(self) -> str:
        return f"{self.name}({self.hp}/{self.max_hp})"


# ---- 여기서부터 작성하세요. ----
class Hero(Character):
    def __init__(self, name: str, hp: int, attack: int) -> None:
        raise NotImplementedError

    def strike(self, target: Character) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

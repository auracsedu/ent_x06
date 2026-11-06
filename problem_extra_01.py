"""
[숙제] 문제 extra 1. 가방을 상자처럼 (컨테이너 매직 메서드: __len__, __getitem__, __contains__, __iter__)

지난주 숙제의 가방 Inventory를 다시 만듭니다. 이번에는 count(), total(), names()
같은 메서드 대신 파이썬 문법이 바로 동작하게 합니다. 아래 식이 모두 동작해야 합니다.

    식                      결과                      메서드
    Inventory()             빈 가방. 물건은 딕셔너리 items 에 {이름: 개수}
    bag.add(item, n=1)      item을 n개 넣습니다. 보통 메서드. 돌려주는 값 없음
    len(bag)                전체 개수(종류 수가 아님)      __len__
    bag["포션"]             그 물건의 개수. 없으면 0        __getitem__
    bag["포션"] = 3         개수를 3으로 맞춥니다.          __setitem__
                            0이면 items에서 이름을 지웁니다. 음수면 ValueError
    "포션" in bag           1개 이상 있으면 True            __contains__
    for name in bag         이름을 정렬된 순서로 하나씩     __iter__
    bag1 + bag2             두 가방을 합친 "새" 가방        __add__
    bag1 == bag2            items가 같으면 True            __eq__
    repr(bag)               "Inventory({'열쇠': 1, '포션': 4})"  이름 정렬 순서. 빈 가방은 "Inventory({})"

예시
    bag = Inventory()
    len(bag)                 -> 0
    bag.add("포션", 3)
    bag.add("포션")
    bag.add("열쇠")
    len(bag)                 -> 5
    bag["포션"]              -> 4
    bag["방패"]              -> 0
    "포션" in bag            -> True
    "방패" in bag            -> False
    list(bag)                -> ["열쇠", "포션"]
    [bag[name] for name in bag]     -> [1, 4]
    repr(bag)                -> "Inventory({'열쇠': 1, '포션': 4})"

    bag["포션"] = 1
    bag["열쇠"] = 0
    list(bag), len(bag)      -> ["포션"], 1
    bag["포션"] = -1         -> ValueError

    a = Inventory(); a.add("포션", 2); a.add("화살", 10)
    b = Inventory(); b.add("포션", 1); b.add("열쇠")
    c = a + b
    c["포션"], c["화살"], c["열쇠"], len(c)    -> 3, 10, 1, 14
    a["포션"]                -> 2            # a, b는 그대로
    c == a + b               -> True
    a == b                   -> False

매직 메서드로 생각하는 법
    리스트와 딕셔너리에 쓰던 len(), [], in, for 는 문법이 아니라 메서드 호출입니다.
        len(x)        x.__len__()
        x[k]          x.__getitem__(k)
        x[k] = v      x.__setitem__(k, v)
        k in x        x.__contains__(k)
        for a in x    x.__iter__() 가 돌려주는 것을 하나씩
    이 메서드들을 만들면 내 클래스도 리스트·딕셔너리처럼 쓸 수 있습니다. 지난주에
    count(), total(), names() 라고 이름 지어 부르던 것이 전부 파이썬 문법으로 바뀝니다.

힌트
    - __len__ 은 int를 돌려줘야 합니다. 종류 수가 아니라 개수의 합입니다.
    - __getitem__ 은 없는 이름에 KeyError 대신 0을 돌려줍니다. dict.get 의 기본값을
      떠올리세요.
    - __iter__ 는 리스트가 아니라 "이터레이터"를 돌려줘야 합니다. 정렬한 리스트를
      그대로 return 하면 TypeError가 납니다. iter() 가 무엇을 돌려주는지 확인하세요.
    - __contains__ 가 없어도 파이썬은 __iter__ 로 돌면서 찾아 주지만, 이 문제는
      __contains__ 를 직접 만드는 문제입니다.
    - __add__: 새 Inventory를 만들고 add 를 다시 쓰면 짧습니다.
    - repr: 딕셔너리를 정렬해 새 dict로 만든 뒤 f-문자열에 넣으면 정렬된 꼴이 나옵니다.
"""


class Inventory:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, item: str, n: int = 1) -> None:
        raise NotImplementedError

    # 여기에 필요한 매직 메서드를 작성하세요.

"""
[도전] 문제 extra 2. 호가창 (OrderBook: 가격 우선, 시간 우선 체결)

거래소의 호가창(order book)을 만듭니다. 사겠다는 주문(buy)과 팔겠다는 주문(sell)이
들어오면, 조건이 맞는 반대편 주문과 짝을 지어 체결(Trade)하고, 남은 양은 호가창에
올려 둡니다. 실제 거래소는 가격별로 정렬된 트리를 쓰지만, 여기서는 딕셔너리와
min/max 로 충분합니다.

주문 하나는 Order(id, side, price, qty) 입니다. side는 "buy" 또는 "sell", price와
qty는 양의 정수입니다. Order, Trade, 그리고 OrderBook의 __init__, best_bid,
best_ask, depth 는 완성되어 있습니다. submit 과 cancel 을 작성하세요.

체결 규칙
    - buy 주문은 "price 이하"로 팔겠다는 sell 주문과 체결됩니다.
      sell 주문은 "price 이상"으로 사겠다는 buy 주문과 체결됩니다.
    - 체결 가능한 반대편 주문이 여럿이면
        가격 우선: 새 주문에게 가장 좋은 가격부터. buy에게는 가장 싼 sell,
                   sell에게는 가장 비싼 buy.
        시간 우선: 같은 가격이면 먼저 들어온 주문부터.
    - 체결 가격은 "먼저 호가창에 올라 있던" 주문의 가격입니다. 체결 수량은 두 주문의
      남은 수량 중 작은 쪽입니다.
    - 수량이 0이 된 주문은 호가창에서 빠지고, 그 가격에 주문이 하나도 안 남으면 그
      가격 자리도 지웁니다. 새 주문에 수량이 남으면 자기 가격 자리의 맨 뒤에 올라갑니다.

OrderBook
    bids     {가격: [Order, ...]}   사겠다는 주문. 리스트는 들어온 순서
    asks     {가격: [Order, ...]}   팔겠다는 주문
    best_bid()        가장 높은 buy 가격. 없으면 None            (완성)
    best_ask()        가장 낮은 sell 가격. 없으면 None           (완성)
    depth(side)       [(가격, 수량 합), ...] 좋은 가격부터       (완성)

    submit(side, price, qty) -> (order_id, trades)              작성
        새 주문에 번호를 1부터 차례로 붙입니다(전부 체결되어도 번호는 붙습니다).
        위 규칙대로 체결하고, 남은 양을 호가창에 올립니다. trades 는 일어난 순서대로의
        Trade 리스트입니다. 체결이 없으면 빈 리스트.
    cancel(order_id) -> bool                                    작성
        호가창에 올라 있는 주문이면 지우고 True. 없는 번호이거나 이미 다 체결된
        주문이면 False.

예시
    book = OrderBook()
    book.best_bid(), book.best_ask()    -> None, None
    book.submit("buy", 100, 5)          -> (1, [])
    book.submit("buy", 101, 3)          -> (2, [])
    book.submit("sell", 102, 4)         -> (3, [])
    book.best_bid(), book.best_ask()    -> 101, 102
    book.depth("buy")                   -> [(101, 3), (100, 5)]
    book.depth("sell")                  -> [(102, 4)]

    book.submit("sell", 100, 6)         -> (4, [Trade(2, 4, 101, 3), Trade(1, 4, 100, 3)])
        # 101에 사겠다는 2번이 가격이 더 좋으니 먼저(3개 전부), 그다음 100의 1번에서 3개.
        # 4번은 6개 다 팔려서 호가창에 올라가지 않습니다.
    book.depth("buy")                   -> [(100, 2)]

    book.submit("buy", 105, 10)         -> (5, [Trade(5, 3, 102, 4)])
        # 체결가는 105가 아니라 올라 있던 3번의 102. 남은 6개는 105에 올라갑니다.
    book.depth("buy")                   -> [(105, 6), (100, 2)]
    book.depth("sell")                  -> []

    book.cancel(1)                      -> True
    book.cancel(1)                      -> False     # 이미 지웠음
    book.cancel(4)                      -> False     # 다 체결된 주문
    book.cancel(99)                     -> False     # 없는 번호
    book.depth("buy")                   -> [(105, 6)]

클래스로 생각하는 법
    submit 은 "반대편에서 체결할 것이 남아 있는 동안 가장 좋은 가격의 맨 앞 주문과
    체결한다"를 반복하는 while 문 하나입니다. 반복이 끝났을 때 수량이 남았으면 그때
    호가창에 올립니다. buy와 sell은 어느 딕셔너리를 보는지, 가격 비교 방향, 가장
    좋은 가격이 min인지 max인지만 다릅니다.
    best_bid/best_ask 는 딕셔너리 키를 min/max 로 훑기만 합니다. 가격 수가 적으면
    이걸로 충분하고, 많아지면 정렬된 자료구조가 필요해집니다. (그게 실제 거래소가
    트리를 쓰는 이유입니다.)

힌트
    - 체결 뒤 남은 수량은 Order 객체의 qty 를 직접 줄입니다. 리스트의 맨 앞을 빼는
      것은 list.pop(0). 그 가격의 리스트가 비면 딕셔너리에서 그 키를 del 합니다.
    - 가격 자리가 아직 없을 때 리스트를 새로 만드는 것은 dict.setdefault 가 편합니다.
    - 반환은 (번호, 리스트) 튜플입니다. 체결이 없어도 빈 리스트를 넣습니다.
    - cancel 은 bids 와 asks 를 모두 훑어 id가 같은 Order를 찾습니다. 찾은 뒤 리스트와
      딕셔너리를 정리하는 것은 submit 에서 한 것과 같습니다. 주문을 {id: Order} 로도
      따로 들고 있으면 빨라지지만, 그러면 체결·취소 때 두 곳을 같이 고쳐야 합니다.
      __init__ 에 속성을 추가해도 됩니다.
    - 예시의 체결 순서를 손으로 한 번 따라가 보고 시작하세요.
"""

from typing import Dict, List, Optional, Tuple


# ---- 아래 Order, Trade 는 완성된 코드입니다. 고치지 마세요. ----
class Order:
    def __init__(self, order_id: int, side: str, price: int, qty: int) -> None:
        self.id = order_id
        self.side = side
        self.price = price
        self.qty = qty

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.side!r}, {self.price}, {self.qty})"


class Trade:
    def __init__(self, buy_id: int, sell_id: int, price: int, qty: int) -> None:
        self.buy_id = buy_id
        self.sell_id = sell_id
        self.price = price
        self.qty = qty

    def __repr__(self) -> str:
        return f"Trade({self.buy_id}, {self.sell_id}, {self.price}, {self.qty})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Trade):
            return NotImplemented
        return (self.buy_id, self.sell_id, self.price, self.qty) == (other.buy_id, other.sell_id, other.price, other.qty)


class OrderBook:
    def __init__(self) -> None:
        self.bids: Dict[int, List[Order]] = {}
        self.asks: Dict[int, List[Order]] = {}
        self.next_id = 1

    def best_bid(self) -> Optional[int]:
        return max(self.bids) if self.bids else None

    def best_ask(self) -> Optional[int]:
        return min(self.asks) if self.asks else None

    def depth(self, side: str) -> List[Tuple[int, int]]:
        book = self.bids if side == "buy" else self.asks
        prices = sorted(book, reverse=(side == "buy"))
        return [(p, sum(o.qty for o in book[p])) for p in prices]

    # ---- 여기서부터 작성하세요. ----
    def submit(self, side: str, price: int, qty: int) -> Tuple[int, List[Trade]]:
        raise NotImplementedError

    def cancel(self, order_id: int) -> bool:
        raise NotImplementedError

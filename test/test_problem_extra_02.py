import pytest

from problem_extra_02 import OrderBook, Trade


def test_체결_없이_올라간다():
    book = OrderBook()
    assert (book.best_bid(), book.best_ask()) == (None, None)
    assert book.submit("buy", 100, 5) == (1, []), "체결이 없으면 (번호, 빈 리스트) 를 돌려줍니다"
    assert book.submit("buy", 101, 3) == (2, [])
    assert book.submit("sell", 102, 4) == (3, [])
    assert (book.best_bid(), book.best_ask()) == (101, 102)
    assert book.depth("buy") == [(101, 3), (100, 5)]
    assert book.depth("sell") == [(102, 4)]


def test_가격이_안_맞으면_체결되지_않는다():
    book = OrderBook()
    book.submit("buy", 100, 5)
    order_id, trades = book.submit("sell", 101, 5)
    assert (order_id, trades) == (2, []), "sell 101은 buy 100과 체결되지 않습니다 (100 < 101)"
    assert book.depth("buy") == [(100, 5)]
    assert book.depth("sell") == [(101, 5)]


def test_같은_가격이면_체결된다():
    book = OrderBook()
    book.submit("buy", 100, 5)
    assert book.submit("sell", 100, 5) == (2, [Trade(1, 2, 100, 5)])
    assert book.depth("buy") == [], "다 체결된 주문은 호가창에서 빠지고, 빈 가격 자리도 지웁니다"
    assert book.depth("sell") == []
    assert (book.best_bid(), book.best_ask()) == (None, None)


@pytest.mark.parametrize(
    "first, second, expected_price",
    [(("buy", 100, 1), ("sell", 95, 1), 100), (("sell", 100, 1), ("buy", 105, 1), 100)],
)
def test_체결가는_먼저_올라_있던_주문의_가격(first, second, expected_price):
    book = OrderBook()
    book.submit(*first)
    _, trades = book.submit(*second)
    assert len(trades) == 1
    assert trades[0].price == expected_price, f"체결가는 새 주문의 가격이 아니라 올라 있던 주문의 가격 {expected_price}입니다"
    assert trades[0].qty == 1


def test_Trade의_buy_id와_sell_id():
    book = OrderBook()
    book.submit("sell", 50, 2)
    _, trades = book.submit("buy", 50, 2)
    assert trades == [Trade(2, 1, 50, 2)], "buy_id가 앞, sell_id가 뒤입니다. 어느 쪽이 새 주문인지와 무관합니다"


def test_부분_체결_새_주문의_남은_양이_올라간다():
    book = OrderBook()
    book.submit("sell", 100, 3)
    assert book.submit("buy", 100, 8) == (2, [Trade(2, 1, 100, 3)])
    assert book.depth("sell") == []
    assert book.depth("buy") == [(100, 5)], "8개 중 3개가 체결되고 5개가 100에 올라가야 합니다"


def test_부분_체결_올라_있던_주문의_수량이_줄어든다():
    book = OrderBook()
    book.submit("buy", 100, 10)
    assert book.submit("sell", 100, 4) == (2, [Trade(1, 2, 100, 4)])
    assert book.depth("buy") == [(100, 6)], "올라 있던 주문은 남은 수량으로 그대로 올라 있어야 합니다"
    assert book.submit("sell", 100, 6) == (3, [Trade(1, 3, 100, 6)])
    assert book.depth("buy") == []


def test_가격_우선():
    book = OrderBook()
    book.submit("buy", 100, 5)
    book.submit("buy", 101, 3)
    book.submit("sell", 102, 4)
    assert book.submit("sell", 100, 6) == (4, [Trade(2, 4, 101, 3), Trade(1, 4, 100, 3)]), "sell에게는 더 비싸게 사 주는 101이 먼저입니다"
    assert book.depth("buy") == [(100, 2)]
    assert book.submit("buy", 105, 10) == (5, [Trade(5, 3, 102, 4)])
    assert book.depth("buy") == [(105, 6), (100, 2)]
    assert book.depth("sell") == []


def test_시간_우선():
    book = OrderBook()
    book.submit("buy", 100, 5)
    book.submit("buy", 100, 5)
    _, trades = book.submit("sell", 100, 7)
    assert trades == [Trade(1, 3, 100, 5), Trade(2, 3, 100, 2)], "같은 가격이면 먼저 들어온 1번이 먼저 체결됩니다"
    assert book.depth("buy") == [(100, 3)]


def test_여러_가격을_쓸어_담는다():
    book = OrderBook()
    book.submit("sell", 100, 2)
    book.submit("sell", 101, 3)
    book.submit("sell", 103, 4)
    order_id, trades = book.submit("buy", 102, 10)
    assert order_id == 4
    assert trades == [Trade(4, 1, 100, 2), Trade(4, 2, 101, 3)], "싼 것부터 102 이하를 모두 체결하고 103은 남겨 둡니다"
    assert book.depth("sell") == [(103, 4)]
    assert book.depth("buy") == [(102, 5)]


def test_번호는_체결_여부와_상관없이_차례로():
    book = OrderBook()
    assert book.submit("sell", 100, 1)[0] == 1
    assert book.submit("buy", 100, 1)[0] == 2, "전부 체결된 주문에도 번호가 붙습니다"
    assert book.submit("buy", 100, 1)[0] == 3


def test_cancel():
    book = OrderBook()
    book.submit("buy", 100, 5)
    book.submit("buy", 100, 2)
    book.submit("sell", 105, 1)
    assert book.cancel(1) is True
    assert book.depth("buy") == [(100, 2)], "취소한 주문만 빠지고 같은 가격의 다른 주문은 남습니다"
    assert book.cancel(1) is False, "이미 취소한 주문은 False"
    assert book.cancel(2) is True
    assert book.depth("buy") == []
    assert book.best_bid() is None, "가격 자리에 주문이 없으면 그 키도 지워야 합니다"
    assert book.cancel(3) is True
    assert book.depth("sell") == []
    assert book.cancel(99) is False


def test_다_체결된_주문은_취소할_수_없다():
    book = OrderBook()
    book.submit("buy", 100, 5)
    book.submit("sell", 100, 5)
    assert book.cancel(1) is False
    assert book.cancel(2) is False


def test_부분_체결된_주문은_남은_양으로_취소된다():
    book = OrderBook()
    book.submit("buy", 100, 5)
    book.submit("sell", 100, 2)
    assert book.cancel(1) is True
    assert book.depth("buy") == []
    assert book.submit("sell", 100, 1) == (3, []), "취소된 주문과는 체결되지 않습니다"


def test_취소_뒤에도_시간_순서가_유지된다():
    book = OrderBook()
    book.submit("sell", 100, 1)
    book.submit("sell", 100, 2)
    book.submit("sell", 100, 3)
    book.cancel(2)
    _, trades = book.submit("buy", 100, 4)
    assert trades == [Trade(4, 1, 100, 1), Trade(4, 3, 100, 3)]

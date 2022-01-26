from class_money import *

class Test_Money:
    def test_mul(self):
        five_dollar = Money(5, 'USD')
        ten_dollar = five_dollar.times(2)
        assert ten_dollar == Money(10, 'USD')

    def test_overriding_mul(self):
        one_dollar = Money(1, 'USD')
        assert one_dollar * 2 == Money(2, 'USD')

    def test_div(self):
        thou4_krw = Money(4000, 'KRW')
        thou_krw = thou4_krw.divide(4)
        assert thou_krw.amount == 1000
        assert thou_krw.currency == 'KRW'

    def test_addition(self):
        one_dollar = Money(1, 'USD')
        two_dollar = Money(2, 'USD')
        three_dollar = Money(3, 'USD')
        assert one_dollar + two_dollar == three_dollar


class Test_Wallet:
    def test_add_two_moneys(self):
        five_dollar = Money(5, 'USD')
        ten_dollar = Money(10, 'USD')
        wallet = Wallet()
        wallet.add(five_dollar, ten_dollar)
        assert wallet.evaluate('USD') == Money(15, 'USD')

    def test_evaluate_diff_currency(self):
        five_usd = Money(5, "USD")
        ten_euro = Money(10, 'EUR')
        wallet = Wallet()
        wallet.add(five_usd, ten_euro)
        assert wallet.evaluate('USD') == Money(17, 'USD')
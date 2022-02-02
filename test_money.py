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
        assert wallet.evaluate('USD') 

    def test_evaluate_euro_usd(self):
        five_usd = Money(5, "USD")
        ten_euro = Money(10, 'EUR')
        wallet = Wallet()
        wallet.add(five_usd, ten_euro)
        assert wallet.evaluate('USD')

    def test_evaluate_usd_krw(self):
        thou_krw = Money(1000, "KRW")
        one_usd = Money(1, 'USD')
        wallet = Wallet()
        wallet.add(thou_krw, one_usd)
        assert wallet.evaluate('KRW') 

    def test_evaluate_different_currency3(self):
        one_usd = Money(1, 'USD')
        one_yen = Money(1, 'JPY')
        wallet = Wallet()
        wallet.add(one_usd, one_yen)
        assert wallet.evaluate('JPY') 

def test_convert():
    one_euro = Money(5, 'EUR')
    expected = Money(6, 'USD')
    actual = convert(one_euro, 'USD')
    assert expected 
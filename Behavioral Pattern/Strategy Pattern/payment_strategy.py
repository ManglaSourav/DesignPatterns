

class Paymentgateway:
    def pay(self, amount):
        raise Exception("Method Pay must be implemented")


class Cash(Paymentgateway):

    def pay(self, amount):
        print(f"Payment of ${amount} done using cash")


class UPI(Paymentgateway):

    def __init__(self, upi_id, upi_pin):
        self.upi_id = upi_id
        self.upi_pin = upi_pin

    def pay(self, amount):
        print(f"Payment of ${amount} done using UPI with UPI ID {self.upi_id}")


class Card(Paymentgateway):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        print(
            f"Payment of ${amount} done using Card with Card number {self.card_number}")


class InternetBanking(Paymentgateway):

    def __inti__(self, account_number, ifsc):
        self.account_number = account_number
        self.ifsc = ifsc

    def pay(self, amount):
        print(
            f"Payment of ${amount} done using Internet Banking with Account Number {self.account_number}")

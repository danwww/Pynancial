class Annuity(object):
    def __init__(self, maturity, par_value, interval, discount_rate):
        super(Annuity, self).__init__()
        self.maturity = maturity
        self.par_value = par_value
        self.interval = interval
        self.discount_rate = discount_rate
        self.payment_discount = discount_rate / interval
        self.total_payments = maturity * interval

class IncomeStream(Annuity):
    def __init__(self, maturity, interval, par_value, discount_rate, coupon_rate):
        Annuity.__init__(self, maturity, par_value, interval, discount_rate)
        self.coupon_rate = coupon_rate
        self.payment_value = (self.par_value * self.coupon_rate) / self.interval
        self.pv = self.present_value_of_stream()
    
    def present_value_of_stream(self):
        payment_no = 1
        pv = 0

        while payment_no <= self.total_payments:
            pv += self.payment_value / ((1 + self.payment_discount) ** payment_no)
            payment_no += 1

        return round(pv, 4)


class Principal(Annuity):
    def __init__(self, maturity, interval, par_value, discount_rate):
        Annuity.__init__(self, maturity, par_value, interval, discount_rate)
        self.pv = self.present_value_of_principal()

    def present_value_of_principal(self):
        payment_no = 1
        pv = self.par_value / ((1 + self.payment_discount) ** self.total_payments)

        return round(pv, 4)    


class Bond(Principal, IncomeStream):
    def __init__(self, maturity, interval, par_value, discount_rate, coupon_rate):
        Principal.__init__(self, maturity, interval, par_value, discount_rate)
        IncomeStream.__init__(self, maturity, interval, par_value, discount_rate, coupon_rate)
        self.pv = self.present_value_of_bond()

    def present_value_of_bond(self):
        pv = self.present_value_of_principal() + self.present_value_of_stream()

        return round(pv, 4)
            


class ConstantProductInvariant:
    def __init__(self, name, asset0, asset1):
        self._name = name
        self._asset0 = asset0
        self._asset1 = asset1

    @property
    def k(self):
        return self._asset0*self._asset1

    @property
    def price(self):
        return self._asset1/self._asset0

    def quote(self, chg_asset0):
        new_asset0 = self._asset0 + chg_asset0
        new_asset1 = self.k / new_asset0
        proceeds = new_asset1 - self._asset1
        quote_price = new_asset1 / new_asset0
        slippage = abs((quote_price / self.price) - 1)
        return {
            'price': quote_price,
            'proceeds': proceeds,
            'slippage': slippage
        }

    def swap(self, chg_asset0):
        quote = self.quote(chg_asset0)
        self._asset0 += chg_asset0
        self._asset1 += quote['proceeds']

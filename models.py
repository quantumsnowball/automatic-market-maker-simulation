class ConstantProductInvariant:
    def __init__(self, name, asset0, asset1):
        self._name = name
        self._pool = [0, 0]
        self.provide_liquidity(asset0, asset1)

    @property
    def name(self):
        return self._name

    @property
    def k(self):
        return self._pool[0]*self._pool[1]

    @property
    def price(self):
        return self._pool[1]/self._pool[0]

    @property
    def pool(self):
        return (self._pool[0], self._pool[1], )

    def provide_liquidity(self, asset0, asset1):
        assert asset0 > 0
        assert asset1 > 0
        self._pool[0] += asset0
        self._pool[1] += asset1

    def withdrawal_liquidity(self, asset0, asset1):
        assert self._pool[0] >= asset0
        assert self._pool[1] >= asset1
        self._pool[0] -= asset0
        self._pool[1] -= asset1

    def quote(self, chg_asset0):
        new_asset0 = self._pool[0] + chg_asset0
        new_asset1 = self.k / new_asset0
        proceeds = new_asset1 - self._pool[1]
        quote_price = new_asset1 / new_asset0
        slippage = abs((quote_price / self.price) - 1)
        return {
            'price': quote_price,
            'proceeds': proceeds,
            'slippage': slippage
        }

    def swap(self, chg_asset0):
        quote = self.quote(chg_asset0)
        self._pool[0] += chg_asset0
        self._pool[1] += quote['proceeds']

    def sell(self, asset0):
        self.swap(+asset0)

    def buy(self, asset0):
        self.swap(-asset0)
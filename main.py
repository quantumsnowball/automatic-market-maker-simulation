class AMM:
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


def main():
    amm = AMM('BTC-ETH', 1494, 23220)
    print(f'old price: {amm.price}')
    # print(f'Product after swap: {amm.k}')
    print(f'new price: {amm.quote(.01)}')
    print(f'new price: {amm.quote(.1)}')
    print(f'new price: {amm.quote(1)}')
    print(f'new price: {amm.quote(10)}')
    print(f'new price: {amm.quote(100)}')
    print(f'new price: {amm.quote(1000)}')
    # print(f'Product after swap: {amm.k}')
    return


if __name__ == '__main__':
    main()

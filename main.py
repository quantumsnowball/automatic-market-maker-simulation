from models import ConstantProductInvariant


def main():
    amm = ConstantProductInvariant('BTC-ETH', 1494, 23220)
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

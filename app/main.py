from exchange_interface import ExchangeInterface


def send_order_with_amount(exchange_interface, amount):
    amount_sent = exchange_interface.send_order(amount)
    ans = f'{amount_sent} is sent to {exchange_interface.name}'
    print(ans)

    return ans


if __name__ == '__main__':
    send_order_with_amount(ExchangeInterface('binance'), 5)

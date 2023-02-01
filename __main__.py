#!/usr/bin/python3
# coding: utf-8


def get_new_bet(recovery, odd, value):
    if (value * odd) <= (recovery + value):
        value += 1
        return get_new_bet(recovery, odd, value)
    else:
        return value


if __name__ == '__main__':
    recovery = int(input("Recovery value: "))
    odd = float(input("Odd value: ").replace(",", "."))

    new_bet = get_new_bet(recovery, odd, 1)
    gain = (new_bet * odd) - (recovery + new_bet)
    total = recovery + new_bet

    print()
    print(f"New bet: {new_bet}")
    print(f"Gain: {gain}")
    print(f"New total: {total}")

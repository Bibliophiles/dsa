def towerBreakers(n, m):
    return 2 if m == 1 or n % 2 == 0 else 1


def towerBreakers(n, m):
    if m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1

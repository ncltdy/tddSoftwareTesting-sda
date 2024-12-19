def is_prime(n):
    if not isinstance(n,int):
        raise TypeError
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3,int(n ** 0.5)+1,2):
        print(i)
        if n % i == 0:
            return False
    return True


def factorial(n):
    multiplayer = n-1
    result = n
    if n < 0:
        return None
    if n == 0:
        return 1
    for i in range(1,n):
        result *= multiplayer
        multiplayer -= 1
    return result


def factorial2(n):
    result = 1
    if n < 0:
        return None
    if n == 0:
        return 1
    for i in range(2,n+1):
        result *= i

    return result
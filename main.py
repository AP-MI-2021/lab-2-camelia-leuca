def get_largest_prime_below(n):
    """
    Gaseste ultimul numar prim mai mic decat un numar dat.
    :param n:un numar intreg
    :return: ultimul numar prim mai mic decat numarul dat sau False daca nu exista
    """
    while n > 2:
        ok = True
        n = n - 1
        for i in range(2, n):
            if n % i == 0:
                ok = False
        if ok:
            return n
    return False


def is_palindrome(n):
    """
    Determina daca un numar dat este palindrom.
    :param n:un numar intreg
    :return:True daca numarul dat este palindrom sau False in caz contrar
    """
    invers = 0
    copie = n
    while n != 0:
        invers = n % 10 + invers * 10
        n = n // 10
    if invers == copie:
        return True
    return False


def is_antipalindorme(n):
    """
    Determina daca un numar este antipalindrom.
    :param n: int
    :return: True daca numarul dat este antipalindrom sau False in caz contrar
    """
    copie = n
    prima_cifra = 1
    while copie > 9:
        prima_cifra = prima_cifra * 10
        copie = copie // 10
    while n > 9:
        if n % 10 == n // prima_cifra:
            return False
        n = n // 10
        n = n // prima_cifra
    return True


def test_is_antipalindrome():
    assert is_antipalindorme(23) is True
    assert is_antipalindorme(22) is False
    assert is_antipalindorme(5) is True


def test_get_largest_prime_below():
    assert get_largest_prime_below(6) == 5
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(1) is False


def test_is_palindrome():
    assert is_palindrome(55) is True
    assert is_palindrome(51) is False
    assert is_palindrome(9) is True


def main():
    while True:
        print('1.Gaseste ultimul numar prim mai mic decat un numar dat - exercitiul 1.')
        print('2.Determina daca un numar dat este palindrom - exercitiul 5.')
        print('3.Determina daca un numar dat este antipalindrom - exercitiul 7.')
        print('x.Iesire din program.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            nr = int(input('Dati numarul: '))
            prim = get_largest_prime_below(nr)
            print(prim)
        elif optiune == '2':
            nr = int(input('Dati numarul: '))
            palindrom = is_palindrome(nr)
            print(palindrom)
        elif optiune == '3':
            nr = int(input('Dati numarul: '))
            antipalindrom = is_antipalindorme(nr)
            print(antipalindrom)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')


test_get_largest_prime_below()
test_is_palindrome()
test_is_antipalindrome()
main()

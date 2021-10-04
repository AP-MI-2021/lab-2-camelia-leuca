def get_largest_prime_below(n):
    '''
    Gaseste ultimul numar prim mai mic decat un numar dat.
    :param n:int
    :return: ultimul numar prim mai mic decat numarul dat sau False daca nu exista
    '''
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
    '''
    Determina daca un numar dat este palindrom.
    :param n:int
    :return:True daca numarul dat este palindrom sau False in caz contrar
    '''
    invers = 0
    copie = n
    while n != 0:
        invers = n % 10 + invers * 10
        n = n // 10
    if invers == copie:
        return True
    return False


def test_get_largest_prime_below():
    assert get_largest_prime_below(6) == 5
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(1) == False


def test_is_palindrome():
    assert is_palindrome(55) == True
    assert is_palindrome(51) == False


def main():
    while True:
        print('1.Gaseste ultimul numar prim mai mic decat un numar dat - exercitiul 1.')
        print('2.Determina daca un numar dat este palindrom - exercitiul 5.')
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
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')


test_get_largest_prime_below()
test_is_palindrome()
main()

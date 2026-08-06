def palindromo(numero):
    if numero < 0:
        return False
    else:
        valor = str(numero)
        if valor == valor[::-1]:
            return True
        else:
            return False

assert(palindromo(121) == True)
assert(palindromo(-121) == False)
assert(palindromo(122) == False)
assert(palindromo(252) == True)
assert(palindromo(873) == False)

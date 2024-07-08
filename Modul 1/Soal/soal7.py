def faktorPrima(n):
    faktor = []
    i = 2
    while i <= n :
        if n % i ==  0:
            faktor.append(i)
            n //= i
        else :
            i += 1
    return tuple(faktor)


print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))
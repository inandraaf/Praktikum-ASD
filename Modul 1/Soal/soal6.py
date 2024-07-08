def apakah_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cetak_bilangan_prima():
    for num in range(2, 1001):
        if apakah_prima(num):
            print(num)


cetak_bilangan_prima()

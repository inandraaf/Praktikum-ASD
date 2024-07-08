def gabungkanDuaListUrut(A, B):
    la = len(A)
    lb = len(B)
    C = list() # C adalah list baru
    i = 0
    j = 0

    # Gabungkan keduanya sampai salah satu kosong
    while i < la and j < lb:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < la: # Jika A mempunyai sisa
        C.append(A[i]) # tumpukkan ke list baru itu
        i += 1 # satu demi satu

    while j < lb: # Jika B mempunyai sisa
        C.append(B[j]) # tumpukkan ke list baru itu
        j += 1 # satu demi satu

    return C

# Contoh penggunaan fungsi dan mencetak hasilnya
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
hasil = gabungkanDuaListUrut(A, B)
print(hasil) # Output: [1, 2, 3, 4, 5, 6, 7, 8]

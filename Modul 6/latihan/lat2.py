def mergeSort(A):
    # Fungsi untuk mencetak list selama proses pembelahan dan penggabungan
    def print_list(msg, lst):
        print(f"{msg}: {lst}")
    
    print_list("Membelah", A)
    
    if len(A) > 1:
        mid = len(A) // 2
        
        # Optimisasi slicing dengan menggunakan copy pada bagian tertentu
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        # Di bawah ini adalah proses penggabungan
        i, j, k = 0, 0, 0
        
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i += 1
            else:
                A[k] = separuhKanan[j]
                j += 1
            k += 1
        
        # Jika ada sisa di separuhKiri
        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i += 1
            k += 1
        
        # Jika ada sisa di separuhKanan
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j += 1
            k += 1
        
        print_list("Menggabungkan", A)

# Contoh penggunaan fungsi
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print("Hasil akhir:", alist)

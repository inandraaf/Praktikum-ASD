def partisi(A, awal, akhir):
    nilaiPivot = A[awal]  # Di sini nilaiPivot kita ambil dari elemen yang paling kiri.
    penandaKiri = awal + 1  # Posisi awal penandaKiri. Lihat Gambar 6.3.
    penandaKanan = akhir  # Posisi awal penandaKanan.

    selesai = False
    while not selesai:  # loop di bawah adalah untuk mengatur ulang posisi semua elemen

        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:  # penandaKiri bergerak ke kanan,
            penandaKiri = penandaKiri + 1  # sampai ketemu suatu nilai yang lebih besar dari nilaiPivot

        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:  # penandaKanan bergerak ke kiri,
            penandaKanan = penandaKanan - 1  # sampai ketemu suatu nilai yang lebih kecil dari nilaiPivot

        if penandaKanan < penandaKiri:  # Kalau dua penanda sudah bersilangan,
            selesai = True  # selesai & lanjut ke penempatan pivot
        else:
            # Tapi kalau belum bersilangan, tukarlah isi yang ditunjuk oleh penandaKiri dan penandaKanan
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    # Kalau acara tukar menukar posisi sudah selesai, kita lalu menempatkan pivot pada posisi yang tepat,
    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp  # yakni posisi penandaKanan. Lihat Gambar 6.3 dan 6.4.
    # Posisi penandaKanan adalah juga titikBelah.

    # Print untuk melihat proses pemisahan
    print(f"Setelah partisi dengan pivot {nilaiPivot}: {A}")

    return penandaKanan  # Fungsi ini mengembalikan titikBelah ke pemanggil

# Contoh penggunaan fungsi partisi
A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
pivot_index = partisi(A, 0, len(A) - 1)
print(f"Array setelah partisi: {A}")
print(f"Index pivot: {pivot_index}")

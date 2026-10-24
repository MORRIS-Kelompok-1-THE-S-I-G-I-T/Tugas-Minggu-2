#=============================================
# PRAKTIKUM 3 : DERAT ARITMATIKA & AKUMULTOR
#=============================================

print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukan Suku Pertama (a): "))
beda = int(input("Masukan Beda Deret    (b): "))

# 1. IMPLEMENTASI WHILE : Validasi input Jumlah satu suku agar harus positif (> 0)
banyak = int(input("Masukan Banyak Suku     (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dari 0!")
    banyak = int(input("Silahkan masukan ulang Banyak suku (n): "))

# 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya
suku = awal
total = 0 # Celengan Akumulator

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku    # Akumulasi penjumlahan bertahap
    suku += beda     # Menyiapkan suku berikutnya

print(f"Total Jumlah Seluruh Deret = {total}")
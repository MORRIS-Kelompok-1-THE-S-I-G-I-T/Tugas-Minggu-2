for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"baris {baris}x{kolom}={baris*kolom}", end=" | ")
    print()

nilai_maba = [12, 32, 35]
nilai_maba.append(95)

print("daftar nilai :", (nilai_maba))
print("daftar nilai :", max(nilai_maba))
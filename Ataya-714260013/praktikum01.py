kehadiran = int(input("Jumlah Kehadiran (1-14): "))
nilai = int(input("Jumlah Nilai (1-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("Lulus - Nilai Memuaskan")
    else:
        print("Remedial - Nilai Ujian Kurang")
else: 
    print("Tidak Lulus - Kehadiran Kurang dari 12")
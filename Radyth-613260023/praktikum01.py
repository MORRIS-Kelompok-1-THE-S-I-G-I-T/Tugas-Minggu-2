kehadiran = int(input("Jumlah Kehadiran (1-14): "))
nilai = int(input("Jumlah Nilai (1-100): "))

if kehadiran >= 17:
    if nilai >= 85:
        print("Lulus - Nilai Lumayan")
    else:
        print("Remedial - Nilai Ujian Kurang")
else: 
    print("Tidak Lulus - Kehadiran Kurang dari 12")
    ######### praktukim01.py ########
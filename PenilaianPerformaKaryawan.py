# Program Penilaian Performa Karyawan
# Menggunakan for loop dan nested if

print("=== Program Penilaian Performa Karyawan ===")

total_nilai = 0

# Loop untuk 3 aspek penilaian
for i in range(1, 4):
    nilai = int(input(f"Masukkan nilai aspek ke-{i} (1-10): "))
    total_nilai += nilai

# Hitung rata-rata
rata_rata = total_nilai / 3

# Nested if untuk menentukan kategori
if rata_rata > 8:
    kategori = "Excellent"
else:
    if rata_rata >= 6:
        kategori = "Good"
    else:
        kategori = "Need Improvement"

# Output hasil
print(f"\nRata-rata nilai: {rata_rata:.2f}")
print(f"Kategori performa: {kategori}")
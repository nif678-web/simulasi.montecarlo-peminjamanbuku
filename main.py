import random

data_simulasi = [
    {"peminjam": 0, "prob": 0.05, "kumulatif": 0.05, "interval": (1, 5)},
    {"peminjam": 1, "prob": 0.10, "kumulatif": 0.15, "interval": (6, 15)},
    {"peminjam": 2, "prob": 0.40, "kumulatif": 0.55, "interval": (16, 55)},
    {"peminjam": 3, "prob": 0.30, "kumulatif": 0.85, "interval": (56, 85)},
    {"peminjam": 4, "prob": 0.15, "kumulatif": 1.00, "interval": (86, 100)}
]

def get_peminjam(bilangan_acak):
    for item in data_simulasi:
        bawah, atas = item["interval"]
        if bawah <= bilangan_acak <= atas:
            return item["peminjam"]
    return 0

jumlah_hari_simulasi = 15
total_peminjam_simulasi = 0

print("=== SIMULASI MONTE CARLO: PEMINJAM PERPUSTAKAAN ===")
print(f"{'Hari ke-':<10} | {'Bilangan Acak':<15} | {'Simulasi Peminjam':<18}")
print("-" * 50)

# Simulasi harian menggunakan random integer 1 sampai 100 (seperti RANDBETWEEN di Excel)
for hari in range(1, jumlah_hari_simulasi + 1):
    bil_acak = random.randint(1, 100)
    peminjam = get_peminjam(bil_acak)
    total_peminjam_simulasi += peminjam

    print(f"{hari:<10} | {bil_acak:<15} | {peminjam:<18} buku")

rata_rata = total_peminjam_simulasi / jumlah_hari_simulasi
print("-" * 50)
print(f"Total Peminjam Selama {jumlah_hari_simulasi} Hari: {total_peminjam_simulasi} buku")
print(f"Rata-rata Peminjam Per Hari: {rata_rata:.2f} buku")

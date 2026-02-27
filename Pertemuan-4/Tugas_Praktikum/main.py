# main.py
from tabulate import tabulate
from konverter import konversi_ke_idr
from kurs import KURS_MATA_UANG

print("=== APLIKASI KONVERTER MATA UANG ===")

tabel = []
for mata_uang, nilai in KURS_MATA_UANG.items():
    tabel.append([mata_uang, nilai])

print(tabulate(tabel, headers=["Mata Uang", "Kurs ke IDR"], tablefmt="grid"))

kode = input("Masukkan kode mata uang: ").upper()
jumlah = float(input("Masukkan jumlah uang: "))

try:
    hasil = konversi_ke_idr(kode, jumlah)
    print(f"Hasil konversi: {jumlah} {kode} = {hasil} IDR")
except ValueError as e:
    print(e)
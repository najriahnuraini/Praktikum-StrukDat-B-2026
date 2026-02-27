# konverter.py
# berisi fungsi konversi mata uang

from kurs import KURS_MATA_UANG

def konversi_ke_idr(mata_uang, jumlah):
    if mata_uang not in KURS_MATA_UANG:
        raise ValueError("Mata uang tidak tersedia")

    return jumlah * KURS_MATA_UANG[mata_uang]
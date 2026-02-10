kelas_A = {"struktur data", "basis data", "AI", "pemrograman web"}
kelas_B = {"struktur data", "machine learning", "AI", "cloud computing"}

print(kelas_A & kelas_B)

kelas_A.update(kelas_B)
print(kelas_A)
import numpy as np
import matplotlib.pyplot as plt

# Variabel yang digunakan
h0 = 50 # ketinggian awal benda (meter)
g = 9.8   # percepatan gravitasi (m/s^2)

# Menghitung waktu yang diperlukan benda untuk mencapai tanah
t_total = np.sqrt((2 * h0) / g)
print(f"Waktu yang diperlukan benda untuk mencapai tanah: {t_total:.2f} detik")

# Membuat array waktu dari 0 hingga t_total
t = np.linspace(0, t_total, 500)

# Menghitung kecepatan sebagai fungsi waktu
v_t = g * t

# Menghitung posisi sebagai fungsi waktu
h_t = h0 - 0.5 * g * t**2

# Print beberapa hasil kecepatan dan posisi pada beberapa titik waktu
print("\nHasil Kecepatan dan Posisi pada beberapa waktu:")
for i in range(0, len(t), 100):  # print hasil setiap 100 data
    print(f"Waktu: {t[i]:.2f} s, Kecepatan: {v_t[i]:.2f} m/s, Posisi: {h_t[i]:.2f} m")

# Membuat grafik kecepatan vs waktu
plt.figure(figsize=(8, 5))
plt.plot(t, v_t, label="Kecepatan (v(t))", color='blue')
plt.title("Grafik Kecepatan vs Waktu")
plt.xlabel("Waktu (detik)")
plt.ylabel("Kecepatan (m/s)")
plt.grid(True)
plt.legend()
plt.show()

# Membuat grafik posisi vs waktu
plt.figure(figsize=(8, 5))
plt.plot(t, h_t, label="Posisi (h(t))", color='green')
plt.title("Grafik Posisi vs Waktu")
plt.xlabel("Waktu (detik)")
plt.ylabel("Ketinggian (meter)")
plt.grid(True)
plt.legend()
plt.show()

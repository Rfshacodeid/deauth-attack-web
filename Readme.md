# Web Deauthentication Attack

Proyek ini adalah contoh sederhana untuk memahami konsep Deauthentication Attack menggunakan antarmuka web. Proyek ini dikembangkan oleh **Rafasha Alfiandi**. Untuk diskusi atau pertanyaan, silakan hubungi melalui [Telegram](http://t.me/Rafashaalfian).

## 📖 Tentang Deauthentication Attack

Deauthentication Attack adalah salah satu jenis serangan dalam jaringan Wi-Fi yang bertujuan untuk memutuskan koneksi antara perangkat klien dan titik akses (Access Point). Serangan ini bekerja dengan mengirimkan frame deauthentication palsu.

⚠️ **Catatan Penting:**
Proyek ini hanya untuk tujuan pembelajaran dan eksperimen dalam lingkungan yang telah disetujui. Jangan gunakan proyek ini untuk tujuan ilegal atau tanpa izin.

## 📋 Fitur
- Antarmuka web sederhana untuk memulai serangan deauthentication.
- Menampilkan daftar perangkat target (klien).
- Menyediakan kontrol untuk memutus koneksi perangkat target.
- Implementasi beberapa serangan tambahan seperti ARP Poisoning, SYN Flood, ICMP Flood, dan UDP Flood.

## 🚀 Instalasi dan Penggunaan

### Prasyarat
- Python (versi 3.7 atau lebih baru)
- Paket berikut harus diinstal:
  - Flask (untuk antarmuka web)
  - Scapy (untuk manipulasi paket jaringan)
  - Threading (untuk eksekusi paralel)

### Langkah-langkah Instalasi
1. Clone repository ini:
   ```bash
   git clone https://github.com/Rafashaalfian/deauth-attack-web.git
   cd deauth-attack-web
   ```
2. Instal dependensi:
   ```bash
   pip install scapy
   ```
3. Pastikan antarmuka Wi-Fi Anda mendukung mode monitor, lalu atur ke mode monitor menggunakan perintah:
   ```bash
   sudo airmon-ng start wlan0
   ```
   Ganti `wlan0` dengan nama antarmuka Wi-Fi Anda.

4. Jalankan aplikasi:
   ```bash
   sudo python3 wifiattack.py atau wifiattack.py
   ```    
5. Akses antarmuka web melalui browser di `http://127.0.0.1:5000`.


### Contoh Penggunaan
1. Pilih jaringan Wi-Fi target dari antarmuka web.
2. Pilih perangkat klien target untuk diputus koneksi.
3. Klik tombol "Deauth" untuk memulai serangan.

### Konfigurasi Skrip Python
Skrip Python dapat dikonfigurasi menggunakan parameter berikut:
- **iface**: Nama antarmuka Wi-Fi yang digunakan (contoh: "wlan0").
- **ap_mac**: Alamat MAC access point target.
- **target_mac**: Alamat MAC perangkat target.
- **target_ip**: Alamat IP perangkat target.
- **gateway_ip**: IP gateway jaringan.
- **target_port**: Port target untuk SYN Flood dan UDP Flood.

Contoh konfigurasi:
```python
iface = "wlan0"  # Antarmuka Wi-Fi yang digunakan
ap_mac = "c8:5a:9f:8c:fb:04"  # MAC address access point target
target_mac = "0c:d2:92:ac:11:83"  # MAC address perangkat target
target_ip = "192.168.1.100"  # IP perangkat target
gateway_ip = "192.168.1.1"  # IP gateway jaringan
target_port = 80  # Port target untuk SYN Flood dan UDP Flood
```

Untuk menjalankan serangan lengkap, gunakan fungsi `full_attack`:
```python
full_attack(iface, ap_mac, target_mac, target_ip, gateway_ip, target_port)
```

## ⚙️ Struktur Proyek
```
.
Deauthentication Attack/
├── wifiattack.py       # File utama untuk menjalankan aplikasi
└── README.md           # Dokumentasi proyek
```

## ⚠️ Peringatan Hukum
Penggunaan proyek ini untuk menyerang jaringan tanpa izin adalah **melanggar hukum**. Pengembang tidak bertanggung jawab atas penyalahgunaan proyek ini. Harap gunakan dengan etika dan tanggung jawab penuh.

## 📫 Kontak
Untuk pertanyaan lebih lanjut, hubungi melalui [Telegram](http://t.me/Rafashaalfian).

---
Dikembangkan dengan ❤️ oleh **Rafasha Alfiandi**

# 🚀 Quick Start - Authentication System

Panduan cepat untuk mulai menggunakan sistem login di aplikasi Cassava Disease Detection.

## 5 Langkah Setup Cepat

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Jalankan Aplikasi
```bash
streamlit run app.py
```

### 3️⃣ Buat Akun Pertama Anda
- Pilih tab **"📝 Sign Up"**
- Isi formulir dengan:
  - **Email**: user@example.com
  - **Username**: myusername
  - **Nama Lengkap**: Nama Anda
  - **Password**: password123
- Klik **"Daftar"**

### 4️⃣ Login dengan Akun Anda
- Pilih tab **"🔐 Login"**
- Masukkan email dan password
- Klik **"Login"**

### 5️⃣ Mulai Analisis!
- Upload foto daun singkong
- Sistem akan menyimpan hasil analisis ke akun Anda
- Data tersimpan secara permanen di database

---

## 📁 File-File Baru Yang Ditambahkan

```
cassava/
├── auth.py                      # Authentication logic & UI
├── database.py                  # SQLite database management
├── cassava_users.db             # Database file (auto-created)
├── AUTHENTICATION_SETUP.md      # Dokumentasi lengkap
├── QUICK_START_AUTH.md          # File ini
├── streamlit/
│   └── secrets.toml.example     # Template untuk secrets
└── requirements.txt             # Updated dengan streamlit-oauth
```

---

## 🔑 Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| 📝 **Sign Up** | Buat akun baru dengan email & password |
| 🔐 **Login** | Login dengan email & password |
| 🚪 **Logout** | Logout dari aplikasi |
| 💾 **Auto Save** | Analisis otomatis tersimpan per user |
| 📊 **User History** | Riwayat analisis personal |
| 🔒 **Secure** | Password dengan hashing PBKDF2 |

---

## 📊 Contoh Testing

### Test User 1
```
Email: demo@example.com
Username: demo
Password: demo123
Nama: Demo User
```

### Test User 2
```
Email: test@example.com
Username: testuser
Password: test123
Nama: Test User
```

Buat akun dengan data di atas, lalu coba login dengan masing-masing untuk memverifikasi sistem bekerja.

---

## ⚙️ Konfigurasi Lanjutan

### Mengaktifkan Google OAuth (Optional)

1. Buka [Google Cloud Console](https://console.cloud.google.com/)
2. Buat project baru
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Copy Client ID dan Client Secret
6. Update file `.streamlit/secrets.toml` (copy dari `secrets.toml.example`)

**Dokumentasi lengkap**: Lihat `AUTHENTICATION_SETUP.md`

---

## 🐛 Troubleshooting

**Q: Database tidak terbuat?**
- A: Jalankan `app.py`, database akan dibuat otomatis

**Q: Lupa password?**
- A: Hubungi admin atau reset database (lihat `AUTHENTICATION_SETUP.md`)

**Q: Ingin reset semua data user?**
- A: Delete file `cassava_users.db` dan jalankan ulang

**Q: Error import?**
- A: Pastikan sudah `pip install -r requirements.txt`

---

## 📞 Need Help?

1. **Dokumentasi**: Baca `AUTHENTICATION_SETUP.md` untuk detail lengkap
2. **Code**: Lihat komentar di `auth.py` dan `database.py`
3. **Database**: Check `cassava_users.db` dengan SQLite Browser

---

**Ready to go?** Run `streamlit run app.py` sekarang! 🎉
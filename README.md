# Portofolio Santri — Flask

## 1. Persiapan
- Install Python 3 dari https://www.python.org/downloads/
- Install Visual Studio Code dari https://code.visualstudio.com/
- Buka folder `portfolio_santri` di VS Code.

## 2. Buat virtual environment (opsional, disarankan)
Windows (Terminal VS Code):
```bash
python -m venv venv
venv\Scripts\activate
```
Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Flask
```bash
pip install -r requirements.txt
```

## 4. Jalankan website
```bash
python app.py
```
Buka browser dan kunjungi http://127.0.0.1:5000

## 5. Personalisasi
Edit `app.py`:
- Ganti `Nama Lengkap Anda` dengan nama Anda.
- Ubah deskripsi, pengalaman, dan keahlian sesuai pengalaman nyata.
- Ganti `emailanda@example.com` pada `templates/index.html` dengan email yang ingin ditampilkan.

Foto dan logo berada di `static/images/`. Ganti file gambarnya dengan foto/logo pilihan Anda dan pertahankan nama file agar tampil otomatis.

## Struktur folder
portfolio_santri/
  app.py
  requirements.txt
  templates/index.html
  static/css/style.css
  static/images/...

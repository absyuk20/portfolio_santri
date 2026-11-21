from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    profil = {
        "nama": "Muhammad Abdul Syukur",
        "sapaan": "Santri • Pengajar • Pengabdi",

        "pesantren": "Pondok Pesantren An Naba Al Islamiyyah",
        "lokasi": "Tonjong, Tajurhalang, Bogor",
        "angkatan": "Angkatan 10 — Akzaara Generation",

        "deskripsi": (
            "Saya adalah Muhammad Abdul Syukur, seorang santri "
            "yang memiliki semangat untuk terus belajar, mengajar, "
            "dan mengabdi. Saya memiliki minat dalam menghafal, "
            "menjelajahi wawasan teknologi, serta mengembangkan "
            "kemampuan diri. Bagi saya, ilmu bukan hanya untuk "
            "diketahui, tetapi juga untuk diamalkan dan dibagikan "
            "agar dapat memberikan manfaat bagi orang lain."
        ),

        "pendidikan": "PAUD • SD • SMP • SMK",

        "hobi": (
            "Menghafal, healing, dan mencari wawasan "
            "baru di bidang teknologi."
        ),

        "cita_cita": (
            "Menjadi pribadi yang sukses di dunia dan akhirat, "
            "serta mampu memberikan manfaat bagi orang lain "
            "melalui ilmu, akhlak, harta, dan wawasan."
        ),

        "email": "absyuk20@gmail.com",
    }

    keahlian = [
        (
            "Bahasa Arab",
            "Memiliki minat dan kemampuan dalam mempelajari "
            "serta memahami bahasa Arab."
        ),
        (
            "Public Speaking",
            "Mampu menyampaikan gagasan dan informasi "
            "di depan umum dengan percaya diri."
        ),
        (
            "Mengajar",
            "Memiliki pengalaman dalam membantu kegiatan "
            "pembelajaran dan berbagi ilmu."
        ),
    ]

    pengalaman = [
        {
            "judul": "Organisasi Santri (OSPPA)",
            "waktu": "Organisasi Santri Pondok Pesantren Al-Kautsar",
            "isi": (
                "Menjadi bagian dari OSPPA pada bagian pengajaran. "
                "Berpartisipasi dalam kegiatan pendidikan, "
                "membantu proses pembelajaran, serta menjalankan "
                "amanah organisasi dengan tanggung jawab."
            )
        },
        {
            "judul": "Perjalanan Pendidikan",
            "waktu": "PAUD – SD – SMP – SMK",
            "isi": (
                "Menempuh perjalanan pendidikan dari PAUD, "
                "Sekolah Dasar, Sekolah Menengah Pertama, "
                "hingga Sekolah Menengah Kejuruan sebagai "
                "proses membangun ilmu dan mengembangkan diri."
            )
        },
        {
            "judul": "Akzaara Generation",
            "waktu": "Angkatan 10",
            "isi": (
                "Menjadi bagian dari keluarga Akzaara Generation "
                "di Pondok Pesantren An Naba Al Islamiyyah, "
                "dengan semangat kebersamaan, ilmu, dan pengabdian."
            )
        },
    ]

    return render_template(
        "index.html",
        profil=profil,
        keahlian=keahlian,
        pengalaman=pengalaman
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
    
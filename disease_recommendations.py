# disease_recommendations.py - Rekomendasi Penanganan Penyakit Daun Singkong

DISEASE_RECOMMENDATIONS = {
    "bacterial_blight": {
        "nama_penyakit": "🔴 Bacterial Blight",
        "deskripsi": "Penyakit bercak bakteri yang menyebabkan bintik-bintik coklat dengan tepi kuning pada daun",
        "severity": "Tinggi",
        "severity_color": "#c62828",
        "gejala": [
            "Bintik-bintik coklat dengan halo kuning pada daun",
            "Gejala dimulai dari daun bawah dan merambat ke atas",
            "Daun dapat mengering dan gugur",
            "Penyebaran cepat saat cuaca lembab"
        ],
        "penanganan": [
            "1. Isolasi tanaman yang terinfeksi",
            "2. Buang daun yang terserang",
            "3. Kurangi kelembaban dengan irigasi drip",
            "4. Rotasi tanaman minimal 2-3 tahun",
            "5. Sanitasi alat pertanian dengan desinfektan"
        ],
        "obat_rekomendasi": [
            {"nama": "Streptomycin", "dosis": "100-200 ppm", "interval": "7-10 hari"},
            {"nama": "Copper Fungicide", "dosis": "500-1000 ppm", "interval": "7 hari"},
            {"nama": "Mancozeb", "dosis": "800-1000 ppm", "interval": "10 hari"}
        ],
        "pencegahan": [
            "Gunakan benih berkualitas dari sumber terpercaya",
            "Tananam dalam jarak yang cukup untuk sirkulasi udara",
            "Hindari menyiram daun di sore hari",
            "Gunakan mulsa untuk mengurangi percikan air ke daun",
            "Monitor tanaman secara berkala"
        ],
        "tingkat_urgensi": "SEGERA (Tinggi)",
        "waktu_pemulihan": "14-30 hari dengan penanganan tepat"
    },
    
    "brown_spot": {
        "nama_penyakit": "🟤 Brown Spot",
        "deskripsi": "Penyakit bintik coklat yang disebabkan oleh jamur dan menyebabkan bintik-bintik coklat kecil pada daun",
        "severity": "Sedang",
        "severity_color": "#f57c00",
        "gejala": [
            "Bintik-bintik coklat kecil (diameter 2-5 mm) pada daun",
            "Bintik dapat bergabung membentuk area besar",
            "Lingkaran konsentrik pada pusat bintik",
            "Daun dapat menguning dan gugur"
        ],
        "penanganan": [
            "1. Potong dan buang bagian daun yang terinfeksi",
            "2. Tingkatkan ventilasi antar tanaman",
            "3. Hindari penyiraman di malam hari",
            "4. Bersihkan sisa-sisa daun di sekitar tanaman",
            "5. Aplikasi fungisida secara preventif"
        ],
        "obat_rekomendasi": [
            {"nama": "Mancozeb", "dosis": "800-1000 ppm", "interval": "7-10 hari"},
            {"nama": "Propineb", "dosis": "1000-1500 ppm", "interval": "7-10 hari"},
            {"nama": "Chlorothalonil", "dosis": "800-1200 ppm", "interval": "10-14 hari"}
        ],
        "pencegahan": [
            "Tanam di lokasi dengan drainase baik",
            "Jaga kebersihan lahan dari sisa tanaman lama",
            "Gunakan varietas yang tahan penyakit jika tersedia",
            "Hindari kelembaban tinggi dengan ventilasi baik",
            "Aplikasi fungisida preventif saat musim hujan"
        ],
        "tingkat_urgensi": "NORMAL (Sedang)",
        "waktu_pemulihan": "20-40 hari dengan penanganan rutin"
    },
    
    "green_mite": {
        "nama_penyakit": "🐜 Green Mite",
        "deskripsi": "Kerusakan akibat serangan tungau hijau yang mengisap cairan daun dan menyebabkan daun mengering",
        "severity": "Sedang",
        "severity_color": "#f57c00",
        "gejala": [
            "Daun pucat dengan bintik-bintik halus",
            "Permukaan daun berubah menjadi keperakan",
            "Daun menggulung dan mengering",
            "Tungau kecil (sulit dilihat) di bagian bawah daun"
        ],
        "penanganan": [
            "1. Semprotkan air pada daun bagian bawah (fungsi mekanis)",
            "2. Buang daun yang parah terserang",
            "3. Tingkatkan kelembaban dengan penyiraman",
            "4. Aplikasi akarisida jika populasi tinggi",
            "5. Hindari pestisida yang membunuh predator alami"
        ],
        "obat_rekomendasi": [
            {"nama": "Sulfur", "dosis": "1000-2000 ppm", "interval": "7 hari"},
            {"nama": "Dicofol", "dosis": "500-1000 ppm", "interval": "7-10 hari"},
            {"nama": "Neem Oil", "dosis": "2-3% solution", "interval": "7 hari"}
        ],
        "pencegahan": [
            "Jaga kelembaban relatif di atas 60%",
            "Hindari penyiraman berlebihan yang menciptakan stress",
            "Hindari over-fertilisasi terutama nitrogen",
            "Lestarikan musuh alami (predator, parasitoid)",
            "Rotasi tanaman dengan jenis berbeda"
        ],
        "tingkat_urgensi": "NORMAL (Sedang)",
        "waktu_pemulihan": "10-25 hari dengan penanganan akarisida"
    },
    
    "daun_sehat": {
        "nama_penyakit": "🌿 Daun Sehat",
        "deskripsi": "Daun singkong dalam kondisi sehat tanpa penyakit. Lanjutkan perawatan preventif rutin.",
        "severity": "Tidak Ada",
        "severity_color": "#2e7d32",
        "gejala": [
            "✅ Warna daun hijau normal",
            "✅ Tidak ada bintik atau diskolorasi",
            "✅ Tekstur daun normal",
            "✅ Tidak ada tanda serangan hama"
        ],
        "penanganan": [
            "1. Lanjutkan pemantauan daun secara berkala",
            "2. Pertahankan kebersihan lahan",
            "3. Irigasi dan pupuk sesuai jadwal",
            "4. Hindari stress pada tanaman",
            "5. Catat kondisi tanaman untuk referensi"
        ],
        "obat_rekomendasi": [
            {"nama": "Tidak perlu pengobatan", "dosis": "N/A", "interval": "N/A"}
        ],
        "pencegahan": [
            "Lakukan monitoring rutin setiap 2-3 hari",
            "Pertahankan nutrisi tanaman dengan pupuk seimbang",
            "Berikan irigasi teratur sesuai kebutuhan",
            "Bersihkan gulma di sekitar tanaman",
            "Aplikasi fungisida preventif saat memasuki musim hujan"
        ],
        "tingkat_urgensi": "BAIK (Tidak Ada)",
        "waktu_pemulihan": "N/A - Terus Monitor"
    },
    
    "mosaic": {
        "nama_penyakit": "🟢 Mosaic",
        "deskripsi": "Penyakit mosaik yang disebabkan virus dan menyebabkan pola tidak teratur dengan warna kuning dan hijau pada daun",
        "severity": "Tinggi",
        "severity_color": "#c62828",
        "gejala": [
            "Pola mosaik kuning dan hijau pada daun",
            "Daun mengalami distorsi bentuk",
            "Pertumbuhan tanaman terhambat",
            "Produksi umbi berkurang signifikan"
        ],
        "penanganan": [
            "1. Isolasi tanaman yang terinfeksi SEGERA",
            "2. Cabut dan bakar tanaman terinfeksi",
            "3. Kontrol serangga vektor (kutu, thrip)",
            "4. Desinfeksi alat dan tangan saat bekerja",
            "5. Jangan gunakan tanaman terinfeksi sebagai benih"
        ],
        "obat_rekomendasi": [
            {"nama": "Tidak ada obat antivirus", "dosis": "Removal saja", "interval": "N/A"},
            {"nama": "Kontrol Vektor - Insektisida", "dosis": "Sesuai label", "interval": "7 hari"},
            {"nama": "Neem Oil untuk vektor", "dosis": "2-3% solution", "interval": "5-7 hari"}
        ],
        "pencegahan": [
            "Gunakan benih yang bebas virus dari sumber terpercaya",
            "Kontrol gulma yang dapat menjadi inang virus",
            "Hindari area tanaman dengan isolasi fisik",
            "Gunakan sarung tangan dan cuci tangan saat menangani tanaman",
            "Kontrol populasi serangga vektor dengan insektisida"
        ],
        "tingkat_urgensi": "DARURAT (Sangat Tinggi)",
        "waktu_pemulihan": "Tidak dapat diobati - Removal adalah solusi"
    }
}

def get_disease_info(category):
    """Dapatkan informasi penyakit berdasarkan kategori"""
    return DISEASE_RECOMMENDATIONS.get(category, None)

def get_all_diseases():
    """Dapatkan semua informasi penyakit"""
    return DISEASE_RECOMMENDATIONS

def format_recommendation_html(disease_info, confidence):
    """Format rekomendasi menjadi HTML yang menarik"""
    if not disease_info:
        return None
    
    html = f"""
    <div style="background: linear-gradient(135deg, #ffffff 0%, #f1f8f4 100%); 
                border: 3px solid {disease_info['severity_color']}; 
                border-radius: 15px; 
                padding: 20px; 
                margin: 20px 0;">
        
        <h2 style="color: {disease_info['severity_color']}; margin-top: 0;">
            {disease_info['nama_penyakit']}
        </h2>
        
        <p style="font-size: 1.1em; color: #1B5E20; margin: 10px 0;">
            <strong>Tingkat Keparahan:</strong> 
            <span style="color: {disease_info['severity_color']}; font-weight: 800;">
                {disease_info['severity']}
            </span>
        </p>
        
        <p style="color: #2E7D32; font-size: 0.95em; line-height: 1.6;">
            {disease_info['deskripsi']}
        </p>
        
        <p style="color: #666; font-size: 0.9em;">
            <strong>Estimasi Waktu Pemulihan:</strong> {disease_info['waktu_pemulihan']}
        </p>
    </div>
    """
    
    return html
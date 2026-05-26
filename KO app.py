import streamlit as st
import time

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(page_title="Virtual Lab Kimia Organik", page_icon="🧪", layout="wide")

# ================= MANAJEMEN STATE (Logika Simulator) =================
# Ini agar web ingat langkah praktikum mana yang sedang dilakukan pengguna
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'current_exp' not in st.session_state:
    st.session_state.current_exp = "Uji Ketidakjenuhan (Iodium)"
if 'current_sample' not in st.session_state:
    st.session_state.current_sample = ""

# ================= DATABASE PERCOBAAN =================
# Semua data praktikum disimpan dalam satu wadah agar layout selalu konsisten
percobaan_db = {
    "Uji Ketidakjenuhan (Iodium)": {
        "modul": "Modul 1: Hidrokarbon",
        "sampel_opsi": ["Heksana (Alkana/Jenuh)", "Minyak Tanah (Mengandung Alkena)"],
        "reagen": "Larutan I₂ (Iodium)",
        "warna_reagen": "#8b4513", # Coklat Iodium
        "aksi_teks": "Kocok Tabung",
        "hasil": {
            "Heksana (Alkana/Jenuh)": {
                "warna_akhir": "#8b4513", # Tetap coklat
                "efek": "none",
                "pengamatan": "Warna coklat I₂ TETAP (tidak pudar).",
                "reaksi": "Heksana + I₂ \\rightarrow \\text{Tidak ada reaksi}",
                "alasan": "Heksana adalah senyawa hidrokarbon jenuh (ikatan tunggal). Ikatan C-C dan C-H sangat stabil sehingga tidak dapat mengalami reaksi adisi untuk memutus ikatan I₂."
            },
            "Minyak Tanah (Mengandung Alkena)": {
                "warna_akhir": "rgba(255,255,255,0.2)", # Bening
                "efek": "none",
                "pengamatan": "Warna coklat I₂ PUDAR/HILANG menjadi bening.",
                "reaksi": "R-CH=CH-R' + I_2 \\rightarrow R-CHI-CHI-R'",
                "alasan": "Minyak tanah mengandung senyawa hidrokarbon tak jenuh (alkena). Terjadi reaksi adisi elektrofilik di mana ikatan rangkap dua terputus untuk mengikat atom Iodium, sehingga warna asli Iodium menghilang."
            }
        }
    },
    "Uji Lucas": {
        "modul": "Modul 2: Alkohol & Fenol",
        "sampel_opsi": ["1-Butanol (Primer)", "2-Butanol (Sekunder)", "t-Butil Alkohol (Tersier)"],
        "reagen": "Pereaksi Lucas (ZnCl₂ dalam HCl pekat)",
        "warna_reagen": "rgba(255,255,255,0.2)", # Bening
        "aksi_teks": "Diamkan & Amati",
        "hasil": {
            "1-Butanol (Primer)": {
                "warna_akhir": "rgba(255,255,255,0.2)",
                "efek": "none",
                "pengamatan": "Larutan tetap bening/jernih.",
                "reaksi": "R-CH_2OH + HCl \\xrightarrow{ZnCl_2} \\text{Tidak bereaksi pada suhu ruang}",
                "alasan": "Karbokation primer yang dihasilkan sangat tidak stabil, sehingga reaksi substitusi nukleofilik (SN1) tidak dapat berjalan tanpa pemanasan ekstrem."
            },
            "2-Butanol (Sekunder)": {
                "warna_akhir": "#e2e8f0", # Agak keruh
                "efek": "cloudy",
                "pengamatan": "Larutan menjadi keruh setelah 5 - 10 menit.",
                "reaksi": "R_2CH-OH + HCl \\xrightarrow{ZnCl_2} R_2CH-Cl \\downarrow + H_2O",
                "alasan": "Bereaksi secara moderat. Karbokation sekunder lebih stabil dari primer, sehingga alkil klorida (yang tidak larut air dan menyebabkan kekeruhan) terbentuk secara perlahan."
            },
            "t-Butil Alkohol (Tersier)": {
                "warna_akhir": "#cbd5e1", # Sangat keruh
                "efek": "cloudy",
                "pengamatan": "Larutan seketika menjadi KERUH dan membentuk dua fasa.",
                "reaksi": "R_3C-OH + HCl \\xrightarrow{ZnCl_2} R_3C-Cl \\downarrow + H_2O",
                "alasan": "Sangat reaktif! Alkohol tersier membentuk karbokation tersier yang sangat stabil. Reaksi substitusi berjalan sangat cepat menghasilkan alkil klorida yang mengendap/keruh."
            }
        }
    },
    "Uji Tollens (Cermin Perak)": {
        "modul": "Modul 3: Aldehid & Keton",
        "sampel_opsi": ["Formaldehida (Aldehid)", "Aseton (Keton)"],
        "reagen": "Pereaksi Tollens (AgNO₃ amoniakal)",
        "warna_reagen": "rgba(255,255,255,0.2)", # Bening
        "aksi_teks": "Panaskan di Penangas Air",
        "hasil": {
            "Formaldehida (Aldehid)": {
                "warna_akhir": "linear-gradient(to right, #94a3b8, #e2e8f0, #94a3b8)", # Efek silver
                "efek": "mirror",
                "pengamatan": "Terbentuk lapisan CERMIN PERAK pada dinding tabung.",
                "reaksi": "R-CHO + 2[Ag(NH_3)_2]^+ + 3OH^- \\rightarrow R-COO^- + 2Ag \\downarrow + 4NH_3 + 2H_2O",
                "alasan": "Aldehid memiliki sifat reduktor yang kuat. Gugus karbonil aldehid dioksidasi menjadi asam karboksilat, sementara ion Perak (Ag⁺) tereduksi menjadi logam perak murni (Ag) yang menempel pada kaca."
            },
            "Aseton (Keton)": {
                "warna_akhir": "rgba(255,255,255,0.2)",
                "efek": "none",
                "pengamatan": "Larutan tetap bening, tidak ada perubahan.",
                "reaksi": "R-CO-R' + \\text{Tollens} \\rightarrow \\text{Tidak ada reaksi}",
                "alasan": "Keton tidak memiliki atom hidrogen alfa yang terikat langsung pada atom karbon karbonil, sehingga tidak dapat dioksidasi oleh oksidator lemah seperti Tollens."
            }
        }
    },
    "Uji Fehling": {
        "modul": "Modul 3: Aldehid & Keton",
        "sampel_opsi": ["Formaldehida (Aldehid)", "Aseton (Keton)"],
        "reagen": "Pereaksi Fehling (Campuran Cu²⁺ basa)",
        "warna_reagen": "#3b82f6", # Biru Fehling
        "aksi_teks": "Panaskan di Penangas Air",
        "hasil": {
            "Formaldehida (Aldehid)": {
                "warna_akhir": "#b91c1c", # Merah bata
                "efek": "precipitate",
                "pengamatan": "Terbentuk ENDAPAN MERAH BATA.",
                "reaksi": "R-CHO + 2Cu^{2+} + 5OH^- \\rightarrow R-COO^- + Cu_2O \\downarrow + 3H_2O",
                "alasan": "Aldehid mereduksi ion Tembaga(II) kompleks yang berwarna biru menjadi endapan Tembaga(I) Oksida (Cu₂O) yang berwarna merah bata."
            },
            "Aseton (Keton)": {
                "warna_akhir": "#3b82f6", # Tetap biru
                "efek": "none",
                "pengamatan": "Larutan tetap berwarna biru jernih.",
                "reaksi": "R-CO-R' + \\text{Fehling} \\rightarrow \\text{Tidak ada reaksi}",
                "alasan": "Sama seperti Tollens, ketiadaan ikatan C-H reaktif pada gugus karbonil membuat keton kebal terhadap oksidator lemah Fehling."
            }
        }
    },
    "Uji Penggaraman (Keasaman)": {
        "modul": "Modul 4: Asam Karboksilat",
        "sampel_opsi": ["Asam Asetat", "Etanol"],
        "reagen": "Larutan NaHCO₃ 5%",
        "warna_reagen": "rgba(255,255,255,0.2)", # Bening
        "aksi_teks": "Hubungkan dengan Air Barit",
        "hasil": {
            "Asam Asetat": {
                "warna_akhir": "rgba(255,255,255,0.2)",
                "efek": "bubbles",
                "pengamatan": "Timbul GELEMBUNG GAS (CO₂) dan Air Barit menjadi KERUH.",
                "reaksi": "CH_3COOH + NaHCO_3 \\rightarrow CH_3COONa + H_2O + CO_2 \\uparrow",
                "alasan": "Asam asetat adalah asam yang cukup kuat untuk mendonasikan protonnya ke ion bikarbonat, menghasilkan asam karbonat yang terurai menjadi gas CO₂. Gas ini bereaksi dengan air barit membentuk endapan BaCO₃ yang keruh."
            },
            "Etanol": {
                "warna_akhir": "rgba(255,255,255,0.2)",
                "efek": "none",
                "pengamatan": "Tidak ada perubahan, tidak ada gelembung.",
                "reaksi": "CH_3CH_2OH + NaHCO_3 \\rightarrow \\text{Tidak ada reaksi}",
                "alasan": "Etanol bersifat netral (sangat lemah asamnya), sehingga tidak memiliki kemampuan untuk membebaskan gas CO₂ dari garam bikarbonat."
            }
        }
    }
}

# ================= CSS UNTUK VISUALISASI 2D TABUNG REAKSI =================
st.markdown("""
<style>
    /* Desain Layout Konsisten */
    .lab-panel { background-color: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; height: 100%;}
    .panel-title { font-size: 1.2em; color: #0f766e; font-weight: bold; border-bottom: 2px solid #0f766e; padding-bottom: 5px; margin-bottom: 15px;}
    
    /* Visualisasi Tabung Reaksi 2D */
    .tube-container { display: flex; justify-content: center; align-items: flex-end; height: 250px; padding: 20px;}
    .test-tube { width: 70px; height: 220px; border: 4px solid #94a3b8; border-top: none; border-radius: 0 0 35px 35px; position: relative; overflow: hidden; background-color: rgba(255,255,255,0.8); box-shadow: inset -5px -5px 10px rgba(0,0,0,0.1);}
    
    /* Cairan di dalam tabung */
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1s ease-in-out; border-radius: 0 0 30px 30px;}
    
    /* Efek Khusus */
    .bubble { position: absolute; background: white; border-radius: 50%; width: 8px; height: 8px; bottom: 10px; animation: rise 2s infinite ease-in;}
    @keyframes rise { 0% { bottom: 0px; opacity: 1; transform: translateX(0); } 100% { bottom: 200px; opacity: 0; transform: translateX(-10px); } }
    
    .precipitate { position: absolute; bottom: 0; width: 100%; height: 20px; background-color: rgba(0,0,0,0.3); border-radius: 0 0 30px 30px;}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039938.png", width=80)
    st.title("Virtual Lab KO")
    st.write("Pilih simulasi praktikum:")
    
    selected_exp = st.selectbox("Daftar Percobaan:", list(percobaan_db.keys()))
    
    # Reset state jika pengguna ganti percobaan
    if selected_exp != st.session_state.current_exp:
        st.session_state.current_exp = selected_exp
        st.session_state.step = 0
        st.session_state.current_sample = ""
        st.rerun()

    st.divider()
    st.caption(f"📚 {percobaan_db[selected_exp]['modul']}")

# Ambil data percobaan yang sedang aktif
data_exp = percobaan_db[st.session_state.current_exp]

st.title(f"🧪 {st.session_state.current_exp}")
st.write("Ikuti urutan **Cara Kerja** di meja praktikum sebelah kiri, dan amati perubahan pada tabung reaksi di sebelah kanan.")

# ================= LAYOUT UTAMA (2 KOLOM KONSISTEN) =================
col_kiri, col_kanan = st.columns([1.2, 1])

# --- KOLOM KIRI: MEJA KERJA (INTERAKTIF) ---
with col_kiri:
    st.markdown('<div class="lab-panel"><div class="panel-title">🛠️ Meja Praktikum (Cara Kerja)</div>', unsafe_allow_html=True)
    
    # Langkah 1: Pilih Sampel
    st.write("**Langkah 1:** Masukkan sampel ke dalam tabung reaksi.")
    sampel_input = st.selectbox("Pilih Sampel:", ["-- Pilih Sampel --"] + data_exp["sampel_opsi"], disabled=(st.session_state.step > 0))
    if st.button("Tambahkan Sampel 💧", disabled=(st.session_state.step > 0 or sampel_input == "-- Pilih Sampel --")):
        st.session_state.current_sample = sampel_input
        st.session_state.step = 1
        st.rerun()

    st.divider()

    # Langkah 2: Tambah Reagen
    st.write(f"**Langkah 2:** Tambahkan {data_exp['reagen']}.")
    if st.button("Teteskan Pereaksi 🧪", disabled=(st.session_state.step != 1)):
        st.session_state.step = 2
        st.rerun()

    st.divider()

    # Langkah 3: Aksi (Kocok/Panaskan)
    st.write(f"**Langkah 3:** {data_exp['aksi_teks']}.")
    if st.button(f"{data_exp['aksi_teks']} 🔥", disabled=(st.session_state.step != 2)):
        with st.spinner("Reaksi sedang berlangsung..."):
            time.sleep(1.5) # Memberi efek delay animasi natural
        st.session_state.step = 3
        st.rerun()

    # Tombol Reset
    st.divider()
    if st.button("🔄 Cuci Tabung (Ulangi)"):
        st.session_state.step = 0
        st.session_state.current_sample = ""
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- KOLOM KANAN: VISUALISASI 2D TABUNG REAKSI ---
with col_kanan:
    st.markdown('<div class="lab-panel"><div class="panel-title">🔬 Visualisasi Tabung Reaksi</div>', unsafe_allow_html=True)
    
    # Logika Warna CSS berdasarkan State
    tinggi_cairan = "0%"
    warna_cairan = "transparent"
    efek_html = ""
    status_teks = "Tabung masih kosong."

    if st.session_state.step == 1:
        tinggi_cairan = "30%"
        warna_cairan = "rgba(255,255,255,0.2)" # Bening (Sampel)
        status_teks = f"Sampel {st.session_state.current_sample} ditambahkan."
        
    elif st.session_state.step == 2:
        tinggi_cairan = "60%"
        warna_cairan = data_exp["warna_reagen"] # Warna gabungan reagen
        status_teks = f"{data_exp['reagen']} ditambahkan. Menunggu perlakuan selanjutnya..."
        
    elif st.session_state.step == 3:
        tinggi_cairan = "60%"
        hasil_data = data_exp["hasil"][st.session_state.current_sample]
        warna_cairan = hasil_data["warna_akhir"]
        
        # Eksekusi Efek Visual
        if hasil_data["efek"] == "bubbles":
            efek_html = '<div class="bubble" style="left:20px;"></div><div class="bubble" style="left:40px; animation-delay: 0.5s;"></div>'
        elif hasil_data["efek"] == "precipitate":
            efek_html = '<div class="precipitate"></div>'
            
        status_teks = f"**Pengamatan:** {hasil_data['pengamatan']}"

    # Render HTML Tabung Reaksi
    html_tube = f"""
    <div class="tube-container">
        <div class="test-tube">
            <div class="liquid" style="height: {tinggi_cairan}; background: {warna_cairan};">
                {efek_html}
            </div>
        </div>
    </div>
    <div style="text-align: center; margin-top: 10px; color: #475569;">
        {status_teks}
    </div>
    """
    st.markdown(html_tube, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ================= JURNAL ANALITIK (MUNCUL SETELAH REAKSI SELESAI) =================
if st.session_state.step == 3:
    st.write("---")
    st.markdown('<div class="panel-title" style="font-size: 1.5em;">📑 Jurnal Hasil Pengamatan & Analisis</div>', unsafe_allow_html=True)
    
    hasil_data = data_exp["hasil"][st.session_state.current_sample]
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("**Persamaan Reaksi Kimia:**")
        st.latex(hasil_data["reaksi"])
        
    with col_b:
        st.success("**Pembahasan Teoritis:**")
        st.write(hasil_data["alasan"])

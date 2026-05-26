import streamlit as st
import time

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(page_title="Virtual Lab Kimia Organik", page_icon="🧪", layout="wide")

# ================= MANAJEMEN STATE =================
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'current_exp' not in st.session_state:
    st.session_state.current_exp = "Uji Ketidakjenuhan (Iodium)"
if 'current_sample' not in st.session_state:
    st.session_state.current_sample = ""

# ================= DATABASE PERCOBAAN =================
percobaan_db = {
    "Uji Ketidakjenuhan (Iodium)": {
        "modul": "Modul 1: Hidrokarbon",
        "sampel_opsi": ["Heksana (Alkana/Jenuh)", "Minyak Tanah (Mengandung Alkena)"],
        "reagen": "Larutan I₂ (Iodium)",
        "warna_reagen": "#8b4513", # Coklat Iodium
        "aksi_teks": "Kocok Tabung",
        "hasil": {
            "Heksana (Alkana/Jenuh)": {
                "warna_akhir": "#8b4513",
                "efek": "none",
                "pengamatan": "Warna coklat I₂ TETAP (tidak pudar).",
                "reaksi": "Heksana + I_2 \\rightarrow \\text{Tidak ada reaksi}",
                "alasan": "Heksana adalah hidrokarbon jenuh yang stabil, tidak dapat memutus ikatan I₂."
            },
            "Minyak Tanah (Mengandung Alkena)": {
                "warna_akhir": "#f8fafc", # Bening
                "efek": "none",
                "pengamatan": "Warna coklat I₂ PUDAR/HILANG menjadi bening.",
                "reaksi": "R-CH=CH-R' + I_2 \\rightarrow R-CHI-CHI-R'",
                "alasan": "Ikatan rangkap pada minyak tanah mengalami reaksi adisi, sehingga warna asli I₂ hilang."
            }
        }
    },
    "Uji Lucas": {
        "modul": "Modul 2: Alkohol & Fenol",
        "sampel_opsi": ["1-Butanol (Primer)", "2-Butanol (Sekunder)", "t-Butil Alkohol (Tersier)"],
        "reagen": "Pereaksi Lucas (ZnCl₂ dalam HCl pekat)",
        "warna_reagen": "#f8fafc", 
        "aksi_teks": "Diamkan & Amati",
        "hasil": {
            "1-Butanol (Primer)": {
                "warna_akhir": "#f8fafc",
                "efek": "none",
                "pengamatan": "Larutan tetap bening/jernih.",
                "reaksi": "R-CH_2OH + HCl \\xrightarrow{ZnCl_2} \\text{Tidak bereaksi pada suhu ruang}",
                "alasan": "Karbokation primer sangat tidak stabil untuk bereaksi secara SN1 pada suhu ruang."
            },
            "2-Butanol (Sekunder)": {
                "warna_akhir": "#e2e8f0",
                "efek": "cloudy",
                "pengamatan": "Larutan menjadi keruh setelah 5 - 10 menit.",
                "reaksi": "R_2CH-OH + HCl \\xrightarrow{ZnCl_2} R_2CH-Cl \\downarrow + H_2O",
                "alasan": "Bereaksi moderat membentuk alkil klorida yang tidak larut."
            },
            "t-Butil Alkohol (Tersier)": {
                "warna_akhir": "#94a3b8",
                "efek": "cloudy",
                "pengamatan": "Larutan seketika menjadi KERUH tebal.",
                "reaksi": "R_3C-OH + HCl \\xrightarrow{ZnCl_2} R_3C-Cl \\downarrow + H_2O",
                "alasan": "Karbokation tersier sangat stabil, substitusi terjadi seketika menghasilkan endapan."
            }
        }
    },
    "Uji Ceric Nitrat": {
        "modul": "Modul 2: Alkohol & Fenol",
        "sampel_opsi": ["1-Butanol", "Fenol"],
        "reagen": "Pereaksi Ceric Nitrat (Kuning)",
        "warna_reagen": "#facc15", 
        "aksi_teks": "Kocok Tabung",
        "hasil": {
            "1-Butanol": {
                "warna_akhir": "#ef4444", # Merah
                "efek": "none",
                "pengamatan": "Warna berubah menjadi MERAH.",
                "reaksi": "R-OH + [Ce(NO_3)_6]^{2-} \\rightarrow [Ce(OR)(NO_3)_5]^{2-} + HNO_3",
                "alasan": "Gugus -OH alifatik berkoordinasi dengan ion Cerium membentuk kompleks berwarna merah."
            },
            "Fenol": {
                "warna_akhir": "#451a03", # Coklat pekat/Hitam
                "efek": "none",
                "pengamatan": "Warna berubah menjadi COKLAT TUA/GELAP.",
                "reaksi": "Ar-OH + Ce^{4+} \\rightarrow \\text{Kompleks Fenol-Cerium (Gelap)}",
                "alasan": "Gugus -OH aromatik (fenol) bereaksi menghasilkan senyawa kompleks berwarna gelap/pekat."
            }
        }
    },
    "Uji Jones": {
        "modul": "Modul 2: Alkohol & Fenol",
        "sampel_opsi": ["1-Butanol", "t-Butil Alkohol"],
        "reagen": "Pereaksi Jones (Jingga/Oranye)",
        "warna_reagen": "#f97316", 
        "aksi_teks": "Tunggu 15 Detik",
        "hasil": {
            "1-Butanol": {
                "warna_akhir": "#10b981", # Hijau
                "efek": "none",
                "pengamatan": "Warna jingga berubah menjadi HIJAU.",
                "reaksi": "CrO_3 + H_2SO_4 + R-OH \\rightarrow Cr^{3+} \\text{(hijau)} + \\text{Asam Karboksilat}",
                "alasan": "Alkohol primer dioksidasi oleh Kromium(VI) jingga yang tereduksi menjadi Kromium(III) hijau."
            },
            "t-Butil Alkohol": {
                "warna_akhir": "#f97316", 
                "efek": "none",
                "pengamatan": "Warna TETAP jingga.",
                "reaksi": "R_3C-OH + \\text{Jones} \\rightarrow \\text{Tidak bereaksi}",
                "alasan": "Alkohol tersier tidak memiliki hidrogen alfa sehingga tidak bisa dioksidasi."
            }
        }
    },
    "Uji Iodoform": {
        "modul": "Modul 2 & 3",
        "sampel_opsi": ["Etanol", "Amil Alkohol"],
        "reagen": "I₂ + NaOH 10%",
        "warna_reagen": "#f8fafc", 
        "aksi_teks": "Panaskan di Penangas",
        "hasil": {
            "Etanol": {
                "warna_akhir": "#fef08a", # Kuning
                "efek": "precipitate",
                "pengamatan": "Terbentuk ENDAPAN KUNING Iodoform.",
                "reaksi": "CH_3CH_2OH + I_2 + NaOH \\rightarrow CHI_3 \\downarrow \\text{(kuning)} + HCOONa",
                "alasan": "Etanol dapat dioksidasi menjadi asetaldehida yang memiliki gugus metil keton, sehingga bereaksi membentuk kristal Iodoform."
            },
            "Amil Alkohol": {
                "warna_akhir": "#f8fafc", 
                "efek": "none",
                "pengamatan": "Tetap bening, tidak ada endapan.",
                "reaksi": "\\text{Amil Alkohol} + I_2/NaOH \\rightarrow \\text{Tidak bereaksi}",
                "alasan": "Strukturnya tidak memiliki / tidak bisa membentuk gugus metil keton yang disyaratkan untuk uji Iodoform."
            }
        }
    },
    "Uji Tollens (Cermin Perak)": {
        "modul": "Modul 3: Aldehid & Keton",
        "sampel_opsi": ["Asetaldehida (Aldehid)", "Aseton (Keton)"],
        "reagen": "Pereaksi Tollens (Ag⁺)",
        "warna_reagen": "#f8fafc", 
        "aksi_teks": "Panaskan di Penangas Air",
        "hasil": {
            "Asetaldehida (Aldehid)": {
                "warna_akhir": "#94a3b8", # Abu-abu perak
                "efek": "mirror",
                "pengamatan": "Terbentuk CERMIN PERAK pada tabung.",
                "reaksi": "R-CHO + 2Ag^+ + 3OH^- \\rightarrow R-COO^- + 2Ag \\downarrow + 2H_2O",
                "alasan": "Aldehid mereduksi ion perak menjadi logam perak."
            },
            "Aseton (Keton)": {
                "warna_akhir": "#f8fafc",
                "efek": "none",
                "pengamatan": "Tetap bening.",
                "reaksi": "R-CO-R' + \\text{Tollens} \\rightarrow \\text{Tidak ada reaksi}",
                "alasan": "Keton tidak memiliki atom H pada karbonil untuk dioksidasi."
            }
        }
    },
    "Uji Fehling": {
        "modul": "Modul 3: Aldehid & Keton",
        "sampel_opsi": ["Asetaldehida (Aldehid)", "Aseton (Keton)"],
        "reagen": "Pereaksi Fehling (Cu²⁺ biru)",
        "warna_reagen": "#3b82f6", 
        "aksi_teks": "Panaskan di Penangas Air",
        "hasil": {
            "Asetaldehida (Aldehid)": {
                "warna_akhir": "#b91c1c", # Merah bata
                "efek": "precipitate",
                "pengamatan": "Terbentuk ENDAPAN MERAH BATA.",
                "reaksi": "R-CHO + 2Cu^{2+} + 5OH^- \\rightarrow R-COO^- + Cu_2O \\downarrow + 3H_2O",
                "alasan": "Aldehid mereduksi ion Tembaga(II) biru menjadi endapan Tembaga(I) Oksida."
            },
            "Aseton (Keton)": {
                "warna_akhir": "#3b82f6",
                "efek": "none",
                "pengamatan": "Larutan tetap berwarna biru jernih.",
                "reaksi": "R-CO-R' + \\text{Fehling} \\rightarrow \\text{Tidak ada reaksi}",
                "alasan": "Keton tidak dapat direduksi oleh Fehling."
            }
        }
    },
    "Uji Penggaraman (Keasaman)": {
        "modul": "Modul 4: Asam Karboksilat",
        "sampel_opsi": ["Asam Asetat", "Etanol"],
        "reagen": "Larutan NaHCO₃ 5%",
        "warna_reagen": "#f8fafc", 
        "aksi_teks": "Hubungkan ke Air Barit",
        "hasil": {
            "Asam Asetat": {
                "warna_akhir": "#f8fafc",
                "efek": "bubbles",
                "pengamatan": "Timbul GELEMBUNG GAS (CO₂)!",
                "reaksi": "CH_3COOH + NaHCO_3 \\rightarrow CH_3COONa + H_2O + CO_2 \\uparrow",
                "alasan": "Asam asetat mendonasikan proton ke bikarbonat, menghasilkan gas CO₂."
            },
            "Etanol": {
                "warna_akhir": "#f8fafc",
                "efek": "none",
                "pengamatan": "Tidak ada perubahan.",
                "reaksi": "CH_3CH_2OH + NaHCO_3 \\rightarrow \\text{Tidak bereaksi}",
                "alasan": "Etanol bersifat netral sehingga tidak bereaksi dengan bikarbonat."
            }
        }
    }
}

# ================= CSS BERSIH & RAPI =================
st.markdown("""
<style>
    /* CSS Tabung Reaksi Murni (Tanpa efek yang menghalangi) */
    .tube-container { display: flex; justify-content: center; align-items: flex-end; height: 300px; padding: 20px;}
    .test-tube { 
        width: 60px; 
        height: 250px; 
        border: 4px solid #cbd5e1; 
        border-top: none; 
        border-radius: 0 0 30px 30px; 
        position: relative; 
        background-color: transparent; /* Transparan murni */
        overflow: hidden; 
    }
    
    .liquid { 
        position: absolute; 
        bottom: 0; left: 0; right: 0; 
        transition: height 0.6s ease, background-color 0.6s ease; 
    }
    
    .precipitate { position: absolute; bottom: 0; width: 100%; height: 25px; background-color: rgba(0,0,0,0.4); }
    
    .bubble { position: absolute; background: rgba(0,0,0,0.2); border-radius: 50%; width: 6px; height: 6px; animation: rise 1.5s infinite ease-in;}
    @keyframes rise { 0% { bottom: 0px; opacity: 1; } 100% { bottom: 200px; opacity: 0; } }
    
    /* Layout Kartu Panel Kanan */
    .control-panel { background: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039938.png", width=80)
    st.title("Virtual Lab KO")
    
    selected_exp = st.selectbox("Pilih Bab Praktikum:", list(percobaan_db.keys()))
    
    if selected_exp != st.session_state.current_exp:
        st.session_state.current_exp = selected_exp
        st.session_state.step = 0
        st.session_state.current_sample = ""
        st.rerun()

    st.caption(f"📚 {percobaan_db[selected_exp]['modul']}")

data_exp = percobaan_db[st.session_state.current_exp]

st.markdown(f"### 🧪 Percobaan: {st.session_state.current_exp}")

# ================= LAYOUT UTAMA (KIRI TABUNG, KANAN KONTROL) =================
# Kolom dibuat proporsional agar sejajar dan tidak perlu scroll
col_visual, col_kontrol = st.columns([1, 1.5])

# --- KOLOM KIRI (VISUALISASI TABUNG) ---
with col_visual:
    tinggi_cairan = "0%"
    warna_cairan = "transparent"
    efek_html = ""

    if st.session_state.step == 1:
        tinggi_cairan = "30%"
        warna_cairan = "#f1f5f9" # Bening sedikit abu
    elif st.session_state.step == 2:
        tinggi_cairan = "60%"
        warna_cairan = data_exp["warna_reagen"]
    elif st.session_state.step == 3:
        tinggi_cairan = "60%"
        hasil_data = data_exp["hasil"][st.session_state.current_sample]
        warna_cairan = hasil_data["warna_akhir"]
        
        if hasil_data["efek"] == "bubbles":
            efek_html = '<div class="bubble" style="left:15px;"></div><div class="bubble" style="left:35px; animation-delay: 0.3s;"></div>'
        elif hasil_data["efek"] == "precipitate":
            efek_html = '<div class="precipitate"></div>'

    html_tube = f"""
    <div class="tube-container">
        <div class="test-tube">
            <div class="liquid" style="height: {tinggi_cairan}; background-color: {warna_cairan};">
                {efek_html}
            </div>
        </div>
    </div>
    """
    st.markdown(html_tube, unsafe_allow_html=True)

# --- KOLOM KANAN (PANEL KONTROL BERTUMPUK RAPAT) ---
with col_kontrol:
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.markdown("#### 🛠️ Meja Praktikum")
    
    # 1. Pilih Sampel
    sampel_input = st.selectbox("1. Pilih Sampel", ["-- Pilih --"] + data_exp["sampel_opsi"], disabled=(st.session_state.step > 0))
    if st.button("💧 Masukkan Sampel", disabled=(st.session_state.step > 0 or sampel_input == "-- Pilih --")):
        st.session_state.current_sample = sampel_input
        st.session_state.step = 1
        st.rerun()

    # 2. Teteskan Reagen
    if st.button(f"🧪 Tambahkan {data_exp['reagen']}", disabled=(st.session_state.step != 1)):
        st.session_state.step = 2
        st.rerun()

    # 3. Lakukan Aksi
    if st.button(f"🔥 {data_exp['aksi_teks']}", disabled=(st.session_state.step != 2)):
        with st.spinner("Reaksi sedang berlangsung..."):
            time.sleep(1)
        st.session_state.step = 3
        st.rerun()

    # 4. Reset
    st.write("---")
    if st.button("🔄 Cuci Tabung (Ulangi)"):
        st.session_state.step = 0
        st.session_state.current_sample = ""
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# ================= KOTAK HASIL (MUNCUL DI BAWAH KETIKA SELESAI) =================
if st.session_state.step == 3:
    hasil_data = data_exp["hasil"][st.session_state.current_sample]
    st.success(f"**Pengamatan:** {hasil_data['pengamatan']}")
    st.info(f"**Reaksi:** $\quad {hasil_data['reaksi']}$")
    st.warning(f"**Pembahasan:** {hasil_data['alasan']}")

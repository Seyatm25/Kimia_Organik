import streamlit as st

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(page_title="Panduan Praktikum & Post-Test KO", page_icon="🔬", layout="wide")

# Custom CSS biar tampilannya clean dan nggak kaku
st.markdown("""
    <style>
    .main-title { font-size: 2.5em; color: #0f766e; font-weight: bold; }
    .sub-title { font-size: 1.2em; color: #475569; margin-bottom: 20px;}
    .card { background-color: #f8fafc; padding: 20px; border-radius: 10px; border-left: 5px solid #0f766e; margin-bottom: 15px;}
    .hasil-positif { background-color: #ecfdf5; padding: 15px; border-radius: 8px; border: 1px solid #10b981;}
    .hasil-negatif { background-color: #fef2f2; padding: 15px; border-radius: 8px; border: 1px solid #ef4444;}
    </style>
""", unsafe_allow_html=True)

# ================= SIDEBAR MENU =================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039938.png", width=100)
    st.markdown("### 🧪 Asisten Virtual KO")
    st.write("Halo, Maba! Pilih menu di bawah untuk mulai belajar:")
    
    menu = st.radio("Navigasi Modul:", [
        "🏠 Beranda",
        "🔥 Modul 1: Hidrokarbon",
        "🍷 Modul 2: Alkohol & Fenol",
        "💊 Modul 3: Aldehid & Keton",
        "🍋 Modul 4: Asam Karboksilat",
        "🎯 Prediktor Post-Test (Pro)"
    ])
    
    st.divider()
    st.caption("Dibuat khusus untuk mempermudah Praktikum Kimia Organik.")

# ================= KONTEN BERANDA =================
if menu == "🏠 Beranda":
    st.markdown('<div class="main-title">Selamat Datang di Web Praktikum KO! 🎉</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Web ini dibikin khusus buat bantu kamu (iya, kamu yang lagi pusing bikin laprak) biar lebih paham sama reaksi-reaksi kimia organik tanpa harus ngafal buta.</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📖 **Pahami Teori**\n\nBaca alat, bahan, dan cara kerja dari tiap modul praktikum yang ada di buku panduanmu.")
    with col2:
        st.success("🔬 **Analisis Hasil**\n\nLihat bocoran hasil reaksi (positif/negatif) beserta alasan logis kenapa hal itu bisa terjadi.")
    with col3:
        st.warning("🎯 **Latihan Post-Test**\n\nGunakan fitur Prediktor Reaksi untuk ngecek jawaban post-test atau jurnalmu.")

# ================= MODUL 1: HIDROKARBON =================
elif menu == "🔥 Modul 1: Hidrokarbon":
    st.title("🔥 Modul 1: Senyawa Hidrokarbon")
    st.write("Di modul ini kita belajar bedanya Alkana (ikatan tunggal), Alkuna (ikatan rangkap tiga), dan Benzena.")
    
    tab1, tab2, tab3 = st.tabs(["Percobaan 1: Alkana", "Percobaan 2: Uji Bayer & Ketidakjenuhan", "Percobaan 3: Alkuna & Benzena"])
    
    with tab1:
        st.subheader("Pembuatan dan Uji Kimia Alkana (Metana)")
        with st.expander("🛠️ Alat, Bahan & Cara Kerja"):
            st.write("""
            **Alat:** Tabung reaksi bertutup selang, bunsen.\n
            **Bahan:** Sodalime, Natrium asetat, larutan $I_2$, $KMnO_4$, dan $K_2Cr_2O_7$.\n
            **Cara Kerja:**
            1. Panaskan campuran sodalime dan natrium asetat. Gas yang keluar adalah gas Metana (Alkana).
            2. Alirkan gas tersebut ke tabung yang berisi larutan $I_2$, $KMnO_4$, dan $K_2Cr_2O_7$.
            """)
        
        st.markdown('**Hasil & Pembahasan:**')
        st.markdown('<div class="hasil-negatif"><b>(-) Semua Uji Negatif (Tidak Bereaksi)</b><br>Metana tidak merubah warna larutan I2, KMnO4, maupun K2Cr2O7.</div>', unsafe_allow_html=True)
        st.markdown("""
        **Kenapa hasilnya begitu?**
        Alkana adalah senyawa hidrokarbon jenuh (hanya punya ikatan tunggal). Ikatan tunggal C-C dan C-H ini sangat kuat dan stabil, sehingga alkana **sangat susah dioksidasi** oleh oksidator kuat sekalipun ($KMnO_4$ / $K_2Cr_2O_7$), dan **tidak bisa mengalami reaksi adisi** dengan Iodium ($I_2$).
        """)

    with tab2:
        st.subheader("Uji Larutan $I_2$ dan Uji Bayer ($KMnO_4$)")
        st.write("Membedakan senyawa jenuh (Heksana) dengan senyawa tak jenuh (mengandung ikatan rangkap seperti beberapa komponen di minyak tanah).")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="card"><b>Uji Heksana (Alkana)</b><br>Ditetesi I2 / KMnO4 warnanya <b>TETAP</b> (tidak pudar).<br><br><i>Alasan:</i> Heksana jenuh, tidak bisa diadisi atau dioksidasi.</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="card"><b>Uji Minyak Tanah</b><br>Ditetesi I2 / KMnO4 warnanya <b>PUDAR</b> dan muncul endapan coklat (MnO2).<br><br><i>Alasan:</i> Minyak tanah campuran hidrokarbon yang mengandung rantai tak jenuh (alkena), sehingga terjadi pemutusan ikatan rangkap (adisi/oksidasi).</div>', unsafe_allow_html=True)

    with tab3:
        st.subheader("Pembuatan Alkuna & Uji Benzena")
        st.write("**Alkuna (Dari Karbit):** Karbit ($CaC_2$) ditambah air akan menghasilkan gas Etuna (Alkuna). Karena etuna punya ikatan rangkap tiga, dia **sangat reaktif** dan langsung memudarkan warna larutan $I_2$ dan $KMnO_4$ (reaksi adisi/pemutusan rangkap).")
        st.write("**Benzena:** Kalau dibakar menghasilkan asap berjelaga tebal karena kadar karbonnya sangat tinggi. Benzena tidak bereaksi dengan air $I_2$ biasa karena ikatan rangkapnya beresonansi (stabil). Harus pakai katalis serbuk besi (Fe) agar terjadi reaksi *substitusi* bukan adisi.")

# ================= MODUL 2: ALKOHOL & FENOL =================
elif menu == "🍷 Modul 2: Alkohol & Fenol":
    st.title("🍷 Modul 2: Alkohol, Eter, dan Fenol")
    
    percobaan = st.selectbox("Pilih Percobaan:", ["Uji Kelarutan", "Uji Lucas", "Uji Ceric Nitrat", "Sifat Asam Fenol"])
    
    if percobaan == "Uji Kelarutan":
        st.markdown('<div class="card"><b>Alat & Bahan:</b> Tabung reaksi, Etanol, Butanol, t-butil alkohol, Amil alkohol, air suling.</div>', unsafe_allow_html=True)
        st.write("**Hasil & Pembahasan:**")
        st.write("- **Etanol (C2):** Larut sempurna dalam air (ikatan hidrogen kuat).")
        st.write("- **1-Butanol (C4):** Kurang larut (mulai membentuk 2 fasa). Makin panjang rantai karbon (non-polar), makin susah larut di air.")
        st.write("- **t-butil alkohol:** Lebih larut dari 1-butanol karena strukturnya bercabang, sehingga area non-polarnya lebih kecil (kompak).")
        
    elif percobaan == "Uji Lucas":
        st.markdown('<div class="card"><b>Fungsi:</b> Membedakan alkohol primer, sekunder, dan tersier menggunakan pereaksi Lucas (ZnCl2 dalam HCl).</div>', unsafe_allow_html=True)
        st.success("✅ **Alkohol Tersier (t-butil alkohol):** Langsung keruh seketika karena sangat reaktif membentuk alkil klorida (karbokation stabil).")
        st.warning("⏳ **Alkohol Sekunder (2-butanol):** Keruh setelah menunggu/dipanaskan 5-10 menit.")
        st.error("❌ **Alkohol Primer (1-butanol):** Tidak keruh (bening) pada suhu ruang.")

    elif percobaan == "Uji Ceric Nitrat":
        st.write("Uji umum untuk mendeteksi adanya gugus fungsi alkohol (-OH).")
        st.markdown('<div class="hasil-positif">Alkohol Primer, Sekunder, dan Tersier akan mengubah warna kuning ceric nitrat menjadi <b>Merah / Merah Muda</b>. Hal ini terjadi karena gugus -OH berikatan kompleks dengan ion Cerium.</div>', unsafe_allow_html=True)

    elif percobaan == "Sifat Asam Fenol":
        st.write("**Hasil:** Fenol memerahkan kertas lakmus biru, artinya dia bersifat asam.")
        st.write("**Kenapa?** Ion fenoksida yang terbentuk ketika fenol melepas H+ sangat distabilkan oleh resonansi cincin benzena. Makanya fenol bisa bereaksi dengan basa kuat (NaOH), sedangkan alkohol biasa tidak bisa.")

# ================= MODUL 3: ALDEHID & KETON =================
elif menu == "💊 Modul 3: Aldehid & Keton":
    st.title("💊 Modul 3: Aldehid & Keton")
    st.write("Aldehid dan Keton sama-sama punya gugus karbonil (C=O). Bedanya, aldehid posisinya di ujung, keton di tengah. Akibatnya, **Aldehid gampang banget dioksidasi (reduktor kuat)**, sedangkan keton susah.")

    tab1, tab2, tab3 = st.tabs(["Pereaksi Tollens", "Pereaksi Fehling", "Pereaksi Schiff & Na-Bisulfit"])
    
    with tab1:
        st.write("**Alat & Bahan:** Asetaldehida (Aldehid), Aseton (Keton), Pereaksi Tollens ($AgNO_3$ dalam suasana basa amoniakal).")
        st.success("✅ **Aldehid:** Terbentuk **Cermin Perak** di dinding tabung. Aldehid mereduksi ion $Ag^+$ menjadi logam perak bebas ($Ag$).")
        st.error("❌ **Keton (Aseton):** Tidak bereaksi (tetap bening). Keton tidak punya hidrogen yang menempel di karbonil, jadi gak bisa dioksidasi Tollens.")

    with tab2:
        st.write("**Alat & Bahan:** Asetaldehida, Aseton, Pereaksi Fehling (campuran $CuSO_4$ dan garam rochelle). Harus dipanaskan.")
        st.success("✅ **Aldehid:** Terbentuk **Endapan Merah Bata**. Aldehid mereduksi ion tembaga(II) yang warnanya biru menjadi tembaga(I) oksida ($Cu_2O$) yang berwarna merah bata.")
        st.error("❌ **Keton:** Tidak bereaksi (larutan tetap biru jernih).")

    with tab3:
        st.write("**Uji Schiff:** Asetaldehida memulihkan warna pereaksi Schiff menjadi **Merah Magenta/Fuksin**. Keton tidak bereaksi.")
        st.write("**Uji Na-Bisulfit ($NaHSO_3$):** Keduanya (Aldehid dan beberapa keton kecil seperti aseton) menghasilkan **endapan kristal putih**. Ini adalah reaksi adisi nukleofilik karena gugus C=O itu polar, jadi ion bisulfit bisa nempel di karbonnya.")

# ================= MODUL 4: ASAM KARBOKSILAT =================
elif menu == "🍋 Modul 4: Asam Karboksilat":
    st.title("🍋 Modul 4: Asam Karboksilat & Derivatnya")
    
    with st.expander("1. Reaksi Penggaraman & Uji Barit ($NaHCO_3$)"):
        st.write("**Cara Kerja:** Asam asetat ditambahkan $NaHCO_3$, lalu gas yang keluar didekatkan dengan batang kaca yang dicelupkan ke air barit ($Ba(OH)_2$).")
        st.markdown('<div class="hasil-positif"><b>Hasil:</b> Timbul gelembung gas, dan air barit menjadi <b>KERUH</b>.</div>', unsafe_allow_html=True)
        st.write("**Penjelasan:** Asam karboksilat bereaksi dengan garam bikarbonat menghasilkan gas Karbondioksida ($CO_2$). Gas ini bereaksi dengan air barit membentuk endapan Barium Karbonat ($BaCO_3$) yang warnanya putih/keruh.")

    with st.expander("2. Pembentukan Senyawa Beraroma (Esterifikasi)"):
        st.write("**Cara Kerja:** Etanol / Amil Alkohol + Asam Asetat + Katalis Asam Sulfat Pekat, lalu dipanaskan.")
        st.write("**Hasil:** Muncul wangi buah-buahan atau wangi khas.")
        st.write("**Penjelasan:** Reaksi antara alkohol dan asam karboksilat dengan bantuan asam sulfat (sebagai dehidrator dan katalis) akan membentuk senyawa **Ester**. Ester ini wujudnya volatil dan punya aroma yang harum (etil asetat = wangi kuteks, amil asetat = wangi pisang).")

    with st.expander("3. Oksidasi Asam Karboksilat ($KMnO_4$)"):
        st.write("**Hasil:** Asam asetat **TIDAK** bisa memudarkan warna $KMnO_4$ (karena asetat sudah merupakan bentuk oksidasi tertinggi). Tapi **Asam Oksalat** BISA memudarkan $KMnO_4$ karena oksalat bisa dioksidasi menjadi $CO_2$ dan air.")

# ================= PREDIKTOR REAKSI (POST-TEST) =================
elif menu == "🎯 Prediktor Post-Test (Pro)":
    st.title("🎯 Prediktor Uji Senyawa Organik")
    st.write("Fitur ini ngebantu kamu nebak hasil reaksi lab dengan cepat buat ngerjain Post-Test atau Laprak. Tinggal pilih senyawanya!")

    col1, col2 = st.columns(2)
    with col1:
        senyawa = st.selectbox("Pilih Senyawa:", ["Alkohol Primer", "Alkohol Sekunder", "Alkohol Tersier", "Formaldehida", "Aseton", "Heksana", "Etil Asetat", "Asam Asetat"])
    with col2:
        pereaksi = st.selectbox("Pilih Pereaksi:", ["Oksidator (K2Cr2O7 / H+)", "Pereaksi Lucas (ZnCl2 / HCl)", "Pereaksi Tollens", "Pereaksi Fehling", "Uji Iodoform (I2 / NaOH)", "NaHCO3 + Uji Barit"])

    # Logika Cepat
    hasil = "(-) Tidak Bereaksi"
    alasan = "Senyawa ini tidak punya gugus fungsi yang cocok untuk bereaksi dengan pereaksi tersebut."

    if pereaksi == "Oksidator (K2Cr2O7 / H+)" and senyawa in ["Alkohol Primer", "Alkohol Sekunder", "Formaldehida"]:
        hasil = "(+) Warna jingga berubah jadi hijau"
        alasan = "Senyawa punya atom Hidrogen alfa, jadi bisa dioksidasi. Cr(VI) jingga tereduksi jadi Cr(III) hijau."
    elif pereaksi == "Pereaksi Lucas (ZnCl2 / HCl)":
        if senyawa == "Alkohol Tersier":
            hasil = "(+) Keruh seketika"
            alasan = "Sangat reaktif, langsung membentuk alkil klorida karena karbokation tersiernya sangat stabil."
        elif senyawa == "Alkohol Sekunder":
            hasil = "(+) Keruh setelah 5-10 menit"
            alasan = "Reaksi berjalan lambat membentuk alkil klorida tak larut air."
    elif pereaksi == "Pereaksi Tollens" and senyawa == "Formaldehida":
        hasil = "(+) Terbentuk Cermin Perak"
        alasan = "Aldehid mereduksi ion Perak (Ag+) menjadi logam Perak murni."
    elif pereaksi == "Pereaksi Fehling" and senyawa == "Formaldehida":
        hasil = "(+) Endapan Merah Bata"
        alasan = "Aldehid mereduksi ion Tembaga (Cu2+) menjadi Cu2O (merah bata)."
    elif pereaksi == "Uji Iodoform (I2 / NaOH)" and senyawa == "Aseton":
        hasil = "(+) Endapan Kuning"
        alasan = "Aseton punya gugus metil keton yang spesifik bereaksi dengan iodium membentuk kristal iodoform kuning."
    elif pereaksi == "NaHCO3 + Uji Barit" and senyawa == "Asam Asetat":
        hasil = "(+) Gelembung gas & air barit keruh"
        alasan = "Asam asetat melepas gas CO2, yang kemudian bereaksi dengan Barium Hidroksida membentuk endapan BaCO3."

    # Tampilan Output Prediktor
    is_positif = "(+)" in hasil
    st.divider()
    if is_positif:
        st.markdown(f'<div class="hasil-positif"><b>Hasil Pengamatan:</b><br>{hasil}<br><br><b>Alasan Teoritis:</b><br>{alasan}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="hasil-negatif"><b>Hasil Pengamatan:</b><br>{hasil}<br><br><b>Alasan Teoritis:</b><br>{alasan}</div>', unsafe_allow_html=True)
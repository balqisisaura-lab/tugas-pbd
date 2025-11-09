import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="BookRelink - Perpustakaan Digital",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Custom dengan Animasi & Color Palette Orange-Blue
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Sembunyikan sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #e4e9f2 0%, #b8d4e8 50%, #7fbbdd 100%);
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #7fbbdd 0%, #f58b05 100%);
        color: white;
        border-radius: 25px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin-top: 0.5rem;
        opacity: 0.95;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 55px;
        padding: 0 35px;
        background: white;
        border-radius: 15px;
        font-weight: 600;
        font-size: 17px;
        color: #7fbbdd;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(127,187,221,0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #7fbbdd 0%, #f58b05 100%);
        color: white !important;
        border: 2px solid white;
        box-shadow: 0 8px 25px rgba(245,139,5,0.4);
    }
    
    /* Search and filter */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #e4e9f2;
        padding: 12px 20px;
        background: white;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        font-size: 16px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #7fbbdd;
        box-shadow: 0 5px 20px rgba(127,187,221,0.3);
    }
    
    .stSelectbox > div > div {
        border-radius: 15px;
        border: 2px solid #e4e9f2;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Book title styling */
    .book-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .book-author {
        font-size: 1.1rem;
        color: #7fbbdd;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    .category-badge {
        display: inline-block;
        padding: 8px 20px;
        border-radius: 25px;
        background: linear-gradient(135deg, #ffe22f 0%, #f58b05 100%);
        color: white;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 0.5rem;
        box-shadow: 0 3px 10px rgba(245,139,5,0.3);
    }
    
    /* Container for book cards */
    div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        border: 2px solid #e4e9f2;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    
    div[data-testid="stVerticalBlock"] > div:has(div.element-container):hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(127,187,221,0.3);
        border-color: #7fbbdd;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #f58b05 0%, #ff9f1a 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(245,139,5,0.3);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(245,139,5,0.5);
        background: linear-gradient(135deg, #ff9f1a 0%, #f58b05 100%);
    }
    
    /* Contact section */
    .contact-section {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #7fbbdd 0%, #f58b05 100%);
        color: white;
        border-radius: 25px;
        margin-top: 2rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.2);
    }
    
    .contact-section h2 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .wa-button {
        display: inline-block;
        background: white;
        color: #f58b05;
        padding: 18px 50px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.2rem;
        margin-top: 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .wa-button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        text-decoration: none;
    }
    
    /* Info cards */
    .info-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #e4e9f2;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        height: 100%;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(127,187,221,0.3);
        border-color: #7fbbdd;
    }
    
    .info-card h3 {
        margin-bottom: 1rem;
        font-size: 1.5rem;
    }
    
    .info-card p {
        color: #666;
        line-height: 1.6;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #7fbbdd, transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📚 BookRelink</h1>
    <p>Perpustakaan Digital - Akses Buku Kapan Saja, Dimana Saja</p>
</div>
""", unsafe_allow_html=True)

# DATA BUKU
books_data = {
    'Judul': [
        'Buku Regresi Spasial Aplikasi',
        'Novel Bumi',
        'Geographically Weighted Regression',
        'Negeri di Ujung Tanduk',
        'Bulan',
        'Tentang Kamu',
        'The Falling Leaf Never Hates The Wind',
        'Matahari'
    ],
    'Penulis': [
        'Hasbi Yasin, dkk',
        'Tere Liye',
        'Rezzy Eko Caraka',
        'Tere Liye',
        'Tere Liye',
        'Tere Liye',
        'Tere Liye',
        'Tere Liye'
    ],
    'Kategori': [
        'Statistik',
        'Novel',
        'Statistik',
        'Novel',
        'Novel',
        'Novel',
        'Novel',
        'Novel'
    ],
    'FileID': [
        '1S3nYha3ItXuVzlY9v6rRZDCbs6w1dXgr',
        '1t2OnQS4sPnXYDL-vrpgIWe3UiPqnixB2',
        '1bxKKe0p9rqWCxrjjQpcJpgYRmq5McDva',
        '1g-FH8NMS8EXhJsq-ptuuefa5ryG8X8qR',
        '1nbfDsUqoYtMB4cxNuf7SDmuO2QsI6x9R',
        '1fN4PsMiUKp0RvkBnR3eq3-ia2VbrL8K-',
        '1i8Aa-dt5nD4ohFrbNsxoZ8RpM8FZ8Mf8',
        '1QAi4nojK7prUgHXeHW2J8fJ6znldKtJm'
    ]
}

df_books = pd.DataFrame(books_data)

# Konversi FILE_ID ke format preview
df_books['Link'] = df_books['FileID'].apply(
    lambda x: f'https://drive.google.com/file/d/{x}/preview'
)

# TABS NAVIGASI
tab1, tab2 = st.tabs(["🏠 Home", "📞 Contact Admin"])

# ============= TAB HOME =============
with tab1:
    # Search dan Filter
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Cari Buku", 
            placeholder="🔍 Ketik judul buku atau nama penulis...",
        )
    
    with col2:
        categories = ['Semua Kategori'] + sorted(df_books['Kategori'].unique().tolist())
        selected_category = st.selectbox(
            "Filter Kategori",
            categories,
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filter data
    filtered_books = df_books.copy()
    
    if selected_category != 'Semua Kategori':
        filtered_books = filtered_books[filtered_books['Kategori'] == selected_category]
    
    if search_query:
        filtered_books = filtered_books[
            filtered_books['Judul'].str.contains(search_query, case=False) |
            filtered_books['Penulis'].str.contains(search_query, case=False)
        ]
    
    # Tampilkan buku
    if len(filtered_books) > 0:
        for idx, row in filtered_books.iterrows():
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.markdown(f'<div class="book-title">📖 {row["Judul"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="book-author">✍️ {row["Penulis"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<span class="category-badge">{row["Kategori"]}</span>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                st.link_button("📥 Buka Buku", row['Link'], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.warning("🔍 Tidak ada buku yang ditemukan. Coba kata kunci lain.")

# ============= TAB CONTACT =============
with tab2:
    st.markdown("""
    <div class="contact-section">
        <h2>📱 Hubungi Admin BookRelink</h2>
        <p style='font-size: 1.2rem; margin: 20px 0;'>
            Punya pertanyaan? Ingin request buku tertentu?<br>
            Atau butuh bantuan mengakses buku?
        </p>
        <p style='font-size: 1.1rem; margin: 20px 0;'>
            Admin kami siap membantu Anda!
        </p>
        <a href="https://wa.me/6289533027725?text=Halo%20admin%20BookRelink,%20saya%20ingin%20bertanya%20tentang%20buku" 
           target="_blank" 
           class="wa-button">
            💬 Chat WhatsApp Admin
        </a>
        <p style='margin-top: 30px; font-size: 1rem; opacity: 0.95;'>
            📞 WhatsApp: 0895-3302-77258
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Info cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #f58b05;">📚 Request Buku</h3>
            <p>Buku yang kamu cari tidak ada? Hubungi admin untuk request!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #7fbbdd;">💡 Bantuan Teknis</h3>
            <p>Kesulitan membuka buku? Admin siap membantu!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #ffe22f;">⭐ Saran & Masukan</h3>
            <p>Punya saran untuk BookRelink? Sampaikan ke admin!</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #7fbbdd; padding: 2rem 0;'>
    <p style='font-size: 1rem; font-weight: 600;'>© 2024 BookRelink - Perpustakaan Digital</p>
    <p style='font-size: 0.9rem;'>Dibuat dengan ❤️ untuk memudahkan akses pendidikan</p>
</div>
""", unsafe_allow_html=True)

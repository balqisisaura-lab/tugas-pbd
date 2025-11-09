import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="BookRelink - Perpustakaan Digital",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Custom
st.markdown("""
<style>
    /* Sembunyikan sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 30px;
        background-color: white;
        border-radius: 8px;
        font-weight: 600;
        font-size: 16px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Book card styling */
    .book-card {
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        margin-bottom: 1rem;
        background: white;
        transition: all 0.3s;
    }
    
    .book-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        border-color: #667eea;
    }
    
    /* Contact section */
    .contact-section {
        text-align: center;
        padding: 3rem;
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white;
        border-radius: 15px;
        margin-top: 2rem;
    }
    
    .wa-button {
        display: inline-block;
        background: white;
        color: #25D366;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 18px;
        margin-top: 1rem;
        transition: all 0.3s;
    }
    
    .wa-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Search box */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 10px;
    }
    
    /* Category badge */
    .category-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        background: #f0f2f6;
        color: #667eea;
        font-size: 14px;
        font-weight: 600;
        margin-top: 5px;
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
        'Unknown',
        'Tere Liye',
        'Rezzy Eko Caraka',
        'Tere Liye',
        'Tere Liye',
        'Unknown',
        'Unknown',
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
            "🔍 Cari Buku", 
            placeholder="Ketik judul buku atau nama penulis...",
            label_visibility="collapsed"
        )
    
    with col2:
        categories = ['Semua Kategori'] + sorted(df_books['Kategori'].unique().tolist())
        selected_category = st.selectbox(
            "Kategori",
            categories,
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    
    # Filter data
    filtered_books = df_books.copy()
    
    if selected_category != 'Semua Kategori':
        filtered_books = filtered_books[filtered_books['Kategori'] == selected_category]
    
    if search_query:
        filtered_books = filtered_books[
            filtered_books['Judul'].str.contains(search_query, case=False) |
            filtered_books['Penulis'].str.contains(search_query, case=False)
        ]
    
    # Info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📚 Total Buku", len(df_books))
    with col2:
        st.metric("✅ Buku Ditemukan", len(filtered_books))
    with col3:
        st.metric("📂 Kategori", df_books['Kategori'].nunique())
    
    st.markdown("---")
    
    # Tampilkan buku
    if len(filtered_books) > 0:
        for idx, row in filtered_books.iterrows():
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"### 📖 {row['Judul']}")
                st.write(f"**✍️ Penulis:** {row['Penulis']}")
                st.markdown(f'<span class="category-badge">{row["Kategori"]}</span>', 
                           unsafe_allow_html=True)
            
            with col2:
                st.markdown("")
                st.markdown("")
                st.link_button(
                    "📥 Buka Buku", 
                    row['Link'], 
                    use_container_width=True,
                    type="primary"
                )
            
            st.markdown("---")
    else:
        st.warning("🔍 Tidak ada buku yang ditemukan. Coba kata kunci lain.")

# ============= TAB CONTACT =============
with tab2:
    st.markdown("""
    <div class="contact-section">
        <h2>📱 Hubungi Admin BookRelink</h2>
        <p style='font-size: 18px; margin: 20px 0;'>
            Punya pertanyaan? Ingin request buku tertentu?<br>
            Atau butuh bantuan mengakses buku?
        </p>
        <p style='font-size: 16px; margin: 20px 0;'>
            Admin kami siap membantu Anda!
        </p>
        <a href="https://wa.me/6289533027725?text=Halo%20admin%20BookRelink,%20saya%20ingin%20bertanya%20tentang%20buku" 
           target="_blank" 
           class="wa-button">
            💬 Chat WhatsApp Admin
        </a>
        <p style='margin-top: 30px; font-size: 14px; opacity: 0.9;'>
            📞 WhatsApp: 0895-3302-77258
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("")
    
    # Info tambahan
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **📚 Request Buku**
        
        Buku yang kamu cari tidak ada? 
        Hubungi admin untuk request!
        """)
    
    with col2:
        st.success("""
        **💡 Bantuan Teknis**
        
        Kesulitan membuka buku?
        Admin siap membantu!
        """)
    
    with col3:
        st.warning("""
        **⭐ Saran & Masukan**
        
        Punya saran untuk BookRelink?
        Sampaikan ke admin!
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 2rem 0;'>
    <p>© 2024 BookRelink - Perpustakaan Digital</p>
    <p>Dibuat dengan ❤️ untuk memudahkan akses pendidikan</p>
</div>
""", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="BookRelink - Perpustakaan Digital",
    page_icon="📚",
    layout="wide"
)

# CSS Custom
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .book-card {
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        margin-bottom: 1rem;
        background: white;
        transition: transform 0.2s;
    }
    .book-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .contact-btn {
        background: #25D366;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        margin-top: 1rem;
    }
    .search-box {
        margin-bottom: 2rem;
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
# Ganti data ini dengan buku-buku yang kamu punya
# Format: Judul, Penulis, Kategori, Link Google Drive
books_data = {
    'Judul': [
        'Belajar Python untuk Pemula',
        'Panduan Web Development',
        'Matematika Dasar',
        'Bahasa Indonesia SBMPTN',
        'Fisika Modern'
    ],
    'Penulis': [
        'Ahmad Surya',
        'Budi Santoso',
        'Dr. Siti Aminah',
        'Prof. Wahyu',
        'Dr. Eka Putra'
    ],
    'Kategori': [
        'Pemrograman',
        'Teknologi',
        'Matematika',
        'Bahasa',
        'Sains'
    ],
    'Link': [
        'https://drive.google.com/file/d/YOUR_FILE_ID_1/view',
        'https://drive.google.com/file/d/YOUR_FILE_ID_2/view',
        'https://drive.google.com/file/d/YOUR_FILE_ID_3/view',
        'https://drive.google.com/file/d/YOUR_FILE_ID_4/view',
        'https://drive.google.com/file/d/YOUR_FILE_ID_5/view'
    ]
}

df_books = pd.DataFrame(books_data)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2702/2702154.png", width=100)
    st.title("Menu")
    
    # Filter Kategori
    categories = ['Semua'] + sorted(df_books['Kategori'].unique().tolist())
    selected_category = st.selectbox("Filter Kategori", categories)
    
    st.markdown("---")
    
    # Kontak Admin
    st.subheader("📞 Hubungi Admin")
    st.markdown("""
    Butuh bantuan atau ingin request buku?
    
    Hubungi admin kami:
    """)
    
    # GANTI NOMOR WA ADMIN DI BAWAH INI
    admin_wa = "6281234567890"  # Ganti dengan nomor WA admin (format: 62xxx)
    wa_link = f"https://wa.me/{admin_wa}?text=Halo%20admin%20BookRelink,%20saya%20ingin%20bertanya%20tentang%20"
    
    st.markdown(f'<a href="{wa_link}" target="_blank" class="contact-btn">💬 Chat WhatsApp</a>', 
                unsafe_allow_html=True)
    
    st.markdown("---")
    st.info(f"📊 Total Buku: {len(df_books)}")

# Main Content
col1, col2 = st.columns([3, 1])

with col1:
    # Search Box
    search_query = st.text_input("🔍 Cari Buku (berdasarkan judul atau penulis)", 
                                 placeholder="Ketik judul atau penulis buku...")

with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing

# Filter berdasarkan kategori
if selected_category != 'Semua':
    filtered_books = df_books[df_books['Kategori'] == selected_category]
else:
    filtered_books = df_books

# Filter berdasarkan pencarian
if search_query:
    filtered_books = filtered_books[
        filtered_books['Judul'].str.contains(search_query, case=False) |
        filtered_books['Penulis'].str.contains(search_query, case=False)
    ]

# Tampilkan hasil
st.markdown("---")
st.subheader(f"📖 Daftar Buku ({len(filtered_books)} buku ditemukan)")

if len(filtered_books) > 0:
    # Tampilkan buku dalam card
    for idx, row in filtered_books.iterrows():
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.markdown(f"### {row['Judul']}")
                st.write(f"**Penulis:** {row['Penulis']}")
                st.write(f"**Kategori:** {row['Kategori']}")
            
            with col3:
                st.markdown("")
                st.markdown("")
                st.link_button("📥 Buka Buku", row['Link'], use_container_width=True)
            
            st.markdown("---")
else:
    st.warning("🔍 Tidak ada buku yang ditemukan. Coba kata kunci lain.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 2rem 0;'>
    <p>© 2024 BookRelink - Perpustakaan Digital</p>
    <p>Dibuat dengan ❤️ untuk memudahkan akses pendidikan</p>
</div>
""", unsafe_allow_html=True)

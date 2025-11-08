# app.py - Main Entry Point
import streamlit as st

# Configure page FIRST, before any other streamlit calls
st.set_page_config(
    page_title="Deteksi Penyakit Daun Singkong",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

from auth import init_session_state, get_current_role, is_authenticated, is_admin
from login import login_page
from responsive_ui import apply_responsive_theme, responsive_hero, responsive_button_grid, add_footer
from navigation import create_navigation_sidebar, show_role_info
from database import init_database

# Apply responsive theme
apply_responsive_theme()

# Initialize database on startup
init_database()

# Initialize session state
init_session_state()

# Check authentication
if not is_authenticated():
    login_page()
    st.stop()

# Create navigation sidebar
create_navigation_sidebar()
show_role_info()

# Get current user info
role = get_current_role()
username = st.session_state.get('username', 'User')

# Minimalist logout button with text
if st.button("🚪 Logout", key="logout_minimal", help="Logout"):
    # Clear all session state
    st.session_state.authenticated = False
    st.session_state.user_id = None
    st.session_state.username = None
    st.session_state.email = None
    st.session_state.user_profile = None
    st.session_state.role = 'user'

    # Show logout message
    st.success("✅ Logout berhasil! Anda telah keluar dari sistem. 👋")
    st.info("🔄 Mengalihkan ke halaman login...")

    # Add small delay for user to see the message
    import time
    time.sleep(1.5)

    st.rerun()

# Style the minimalist logout button
st.markdown("""
    <style>
    /* Minimalist logout button with text */
    [data-testid="stButton"][aria-label="Logout"] {
        position: fixed !important;
        top: 1rem !important;
        right: 1rem !important;
        z-index: 10001 !important;
        background: #F44336 !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.5rem 1rem !important;
        color: white !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        white-space: nowrap !important;
    }

    [data-testid="stButton"][aria-label="Logout"]:hover {
        background: #C62828 !important;
        transform: scale(1.1) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        [data-testid="stButton"][aria-label="Logout"] {
            top: 0.8rem !important;
            right: 0.8rem !important;
            width: 35px !important;
            height: 35px !important;
            font-size: 1rem !important;
        }
    }

    @media (max-width: 480px) {
        [data-testid="stButton"][aria-label="Logout"] {
            top: 0.6rem !important;
            right: 0.6rem !important;
            width: 30px !important;
            height: 30px !important;
            font-size: 0.9rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Fixed logout button in bottom-right corner
st.markdown("""
    <style>
    /* Fixed logout button in bottom-right */
    .logout-bottom {
        position: fixed !important;
        bottom: 1rem !important;
        right: 1rem !important;
        z-index: 10001 !important;
        background: #F44336 !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
        border-radius: 0.5rem !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        white-space: nowrap !important;
    }

    .logout-bottom:hover {
        background: #C62828 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .logout-bottom {
            bottom: 0.8rem !important;
            right: 0.8rem !important;
            padding: 0.4rem 0.8rem !important;
            font-size: 0.8rem !important;
        }
    }

    @media (max-width: 480px) {
        .logout-bottom {
            bottom: 0.6rem !important;
            right: 0.6rem !important;
            padding: 0.3rem 0.6rem !important;
            font-size: 0.75rem !important;
        }
    }

    /* Ensure content doesn't overlap - remove top padding since logout moved to bottom */
    .main-content {
        padding-top: 2rem !important;
    }

    @media (max-width: 768px) {
        .main-content {
            padding-top: 1.5rem !important;
        }
    }

    @media (max-width: 480px) {
        .main-content {
            padding-top: 1rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)


# Display welcome message with top padding to avoid overlap
st.markdown('<div class="main-content">', unsafe_allow_html=True)
responsive_hero(f"Selamat Datang, {username}! 👋", "Sistem Deteksi Penyakit Daun Singkong dengan deep learning")
st.markdown('</div>', unsafe_allow_html=True)

# Show role-specific menu
if is_admin():
    st.markdown("## 📋 Menu Admin")

    st.info("""
    **👑 Fitur Admin yang tersedia:**

    - 📊 Dashboard untuk melihat statistik sistem
    - 📁 Kelola data training dan model
    - 🧪 Test model dengan dataset uji
    - 📈 Pantau semua aktivitas deteksi user
    """)

    # Admin menu buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 Dashboard Admin", use_container_width=True, key="admin_dashboard"):
            st.switch_page("pages/01_📊_Dashboard_Admin.py")

    with col2:
        if st.button("📁 Kelola Training", use_container_width=True, key="admin_training"):
            st.switch_page("pages/02_📁_Kelola_Training.py")

    with col3:
        if st.button("🧪 Test Model", use_container_width=True, key="admin_test"):
            st.switch_page("pages/03_🧪_Test_Model.py")

    # Additional admin buttons
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("🔍 Deteksi Penyakit", use_container_width=True, key="admin_detect"):
            st.switch_page("pages/04_🔍_Klasifikasi.py")

    with col5:
        if st.button("📈 Riwayat Deteksi", use_container_width=True, key="admin_history"):
            st.switch_page("pages/05_📈_Riwayat_Klasifikasi.py")

    with col6:
        if st.button("⚙️ Pengaturan Akun", use_container_width=True, key="admin_settings"):
            st.switch_page("pages/06_⚙️_Pengaturan.py")

else:
    st.markdown("## 👤 Menu User")

    st.info("""
    **Anda dapat menggunakan fitur berikut:**

    - 🔍 **Deteksi Penyakit** - Upload gambar daun singkong untuk mendeteksi penyakit
    - 📈 **Riwayat Deteksi** - Melihat riwayat hasil deteksi Anda
    - ⚙️ **Pengaturan Akun** - Kelola informasi akun dan password Anda
    """)

    # User menu buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔍 Deteksi Penyakit", use_container_width=True, key="user_detect"):
            st.switch_page("pages/04_🔍_Klasifikasi.py")

    with col2:
        if st.button("📈 Riwayat Deteksi", use_container_width=True, key="user_history"):
            st.switch_page("pages/05_📈_Riwayat_Klasifikasi.py")

    with col3:
        if st.button("⚙️ Pengaturan Akun", use_container_width=True, key="user_settings"):
            st.switch_page("pages/06_⚙️_Pengaturan.py")

# Footer with info
add_footer()
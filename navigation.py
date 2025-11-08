# navigation.py - Custom Navigation System
import streamlit as st
from auth import get_current_role, is_admin

def create_navigation_sidebar():
    """Create organized navigation sidebar based on user role"""
    role = get_current_role()
    
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 🌿 Navigasi Menu")
        st.markdown("---")
        
        if is_admin():
            # Admin Navigation
            st.markdown("#### 👑 Menu Admin")
            admin_menu = {
                "📊 Dashboard Admin": "pages/01_📊_Dashboard_Admin.py",
                "📁 Kelola Training": "pages/02_📁_Kelola_Training.py",
                "🧪 Test Model": "pages/03_🧪_Test_Model.py",
            }
            
            for menu_name, page_path in admin_menu.items():
                if st.button(menu_name, use_container_width=True, key=f"admin_{menu_name}"):
                    st.switch_page(page_path)
            
            st.markdown("---")
            st.markdown("#### 👤 Menu User")
            
        # User Navigation (available for both user and admin)
        user_menu = {
            "🔍 Deteksi Penyakit": "pages/04_🔍_Klasifikasi.py",
            "📈 Riwayat Deteksi": "pages/05_📈_Riwayat_Klasifikasi.py",
        }
        
        for menu_name, page_path in user_menu.items():
            if st.button(menu_name, use_container_width=True, key=f"user_{menu_name}"):
                st.switch_page(page_path)
        
        st.markdown("---")


def show_role_info():
    """Display current user role info in sidebar"""
    with st.sidebar:
        st.markdown("---")
        role_emoji = "👑" if is_admin() else "👤"
        role_text = "Admin" if is_admin() else "User"
        
        username = st.session_state.get('username', 'User')
        email = st.session_state.get('email', 'user@example.com')
        
        st.markdown(f"### {role_emoji} {username}")
        st.markdown(f"**Role:** {role_text}")
        st.caption(f"📧 {email}")


def show_logout_button():
    """Show logout button in sidebar"""
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1:
            st.caption("⚙️ Pengaturan")
        with col2:
            if st.button("🚪 Logout", use_container_width=True, key="logout_btn_nav"):
                # Clear all session state
                st.session_state.authenticated = False
                st.session_state.user_id = None
                st.session_state.username = None
                st.session_state.email = None
                st.session_state.user_profile = None
                st.session_state.role = 'user'

                # Show logout message and redirect
                st.success("✅ Logout berhasil! Anda telah keluar dari sistem. 👋")
                st.info("🔄 Mengalihkan ke halaman login...")

                # Add small delay for user to see the message
                import time
                time.sleep(1.5)

                st.rerun()


def create_home_button():
    """Create home button in sidebar"""
    with st.sidebar:
        if st.button("🏠 Home", use_container_width=True, key="home_button"):
            st.switch_page("app.py")
# auth.py
import streamlit as st
from database import (
    register_user, login_user, login_or_register_google,
    get_user_profile, email_exists, username_exists, get_user_role
)

def init_session_state():
    """Initialize session state for authentication"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'email' not in st.session_state:
        st.session_state.email = None
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = None
    if 'role' not in st.session_state:
        st.session_state.role = 'user'



def show_logout_button():
    """Show logout button in sidebar"""
    if st.session_state.authenticated:
        with st.sidebar:
            st.markdown("---")
            
            # Show user info
            role_emoji = "👑" if st.session_state.role == 'admin' else "👤"
            role_text = "Admin" if st.session_state.role == 'admin' else "User"
            st.markdown(f"{role_emoji} **{st.session_state.username}** ({role_text})")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"📧 {st.session_state.email}")
            with col2:
                if st.button("Logout 🚪", use_container_width=True, key="logout_btn"):
                    # Clear all session state
                    st.session_state.authenticated = False
                    st.session_state.user_id = None
                    st.session_state.username = None
                    st.session_state.email = None
                    st.session_state.user_profile = None
                    st.session_state.role = 'user'
                    st.success("Logout berhasil! 👋")
                    st.rerun()

def require_login():
    """Check if user is logged in, redirect to login if not"""
    init_session_state()
    
    if not st.session_state.authenticated:
        st.error("❌ Anda harus login terlebih dahulu!")
        st.info("Silakan login di halaman utama.")
        st.stop()

def get_current_user_id():
    """Get current user ID"""
    return st.session_state.get('user_id')

def get_current_username():
    """Get current username"""
    return st.session_state.get('username')

def get_current_role():
    """Get current user role"""
    return st.session_state.get('role', 'user')

def is_admin():
    """Check if current user is admin"""
    return st.session_state.get('role') == 'admin'

def require_admin():
    """Require admin role - with strict validation"""
    init_session_state()
    
    # Get current role and validate
    current_role = st.session_state.get('role', 'user')
    is_authenticated = st.session_state.get('authenticated', False)
    
    # If not authenticated or not admin, show error and stop
    if not is_authenticated:
        st.error("❌ Anda harus login terlebih dahulu!")
        st.info("Silakan login di halaman utama.")
        st.stop()
    
    if current_role != 'admin':
        st.error("❌ Anda tidak memiliki akses ke halaman ini. Hanya admin yang dapat mengakses.")
        st.info("Hubungi administrator untuk mendapatkan akses admin.")
        st.stop()

def is_authenticated():
    """Check if user is authenticated"""
    return st.session_state.get('authenticated', False)
# login.py - Simple and clear login page
import streamlit as st
from database import register_user, login_user, email_exists, username_exists, get_user_profile

def login_page():
    """Simple and clear login page"""
    # Clean login page - hide sidebar but keep normal layout
    st.markdown("""
        <style>
        /* Hide sidebar elements */
        [data-testid="collapsedControl"] { display: none !important; }
        [data-testid="stSidebarNav"] { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="stSidebarContent"] { display: none !important; }
        [data-testid="stSidebarHeader"] { display: none !important; }
        .stSidebar { display: none !important; }

        /* Hide header and footer */
        .stApp > header { display: none !important; }
        .stApp > footer { display: none !important; }

        /* Normal layout for 100% zoom */
        [data-testid="stAppViewContainer"] > section {
            padding-top: 2rem !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Enhanced CSS with better visibility and modern design
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 50%, #A5D6A7 100%);
            background-attachment: fixed;
        }

        /* Flexible main content centering */
        [data-testid="stAppViewContainer"] > section {
            max-width: 600px;
            margin: 0 auto !important;
            padding: 1rem;
        }

        /* Responsive max-width */
        @media (max-width: 768px) {
            [data-testid="stAppViewContainer"] > section {
                max-width: 95%;
                padding: 0.5rem;
            }
        }

        .stTabs {
            background-color: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 12px 40px rgba(76, 175, 80, 0.15);
            border: 2px solid rgba(76, 175, 80, 0.1);
        }

        .stTextInput label {
            color: #1B5E20 !important;
            font-weight: 700 !important;
            font-size: 1.1em !important;
        }

        .stTextInput input {
            background-color: #ffffff !important;
            color: #1B5E20 !important;
            border: 3px solid #4CAF50 !important;
            border-radius: 10px !important;
            padding: 12px !important;
            font-size: 1em !important;
        }

        .stTextInput input:focus {
            border-color: #2E7D32 !important;
            box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2) !important;
        }

        .stButton button {
            background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%) !important;
            color: white !important;
            font-weight: 700 !important;
            font-size: 1.1em !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease !important;
        }

        .stButton button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4) !important;
            background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%) !important;
        }

        .stMarkdown h1 {
            color: #1B5E20 !important;
            font-weight: 800 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1) !important;
        }

        .stMarkdown h3 {
            color: #2E7D32 !important;
            font-weight: 700 !important;
        }

        .stMarkdown p {
            color: #1B5E20 !important;
            font-weight: 500 !important;
        }

        /* Success messages */
        .stSuccess {
            background-color: rgba(232, 245, 233, 0.95) !important;
            border: 2px solid #4CAF50 !important;
            color: #2E7D32 !important;
            border-radius: 10px !important;
        }

        /* Error messages */
        .stError {
            background-color: rgba(255, 235, 238, 0.95) !important;
            border: 2px solid #F44336 !important;
            color: #C62828 !important;
            border-radius: 10px !important;
        }

        /* Warning messages */
        .stWarning {
            background-color: rgba(255, 243, 224, 0.95) !important;
            border: 2px solid #FF9800 !important;
            color: #E65100 !important;
            border-radius: 10px !important;
        }

        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: rgba(76, 175, 80, 0.1) !important;
            border-radius: 10px 10px 0 0 !important;
            color: #2E7D32 !important;
            font-weight: 600 !important;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: #4CAF50 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Flexible container - responsive columns
    if st.session_state.get('show_signup', False):
        # Signup mode - wider for more fields
        col_left, col_center, col_right = st.columns([0.5, 3, 0.5])
    else:
        # Login mode - standard width
        col_left, col_center, col_right = st.columns([1, 2, 1])
    
    with col_center:
        st.markdown("<h1 style='text-align: center; color: #1B5E20; font-size: 2em; margin-bottom: 0.5em;'>🌿 Deteksi Penyakit Daun Singkong</h1>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Initialize signup mode
        if 'show_signup' not in st.session_state:
            st.session_state.show_signup = False

        # Show signup form if requested
        if st.session_state.show_signup:
            # SIGNUP FORM
            st.markdown("### 📝 Buat Akun Baru")

            new_username = st.text_input("👨‍💻 Username", placeholder="username unik", key="signup_username", help="Username harus unik dan akan digunakan untuk login")
            new_fullname = st.text_input("📋 Nama Lengkap", placeholder="Nama lengkap Anda", key="signup_fullname", help="Nama lengkap untuk identifikasi")
            new_password = st.text_input("🔐 Password", type="password", placeholder="Min 6 karakter", key="signup_password", help="Password minimal 6 karakter")
            confirm_password = st.text_input("🔐 Konfirmasi Password", type="password", placeholder="Ulangi password", key="signup_confirm", help="Harus sama dengan password di atas")

            # Register button - flexible
            st.markdown("---")
            if st.button("✨ Buat Akun", use_container_width=True, type="secondary"):
                    if not all([new_username, new_password, confirm_password]):
                        st.error("⚠️ Semua field wajib diisi!")
                    elif new_password != confirm_password:
                        st.error("❌ Konfirmasi password tidak cocok!")
                    elif len(new_password) < 6:
                        st.error("⚠️ Password minimal 6 karakter!")
                    elif username_exists(new_username):
                        st.error("❌ Username sudah digunakan!")
                    else:
                        with st.spinner("🔄 Membuat akun..."):
                            success, message = register_user(None, new_username, new_password, new_fullname)
                        if success:
                            st.success("✅ Akun berhasil dibuat! Silakan login dengan username dan password Anda.")
                            st.balloons()
                            # Auto-login after successful registration
                            st.session_state.authenticated = True
                            st.session_state.username = new_username
                            st.session_state.role = 'user'
                            # Get user ID from database
                            from database import get_connection
                            conn = get_connection()
                            cursor = conn.cursor()
                            cursor.execute('SELECT id FROM users WHERE username = ?', (new_username,))
                            user_data = cursor.fetchone()
                            if user_data:
                                st.session_state.user_id = user_data['id']
                                st.session_state.user_profile = get_user_profile(user_data['id'])
                            conn.close()
                            st.rerun()
                        else:
                            st.error(f"❌ {message}")
        else:
            # LOGIN FORM
            st.markdown("### 🔐 Masuk ke Akun Anda")

            username = st.text_input("👨‍💻 Username", placeholder="Masukkan username", help="Masukkan username yang terdaftar")
            password = st.text_input("🔐 Password", type="password", placeholder="Masukkan password", help="Password case-sensitive")

            # Flexible responsive login button
            if st.button("🚀 Masuk", use_container_width=True, type="primary"):
                    if username and password:
                        with st.spinner("🔄 Memverifikasi kredensial..."):
                            success, user_id, actual_username, role_or_error = login_user(username, password)
                        if success:
                            st.session_state.authenticated = True
                            st.session_state.user_id = user_id
                            st.session_state.username = actual_username
                            st.session_state.role = role_or_error
                            st.session_state.user_profile = get_user_profile(user_id)
                            st.success(f"✅ Selamat datang, {actual_username}!")
                            st.balloons()
                            st.rerun()
                        else:
                            st.error(f"❌ {role_or_error}")
                    else:
                        st.error("⚠️ Username dan password wajib diisi!")

            # Link to signup - flexible layout
            st.markdown("---")
            st.markdown("<div style='text-align: center; margin: 1rem 0;'>", unsafe_allow_html=True)
            if st.button("📝 Belum memiliki akun? Daftar di sini", help="Klik untuk membuat akun baru"):
                st.session_state.show_signup = True
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    login_page()
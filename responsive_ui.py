# responsive_ui.py - Responsive Design Components
import streamlit as st

def get_responsive_css():
    """CSS responsif untuk semua device"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body, [class^='css'] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 50%, #A5D6A7 100%);
        background-attachment: fixed;
    }
    
    /* MOBILE (0px - 640px) */
    @media (max-width: 640px) {
        .hero-title {
            font-size: 1.8em;
            font-weight: 700;
            color: #000000 !important;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9) !important;
            margin: 0.8em 0;
            text-align: center;
        }

        .hero-subtitle {
            font-size: 1em;
            color: #000000 !important;
            font-weight: 500;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
            margin-bottom: 1.5em;
            text-align: center;
        }
        
        .hero {
            padding: 1.2em;
            border-radius: 15px;
            margin-bottom: 1.5em;
        }
        
        .result-card {
            padding: 1.2em;
            border-radius: 15px;
            margin-bottom: 1em;
        }
        
        .info-box {
            padding: 1.2em;
            border-radius: 15px;
            margin: 1em 0;
        }
        
        .stMarkdown h1, h2, h3 {
            font-size: 1.3em !important;
        }
        
        .classification-text {
            font-size: 0.9em;
        }
        
        .confidence-badge {
            font-size: 0.8em;
            padding: 0.5em 1em;
        }
    }
    
    /* TABLET (641px - 1024px) */
    @media (min-width: 641px) and (max-width: 1024px) {
        .hero-title {
            font-size: 2.2em;
            font-weight: 700;
            color: #000000 !important;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9) !important;
            margin: 0.8em 0;
            text-align: center;
        }

        .hero-subtitle {
            font-size: 1.1em;
            color: #000000 !important;
            font-weight: 500;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
            margin-bottom: 1.5em;
            text-align: center;
        }
        
        .hero {
            padding: 1.5em;
            border-radius: 18px;
            margin-bottom: 1.8em;
        }
        
        .result-card {
            padding: 1.5em;
            border-radius: 18px;
            margin-bottom: 1.2em;
        }
        
        .info-box {
            padding: 1.5em;
            border-radius: 18px;
            margin: 1.2em 0;
        }
        
        .stMarkdown h1, h2, h3 {
            font-size: 1.5em !important;
        }
        
        .classification-text {
            font-size: 0.95em;
        }
    }
    
    /* DESKTOP (1025px+) */
    @media (min-width: 1025px) {
        .hero-title {
            font-size: 3em;
            font-weight: 800;
            color: #000000 !important;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9) !important;
            margin: 1em 0;
            text-align: center;
        }

        .hero-subtitle {
            font-size: 1.3em;
            color: #000000 !important;
            font-weight: 500;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
            margin-bottom: 2em;
            text-align: center;
        }
        
        .hero {
            padding: 2em;
            border-radius: 20px;
            margin-bottom: 2em;
        }
        
        .result-card {
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(76, 175, 80, 0.2);
            border: 2px solid #4CAF50;
        }
        
        .info-box {
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border: 2px solid #81C784;
        }
        
        .classification-text {
            font-size: 1em;
        }
    }
    
    /* SHARED STYLES - Enhanced visibility */
    .hero {
        background: linear-gradient(135deg, rgba(232, 245, 233, 0.95) 0%, rgba(200, 230, 201, 0.95) 100%) !important;
        border: 2px solid rgba(76, 175, 80, 0.3) !important;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2) !important;
    }

    .result-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(241, 248, 244, 0.98) 100%) !important;
        border: 2px solid rgba(76, 175, 80, 0.4) !important;
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.25) !important;
    }

    .info-box {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(241, 248, 244, 0.98) 100%) !important;
        text-align: center !important;
        border: 2px solid rgba(76, 175, 80, 0.3) !important;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2) !important;
    }

    /* Enhanced card content visibility */
    .result-card h1, .result-card h2, .result-card h3, .result-card h4 {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .result-card p, .result-card div, .result-card span {
        color: #000000 !important;
        font-weight: 600 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    .info-box h1, .info-box h2, .info-box h3, .info-box h4 {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .info-box p, .info-box div, .info-box span {
        color: #000000 !important;
        font-weight: 600 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }
    
    .confidence-high { 
        color: #1B5E20 !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.15);
    }
    
    .confidence-medium { 
        color: #D84315 !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.15);
    }
    
    .confidence-low { 
        color: #B71C1C !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.15);
    }
    
    /* Main text styling - High contrast */
    .stMarkdown h1 {
        color: #000000 !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.9) !important;
    }

    .stMarkdown h2 {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .stMarkdown h3 {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .stMarkdown h4 {
        color: #000000 !important;
        font-weight: 700 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Improve text visibility - Maximum contrast for all text */
    .stMarkdown p, .stMarkdown li, .stMarkdown div, .stMarkdown span {
        color: #000000 !important;
        font-weight: 700 !important;
        line-height: 1.6;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    .stMarkdown strong, .stMarkdown b {
        color: #000000 !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    /* All text elements with maximum visibility */
    .stText, .stCaption, .stSubheader, .stHeader {
        color: #000000 !important;
        font-weight: 700 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Specific text elements */
    .stTextInput label, .stFileUploader label, .stTextArea label {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    /* Progress text */
    .stProgress > div > div > div {
        color: #000000 !important;
        font-weight: 700 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Subheader styling */
    .stSubheader {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    /* Alert boxes with maximum visibility */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.99) !important;
        border: 4px solid #2E7D32 !important;
        color: #000000 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
    }

    .stAlert > div {
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 1.1em !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    .stAlert p {
        color: #000000 !important;
        font-weight: 700 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Success messages - Maximum visibility */
    .stSuccess {
        background-color: rgba(232, 245, 233, 0.99) !important;
        border: 4px solid #1B5E20 !important;
        color: #000000 !important;
        box-shadow: 0 4px 12px rgba(27, 94, 32, 0.2) !important;
    }

    .stSuccess > div {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.1em !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .stSuccess p {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Warning messages - Maximum visibility */
    .stWarning {
        background-color: rgba(255, 248, 225, 0.99) !important;
        border: 4px solid #E65100 !important;
        color: #000000 !important;
        box-shadow: 0 4px 12px rgba(230, 81, 0, 0.2) !important;
    }

    .stWarning > div {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.1em !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .stWarning p {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Error messages - Maximum visibility */
    .stError {
        background-color: rgba(255, 235, 238, 0.99) !important;
        border: 4px solid #B71C1C !important;
        color: #000000 !important;
        box-shadow: 0 4px 12px rgba(183, 28, 28, 0.2) !important;
    }

    .stError > div {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.1em !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .stError p {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Info messages - Maximum visibility */
    .stInfo {
        background-color: rgba(232, 245, 255, 0.99) !important;
        border: 4px solid #0D47A1 !important;
        color: #000000 !important;
        box-shadow: 0 4px 12px rgba(13, 71, 161, 0.2) !important;
    }

    .stInfo > div {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.1em !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    .stInfo p {
        color: #000000 !important;
        font-weight: 800 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }
    
    /* Button responsif */
    .stButton > button {
        border-radius: 10px;
        font-weight: 700 !important;
        transition: all 0.3s ease;
        color: #FFFFFF !important;
        background-color: #2E7D32 !important;
        border: 2px solid #1B5E20 !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
        background-color: #1B5E20 !important;
    }
    
    /* Input responsif */
    .stTextInput > div > div > input {
        border-radius: 10px;
        color: #1B5E20 !important;
        font-weight: 600;
    }
    
    .stFileUploader, .stTextArea {
        border-radius: 10px;
    }
    
    /* Metric styling - Ultra maximum visibility */
    .stMetric {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(240, 248, 240, 0.98) 100%) !important;
        border: 3px solid #2E7D32 !important;
        border-radius: 12px !important;
        padding: 1.2em !important;
        color: #000000 !important;
        box-shadow: 0 4px 15px rgba(46, 125, 50, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }

    .stMetric > div > div > div > div {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.8em !important;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9) !important;
        letter-spacing: 0.5px !important;
    }

    /* Metric label */
    .stMetric label {
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 1.2em !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
        margin-bottom: 0.5em !important;
    }

    /* Metric delta */
    .stMetric > div > div > div > div:last-child {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 1.1em !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Metric container text */
    .stMetric > div > div {
        color: #000000 !important;
        font-weight: 700 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }
    
    /* Image responsif */
    img {
        max-width: 100%;
        height: auto;
        display: block;
    }
    
    /* Sidebar responsif */
    .stSidebar {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 50%, #A5D6A7 100%);
    }
    
    .stSidebar [data-testid="stMarkdownContainer"] {
        color: #1B5E20 !important;
        font-weight: 600 !important;
    }
    
    @media (max-width: 640px) {
        .stSidebar {
            width: 100% !important;
        }
    }
    
    /* Table styling - Maximum visibility */
    .stDataFrame {
        font-size: 0.95em !important;
        color: #000000 !important;
        background-color: rgba(255, 255, 255, 0.98) !important;
        border: 2px solid #4CAF50 !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
    }

    .stDataFrame table {
        color: #000000 !important;
        font-weight: 600 !important;
        border-collapse: collapse !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    .stDataFrame tbody tr {
        color: #000000 !important;
        font-weight: 600 !important;
        border-bottom: 1px solid rgba(76, 175, 80, 0.3) !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    .stDataFrame tbody tr:hover {
        background-color: rgba(76, 175, 80, 0.1) !important;
    }

    .stDataFrame thead th {
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 1.1em !important;
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.3) 0%, rgba(46, 125, 50, 0.3) 100%) !important;
        border-bottom: 2px solid #2E7D32 !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8) !important;
    }

    /* DataFrame cell content */
    .stDataFrame tbody td {
        color: #000000 !important;
        font-weight: 600 !important;
        padding: 0.75em !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }
    
    @media (max-width: 640px) {
        .stDataFrame {
            font-size: 0.8em;
        }
    }
    
    /* Column spacing responsif */
    .stColumns > * > .stColumn {
        padding: 0 0.5rem;
    }
    
    @media (max-width: 640px) {
        .stColumns > * > .stColumn {
            padding: 0.25rem;
        }
    }
    
    /* Spinner text - High visibility */
    .stSpinner {
        color: #000000 !important;
        font-weight: 700 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    .stSpinner > div > div > div {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 1.1em !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Progress bar styling */
    .stProgress > div > div {
        background-color: #4CAF50 !important;
        border-radius: 5px !important;
    }

    /* File uploader text */
    .stFileUploader > div > div > div > div {
        color: #000000 !important;
        font-weight: 700 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Selectbox text */
    .stSelectbox > div > div > div {
        color: #000000 !important;
        font-weight: 600 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Radio button text */
    .stRadio > div > label {
        color: #000000 !important;
        font-weight: 600 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Checkbox text */
    .stCheckbox > div > label {
        color: #000000 !important;
        font-weight: 600 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Number input text */
    .stNumberInput > div > div > input {
        color: #000000 !important;
        font-weight: 600 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Text input styling */
    .stTextInput > div > div > input {
        color: #000000 !important;
        font-weight: 600 !important;
        border: 2px solid #4CAF50 !important;
        border-radius: 5px !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.7) !important;
    }

    /* Text input focus */
    .stTextInput > div > div > input:focus {
        border-color: #2E7D32 !important;
        box-shadow: 0 0 5px rgba(46, 125, 50, 0.3) !important;
    }
    </style>
    """

def apply_responsive_theme():
    """Apply responsive theme ke aplikasi"""
    st.markdown(get_responsive_css(), unsafe_allow_html=True)

def get_responsive_layout():
    """Get responsive column layout berdasarkan screen size"""
    # Streamlit tidak bisa detect screen size di backend
    # Jadi kita return config untuk client-side atau gunakan fixed responsive
    return {
        "mobile": 1,      # Single column di mobile
        "tablet": 2,      # Dua column di tablet
        "desktop": 3      # Tiga column di desktop
    }

def responsive_columns(layout_config):
    """
    Membuat responsive columns
    layout_config = {
        "mobile": 1,
        "tablet": 2, 
        "desktop": 3
    }
    """
    # Streamlit columns default responsif di mobile, tapi kita bisa optimize dengan custom CSS
    # Untuk sekarang return columns untuk desktop, akan auto-collapse di mobile
    return layout_config.get("desktop", 1)

def add_footer():
    """Add responsive footer"""
    st.markdown("---")
    st.markdown("""
        <div class="info-box" style="text-align: center;">
        <h3>ℹ️ Tentang Sistem</h3>
        <p>Sistem ini menggunakan Deep Learning CNN untuk mendeteksi penyakit pada daun singkong dengan akurasi tinggi.</p>
        <p style="font-size: 0.9em; color: #1B5E20;">🔒 Data Aman | 💾 Otomatis Tersimpan | 🌐 Akses Mana saja</p>
        </div>
    """, unsafe_allow_html=True)

def responsive_hero(title, subtitle, emoji="🌿"):
    """Create responsive hero section"""
    st.markdown(f"""
        <div class="hero">
            <div class="hero-title">{emoji} {title}</div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
    """, unsafe_allow_html=True)

def responsive_button_grid(buttons_config, columns=None):
    """
    Create responsive button grid
    buttons_config = [
        {"label": "Button 1", "page": "page.py"},
        {"label": "Button 2", "page": "page.py"}
    ]
    """
    if columns is None:
        # Auto-detect based on button count
        if len(buttons_config) <= 2:
            columns = len(buttons_config)
        elif len(buttons_config) <= 4:
            columns = 2
        else:
            columns = 3
    
    cols = st.columns(columns)
    
    for idx, button_config in enumerate(buttons_config):
        with cols[idx % columns]:
            if st.button(button_config["label"], use_container_width=True):
                st.switch_page(button_config["page"])
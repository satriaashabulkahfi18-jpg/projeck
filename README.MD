# Cassava Disease Detection System 🌿

A comprehensive deep learning system for detecting cassava leaf diseases using computer vision and Streamlit web interface.

## Features

- 🔍 **Disease Detection**: Multi-class classification for 6 categories (5 diseases + healthy leaves + non-cassava detection)
- 🤖 **Deep Learning**: VGG16-based CNN model with high accuracy
- 👥 **User Management**: Role-based authentication (Admin/User)
- 📊 **Analytics Dashboard**: Admin panel for system monitoring
- 📱 **Responsive Design**: Mobile-friendly web interface
- 💾 **Persistent Storage**: SQLite database with Hugging Face Spaces compatibility
- 🔒 **Secure Authentication**: Password hashing and session management
- 🚫 **Non-Cassava Detection**: Explicit detection and rejection of non-cassava images
- 📋 **Object Detection Ready**: Framework prepared for future bounding box detection (Phase 2)

## Deployment on Hugging Face Spaces

### Prerequisites
- Hugging Face account
- GitHub repository
- Model files uploaded to Hugging Face Spaces storage

### Setup Steps

1. **Clone this repository to GitHub**
2. **Create Hugging Face Space**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Create new Space with Streamlit
   - Connect your GitHub repository

3. **Upload Model Files**
   - Upload your trained models to the Space's persistent storage
   - Models should be placed in the `model/` directory:
     - `model/vgg16_multitask.h5` (main model)
     - `model/vggnew_model.h5` (alternative model)

4. **Configure Secrets** (if needed)
   - Add any required secrets in Space settings

5. **Deploy**
   - The app will automatically initialize the database on first run
   - Models will be loaded from relative paths

### Database Setup
The application automatically creates the SQLite database (`cassava_users.db`) on first startup. The database includes:
- User authentication tables
- Analysis history tracking
- User profiles

### Model Loading
Models are loaded using relative paths for deployment compatibility:
```python
model_path = "model/vgg16_multitask.h5"
model = tf.keras.models.load_model(model_path)
```

## Local Development

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd cassava-disease-detection

# Install dependencies
pip install -r requirements.txt
```

### Running the App
```bash
streamlit run app.py
```

### Default Admin Account
- **Username**: admin
- **Password**: admin123
- **Role**: Administrator

## Project Structure

```
cassava-disease-detection/
├── app.py                      # Main application entry point
├── database.py                 # Database operations
├── auth.py                     # Authentication functions
├── login.py                    # Login page component
├── navigation.py               # Navigation sidebar
├── responsive_ui.py            # UI components and styling
├── disease_recommendations.py  # Disease treatment recommendations
├── cassava_leaf_characteristics.py  # Leaf analysis utilities
├── admin_setup.py              # Admin account setup utility
├── leaf_segmentation.py        # Leaf segmentation utilities
├── binary_classifier_cnn.ipynb # Binary classification notebook
├── analysis_history.json       # Analysis history storage
├── cassava_users.db            # SQLite database (auto-created)
├── pages/                      # Streamlit pages
│   ├── 01_📊_Dashboard_Admin.py
│   ├── 02_📁_Kelola_Training.py
│   ├── 03_🧪_Test_Model.py
│   ├── 04_🔍_Klasifikasi.py
│   ├── 05_📈_Riwayat_Klasifikasi.py
│   └── 06_⚙️_Pengaturan.py
├── model/                      # ML models (not in git)
│   ├── vgg16_multitask.h5
│   ├── vggnew_model.h5
│   └── metrics.json
├── streamlit/                  # Streamlit configuration
│   ├── config.toml
│   └── secrets.toml.example
├── models/                     # Additional models directory
├── dataset/                    # Training data (not in git)
├── requirements.txt            # Python dependencies
├── packages.txt               # System packages
├── README.MD                  # Project documentation
├── .gitignore                 # Git ignore rules
├── QUICK_START_AUTH.md         # Authentication quick start guide
├── NON_CASSAVA_DETECTION_GUIDE.md  # Non-cassava detection guide
├── OBJECT_DETECTION_GUIDE.md   # Object detection phase guide
└── .qodo/                     # Development tools
```

## Disease Categories

The system detects 6 categories:
1. 🌿 **Daun Sehat** (Healthy Leaf)
2. 🔴 **Bacterial Blight**
3. 🟤 **Brown Spot**
4. 🐜 **Green Mite**
5. 🟢 **Mosaic**
6. ❌ **Bukan Daun Singkong** (Non-Cassava) - Explicit detection and rejection

### Non-Cassava Detection
- **Purpose**: Prevents false positives by explicitly training on non-cassava images
- **Threshold**: Configurable rejection threshold (default: 25% confidence)
- **Training**: Model trained with 100+ non-cassava images for better discrimination

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **ML Framework**: TensorFlow/Keras
- **Database**: SQLite
- **Computer Vision**: OpenCV, PIL
- **Authentication**: Custom session-based with PBKDF2 hashing
- **Deployment**: Hugging Face Spaces
- **Development Tools**: Qodo for code quality

## Authentication System

The application includes a complete user authentication system with the following features:

### User Management
- **Sign Up**: New user registration with email validation
- **Login/Logout**: Secure session-based authentication
- **Role-based Access**: Admin and regular user roles
- **Password Security**: PBKDF2 hashing for secure password storage

### Database Integration
- **Persistent Storage**: SQLite database with automatic initialization
- **User Profiles**: Email, username, full name, role, and registration date
- **Analysis History**: Per-user classification history tracking

### Quick Start Authentication
See `QUICK_START_AUTH.md` for step-by-step authentication setup guide.

Default admin account:
- **Username**: admin
- **Password**: admin123
- **Role**: Administrator

## Advanced Features

### Non-Cassava Detection System
The system includes explicit training for non-cassava image detection to reduce false positives:

- **Training**: Model trained with 100+ non-cassava images
- **Threshold**: Configurable rejection threshold (default: 25%)
- **Accuracy**: Improved from ~80-85% to ~90-95% with 6-class classification

See `NON_CASSAVA_DETECTION_GUIDE.md` for detailed implementation guide.

### Object Detection (Phase 2 - Future)
Framework prepared for bounding box detection capabilities:

- **Use Cases**: Disease area localization, soil/stem/insect detection
- **Models**: YOLOv8, Faster R-CNN, RetinaNet support
- **Integration**: 3-task learning (classification + binary + detection)

See `OBJECT_DETECTION_GUIDE.md` for comprehensive phase 2 implementation guide.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the GitHub repository
- Check the documentation files:
  - `QUICK_START_AUTH.md` - Authentication setup
  - `NON_CASSAVA_DETECTION_GUIDE.md` - Non-cassava detection
  - `OBJECT_DETECTION_GUIDE.md` - Object detection guide
- Contact the maintainers

---

**Note**: Model files and datasets are not included in the repository due to size constraints. Upload them separately to your Hugging Face Space storage.
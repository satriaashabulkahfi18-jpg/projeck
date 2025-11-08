# database.py
import sqlite3
import os
from datetime import datetime
import hashlib
import secrets

DB_FILE = "cassava_users.db"

def get_connection():
    """Get database connection"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize database with tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            role TEXT DEFAULT 'user' CHECK(role IN ('admin', 'user')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP,
            is_google_auth BOOLEAN DEFAULT 0
        )
    ''')
    
    # User profiles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE,
            full_name TEXT,
            profile_picture_url TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Analysis history table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            image_filename TEXT,
            prediction TEXT,
            confidence REAL,
            analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            details TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash password with salt"""
    salt = secrets.token_hex(32)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode(), 100000)
    return pwd_hash.hex(), salt

def verify_password(stored_hash, stored_salt, provided_password):
    """Verify password"""
    pwd_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), stored_salt.encode(), 100000)
    return pwd_hash.hex() == stored_hash

def register_user(email, username, password, full_name="", role="user"):
    """Register a new user (user role only, admin by default)"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        pwd_hash, salt = hash_password(password)

        # Ensure role is valid
        if role not in ['admin', 'user']:
            role = 'user'

        cursor.execute('''
            INSERT INTO users (email, username, password_hash, salt, role)
            VALUES (?, ?, ?, ?, ?)
        ''', (email, username, pwd_hash, salt, role))

        user_id = cursor.lastrowid

        # Create user profile
        cursor.execute('''
            INSERT INTO user_profiles (user_id, full_name)
            VALUES (?, ?)
        ''', (user_id, full_name))

        conn.commit()
        conn.close()
        return True, "Akun berhasil dibuat! ✅"
    except sqlite3.IntegrityError:
        return False, "Username sudah terdaftar! ❌"
    except Exception as e:
        return False, f"Error: {str(e)}"

def login_user(username_or_email, password):
    """Login user with username or email and password"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Try to find user by username first, then by email
        cursor.execute('SELECT * FROM users WHERE username = ? OR email = ?', (username_or_email, username_or_email))
        user = cursor.fetchone()

        if user and verify_password(user['password_hash'], user['salt'], password):
            # Update last login
            cursor.execute('UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?', (user['id'],))
            conn.commit()
            conn.close()
            return True, user['id'], user['username'], user['role']
        else:
            conn.close()
            return False, None, None, "Username/email atau password salah! ❌"
    except Exception as e:
        return False, None, None, f"Error: {str(e)}"

def login_or_register_google(email, name):
    """Login or register user via Google OAuth"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        
        if user:
            # Update last login
            cursor.execute('UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?', (user['id'],))
            conn.commit()
        else:
            # Create new user from Google OAuth (always user role)
            username = email.split('@')[0]
            cursor.execute('''
                INSERT INTO users (email, username, password_hash, salt, is_google_auth, role)
                VALUES (?, ?, ?, ?, 1, ?)
            ''', (email, username, 'google_oauth', 'google_oauth', 'user'))
            
            user_id = cursor.lastrowid
            
            # Create user profile
            cursor.execute('''
                INSERT INTO user_profiles (user_id, full_name)
                VALUES (?, ?)
            ''', (user_id, name))
            
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
        
        conn.commit()
        conn.close()
        return True, user['id'], user['username'], user['email'], user['role']
    except Exception as e:
        return False, None, None, None, f"Error: {str(e)}"

def get_user_profile(user_id):
    """Get user profile"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT u.*, p.full_name, p.profile_picture_url
            FROM users u
            LEFT JOIN user_profiles p ON u.id = p.user_id
            WHERE u.id = ?
        ''', (user_id,))
        
        profile = cursor.fetchone()
        conn.close()
        return dict(profile) if profile else None
    except Exception as e:
        return None

def save_analysis(user_id, image_filename, prediction, confidence, details=""):
    """Save analysis to history"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO analysis_history (user_id, image_filename, prediction, confidence, details)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, image_filename, prediction, confidence, details))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def get_user_history(user_id, limit=10):
    """Get user's analysis history"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM analysis_history 
            WHERE user_id = ? 
            ORDER BY analysis_date DESC 
            LIMIT ?
        ''', (user_id, limit))
        
        history = cursor.fetchall()
        conn.close()
        return [dict(row) for row in history]
    except Exception as e:
        return []

def email_exists(email):
    """Check if email already exists"""
    if not email:  # Allow null emails for username-only login
        return False
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists
    except:
        return False

def username_exists(username):
    """Check if username already exists"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists
    except:
        return False

def get_user_role(user_id):
    """Get user role"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT role FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result['role'] if result else 'user'
    except:
        return 'user'

def get_all_users(role_filter=None):
    """Get all users, optionally filtered by role"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        if role_filter:
            cursor.execute('SELECT id, email, username, role, created_at FROM users WHERE role = ? ORDER BY created_at DESC', (role_filter,))
        else:
            cursor.execute('SELECT id, email, username, role, created_at FROM users ORDER BY created_at DESC')
        
        users = cursor.fetchall()
        conn.close()
        return [dict(user) for user in users]
    except:
        return []

def update_user_role(user_id, new_role):
    """Update user role (admin only)"""
    try:
        if new_role not in ['admin', 'user']:
            return False
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET role = ? WHERE id = ?', (new_role, user_id))
        conn.commit()
        conn.close()
        return True
    except:
        return False

def get_statistics():
    """Get system statistics"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Total users
        cursor.execute('SELECT COUNT(*) as count FROM users')
        total_users = cursor.fetchone()['count']
        
        # Admin count
        cursor.execute("SELECT COUNT(*) as count FROM users WHERE role = 'admin'")
        admin_count = cursor.fetchone()['count']
        
        # User count
        cursor.execute("SELECT COUNT(*) as count FROM users WHERE role = 'user'")
        user_count = cursor.fetchone()['count']
        
        # Total classifications
        cursor.execute('SELECT COUNT(*) as count FROM analysis_history')
        total_classifications = cursor.fetchone()['count']
        
        conn.close()
        
        return {
            'total_users': total_users,
            'admin_count': admin_count,
            'user_count': user_count,
            'total_classifications': total_classifications
        }
    except:
        return {
            'total_users': 0,
            'admin_count': 0,
            'user_count': 0,
            'total_classifications': 0
        }

def get_recent_activities(limit=20):
    """Get recent classification activities"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT
                ah.id,
                u.username,
                u.email,
                ah.prediction,
                ah.confidence,
                ah.analysis_date,
                ah.image_filename
            FROM analysis_history ah
            JOIN users u ON ah.user_id = u.id
            ORDER BY ah.analysis_date DESC
            LIMIT ?
        ''', (limit,))

        activities = cursor.fetchall()
        conn.close()
        return [dict(activity) for activity in activities]
    except:
        return []

def update_user_password(user_id, current_password, new_password):
    """Update user password with current password verification"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # First, verify current password
        cursor.execute('SELECT password_hash, salt FROM users WHERE id = ?', (user_id,))
        user_data = cursor.fetchone()

        if not user_data:
            conn.close()
            return False, "User tidak ditemukan! ❌"

        if not verify_password(user_data['password_hash'], user_data['salt'], current_password):
            conn.close()
            return False, "Password saat ini salah! ❌"

        # If current password is correct, update to new password
        pwd_hash, salt = hash_password(new_password)

        cursor.execute('''
            UPDATE users
            SET password_hash = ?, salt = ?
            WHERE id = ?
        ''', (pwd_hash, salt, user_id))

        conn.commit()
        conn.close()
        return True, "Password berhasil diubah! ✅"
    except Exception as e:
        return False, f"Error updating password: {str(e)}"

def update_user_profile(user_id, full_name=None, username=None):
    """Update user profile information"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Update username in users table if provided
        if username:
            cursor.execute('UPDATE users SET username = ? WHERE id = ?', (username, user_id))

        # Update full_name in user_profiles table if provided
        if full_name is not None:
            cursor.execute('''
                UPDATE user_profiles
                SET full_name = ?
                WHERE user_id = ?
            ''', (full_name, user_id))

        conn.commit()
        conn.close()
        return True, "Profil berhasil diubah! ✅"
    except sqlite3.IntegrityError:
        return False, "Username sudah digunakan! ❌"
    except Exception as e:
        return False, f"Error updating profile: {str(e)}"

# Initialize database on import
init_database()
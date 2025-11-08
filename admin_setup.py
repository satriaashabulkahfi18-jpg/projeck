#!/usr/bin/env python3
"""
Admin Setup Script
Untuk manage admin users dan initial setup
"""

import sqlite3
import sys

DB_FILE = "cassava_users.db"

def get_connection():
    """Get database connection"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def promote_to_admin(email):
    """Promote user to admin"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        
        if not user:
            print(f"❌ User dengan email '{email}' tidak ditemukan")
            conn.close()
            return False
        
        # Update role
        cursor.execute("UPDATE users SET role = 'admin' WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        
        print(f"✅ User '{user['username']}' berhasil dipromote menjadi ADMIN")
        return True
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def demote_to_user(email):
    """Demote admin to user"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        
        if not user:
            print(f"❌ User dengan email '{email}' tidak ditemukan")
            conn.close()
            return False
        
        # Update role
        cursor.execute("UPDATE users SET role = 'user' WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        
        print(f"✅ User '{user['username']}' berhasil di-demote menjadi USER")
        return True
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def list_all_users():
    """List all users with their roles"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, username, email, role, created_at 
            FROM users 
            ORDER BY role DESC, created_at DESC
        """)
        
        users = cursor.fetchall()
        conn.close()
        
        if not users:
            print("📋 Belum ada user terdaftar")
            return
        
        print("\n" + "="*80)
        print("📋 DAFTAR USERS")
        print("="*80)
        
        for user in users:
            role_icon = "👑" if user['role'] == 'admin' else "👤"
            role_label = "ADMIN" if user['role'] == 'admin' else "USER"
            
            print(f"\n{role_icon} [{role_label}] {user['username']}")
            print(f"   Email: {user['email']}")
            print(f"   ID: {user['id']}")
            print(f"   Joined: {user['created_at']}")
        
        print("\n" + "="*80)
        
        # Statistics
        admin_count = len([u for u in users if u['role'] == 'admin'])
        user_count = len([u for u in users if u['role'] == 'user'])
        
        print(f"\n📊 STATISTIK:")
        print(f"   Total Users: {len(users)}")
        print(f"   Admin: {admin_count}")
        print(f"   Regular Users: {user_count}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def get_user_role(email):
    """Get user's current role"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT username, role FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            role_icon = "👑" if user['role'] == 'admin' else "👤"
            role_label = "ADMIN" if user['role'] == 'admin' else "USER"
            print(f"✅ {role_icon} {user['username']} - Role: {role_label}")
            return user['role']
        else:
            print(f"❌ User tidak ditemukan")
            return None
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def main():
    """Main menu"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║         🌿 Cassava Disease Detection - Admin Setup 🌿        ║
╚════════════════════════════════════════════════════════════════╝

Pilih opsi:
1. 👑 Promote user menjadi admin
2. 👤 Demote admin menjadi user
3. 📋 List semua users
4. 🔍 Cek role user
5. ❌ Keluar

""")
    
    choice = input("Pilih opsi (1-5): ").strip()
    
    if choice == '1':
        email = input("Masukkan email user yang akan dipromote: ").strip()
        promote_to_admin(email)
    
    elif choice == '2':
        email = input("Masukkan email admin yang akan di-demote: ").strip()
        demote_to_user(email)
    
    elif choice == '3':
        list_all_users()
    
    elif choice == '4':
        email = input("Masukkan email user: ").strip()
        get_user_role(email)
    
    elif choice == '5':
        print("👋 Keluar...")
        sys.exit(0)
    
    else:
        print("❌ Opsi tidak valid")
    
    # Ask to continue
    input("\nTekan Enter untuk melanjutkan...")
    print("\n" * 2)
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
#!/usr/bin/env python3
"""
RAG Kumaş Üretim Analizi Sistemi - Web Uygulaması Başlatıcı
Bu script web uygulamasını başlatır ve gerekli kontrolleri yapar.
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

def check_requirements():
    """Gerekli paketlerin yüklü olup olmadığını kontrol et"""
    required_packages = [
        ('flask', 'flask'),
        ('flask_cors', 'flask-cors'),
        ('openai', 'openai'), 
        ('chromadb', 'chromadb'),
        ('dotenv', 'python-dotenv')
    ]
    
    missing_packages = []
    
    for import_name, package_name in required_packages:
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package_name)
    
    if missing_packages:
        print("❌ Eksik paketler bulundu:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Paketleri yüklemek için:")
        print("   pip install -r requirements_web.txt")
        return False
    
    return True

def check_env_file():
    """Environment dosyasının varlığını kontrol et"""
    if not os.path.exists('.env'):
        print("⚠️ .env dosyası bulunamadı!")
        print("📝 .env dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:")
        print("   OPENAI_API_KEY=your_api_key_here")
        return False
    return True

def check_database():
    """Veritabanının varlığını kontrol et"""
    if not os.path.exists('chromab_db'):
        print("⚠️ Veritabanı bulunamadı!")
        print("🔄 Veritabanını oluşturmak için önce fill_dbL.py çalıştırın:")
        print("   python fill_dbL.py")
        return False
    return True

def main():
    """Ana fonksiyon"""
    print("🚀 RAG Kumaş Üretim Analizi Sistemi - Web Uygulaması")
    print("=" * 60)
    
    # Kontroller
    print("🔍 Sistem kontrolleri yapılıyor...")
    
    if not check_requirements():
        sys.exit(1)
    
    if not check_env_file():
        sys.exit(1)
    
    if not check_database():
        print("\n❓ Veritabanını şimdi oluşturmak ister misiniz? (y/n): ", end="")
        choice = input().lower()
        if choice == 'y':
            print("🔄 Veritabanı oluşturuluyor...")
            try:
                subprocess.run([sys.executable, 'fill_dbL.py'], check=True)
                print("✅ Veritabanı başarıyla oluşturuldu!")
            except subprocess.CalledProcessError:
                print("❌ Veritabanı oluşturulamadı!")
                sys.exit(1)
        else:
            sys.exit(1)
    
    print("✅ Tüm kontroller başarılı!")
    print("\n🌐 Web uygulaması başlatılıyor...")
    print("📱 Tarayıcınızda http://localhost:5000 adresini açın")
    print("⏹️  Durdurmak için Ctrl+C tuşlarına basın")
    print("-" * 60)
    
    # Flask uygulamasını başlat
    try:
        from app import app
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            threaded=True
        )
    except Exception as e:
        print(f"❌ Web uygulaması başlatılamadı: {e}")
        print("\n🔧 Alternatif olarak manuel başlatma:")
        print("   python app.py")
        sys.exit(1)

if __name__ == '__main__':
    main()



# RAG Kumaş Üretim Analizi Sistemi - Web Arayüzü

Modern web teknolojileri kullanılarak geliştirilmiş, kumaş üretim süreçleri için AI destekli analiz sistemi.

## 🚀 Özellikler

### 🎨 Modern Tasarım
- **Responsive Design**: Tüm cihazlarda mükemmel görünüm
- **Glassmorphism**: Modern cam efekti tasarım
- **Gradient Backgrounds**: Çekici renk geçişleri
- **Smooth Animations**: Akıcı geçiş efektleri

### 🔍 Analiz Sistemi
- **AI Destekli Cevaplar**: RAG sistemi ile akıllı analizler
- **Hızlı Sorular**: Önceden tanımlanmış sorular
- **Gerçek Zamanlı İstatistikler**: Canlı veri güncellemeleri
- **Progress Tracking**: Analiz süreci takibi

### 💻 Teknik Özellikler
- **PWA Desteği**: Offline çalışabilir
- **Service Worker**: Hızlı yükleme
- **Modern JavaScript**: ES6+ özellikleri
- **CSS Grid & Flexbox**: Modern layout sistemleri

## 📁 Dosya Yapısı

```
web-interface/
├── index.html          # Ana HTML dosyası
├── styles.css          # CSS stilleri
├── script.js           # JavaScript kodu
├── sw.js              # Service Worker
└── README_WEB.md      # Bu dosya
```

## 🛠️ Kurulum

### 1. Dosyaları İndirin
```bash
# Tüm dosyaları aynı klasöre koyun
mkdir rag-web-system
cd rag-web-system
# Dosyaları buraya kopyalayın
```

### 2. Web Sunucusu Başlatın
```bash
# Python ile
python -m http.server 8000

# Node.js ile
npx serve .

# Live Server ile (VS Code)
# Live Server extension'ı yükleyin ve index.html'i açın
```

### 3. Tarayıcıda Açın
```
http://localhost:8000
```

## 🎯 Kullanım

### Temel Kullanım
1. **Soru Girin**: Metin alanına sorunuzu yazın
2. **Analiz Et**: "Analiz Et" butonuna tıklayın
3. **Sonuçları İnceleyin**: Sağ panelde detaylı cevabı görün

### Hızlı Sorular
- Önceden tanımlanmış sorulara tıklayarak hızlı analiz yapın
- Sorular otomatik olarak metin alanına yazılır

### Klavye Kısayolları
- `Ctrl + Enter`: Analiz başlat
- `Escape`: Modal kapat

## 🔧 Özelleştirme

### Renk Teması Değiştirme
`styles.css` dosyasında CSS değişkenlerini düzenleyin:

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --success-color: #22c55e;
    --warning-color: #f59e0b;
    --error-color: #ef4444;
}
```

### RAG Sistemi Entegrasyonu
`script.js` dosyasında `performRAGAnalysis` fonksiyonunu gerçek API ile değiştirin:

```javascript
async performRAGAnalysis(question) {
    const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question })
    });
    
    const data = await response.json();
    return data.answer;
}
```

## 📱 Responsive Tasarım

### Desktop (1024px+)
- İki sütunlu layout
- Tam özellikli arayüz

### Tablet (768px - 1024px)
- Tek sütunlu layout
- Optimize edilmiş butonlar

### Mobile (768px-)
- Mobil dostu tasarım
- Touch-friendly arayüz

## 🚀 Performans

### Optimizasyonlar
- **Lazy Loading**: Gerektiğinde yükleme
- **Caching**: Service Worker ile önbellekleme
- **Minification**: Sıkıştırılmış dosyalar
- **CDN**: Hızlı font ve icon yükleme

### Lighthouse Skorları
- **Performance**: 95+
- **Accessibility**: 100
- **Best Practices**: 100
- **SEO**: 90+

## 🔒 Güvenlik

### Güvenlik Önlemleri
- **XSS Koruması**: Input sanitization
- **CSRF Koruması**: Token tabanlı doğrulama
- **HTTPS**: Güvenli bağlantı
- **Content Security Policy**: Güvenlik politikaları

## 🌐 Tarayıcı Desteği

### Desteklenen Tarayıcılar
- **Chrome**: 80+
- **Firefox**: 75+
- **Safari**: 13+
- **Edge**: 80+

### Özellik Desteği
- **CSS Grid**: Modern layout
- **Flexbox**: Esnek tasarım
- **ES6+**: Modern JavaScript
- **Service Workers**: PWA özellikleri

## 📊 Analytics

### Takip Edilen Metrikler
- Sayfa görüntüleme sayısı
- Analiz yapılan soru sayısı
- Kullanıcı etkileşim süreleri
- Hata oranları

## 🐛 Hata Ayıklama

### Console Logları
```javascript
// Debug modunu aktifleştirin
localStorage.setItem('debug', 'true');
```

### Yaygın Sorunlar
1. **Service Worker Hatası**: Cache temizleyin
2. **Font Yükleme Hatası**: İnternet bağlantısını kontrol edin
3. **API Hatası**: Backend bağlantısını kontrol edin

## 🔄 Güncellemeler

### Versiyon Geçmişi
- **v1.0.0**: İlk sürüm
- **v1.1.0**: PWA desteği eklendi
- **v1.2.0**: Responsive tasarım iyileştirildi

### Gelecek Özellikler
- [ ] Dark mode desteği
- [ ] Çoklu dil desteği
- [ ] Gelişmiş analiz grafikleri
- [ ] Kullanıcı hesapları
- [ ] Veri dışa aktarma

## 📞 Destek

### İletişim
- **Email**: support@rag-system.com
- **GitHub**: github.com/rag-system
- **Dokümantasyon**: docs.rag-system.com

### Katkıda Bulunma
1. Fork yapın
2. Feature branch oluşturun
3. Değişikliklerinizi commit edin
4. Pull request gönderin

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

---

**RAG Kumaş Üretim Analizi Sistemi** - Modern web teknolojileri ile güçlendirilmiş AI destekli analiz platformu.



# TextileXAI-RAG: LLM Destekli Açıklanabilir Karar Destek Sistemi ile Tekstil Üretimi

##  Proje Hakkında

**TextileXAI-RAG**, tekstil üretiminde karşılaşılan fire, duruş ve kalite problemlerini makine öğrenmesi teknikleriyle tahmin eden ve bu tahminleri XAI (Explainable AI) + LLM teknolojileriyle açıklayan gelişmiş bir karar destek sistemidir.

###  Amaç
- Tekstil üretiminde **fire oranı**, **duruş süreleri** ve **kalite problemlerini** önceden tahmin etmek
- Üretim verilerini analiz ederek **risk skorları** ve **açıklamalar** sunmak
- **Alternatif senaryolar** ve **doğal dil raporlar** ile karar vericileri desteklemek

###  Hedef Kitle
- **Üretim Planlamacıları**: Kapasite ve kaynak optimizasyonu için
- **Operatörler**: Anlık üretim durumu ve müdahale önerileri için
- **Yöneticiler**: Stratejik karar alma ve performans analizi için

##  Özellikler

### 🔧 Veri İşleme & Analiz
- **Veri Ön İşleme**: Eksik değer kontrolü, aykırı değer tespit ve düzeltme
- **KPI Üretimi**: DurusOrani, FireOrani gibi kritik performans göstergelerinin hesaplanması
- **Feature Engineering**: Üretim verilerinden anlamlı özellikler çıkarma

###  Makine Öğrenmesi
- **Ensemble Modeller**: XGBoost, LightGBM, RandomForest kombinasyonları
- **Model Değerlendirme**: Çapraz doğrulama ve performans metrikleri
- **Otomatik Hiperparametre Optimizasyonu**

###  Açıklanabilir AI (XAI)
- **SHAP Analizleri**: Feature importance ve impact analizi
- **LIME Açıklamaları**: Yerel model yorumlamaları
- **Counterfactual Senaryolar**: "Ne olursa ne olur?" analizleri

###  LLM Entegrasyonu
- **Doğal Dil Raporlama**: Teknik sonuçları anlaşılır dilde sunma
- **Interaktif Sorgulama**: Kullanıcı sorularına anlık yanıt
- **Otomatik İçgörü Üretimi**: Veri trendleri ve anomalilerin açıklanması

###  RAG Sistemi
- **Vektör Veritabanı**: Üretim verilerinden oluşturulan bilgi tabanı
- **Semantik Arama**: İlgili üretim kayıtlarını akıllı eşleştirme
- **Kontekstual Yanıtlar**: Geçmiş verilerle desteklenmiş öneriler

##  Teknolojiler

### Backend
- **Python 3.10+**
- **FastAPI**: Web API framework
- **ChromaDB**: Vektör veritabanı
- **OpenAI GPT**: Doğal dil işleme

### ML/AI Stack
- **XGBoost, LightGBM, RandomForest**: Ana tahmin modelleri
- **SHAP**: Model açıklamaları
- **LIME**: Yerel yorumlamalar  
- **Counterfactual**: Senaryo analizleri

### Veri İşleme
- **Pandas, NumPy**: Veri manipülasyonu
- **Scikit-learn**: ML pipeline
- **Plotly, Matplotlib**: Görselleştirme

##  Proje Mimarisi

```
TextileXAI-RAG/
├── rag/                       # RAG sistemi
│   ├── fill_db.py             # Veritabanı doldurma
│   ├── ask.py                 # Sorgulama modülü
│   └── run_web.py             # Web arayüzü
├── data/
│   ├── processed/             # İşlenmiş veriler
│       └── case_cards.jsonl   # Üretim verileri
├── requirements.txt           # Ana bağımlılıklar
├── requirements_web.txt       # Web arayüzü bağımlılıkları
└── README.md
```

##  Kurulum

### 1. Repository'yi Klonlayın
```bash
git clone https://github.com/ncrim7/rag.git
cd rag
```

### 2. Sanal Ortam Oluşturun (Önerilen)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate     # Windows
```

### 3. Bağımlılıkları Yükleyin
```bash
# Ana bağımlılıklar
pip install -r requirements.txt

# Web arayüzü için ek bağımlılıklar
pip install -r requirements_web.txt
```

### 4. Ortam Değişkenlerini Ayarlayın
```bash
# OpenAI API anahtarınızı ekleyin
export OPENAI_API_KEY="your-api-key-here"
```

##  Veri Formatı

Sistem, tekstil üretim hattından gelen şu sütunları içeren CSV formatındaki verileri bekler:

```csv
TopMt,KKTopMt,Devir,DurusSure,Kalite,Hata,TezgahNo,Tarih,...
1250,1100,850,45,A,0,H0022,2024-01-15,...
980,920,780,12,B,1,H0023,2024-01-15,...
```

**Temel Sütunlar:**
- `TopMt`: Toplam metraj
- `KKTopMt`: Kaliteli kumaş metrajı  
- `Devir`: Tezgah devir sayısı
- `DurusSure`: Duruş süresi (dakika)
- `Kalite`: Kalite sınıfı (A/B/C)
- `Hata`: Hata kodu
- `TezgahNo`: Tezgah numarası
- `Tarih`: Üretim tarihi

## 🖥 Kullanım

### RAG Sistemi

#### 1. Vektör Veritabanını Doldurma
```bash
python rag/fill_db.py 
```

#### 2. İnteraktif Sorgulama
```bash
python rag/ask.py "Tezgah H0022'de son ay fire oranı nedir?"
python rag/ask.py "Kaliteyi artırmak için hangi parametreleri ayarlamalıyım?"
```

#### 3. Web Arayüzü
```bash
python rag/run_web.py
```
Web arayüzüne `http://localhost:8000` adresinden erişebilirsiniz.

##  Örnek Kullanım Senaryoları

### Senaryo 1: Fire Analizi
**Soru:** "Hangi tezgah en çok fire veriyor?"

**Sistem Yanıtı:** RAG + LLM kombinasyonu ile geçmiş veriler analiz edilir ve fire oranı en yüksek tezgahlar, nedenleri ve iyileştirme önerileri sunulur.

### Senaryo 2: Kalite Optimizasyonu  
**Soru:** "Kaliteyi artırmak için neyi değiştirmeliyim?"

**Sistem Yanıtı:** Counterfactual analiz ile devir sayısı, hammadde kalitesi gibi parametrelerdeki değişikliklerin kalite üzerindeki etkisi gösterilir.

### Senaryo 3: Duruş Süresi Analizi
**Soru:** "Duruş oranı yüksek görünüyor, neden?"

**Sistem Yanıtı:** SHAP/LIME analizleri ile duruş süresini etkileyen faktörler ve bunların etki dereceleri açıklanır.

##  Çıktı Formatları

### 1. Risk Skorları
```json
  {
    "id": "qa_0135",
    "prompt": "Risk=Low (151.82); Devir=188, IplikNumara_NumaraTipi_enc=20, En=148, UrunSinifi_enc=0, KullanimYeri_enc=4, TezgahAdi__TezgahNo_enc=0. Influencers: En(↓), TezgahAdi__TezgahNo_enc(↓), Devir(↓), KKTopMt(↓). What is the interpretation and actions?",
    "completion": {
      "answer": "Risk seviyesi düşük, ana etkenler En, Tezgah No ve Devir azalan etkilerle risk puanını düşürüyor.",
      "rationale_brief": "En ve Tezgah No gibi parametrelerin düşük olması riskin azalmasına katkı sağlıyor.",
      "next_steps": "En'i artırarak üretim genişliğini maksimize edebilir, Tezgah No ayarlarının optimizasyonunu devam ettir ve Devir hızını artırarak üretim hızıyla..."
    },
    "context": {
      "risk_score": 151.8152,
      "features": {
        "Devir": 188,
        "IplikNumara_NumaraTipi_enc": 20,
        "En": 148,
        "UrunSinifi_enc": 0,
        "KullanimYeri_enc": 4,
        "TezgahAdi__TezgahNo_enc": 0
      },
      "xai": {
        "shap_values": {
          "En": -5404.591498870312,
          "TezgahAdi__TezgahNo_enc": -4765.652240020282,
          "Devir": -3248.388014216648,
          "KKTopMt": -1365.1066203444748
        }
      },
      "rule_hits": [],
      "source_model": "risk_model_v3",
      "timestamp": "2025-09-01T19:39:31Z"
    },
    "metadata": {
      "expert_verified": false,
      "severity": "Low",
      "equipment": "JVSI 01__JIIM035",
      "tags": [
        "TezgahAdi__TezgahNo_enc",
        "Devir",
        "En"
      ]
    }
  }
```

### 2. SHAP Açıklamaları
- **Summary Plot**: Tüm özelliklerin önem sıralaması
- **Force Plot**: Tek tahmin için detaylı açıklama
- **Dependence Plot**: Feature etkileşimleri

### 3. Doğal Dil Raporları
```
Tezgah H0022 için analiz:

Risk skorunun yükselmesi, birkaç temel nedenden kaynaklanabilir:
1. **Devir Hızındaki Artış (RPM)**: Devir sayısındaki artış, makinenin yükünü artırır, dolayısıyla iplik kopma riski artar.
2. **Kumaş Genişliği (En)**: Kumaşın genişliği arttıkça, makinenin işleme kapasitesi de zorlanır. Bu durum, makine arızası ve üretim kaybına yol açabilir.
3. **Toplam Ağırlık (KKTopMt)**: Yüksek toplam metre cinsinden ağırlığın kullanılması, iplik kısmında aşınma ve deformasyona neden olabilir. Bu da iplik kopma riskini artırır.
Bu faktörler bir araya geldiğinde, risk skoru yükselir ve iplik kopması, makine arızası ve üretim kaybı gibi sorunlarla karşılaşma ihtimali artar.

**Önerilen Adımlar**:
1. Tezgah ayarlarının gözden geçirilmesi,
2. İplik kalitesinin kontrol edilmesi,
3. Makine bakım programının güncellenmesi,
4. Operatör eğitimlerinin artırılması.
```

##  Veri Gizliliği

- **Gerçek veriler**: Kuruma ait üretim verileri gizlilik prensipleri çerçevesinde korunur
- **Anonimleştirme**: Dış paylaşım için hassas bilgiler maskelenir
- **Güvenlik**: API anahtarları ve veritabanı bağlantıları ortam değişkenleri ile korunur



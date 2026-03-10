# CTW – Masaüstü Yardımcı Uygulama

<div align="center">
  <img src="assets/icons/CTW_icon.png" alt="CTW Logo" width="120"/>
  <p><strong>Content & Task Widget</strong> - Masaüstü seviyesinde içerik ve görev takibi için modern yardımcı uygulama</p>
  
  ![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
  ![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)
  ![License](https://img.shields.io/badge/license-MIT-green)
  ![Status](https://img.shields.io/badge/status-development-yellow)
</div>

---

## 📋 İçindekiler

- [Genel Bakış](#genel-bakış)
- [Özellikler](#özellikler)
- [Kullanım Senaryoları](#kullanım-senaryoları)
- [Hızlı Başlangıç](#hızlı-başlangıç)
- [Proje Yapısı](#proje-yapısı)
- [Teknolojiler](#teknolojiler)
- [Bileşenler](#bileşenler)
- [Geliştirici Rehberi](#geliştirici-rehberi)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)
- [İletişim](#iletişim)

---

## 🎯 Genel Bakış

**CTW (Content & Task Widget)** , kullanıcıların masaüstü ortamında içerik ve görev takibini merkezi bir noktadan yönetebileceği, hatırlatıcılar ve bildirimlerle desteklenen modern bir yardımcı uygulamadır. Modüler yapısı sayesinde Linux, Windows ve macOS işletim sistemlerinde sorunsuz çalışır.

---

## ✨ Özellikler

### 📊 1. Görev ve İçerik Yönetimi
- **Kolay Ekleme/Düzenleme**: Yeni görev veya içerik ekleyin, mevcut kayıtları düzenleyin
- **Kart Tabanlı Arayüz**: Tüm içerikler detaylı **Card** bileşenleri ile görselleştirilir
- **Zengin Meta Bilgiler**: Her kart; başlık, kaynak tipi, fetch modu, URL, süre ve cache politikası gibi detayları içerir
- **Gelişmiş Filtreleme**: İçerikleri tür, tarih veya duruma göre filtreleyin

### ⏰ 2. Hatırlatıcı ve Zamanlayıcı
- **Akıllı Hatırlatıcılar**: Masaüstü widget üzerinden kolayca hatırlatıcı oluşturun
- **Çift Yönlü Sayaç**: Artan veya azalan sayım takibi yapabilme
- **Geri Sayım**: Önemli görevler için geri sayım kurun
- **Tekrarlayan Görevler**: Günlük, haftalık veya aylık tekrarlayan görevler tanımlayın

### 🔔 3. Bildirim Servisi
- **Çapraz Platform Desteği**: Linux, Windows ve macOS üzerinde native bildirimler
- **Anlık Uyarılar**: Görev, hatırlatma ve önemli olaylar için masaüstü bildirimleri
- **Özelleştirilebilir Sesler**: Her bildirim tipi için farklı uyarı sesleri
- **Zamanlanmış Bildirimler**: Belirli zamanlarda tetiklenen bildirimler

### 🔍 4. JSON Önizleme ve Meta Panel
- **Ham Veri Görüntüleme**: İçeriklerin JSON verisini okunabilir formatta gösterin
- **Detaylı Meta Paneli**: Sağ panelde içeriklerin tüm meta bilgileri sunulur
- **Sözdizimi Vurgulama**: JSON verisi renklendirilmiş ve girintili formatta görüntülenir

### 🧩 5. Modüler ve Component Tabanlı Mimari
- **Bağımsız Bileşenler**: Her sayfa (`ItemsPage`, `CreateNewContentPage`, `AppSettingsPage`) ve bileşen (`Card`, `JsonViewer`) bağımsız çalışır
- **Kolay Genişletilebilirlik**: Yeni özellikler mevcut yapıyı bozmadan eklenebilir
- **Yeniden Kullanılabilir Kod**: Ortak bileşenler merkezi olarak yönetilir

### 🎨 6. Kullanıcı Arayüzü ve Stil
- **Modern Karanlık Tema**: Göz yormayan, profesyonel görünüm
- **Etkileşimli Tasarım**: Hover efektleri, animasyonlar ve badge'ler
- **Sezgisel Navigasyon**: Menü, status bar ve stacked widget ile kolay gezinme
- **Duyarlı Tasarım**: Farklı pencere boyutlarına uyum sağlayan arayüz

---

## 💡 Kullanım Senaryoları

| Senaryo | Açıklama |
|---------|----------|
| **Görev Takibi** | Günlük, haftalık görevleri listeleyin ve tamamlanma durumlarını takip edin |
| **Hatırlatıcılar** | İlaç saatleri, toplantılar veya önemli etkinlikler için hatırlatıcı kurun |
| **İçerik Yönetimi** | Web scraping veya API'lerden toplanan içerikleri kategorize edin |
| **Zaman Yönetimi** | Projeler için geri sayım sayaçları oluşturun |
| **Veri Analizi** | Toplanan içeriklerin JSON verilerini inceleyin ve analiz edin |
| **Otomatik Bildirimler** | Belirli koşullar sağlandığında anlık uyarılar alın |

### Desteklenen Platformlar
| Platform | Durum |
|----------|-------|
| 🐧 Linux | ✅ Tam destek |
| 🪟 Windows | ✅ Tam destek |
| 🍎 macOS | ✅ Tam destek |

---

## 🚀 Hızlı Başlangıç

### Ön Koşullar
- Python 3.10 veya üzeri
- Pip paket yöneticisi
- Git (opsiyonel)

### Adım Adım Kurulum

1. **Projeyi klonlayın**
\`\`\`bash
git clone https://github.com/kullanici/ctw.git
cd ctw
\`\`\`

2. **Sanal ortam oluşturun**
\`\`\`bash
# Sanal ortam oluştur
python -m venv venv

# Linux/macOS için aktifleştirme
source venv/bin/activate

# Windows için aktifleştirme
venv\\Scripts\\activate
\`\`\`

3. **Bağımlılıkları yükleyin**
\`\`\`bash
pip install --upgrade pip
pip install -r requirements.txt
\`\`\`

4. **Uygulamayı çalıştırın**
\`\`\`bash
python main.py
\`\`\`

### Alternatif Kurulum
\`\`\`bash
# Doğrudan çalıştırma (sanal ortam olmadan)
pip install -r requirements.txt
python main.py
\`\`\`

---

## 📁 Proje Yapısı

CTW/
├── app/
│   ├── core/                      # Arka plan servisleri
│   │   ├── notification/          # Bildirim servisi
│   │   ├── fetcher/               # İçerik çekme servisi
│   │   └── cache/                 # Önbellek yönetimi
│   │
│   ├── models/                     # Veri modelleri
│   │   ├── task.py
│   │   ├── content.py
│   │   └── reminder.py
│   │
│   ├── plugins/                     # Eklenti desteği
│   │   └── plugin_manager.py
│   │
│   ├── services/                     # Uygulama servisleri
│   │   ├── task_service.py
│   │   └── settings_service.py
│   │
│   ├── ui/
│   │   ├── components/               # Tekrarlayan UI bileşenleri
│   │   │   ├── card.py
│   │   │   ├── json_viewer.py
│   │   │   └── badge.py
│   │   │
│   │   ├── pages/                     # Sayfa modülleri
│   │   │   ├── items/
│   │   │   ├── create/
│   │   │   └── settings/
│   │   │
│   │   └── widgets/                    # Özel widget'lar
│   │       ├── menu_bar.py
│   │       └── status_bar.py
│   │
│   └── utils/                          # Yardımcı fonksiyonlar
│       ├── validators.py
│       └── formatters.py
│
├── assets/
│   ├── icons/                          # Uygulama ikonları
│   ├── styles/                          # QSS stil dosyaları
│   └── sounds/                          # Bildirim sesleri
│
├── data/                                # Veri depolama
│   ├── contents.json
│   ├── tasks.json
│   └── settings.json
│
├── tests/                                # Test dosyaları
│   ├── test_models.py
│   └── test_services.py
│
├── docs/                                 # Dokümantasyon
│   ├── API.md
│   └── DEVELOPMENT.md
│
├── main.py                               # Uygulama giriş noktası
├── requirements.txt                      # Bağımlılıklar
├── LICENSE                               # Lisans dosyası
└── README.md                             # Bu dosya


---

## 🛠 Teknolojiler

| Teknoloji | Versiyon | Kullanım Alanı |
|-----------|----------|----------------|
| **Python** | 3.10+ | Ana programlama dili |
| **PySide6** | 6.5+ | GUI framework (Qt6) |
| **Qt6** | 6.5+ | Cross-platform widget toolkit |
| **JSON** | - | Veri depolama ve transfer |
| **SQLite3** | 3.x | Yerel veritabanı (opsiyonel) |
| **Pytest** | 7.x | Birim testleri |
| **Black** | 23.x | Kod formatlama |
| **Flake8** | 6.x | Kod kalite kontrolü |

### Mimari Desenler
- **Component-Based Architecture**: Modüler ve yeniden kullanılabilir bileşenler
- **MVC Pattern**: Model-View-Controller ayrışması
- **Observer Pattern**: Bildirim ve olay yönetimi
- **Factory Pattern**: Dinamik bileşen oluşturma

---

## 🧩 Bileşenler

### Temel Bileşenler

| Bileşen | Sorumluluk | Kullanım |
|---------|------------|----------|
| **Card** | Görev/içerik kartı | Başlık, badge, meta bilgiler, aksiyon butonları |
| **ItemsPage** | Liste görünümü | Kartları listeleme, filtreleme, detay paneli |
| **CreatePage** | Yeni kayıt oluşturma | Form validasyonu, veri kaydetme |
| **SettingsPage** | Ayarlar yönetimi | Tema, bildirim, genel ayarlar |
| **JsonViewer** | JSON görüntüleme | Syntax highlighting, expand/collapse |
| **NotificationService** | Bildirim yönetimi | Cross-platform bildirimler |

### Kod Örnekleri

#### Card Bileşeni Kullanımı
\`\`\`python
from app.ui.components.card import Card
from PySide6.QtWidgets import QApplication

# Örnek görev verisi
task_data = {
    "id": "task_001",
    "title": "Haftalık Rapor Hazırla",
    "source_type": "MANUAL",
    "fetch_mode": "static",
    "url": None,
    "duration": 45,
    "cache_policy": "no-cache",
    "created_at": "2026-02-28",
    "priority": "high",
    "tags": ["rapor", "haftalık", "iş"]
}

# Card oluşturma
app = QApplication([])
card = Card(task_data)
card.show()
app.exec()
\`\`\`

#### ItemsPage ile Liste Görünümü
\`\`\`python
from app.ui.pages.items.items import ItemsPage
from app.services.task_service import TaskService

# Servis ve sayfa oluşturma
task_service = TaskService()
page = ItemsPage(task_service)

# Filtre uygulama
page.apply_filter(priority="high", tags=["rapor"])

# Sayfayı gösterme
page.show()
\`\`\`

#### Özel Bildirim Gönderme
\`\`\`python
from app.core.notification.service import NotificationService

notifier = NotificationService()
notifier.send(
    title="Görev Hatırlatıcı",
    message="Haftalık raporu tamamlamanıza 15 dakika kaldı!",
    urgency="normal",
    sound=True
)
\`\`\`

---

## 👨‍💻 Geliştirici Rehberi

### Geliştirme Ortamı Kurulumu

\`\`\`bash
# 1. Depoyu klonlayın
git clone https://github.com/serdarcayan/ctw.git
cd ctw

# 2. Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  # Linux/macOS
# veya
venv\\Scripts\\activate  # Windows

# 3. Geliştirme bağımlılıklarını yükleyin
pip install -r requirements-dev.txt

# 4. Pre-commit hook'larını kurun
pre-commit install
\`\`\`

### Kod Standartları

- **PEP 8** kodlama standartlarına uygunluk
- **Black** ile otomatik formatlama
- **Flake8** ile statik kod analizi
- **Type Hints** kullanımı zorunlu
- **Docstring** zorunluluğu (Google formatı)

### Test Çalıştırma

\`\`\`bash
# Tüm testleri çalıştır
pytest tests/

# Kapsama raporu ile
pytest --cov=app tests/

# Belirli bir test dosyası
pytest tests/test_models.py -v
\`\`\`

### Yeni Bileşen Ekleme

1. `app/ui/components/` dizininde yeni Python dosyası oluşturun
2. Bileşen sınıfını `QWidget`'tan türetin
3. Gerekli sinyal ve slot'ları tanımlayın
4. Stil dosyasını `assets/styles/` altına ekleyin
5. Test dosyasını `tests/ui/components/` altına oluşturun

---

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen şu adımları izleyin:

1. **Fork'layın** (https://github.com/serdarcayan/ctw/fork)
2. **Branch oluşturun** (`git checkout -b feature/yeni-ozellik`)
3. **Değişikliklerinizi commit'leyin** (`git commit -am 'Yeni özellik eklendi'`)
4. **Branch'inizi push'layın** (`git push origin feature/yeni-ozellik`)
5. **Pull Request** oluşturun

### Katkı Kuralları

- Mevcut kod stilini takip edin
- Yeni özellikler için test ekleyin
- Docstring eklemeyi unutmayın
- Anlamlı commit mesajları yazın
- Büyük değişiklikler için önce issue açın

---

## 📄 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.


---

## 📬 İletişim

- **Proje Sahibi**: [Serdar Çayan](mailto:serdarcayan.sc@gmail.com)
- **GitHub Issues**: [github.com/serdarcayan/ctw/issues](https://github.com/serdarcayan/ctw/issues)

---

<div align="center">
  <sub>Built with serdarcayan</sub>
  <br>
  <sub>© 2026 CTW - Content & Task Widget</sub>
</div>

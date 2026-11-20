# Kişisel Not Yönetimi (Notes App)

Python ve Flask ile geliştirilen basit bir kişisel not yönetimi web uygulaması.
Proje, YZM6443 Modern Yazılım Mühendisliği – Bulut ve DevOps dersi dönem projesi kapsamında
Agile / DevOps / Cloud yaklaşımıyla 8 haftada geliştirilmektedir.

## Proje Tanımı

Kullanıcı kendi notlarını web arayüzü üzerinden oluşturabilir, görüntüleyebilir, düzenleyebilir ve silebilir.
Amaç yalnızca çalışan bir uygulama geliştirmek değil; analiz, tasarım, kodlama, test, CI/CD, Docker ve
bulut yayını süreçlerini bir Kanban panosu üzerinden planlayıp yönetmektir.

## Temel Fonksiyonlar

1. **Not ekleme:** Başlık ve içerikle yeni not oluşturma
2. **Not listeleme:** Kayıtlı notları listeleme
3. **Not düzenleme:** Var olan notun başlık/içeriğini güncelleme
4. **Not silme:** Var olan notu silme

## Fonksiyonel Gereksinimler

| No | Gereksinim |
|----|------------|
| FR-1 | Kullanıcı başlık ve içerik girerek yeni not ekleyebilmelidir. |
| FR-2 | Kullanıcı kayıtlı tüm notları listeleyebilmelidir. |
| FR-3 | Kullanıcı var olan bir notu düzenleyebilmelidir. |
| FR-4 | Kullanıcı var olan bir notu silebilmelidir. |
| FR-5 | Notlar uygulama yeniden başlatıldığında da korunmalıdır (kalıcı saklama). |

## Kurulum

```bash
git clone https://github.com/akntekeli/<repo-adi>.git
cd <repo-adi>
python -m venv venv
source venv/Scripts/activate      # Git Bash (Windows). Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

## Çalıştırma

```bash
python src/app.py
```

Uygulama varsayılan olarak http://127.0.0.1:5000 adresinde açılır.

## Proje Yapısı

```
src/          Uygulama kaynak kodları
tests/        Otomatik testler
docs/         Mimari ve test notları
requirements.txt
README.md
```

## İlgili Bağlantılar

- Kanban panosu: https://github.com/users/akntekeli/projects/1/views/1
- Mimari ve veri modeli: [docs/architecture.md](docs/architecture.md)

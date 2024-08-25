# OznInstakit 🚀

**OznInstakit**, Instagram kullanıcı bilgilerini çıkarmak ve görüntülemek için Python'da yazılmış bir komut satırı aracıdır. Instaloader modülünü kullanarak Instagram hesapları hakkında kapsamlı bilgi toplamanıza ve yönetmenize yardımcı olur. Kullanıcı dostu bir arayüz ve geniş bir özellik yelpazesi sunar.

## İçindekiler 📚

- [Özellikler](#özellikler-🌟)
- [Kurulum](#kurulum-📦)
- [Kullanım](#kullanım-📈)
- [İpuçları](#ipuçları-💡)
- [Denemeler](#denemeler-🔬)
- [Katkıda Bulunma](#katkıda-bulunma-🤝)
- [Lisans](#lisans-📜)
- [Teşekkürler](#teşekkürler-🙏)

## Özellikler 🌟

- **Giriş Seçeneği**: Instagram hesabınıza giriş yaparak ek bilgi ve işlemler gerçekleştirme imkanı.
- **Kullanıcı Adı Tarama**: Hedef kullanıcı adını girerek Instagram profil bilgilerini toplama.
- **Taranan Kullanıcı Adlarını Gösterme**: Taranan kullanıcı adlarının günlüğünü tutar ve bunları gözden geçirme.
- **Detaylı Bilgi**: Her kullanıcı için şu bilgileri sağlar:
  - Kullanıcı ID
  - Kullanıcı Adı
  - Tam Adı (varsa)
  - Zamirler (varsa)
  - Yakın zamanda katılma durumu
  - Takipçi Sayısı
  - Takip Edilen Sayısı
  - Biyografi (varsa)
  - Dış URL (varsa)
  - Takip/ takip eden durumu (giriş yapıldıysa)
  - İstek/istekli durumu (giriş yapıldıysa)
  - Toplam Gönderi Sayısı
  - Özel Hesap Durumu
  - Doğrulanmış Hesap Durumu
  - Profesyonel Hesap Durumu
  - Profesyonel Hesap Kategorisi (varsa)
  - İşletme Hesap Durumu
  - İşletme Hesap Kategorisi (varsa)
  - İşletme E-postası (varsa)
  - İşletme Telefonu (varsa)
  - Denetim Durumu
  - Denetçi Durumu (giriş yapıldıysa)
  - Denetlenen Durumu (giriş yapıldıysa)
  - Koruyucu ID (varsa)
  - Engelleme/Sınırlama Durumu (giriş yapıldıysa)
  - Kılavuzlar Erişilebilirliği
  - Karşılıklı Takipçiler (giriş yapıldıysa)
- **Bilgileri Kaydetme**: Taranan kullanıcı adları hakkında bilgileri metin dosyasına kaydetme.
- **Profil Resmi İndirme**: Kullanıcının profil resmini indirme.
- **Son Gönderileri İndirme**: Kullanıcının profilinden en fazla 50 son gönderiyi indirme (daha fazlasını da indirebilirsiniz).
- **Kayıtları Temizleme**: Taranan kullanıcı adlarının günlüğünü temizleme.

## Kurulum 📦

1. **Python 3 veya Üstü Yükleyin**: Sisteminizde Python 3 veya daha üst bir sürümün yüklü olduğundan emin olun.
2. **Terminal veya Komut İstemi Açın**.
3. **OznInstakit Deposu'nu Klonlayın**:

  git clone https://github.com/ibrahimsql/ozninstakit.git

   ### OznInstakit Dizinine Geçin:

cd OznInstakit

   ## Gerekli Python Modüllerini Yükleyin
   
      pip install -r requirements.txt
   

## Kullanım 📈

1. **Terminal veya Komut İstemi Açın** ve OznInstakit dizinine gidin.
2. **Aracı Başlatın**:
      python main.py

3. Ekrandaki talimatları izleyerek Instagram hesabınıza giriş yapın (isteğe bağlı) ve kullanıcı adlarını tarayın.
4. Menüden istediğiniz seçenekleri seçerek taranan kullanıcı adları hakkında bilgi görüntüleyin, kaydedin veya indirin.

## İpuçları 💡

* **Giriş Sorunları**: Instaloader'ı kaldırıp tekrar yüklemek için `pip install -r requirements.txt` komutunu çalıştırın; aksi takdirde giriş hatalarıyla karşılaşabilirsiniz. *Önemli*
* **Geri Dönme**: Yanlışlıkla bir seçenek seçtiyseniz ve tarama yapmak istemiyorsanız, kullanıcı adı alanına `.b` girerek önceki menüye dönebilirsiniz.
* **Oturum Yönetimi**: Giriş yaptıktan sonra tekrar `main.py` çalıştırırsanız, araç sizi önceki oturumunuzu seçmeye yönlendirecektir. Alternatif olarak, giriş yapmadan devam etmek isterseniz negatif değerler girin, örneğin -1.

## Denemeler 🔬

Beta sürümünü denemek isterseniz, `main.py` dosyasını çalıştırmadan önce beta dalına geçin ve düzenli olarak güncellemeleri kontrol edin:
git pull
git checkout beta


## Katkıda Bulunma 🤝

OznInstakit’e katkıda bulunmak için lütfen bir pull request oluşturun. Herhangi bir öneriniz, hata düzeltmeniz veya eklemek istediğiniz yeni özellikler varsa, katkılarınızı görmekten mutluluk duyarız!

## Lisans 📜

OznInstakit, MIT Lisansı altında lisanslanmıştır.

## Teşekkürler 🙏

Geri bildiriminiz ve desteğiniz için teşekkür ederiz! 🤗# OznInstakit-X

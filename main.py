#!/usr/bin/env python3
# Sürüm: 1.1
from datetime import datetime
import instaloader
from core.init import *

L = instaloader.Instaloader()

def öncekiOturumuYükle(kullanıcı_adı):
    """
    Mevcut oturum dosyasını yükler ve kullanıcı adı ile giriş yapar.
    """
    try:
        L.load_session_from_file(kullanıcı_adı)
        Yazdır('s', 'Oturum yüklendi: %s' % L.test_login())
        input('Devam etmek için Enter tuşuna basın: ')
    except Exception as e:
        Yazdır('d', 'Oturum yükleme başarısız! Giriş yapmadan devam etmek için Enter tuşuna basın.')
        Yazdır('w', f'Hata: {e}')
        input('\n:$ ')

def yeniGiriş():
    """
    Kullanıcıdan Instagram kimlik bilgilerini alarak yeni bir oturum başlatır.
    """
    afiş()
    Yazdır('w', '\n1: Instagram\'a Giriş Yap')
    Yazdır('w', '2: Giriş yapmadan - sınırlı özellikler')
    seçenek = input('\n:$ ')
    if seçenek == '1':
        afiş()
        Yazdır('i', '\nGiriş yapmak için aşağıya kimlik bilgilerinizi girin')
        kullanıcı_adı = input('\nKullanıcı Adı: ')
        try:
            L.interactive_login(kullanıcı_adı)
            L.save_session_to_file()
            Yazdır('s', '\nBaşarıyla giriş yapıldı')
            input('Devam etmek için Enter tuşuna basın: ')
        except instaloader.exceptions.BadCredentialsException:
            afiş()
            Yazdır('d', 'Geçersiz kimlik bilgileri')
            Yazdır('w', 'Tekrar deneyin')

def ana_fonksiyon():
    """
    Kullanıcı tarama döngüsünü başlatır ve kullanıcıdan hedef kullanıcı adını ister.
    """
    afiş()
    Yazdır('i', 'Kullanıcılar taranıyor...')
    while True:
        hedef_kullanıcı = input('\nHedef kullanıcı adı: ')
        if hedef_kullanıcı == '':
            Yazdır('w', 'Kullanıcı adı boş olamaz')
            continue
        if hedef_kullanıcı == '.b':  # ! Eğer yanlışlıkla kullanıcı tarama seçildi ise, döngüden çıkmak için `.b` yazın.
            return
        afiş()
        Yazdır('i', f'\n{hedef_kullanıcı} üzerinde tarama başlatılıyor')
        print('`````````````````````````````````````````````````\n')
        başlangıç_zamanı = datetime.now()
        try:
            profil = instaloader.Profile.from_username(L.context, hedef_kullanıcı)
            break
        except instaloader.exceptions.ConnectionException as e:
            afiş()
            Yazdır('d', f'\n{e}')
            Yazdır('w', 'Lütfen tekrar deneyin')
        except instaloader.exceptions.ProfileNotExistsException as e:
            afiş()
            Yazdır('d', f'\nKullanıcı "{hedef_kullanıcı}" mevcut değil: {e}')
            Yazdır('w', 'Yazım hatalarını kontrol edin ve tekrar deneyin')
        except instaloader.exceptions.LoginRequiredException as r:
            afiş()
            Yazdır('w', f'\n{r}')
            Yazdır('d', 'Tekrar deneyin veya önce giriş yapın')
            exit()
        except instaloader.exceptions.QueryReturnedBadRequestException as b:
            afiş()
            Yazdır('d', f'\n{b}')
            
    Yazdır('i', f'Tarama {geçenZaman(başlangıç_zamanı)} saniyede tamamlandı\n')
    bilgi(profil)
    indir(profil)

if __name__ == '__main__':
    öncekiOturumlar = oturumlarıGöster()
    if öncekiOturumlar:
        afiş()
        Yazdır('s', f'\n{len(öncekiOturumlar)} oturumunuz var.')
        print('`````````````````````````````````````````````````\n')
        for id, oturum in enumerate(öncekiOturumlar, 1):
            print(f'      {id}. {oturum}')
        Yazdır('s', '\nOturumu yüklemek için kimliği girin.')
        Yazdır('s', 'Ya da yeni bir kullanıcı adı ile giriş yapmak için 0\'ı girin.')
        seçenek = int(input('\n:$ '))
        if seçenek == 0:
            afiş()
            Yazdır('i', '\nGiriş yapmak için aşağıya kimlik bilgilerinizi girin.')
            kullanıcı_adı = input('\nKullanıcı Adı: ')
            try:
                L.interactive_login(kullanıcı_adı)
                L.save_session_to_file()
                Yazdır('s', '\nBaşarıyla giriş yapıldı')
            except Exception as e:  # Hata mesajını göstermek için tüm hataları yakala
                afiş()
                Yazdır('d', e)
                Yazdır('d', 'Geçersiz kimlik bilgileri')
                Yazdır('w', 'Tekrar deneyin')
                input('\n:$ ')

        elif seçenek > 0:
            oturum_id = seçenek - 1
            oturum_dosyası = öncekiOturumlar[oturum_id]
            kullanıcı_adı = oturum_dosyası.replace('session-', '')
            öncekiOturumuYükle(kullanıcı_adı)
        else:
            pass

    else:
        yeniGiriş()
    while True:
        afiş()
        print('\033[1;33ma: Kullanıcıları Tara         b: Taranan Kullanıcıları Gör        c: Çıkış\033[0m\n\n')
        seçenek = input(':$ ')
        
        if seçenek.strip().lower()[0] == 'c':
            exit('\nHoşça kal 👋')
        
        elif seçenek.strip().lower()[0] == 'b':
            tarananlar()
        
        else:
            ana_fonksiyon()

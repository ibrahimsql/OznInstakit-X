from datetime import datetime

class KullanıcıProfili:
    """
    instaloader Profilinden `_metadata` alır ve bir `KullanıcıProfili` nesnesi döndürür.
    """
    def __init__(self, veri):
        self.veri = veri

    @property
    def kullanıcı_adı(self) -> str:
        return self.veri.get('username', '')

    @property
    def tam_ad(self) -> str:
        return self.veri.get('full_name', '')

    @property
    def biyografi(self) -> str:
        return self.veri.get('biography', '')

    @property
    def dış_url(self) -> str:
        return self.veri.get('external_url', '')

    @property
    def izleyici_engellendi(self) -> bool:
        return self.veri.get('blocked_by_viewer', False)

    @property
    def izleyici_kısıtlandı(self) -> bool:
        return self.veri.get('restricted_by_viewer', False)

    @property
    def takipçiler(self) -> int:
        return self.veri.get('edge_followed_by', {}).get('count', 0)

    @property
    def takip_edilenler(self) -> int:
        return self.veri.get('edge_follow', {}).get('count', 0)

    @property
    def rehberler_var_mı(self) -> bool:
        return self.veri.get('has_guides', False)

    @property
    def id(self) -> int:
        return int(self.veri.get('id', 0))

    @property
    def iş_hesabı_mı(self) -> bool:
        return self.veri.get('is_business_account', False)

    @property
    def profesyonel_hesap_mı(self) -> bool:
        return self.veri.get('is_professional_account', False)

    @property
    def kategori_adı(self) -> str:
        return self.veri.get('category_name', '')

    @property
    def denetim_etkin_mi(self) -> bool:
        return self.veri.get('is_supervision_enabled', False)

    @property
    def izleyicinin_velisi_mi(self) -> bool:
        return self.veri.get('is_guardian_of_viewer', False)

    @property
    def izleyici_tarafından_denetleniyor_mu(self) -> bool:
        return self.veri.get('is_supervised_by_viewer', False)

    @property
    def denetlenen_kullanıcı_mı(self) -> bool:
        return self.veri.get('is_supervised_user', False)

    @property
    def yeni_katıldı_mı(self) -> bool:
        return self.veri.get('is_joined_recently', False)

    @property
    def veli_id(self) -> int:
        return self.veri.get('guardian_id', 0)

    @property
    def iş_eposta(self) -> str:
        return self.veri.get('business_email', '')

    @property
    def iş_telefon(self) -> str:
        return self.veri.get('business_phone_number', '')

    @property
    def iş_kategori_adı(self) -> str:
        return self.veri.get('business_category_name', '')

    @property
    def özel_hesap_mı(self) -> bool:
        return self.veri.get('is_private', False)

    @property
    def doğrulanmış_hesap_mı(self) -> bool:
        return self.veri.get('is_verified', False)

    @property
    def ortak_takip_edenler(self) -> dict:
        return self.veri.get('edge_mutual_followed_by', {})

    @property
    def zamirler(self) -> list:
        return self.veri.get('pronouns', [])

def takipçiler(profil: object) -> dict:
    """
    Bir profil nesnesi alır ve takipçilerin bir sözlüğünü döndürür.
    """
    takipçi_listesi = {}
    takipçi_objeleri = profil.get_followers()
    for sıra, takipçi in enumerate(takipçi_objeleri, 1):
        takipçi_listesi[sıra] = {
            'kullanıcı_adı': takipçi.username, 
            'tam_ad': takipçi.full_name, 
            'id': takipçi.id
        }
    return takipçi_listesi

def takip_edilenler(profil: object) -> dict:
    """
    Bir profil nesnesi alır ve takip edilenlerin bir sözlüğünü döndürür.
    """
    takip_edilen_listesi = {}
    takip_edilen_objeleri = profil.get_followees()
    for sıra, takip_edilen in enumerate(takip_edilen_objeleri, 1):
        takip_edilen_listesi[sıra] = {
            'kullanıcı_adı': takip_edilen.username, 
            'tam_ad': takip_edilen.full_name, 
            'id': takip_edilen.id
        }
    return takip_edilen_listesi

def benzersiz_kullanıcılar(veri):
    benzersiz = {}
    print('\n╭─────────────────────────────────────────────╮')
    print('│{:^45}│'.format('Taranan kullanıcılar (benzersiz)'))
    print('├─────┬─────────────────────────┬─────────────┤')
    print('│{: ^5}│{: ^25}│ {: ^11} │'.format('Srno', 'Kullanıcı Adı', 'Taranma Saati'))
    print('├─────┼─────────────────────────┼─────────────┤')
    for satır in reversed(veri):
        kullanıcı = satır.split(',')[0].strip()
        ham_veri = satır.split(',')[1].strip()
        zaman_objesi = datetime.strptime(ham_veri, '%Y-%m-%d %H:%M:%S')
        zaman = zaman_objesi.strftime('%H:%M %d/%m')
        if kullanıcı not in benzersiz:
            benzersiz[kullanıcı] = zaman
    sıra_no = 0
    for kullanıcı, zaman in benzersiz.items():
        sıra_no += 1
        print(f'│{sıra_no: ^5}│{kullanıcı: ^25}│ {zaman: ^8} │')
    print('├─────┴──────────────────┬──────┴─────────────┤')
    print('│   c: Günlüğü Temizle{: ^20}q: Çıkış   │'.format('│'))
    print('╰────────────────────────┴────────────────────╯\n')

def tüm_kullanıcılar(veri):
    print('\n╭─────────────────────────────────────────────╮')
    print('│{:^45}│'.format('Taranan kullanıcılar (tüm)'))
    print('├─────┬─────────────────────────┬─────────────┤')
    print('│{: ^5}│{: ^25}│ {: ^11} │'.format('Srno', 'Kullanıcı Adı', 'Taranma Saati'))
    print('├─────┼─────────────────────────┼─────────────┤')
    for sıra, satır in enumerate(reversed(veri), 1):
        kullanıcı_adı = satır.split(',')[0].strip()
        ham_zaman = satır.split(',')[1].strip()
        zaman_objesi = datetime.strptime(ham_zaman, '%Y-%m-%d %H:%M:%S')
        print(f'│{sıra: ^5}│{kullanıcı_adı: ^25}│ {zaman_objesi.strftime("%H:%M %m/%d"): ^8} │')
    print('├─────┴──────────────────┬──────┴─────────────┤')
    print('│   c: Günlüğü Temizle{: ^20}q: Çıkış   │'.format('│'))
    print('╰────────────────────────┴────────────────────╯\n')

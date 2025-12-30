# on_isleme.py
# Metin ön işleme işlemleri

import re

# Türkçe stopword listesi
TURKCE_STOPWORDS = [
    'bir', 'bu', 've', 'de', 'da', 'ile', 'için', 'var', 'ben', 'sen',
    'o', 'biz', 'siz', 'onlar', 'ne', 'ki', 'ama', 'ancak', 'fakat',
    'çünkü', 'eğer', 'gibi', 'kadar', 'daha', 'en', 'çok', 'az',
    'her', 'hiç', 'bazı', 'tüm', 'bütün', 'şu', 'şey', 'olan',
    'olarak', 'oldu', 'olmuş', 'olacak', 'ise', 'mi', 'mı',
    'mu', 'mü', 'ya', 'hem', 'veya', 'yani', 'sadece', 'bile',
    'diye', 'göre', 'sonra', 'önce', 'şimdi', 'zaman', 'kendi',
    'aynı', 'böyle', 'şöyle', 'nasıl', 'neden', 'niçin', 'hangi'
]

def kucuk_harfe_cevir(metin):
    """Metni küçük harfe çevirir"""
    return metin.lower()

def noktalama_temizle(metin):
    """Noktalama işaretlerini temizler"""
    temiz_metin = re.sub(r'[^\w\sğüşıöçĞÜŞİÖÇ]', ' ', metin)
    return temiz_metin

def sayilari_temizle(metin):
    """Sayıları temizler"""
    return re.sub(r'\d+', '', metin)

def stopword_temizle(metin, stopwords=None):
    """Stopword'leri temizler"""
    if stopwords is None:
        stopwords = TURKCE_STOPWORDS
    kelimeler = metin.split()
    temiz_kelimeler = [kelime for kelime in kelimeler if kelime not in stopwords]
    return ' '.join(temiz_kelimeler)

def fazla_bosluk_temizle(metin):
    """Fazla boşlukları temizler"""
    return ' '.join(metin.split())

def metin_on_isle(metin):
    """Tüm ön işleme adımlarını uygular"""
    metin = kucuk_harfe_cevir(metin)
    metin = noktalama_temizle(metin)
    metin = sayilari_temizle(metin)
    metin = stopword_temizle(metin)
    metin = fazla_bosluk_temizle(metin)
    return metin

def veri_on_isle(veri, metin_sutunu='Metin'):
    """DataFrame'deki tüm metinleri ön işler"""
    veri['islenmiş_metin'] = veri[metin_sutunu].apply(metin_on_isle)
    return veri
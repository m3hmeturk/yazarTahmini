# ozellik_cikarimi.py
# TF-IDF özellik çıkarımı işlemleri

from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def tfidf_olustur(max_ozellik=5000, min_df=2, max_df=0.95):
    """TF-IDF vektörleyici oluşturur"""
    vektorleyici = TfidfVectorizer(
        max_features=max_ozellik,
        min_df=min_df,
        max_df=max_df,
        ngram_range=(1, 2)
    )
    return vektorleyici

def ozellikleri_cikar(metinler, vektorleyici=None, egit=True):
    """Metinlerden TF-IDF özellikleri çıkarır"""
    if vektorleyici is None:
        vektorleyici = tfidf_olustur()
    
    if egit:
        ozellik_matrisi = vektorleyici.fit_transform(metinler)
    else:
        ozellik_matrisi = vektorleyici.transform(metinler)
    
    return ozellik_matrisi, vektorleyici

def vektorleyici_kaydet(vektorleyici, dosya_yolu):
    """Vektörleyiciyi dosyaya kaydeder"""
    with open(dosya_yolu, 'wb') as dosya:
        pickle.dump(vektorleyici, dosya)
    print(f"Vektörleyici kaydedildi: {dosya_yolu}")

def vektorleyici_yukle(dosya_yolu):
    """Kaydedilmiş vektörleyiciyi yükler"""
    with open(dosya_yolu, 'rb') as dosya:
        vektorleyici = pickle.load(dosya)
    return vektorleyici

def ozellik_bilgisi(vektorleyici, ozellik_matrisi):
    """Özellik çıkarımı hakkında bilgi verir"""
    print("=== Özellik Çıkarımı Bilgisi ===")
    print(f"Toplam özellik sayısı: {len(vektorleyici.get_feature_names_out())}")
    print(f"Matris boyutu: {ozellik_matrisi.shape}")
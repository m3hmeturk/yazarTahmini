# veri_yukleme.py
# Excel'den veri yükleme işlemleri

import pandas as pd

def veri_yukle(dosya_yolu):
    """Excel dosyasından veriyi yükler"""
    veri = pd.read_excel(dosya_yolu)
    return veri

def veri_bilgisi(veri):
    """Veri seti hakkında bilgi verir"""
    print("=== Veri Seti Bilgisi ===")
    print(f"Toplam örnek sayısı: {len(veri)}")
    print(f"Sütunlar: {list(veri.columns)}")
    print(f"\nYazar dağılımı:")
    print(veri['Yazar'].value_counts())
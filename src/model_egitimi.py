# model_egitimi.py
# Naive Bayes ve SVM model eğitimi

from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, cross_val_score
import pickle

def veri_bol(X, y, test_orani=0.2, rastgele_durum=42):
    """Veriyi eğitim ve test setlerine böler"""
    X_egitim, X_test, y_egitim, y_test = train_test_split(
        X, y, 
        test_size=test_orani, 
        random_state=rastgele_durum,
        stratify=y
    )
    print(f"Eğitim seti: {X_egitim.shape[0]} örnek")
    print(f"Test seti: {X_test.shape[0]} örnek")
    return X_egitim, X_test, y_egitim, y_test

def naive_bayes_egit(X_egitim, y_egitim, alpha=1.0):
    """Multinomial Naive Bayes modeli eğitir"""
    model = MultinomialNB(alpha=alpha)
    model.fit(X_egitim, y_egitim)
    print("Naive Bayes modeli eğitildi.")
    return model

def svm_egit(X_egitim, y_egitim, C=1.0, max_iter=10000):
    """LinearSVC (SVM) modeli eğitir"""
    model = LinearSVC(C=C, max_iter=max_iter, random_state=42)
    model.fit(X_egitim, y_egitim)
    print("SVM modeli eğitildi.")
    return model

def capraz_dogrulama(model, X, y, katman_sayisi=5):
    """Çapraz doğrulama ile model performansını ölçer"""
    skorlar = cross_val_score(model, X, y, cv=katman_sayisi, scoring='accuracy')
    print(f"Çapraz Doğrulama ({katman_sayisi} katman):")
    print(f"  Ortalama Doğruluk: {skorlar.mean():.4f}")
    print(f"  Standart Sapma: {skorlar.std():.4f}")
    return skorlar

def model_kaydet(model, dosya_yolu):
    """Modeli dosyaya kaydeder"""
    with open(dosya_yolu, 'wb') as dosya:
        pickle.dump(model, dosya)
    print(f"Model kaydedildi: {dosya_yolu}")

def model_yukle(dosya_yolu):
    """Kaydedilmiş modeli yükler"""
    with open(dosya_yolu, 'rb') as dosya:
        model = pickle.load(dosya)
    return model
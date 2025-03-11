#Sözlük yapısı (Dictionary) ve özellikleri
#Sözlükler, anahtar-değer çiftlerini depolayan bir veri yapısıdır.
#Sözlükler, süslü parantezler {} içinde virgülle ayrılmış anahtar-değer çiftlerini içerir.
#Sözlüklerde anahtarlar benzersiz olmalıdır, ancak değerler benzersiz olmak zorunda değildir.
#Sözlüklerde anahtarlar değiştirilemezdir, bu nedenle anahtarlar dize, sayı veya demet gibi değiştirilebilir olmalıdır.
#Sözlüklerde değerler değiştirilebilir.
#Sözlüklerde değerlere erişmek için anahtarları kullanabiliriz.
#Sözlüklerde anahtarlar ve değerler farklı veri türlerinden olabilir.
#Sözlüklerde değerler listeler, sözlükler ve hatta başka sözlükler olabilir.
#Sözlüklerde değerlerin sırası önemli değildir, ancak anahtarların sırası önemlidir.
#Sözlüklerde len() fonksiyonu, sözlükteki anahtar sayısını döndürür.
#Sözlüklerde in anahtar kelimesi, belirli bir anahtarın sözlükte olup olmadığını kontrol eder.
#Sözlüklerde del anahtar kelimesi, belirli bir anahtarı siler.
#Sözlüklerde clear() fonksiyonu, sözlüğü temizler.
#Sözlüklerde values() fonksiyonu, sözlükteki tüm değerleri döndürür.
#Sözlüklerde keys() fonksiyonu, sözlükteki tüm anahtarları döndürür.
#Sözlüklerde items() fonksiyonu, sözlükteki tüm anahtar-değer çiftlerini döndürür.
#Sözlüklerde copy() fonksiyonu, sözlüğün bir kopyasını döndürür.
#Sözlüklerde update() fonksiyonu, bir sözlüğü başka bir sözlükle günceller.
#Sözlüklerde pop() fonksiyonu, belirli bir anahtarı kaldırır ve değerini döndürür.
#Sözlüklerde popitem() fonksiyonu, son anahtar-değer çiftini kaldırır ve döndürür.
#Sözlüklerde fromkeys() fonksiyonu, belirli bir değere sahip bir sözlük oluşturur.
#Sözlüklerde setdefault() fonksiyonu, belirli bir anahtara sahip bir değer döndürür. Anahtar yoksa, anahtar ve belirtilen değeri ekler.
#Sözlüklerde get() fonksiyonu, belirli bir anahtara sahip bir değer döndürür. Anahtar yoksa, belirtilen bir değer döndürür.

#Örnek 1
#Sözlük oluşturma
sozluk = {
    "marka": "Ford",
    "model": "Mustang",
    "yıl": 1964
}
print(sozluk)
#Çıktı: {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1964}
#Bu sözlüğe tek bir anahtar-değer çifti ekleyelim.
sozluk["renk"] = "kırmızı"
print(sozluk)
#Çıktı: {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1964, 'renk': 'kırmızı'}

#Bu sözlükten bir anahtar-değer çiftini kaldıralım.
del sozluk["renk"]
print(sozluk)
#Çıktı: {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1964}

#Bu sözlüğe birden fazla anahtar-değer çifti ekleyelim.
sozluk.update({"renk": "kırmızı", "fiyat": 50000})
print(sozluk)
#Çıktı: {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1964, 'renk': 'kırmızı', 'fiyat': 50000}

#Bu sözlüğün kopyasını oluşturalım.
sozluk_kopya = sozluk.copy()
print(sozluk_kopya)
#Çıktı: {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1964, 'renk': 'kırmızı', 'fiyat': 50000}

#Bu sözlüğün tüm anahtarlarını döndürelim.
anahtarlar = sozluk.keys()
print(anahtarlar)
#Çıktı: dict_keys(['marka', 'model', 'yıl', 'renk', 'fiyat'])
#Bu sözlüğün tüm değerlerini döndürelim.
degerler = sozluk.values()
print(degerler)
#Çıktı: dict_values(['Ford', 'Mustang', 1964, 'kırmızı', 50000])
#Bu sözlüğün tüm anahtar-değer çiftlerini döndürelim.
ciftler = sozluk.items()
print(ciftler)
#Çıktı: dict_items([('marka', 'Ford'), ('model', 'Mustang'), ('yıl', 1964), ('renk', 'kırmızı'), ('fiyat', 50000)])
#Bu sözlüğün belirli bir anahtarına sahip değerini döndürelim.
deger = sozluk.get("model")
print(deger)
#Çıktı: Mustang
#Bu sözlüğün belirli bir anahtarına sahip değerini döndürelim. Anahtar yoksa belirtilen bir değer döndürelim.
deger = sozluk.get("kilometre", 0)
print(deger)
#Çıktı: 0

#Şimdi olmayan bir değeri çağırmayı deneyelim ve hata alalım.
#deger = sozluk["kilometre"]
#print(deger)
#Çıktı: KeyError: 'kilometre'

#Şimdi ise hata almamak için get() fonksiyonunu kullanalım ve bir parametre daha ekleyerek istediğimiz hata mesajını döndürelim
deger = sozluk.get("kilometre", "Anahtar bulunamadı.")
print(deger)
#Çıktı: Anahtar bulunamadı.

#Şimdi pop fonksiyonunu kullanarak belirli bir anahtarı kaldıralım ve değerini döndürelim.
deger = sozluk.pop("fiyat")
print(deger)
print(sozluk)
#Çıktı: 50000
#Çıktı: {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1964, 'renk': 'kırmızı'}

#Şimdi popitem fonksiyonunu kullanarak son anahtar-değer çiftini kaldıralım ve döndürelim.
cift = sozluk.popitem()
print(cift)
print(sozluk)
#Çıktı: ('renk', 'kırmızı')
#Çıktı: {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1964}

#Şimdi clear fonksiyonunu kullanarak sözlüğü temizleyelim.
sozluk.clear()
print(sozluk)
#Çıktı: {}

#Bu sözlüğü şimdi bir for döngüsü ile tarayalım.
sozluk = {
    "marka": "Toyota",
    "model": "Corolla",
    "yıl": 2013
}
for anahtar in sozluk:
    print(anahtar, sozluk[anahtar])



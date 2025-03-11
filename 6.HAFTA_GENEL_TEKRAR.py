#GENEL TEKRAR
#List(Liste) Veri Yapısı
#Köşeli parantez ile tanımlanır.Bu simge, list veri yapısına özel bir simgedir.

my_list_1=[]

#en sık kullanılan list fonksiyonları
#listeye sonradan eleman ekleme 
#1) append() fonksiyonu: listeye eleman ekler
#yani listenin -1. indexine eleman ekler

my_list_1.append("Burdur")
my_list_1.append("Mehmet")
my_list_1.append("Akif")
my_list_1.append("Ersoy")
my_list_1.append("Üniversitesi")
#bir listenin tüm elemanlarını [] simgesi içerisinde yan yana yazdırmak için
#liste değişkeninin adı yazdırılır. Bu örnekte my_list_1

print(my_list_1)
print("-"*50)
#Çıktı: ['Burdur', 'Mehmet', 'Akif', 'Ersoy', 'Üniversitesi']

#2) insert() fonksiyonu:
#insert() fonksiyonu ile append metodunun farkı: append() tüm elemanları -1.
#indexe yani en sona eklerdi

#insert() fonksiyonu ise istediğimiz index değerine ekler.
#insert() fonksiyonu ile -1. indexe eklemek istersek

my_list_1.insert(-1,"Üniversitesi")
print(my_list_1)
print("-"*50)
#Çıktı: ['Burdur', 'Mehmet', 'Akif', 'Ersoy', 'Üniversitesi', 'Üniversitesi']
#aynı zamanda istediğimiz indexe ekleyebiliriz

#ikinci indexe ztyo ifadesi ekleme
my_list_1.insert(2,"ZTYO")
print(my_list_1)
print("-"*50)

#listenizin elemanlarını kopyalamak için copy() fonksiyonunu kullanabilirsiniz
#değer bazlı kopyalamak için copy() fonksiyonu kullanılır

my_list_2=my_list_1.copy()
print(my_list_2)
print("-"*50)

#referans bazlı kopyalamak için ise "=" işareti kullanılır
my_list_3=my_list_1
my_list_1.append("kopya değer")
print(f"orijinal liste {my_list_1}")
print("-"*50)
print(f"kopyalanan liste {my_list_2}")
print("-"*50)
print(f"referans kopya liste {my_list_3}") #değerini değil referansını içine atıyoruz yani birebir kopyalayacaktır
print("-"*50)

#Listeden eleman silme
#1) remove() fonksiyonu: remove() fonksiyonu ile belirli bir elemanı sileriz
#remove fonksiyonu içerisine değer alır bu değer listenin içinde varsa siler

my_list_1.remove("Akif")
print(f"remove ile silme sonrasında liste {my_list_1}")
print("-"*50)

#2) pop() fonksiyonu: pop() fonksiyonu ile belirli bir index numarasındaki elemanı sileriz
#varsayılan silme indeksi=-1 yani en son elemanı siler
my_list_1.pop()
print(f"pop ile silme sonrasında liste {my_list_1}")
print("-"*50)

#3) delete anahtar kelimesi: del anahtar kelimesi ile belirli bir index numarasındaki elemanı sileriz
#del ile ilk 3 değeri silin (3. değer dahil)
#del ile -2. indexteki elemanı silin
#del ile direkt listeyi silin

#şu an elimizdeki listeyi bastıralım
print(f"poptan sonraki ilk liste {my_list_1}")
print("-"*50)

del my_list_1[0:3]
print(f"del ile 3. eleman dahil silme sonrasında liste {my_list_1}")
print("-"*50)

del my_list_1[-2]
print(f"del ile -2. elemanı silme sonrasında liste {my_list_1}")
print("-"*50)

del my_list_1
#print(f"del ile silme sonrasında liste {my_list_1}")

#listelerde indeksleme işlemi
#liste_adı[tek_deger] => o indeksteki elemanı getirir (tek eleman getirir)
#liste_adı[:bitiş_indeksi] => başlangıç indeksinden "0" bitiş indeksine kadar olan elemanları getirir (bitiş değeri indekse dahil değildir)
#liste_adı[başlangıç:bitiş] => başlangıç indeksinden bitiş indeksine kadar olan elemanları getirir (bitiş değeri indekse dahil değildir)
#liste_adı[başlangıç:bitiş:artış]=>başlangıç değerinden bitiş değerine kadar olan elemanları artış sırasına göre getirir
#NOT: liste_adı[::artış] ifadesine göre artış miktarı -1 ise bu ifade liste elemanlarını tersten sıralamaya yarar
#çünkü -1. indeks son indeks olduğu için onu başlangıç haline getirir ve sondan başa doğru bir indeksleme yapar

my_list_4=["Burdur","Mehmet","Akif",18,65,True,123.856,"Ersoy",False,"Üniversitesi","Bucak",21,45,True,65.43,1298.65,"ZTYO",False]

eleman_1=my_list_4[::3]
print(f"my_list_4[::3]'nin 2.elemanı = {eleman_1[1]}")
print(f"eleman 1= {eleman_1}")
print("-"*50)

eleman_1=my_list_4[2::2]
print(f"eleman 1 = {eleman_1}")
print(f"my_list_4[2::2]'nin 1.elemanı = {eleman_1[0]}")
print("-"*50)
print(f"my_list_4[2::2]'nin 3.elemanı = {eleman_1[2]}")
print("-"*50)
#negatif indeksleme yapalım
#artış miktarı -1 olduğu için sıralama kesinlikle soldan yani tersten başlayacaktır
#sonrasında başlangıç değeri olarak 1. indeks verilmiş
#başlangıç indeksi her zaman dahildir yine dahil ve burada birinci indekste "Mehmet" elemanı var sıralama tersten
#olduğu için bitiş noktası 0. indeks olacak bundan dolayı 1. indeksin solunda sadece 0. indeks olduğu için
#elemanları ["Mehmet","Burdur"] olacaktır.
eleman_1=my_list_4[1::-1]
print(f"my_list_4[1::-1]'nin 5.elemanı = {eleman_1}")

#for döngüsü kullanarak listenin elemanlarına tek tek erişme

for eleman in my_list_4:
    print(eleman)
print("-"*50)

#boş bir listeye 1 den 100 e kadar olan sayıları ekleyip yazdıralım (100 dahil)
#ekleyen kodu yazdırınız

my_list_5=[]
for i in range(1,101):
    my_list_5.append(i)
print(my_list_5)
print("-"*50)

#iki adet boş liste içerisine, birine 0-100 aralığındaki tek sayıları 
#diğerine ise çift sayıları ekleyen kodu yazın

my_list_6=[]
my_list_7=[]

for i in range(0,101):
    if i%2==0:
        my_list_6.append(i)
    else:
        my_list_7.append(i)
print(f"çift sayılar={my_list_6}")
print("-"*50)
print(f"tek sayılar={my_list_7}")

#En sık kullanılan 2. Veri yapısı : Sözlükler (Dictionary)
#aşağıdaki gibi tanımlanır 
#dictionary veri yapısı "key":value şeklinde tanımlanmasıyla diğer tüm veri yapılarından apayrı bir yere sahiptir

my_dict_1={"isim":"Süleyman Efe","soyisim":"Metik","ders-sayısı":5,"dersler":["Orta Düzey Programlama","Python Programlama","OOP"]}
#sadece key değerlerini yazdırmak için keys() fonksiyonu kullanılır
print(f"sadece keys'ler {my_dict_1.keys()}")
print("-"*50)
#sadece value değerlerini yazdırmak için values() fonksiyonu kullanılır
print(f"sadece values'ler {my_dict_1.values()}")
print("-"*50)
#sadece key ve value değerlerini yazdırmak için items() fonksiyonu kullanılır
print(f"hem keyler hem de valuelar {my_dict_1.items()}")
print("-"*50)
#Derslerin sayısını getiren kodu yazın (dersler key'ini kullanarak) çıktısı 3 olmalı

print(f"ders sayısı {len(my_dict_1['dersler'])}")
#değerlerin kendisi
print(f"dersler {my_dict_1['dersler']}")
#herhangi bir değere erişmek için aşağıdaki formülü izleriz
#dictionary_adı['anahtar_adı']

#bir key'e ait değeri güncellemek 
#bunun için aşağıdaki formülü izleriz
#dictionary_adı['anahtar_adı']='yeni_değer'
print("-"*50)
print(f"orijinal dersler {my_dict_1['dersler']}")
my_dict_1['dersler']=['Orta Düzey Programlama','Python Programlama','OOP','Bilgi Güvenliği']
print(f"yeni dersler {my_dict_1['dersler']}")
#yeni bir key ve buna ait değerler eklemek için

my_dict_1["department"]="Management Information Systems"
print(my_dict_1.items())
print("-"*50)

#for döngüsü ile hem keys hem de values değerlerine erişim
#her ikisine de aynı anda erişmek için .items() fonksiyonu kullanılır
#iki değer döndüğü için bu fonksiyondan, fordan sonra iki geçiçi değişken tanımlanır

#örnek
for degisken_key,degisken_value in my_dict_1.items():
    print(f"anahtar={degisken_key} deger={degisken_value}")
print("-"*50)
#NOT:Genellikle dictionary veri yapısında şartlar/koşullar işlenirken
#özellikle veri bilimi alanında %99.9 values değerleri üzerinden işlem yapılır
#ancak , values'ta meydana gelecek değişiklikler izzlenebilsin diye onun
#ait olduğu key bilgisi de (adı da) yazdırılır veya işlenir
#bundan dolayı aynı anda hem key hem de values bilgisine ihtiyaç duyulduğu için
#bu tarz işlemlerin %100'ünde dictionary.items() fonksiyonu kullanılır

#1) Yukarıdaki dictionary içerisine 'maaslar' isminde bir key ekleyin
#bu key'in değerleri[23000,25000,32000,106000,85000,92000] olacak
#2) Maaşı 0 ila 25000 arasında olanlara %30, 25000 ila 90000 arasında olanlara %20 ,90000 ve üzerine %15 zam yapın
#zamlı maaşları yeni bir listeyle döndürün

my_dict_1["maaslar"]=[23000,25000,32000,106000,85000,92000]
list_maaslar=[]
"""print(my_dict_1.items())
for maaslar in my_dict_1["maaslar"]:
    if maaslar<=25000:
        maaslar=maaslar*1.30
    elif maaslar>25000 and maaslar<=90000:
        maaslar=maaslar*1.20
    else:
        maaslar=maaslar*1.15
    list_maaslar.append(maaslar)
print(f"zamlı maaşlar {list_maaslar}")"""

for my_value in my_dict_1["maaslar"]:
    if my_value>0 and my_value<=25000:
        list_maaslar.append(my_value*1.3)
    elif my_value>25000 and my_value<=90000:
        list_maaslar.append(my_value*1.2)
    elif my_value>90001:
        list_maaslar.append(my_value*1.15)
print(f"güncel maaşlar {my_dict_1['maaslar']}")
print(f"zamlı maaşlar {list_maaslar}")
my_dict_1["maaslar"]=list_maaslar
print(f"güncel maaşlar {my_dict_1['maaslar']}")
print("-"*50)

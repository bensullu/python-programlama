my_list=[]
my_list_2=list()

print(type(my_list))
print(type(my_list_2))

#listelere eleman ekleme 1.yol append() metodu ile
#append fonksiyonu içerisine parametre olarak verilen her şey (1 adet olmak kaydıyla)
#son eleman olarak listeye eklenir

#not: bir listeti daha tanınmlama aşamasında içerisine eleman vererek de tanımlayabiliriz
#not: listenin içerisine herhangi bir tipte eleman eklenebilir

my_list_3=[5,86.53,"ztyo",True]
print(my_list_3[2])

my_list_4=[]
my_list_4.append("Burdur")
my_list_4.append("Mehmet")
my_list_4.append("Akif")
#çoklu eleman ekleme
my_list_4.append(["Ersoy","Üniversitesi",6,True,985.412])
print(my_list_4[-1])

print(f"Listenin uzunluğu={len(my_list_4)}")
print(f"Listenin son elemanı={my_list_4[-1]}")
print(f"Listenin ilk elemanı={my_list_4[0]}")
print(f"listenin son elemanının son elemanı={my_list_4[-1][-1]}")

#1 den 100 e kadar olan bütün sayıları 100 de dahil boş bir listeye ekleyip sonra da bu listeyi yazdırın
my_list_5=[]
for i in range(1,101):
    my_list_5.append(i)
print(my_list_5)

#iki adet boş liste oluşturun bu listelerden birine 1 den 100 e kadar olan tek sayıları
#diğer listeye de 0 dan 100 e kadar olan çift sayıları ekleyin
#sonra bu iki listeyi yazdırın
my_list_6=[]
my_list_7=[]
for i in range(0,101):
    if i%2==0:
        my_list_6.append(i)
    else:
        my_list_7.append(i)
print(f"çift sayılar={my_list_6}")
print(f"tek sayılar={my_list_7}")

#listelere eleman ekleme 2.yol insert() metodu ile
#append metodu listenin sonuna eleman eklerken "-1" olarak insert metodu listenin herhangi bir yerine eleman ekler
#insert metodu içerisine iki parametre alır
#1.parametre eklenecek elemanın index numarası
#2.parametre eklenecek elemanın değeri
#özellikle belirli bir index numarasına eleman eklemek istiyorsanız
#insert (indeks no,"eklenecek değer") şeklinde kullanılır

my_list_8=[1,2,3,4,5,6,7,8,9,10]
print(f"orijinal listedeki 2. index= {my_list_8[2]}")
my_list_8.insert(2,100)
print(f"100 eklenmiş listedeki 2. index= {my_list_8[2]}")
print(f"listenin güncellenmiş hali= {my_list_8}")

#listelerde eleman silme 1.yol pop() metodu ile
#pop metodu içerisine parametre almaz ve listenin son elemanını siler
#pop metodu içerisine parametre verilirse o index numarasındaki elemanı siler

my_list_9=[1,2,3,4,5,6,7,8,9,10]
print(f"son eleman silinmemiş liste={my_list_9}")
my_list_9.pop()
print(f"son eleman silinmiş liste={my_list_9}")
my_list_9.pop(2)
print(f"2. index silinmiş liste={my_list_9}")

#listelerde eleman silme 2.yol remove() metodu ile
#remove metodu içerisine parametre olarak silinecek değeri alır
#remove metodu silinecek değeri bulur ve siler
#eğer silinecek değer listede yoksa hata verir

my_list_10=[1,2,3,4,5,6,7,8,9,"bam",True,False,"mehmet","akif"]
print(f"3. index silinmemiş liste={my_list_10}")
my_list_10.remove("akif")
print(f"akif değeri silinmiş liste={my_list_10}")
my_list_10.remove(my_list_10[9])
print(f"10. index silinmiş liste={my_list_10}")

#clear() metodu ile listeyi temizleme
#clear metodu içerisine parametre almaz ve listenin tüm elemanlarını siler

my_list_11=[1,2,3,4,5,6,7,8,9,10]
print(f"temizlenmemiş liste={my_list_11}")
my_list_11.clear()
print(f"temizlenmiş liste={my_list_11}")

#listelerde eleman silme 3.yol del anahtar kelimesi ile
#del anahtar kelimesi ile listelerden eleman silebiliriz
#not: bu da sqldeki drop table ifadesi ile aynı işlevi görür
#belleğe gider liste için ayrılan yeri ve listeyi siler

my_list_12=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f"silinmemiş liste={my_list_12}")
del my_list_12
#print(f"silinmiş liste={my_list_12}")
#bu şekilde listeyi tamamen siler
#çalıştırılısa hata verir çünkü bellekte yer ayrılmamıştır

#del anahtar kelimesi ile çoklu eleman silme
#çoklu eleman silme işleminde del liste_değişkeni [başlangıç:bitiş] şeklinde kullanılır
#bu şekilde belirtilen aralıktaki elemanlar silinir

my_list_13=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f"silinmemiş liste={my_list_13}")
del my_list_13[2:-1]
print(f"2. index ile son eleman arasındaki elemanlar silinmiş liste={my_list_13}")

#copy fonksiyonu ile listeyi kopyalama 
#copy fonksiyonu ile bir listeyi kopyalayabiliriz

my_list_14=[1,2,3,4,5,6,7,8,9,10]
my_list_15=my_list_14.copy()
print(f"orijinal liste={my_list_14}")
print(f"kopyalanan liste={my_list_15}")

#count fonksiyonu ile listedeki eleman sayısını bulma
#count fonksiyonu içerisine parametre olarak aranan elemanı alır

my_list_16=["Burdur","Mehmet","Akif","Ersoy","Üniversitesi"]
print(f"liste={my_list_16}")
print(f"Ersoy elemanı listede {my_list_16.count("Ersoy")} adet bulunmaktadır")

#extend fonksiyonu ile listeyi genişletme
#extend fonksiyonu içerisine parametre olarak başka bir listeyi alır
#ve bu listeyi genişletir

my_list_17=[1,2,3,4,5]
print(f"liste 1={my_list_17}")
print(f"liste 2={my_list_16}")
my_list_17.extend(my_list_16)
print(f"listeler birleştirilmiş hali={my_list_17}")

#index fonksiyonu ile elemanın index numarasını bulma
#index fonksiyonu içerisine parametre olarak aranan elemanı alır

my_list_18=["Burdur","Mehmet","Akif","Ersoy","Üniversitesi"]
print(f"liste={my_list_18}")
print(f"Akif elemanının index numarası={my_list_18.index("Akif")}")

#reverse fonksiyonu ile listeyi ters çevirme
#reverse fonksiyonu içerisine parametre almaz ve listeyi ters çevirir

my_list_19=[1,2,3,4,5,6,7,8,9,10]
print(f"liste={my_list_19}")
my_list_19.reverse()
print(f"ters çevrilmiş liste={my_list_19}")

#sort fonksiyonu ile listeyi sıralama
#sort fonksiyonu içerisine parametre almaz ve listeyi küçükten büyüğe sıralar
#karışık bir listede örnek olarak string ve integer değerler varsa hata verir

my_list_20=[5,8,1,3,9,2,4,7,6,10]
print(f"karışık liste={my_list_20}")
my_list_20.sort()
print(f"sıralanmış liste={my_list_20}")

#sort fonksiyonu içerisine reverse=True parametresi verilirse listeyi büyükten küçüğe sıralar

my_list_21=[5,8,1,3,9,2,4,7,6,10]
print(f"karışık liste={my_list_21}")
my_list_21.sort(reverse=True)
print(f"büyükten küçüğe (tersten) sıralanmış liste={my_list_21}")

my_list_22=["Burdur","Akif","Üniversitesi","Mehmet","Ersoy"]
print(f"karışık liste={my_list_22}")
my_list_22.sort()
print(f"sıralanmış liste={my_list_22}")
#string ifadeler için ise alfabetik olarak sıralar
#itemlerin farklı veri tipinde olmaları hataya yol açacaktır.



#my_list_23 te olup my_list_24 te olmayan elemanları yeni bir listeye ekleyin
my_list_23=[1,2,3,4,5,6,7,8,9,10]
my_list_24=[7,8,9,10,11,12,13,14,15]
print(f"my_list_23 in içerisi {my_list_23}")
print(f"my_list_24 in içerisi {my_list_24}")
my_list_25=[]
for i in my_list_23:
    if i not in my_list_24: #not u silip sadece in yaparsak iki kümenin kesişimini buluruz
        my_list_25.append(i)
print(f"my_list_25 in içerisi {my_list_25}")

#1 ve 100 arasında (100 dahil)
#2 ye tam bölünenleri bir listeye
#3 e tam bölünenleri başka bir listeye
#4 e tam bölünenleri başka bir listeye
#5 e tam bölünenleri başka bir listeye ekleyip bunları yazdırın
my_list_bos=[]
my_list_26=[]
my_list_27=[]
my_list_28=[]
my_list_29=[]
for i in range(1,101):
    my_list_bos.append(i)
print(f"my_list_bos değerleri={my_list_bos}")
for i in my_list_bos:
    if i%2==0:
        my_list_26.append(i)
    if i%3==0:
        my_list_27.append(i)
    if i%4==0:
        my_list_28.append(i)
    if i%5==0:
        my_list_29.append(i)
print(f"2 ye tam bölünenler={my_list_26}")
print(f"3 e tam bölünenler={my_list_27}")
print(f"4 e tam bölünenler={my_list_28}")
print(f"5 e tam bölünenler={my_list_29}")

#python veri yapıları-2 : Set(Kümeler)
#setlerde elemanlar sırasızdır ve index numarası yoktur
#kümelerde sıralamanın hiçbir önemi yoktur
#Süslü parantez ile tanımlanır
#Süslü parantez aynı zamanda dictionary veri yapısının da simgesidir
#boş bir set oluşturmak için aşağıdaki söz dizimi takip edilir

my_set_1=set()
print(type(my_set_1))
#set veri yapısı kümelerle aynı özellikleri taşıdığı için 
#aşağıdaki işlemleri daha kısa kod ile yapabilir
#fark işlemleri (bir kümede olup diğerinde olmayan elemanlar)
#birleşim(union) işlemi (iki kümenin birleşimi)
#kesişim(intersection) işlemi (iki kümenin ortak elemanları)
#bir kümede aynı elemandan birden fazla olamaz
#yazdırırıken sadece bir tanesinin yazdırıldığını görürüz

kume_1={1,2,3,4,5,6,7,8,9,10}
kume_2={6,7,8,9,10,11,12,13,14,15}

#birinci kümede olup da ikinci kümede olmayan elemanlar 
print(f"küme 1 fark küme 2{kume_1.difference(kume_2)}") #difference metodu ile fark işlemi yapılır
#ikinci kümede olup da birinci kümede olmayan elemanlar
print(f"küme 2 fark küme 1 {kume_2.difference(kume_1)}")
#iki kümenin birleşimi
print(f"iki kümenin birleşimi işlemi{kume_1.union(kume_2)}")
#iki kümenin kesişimi
print(f"iki kümenin kesişimi {kume_1.intersection(kume_2)}")

#not kümelerde kesişim işlemi "-" işareti ile de yapılabilir
print(f"küme 1 fark küme 2 {kume_1-kume_2} gibi")
print(f"küme 2 fark küme 1 {kume_2-kume_1} gibi")

#iki listenin birleşimini yazan kod(değerler tekrar etmeyecek şekilde)(sete dönüştürmeden)
my_list_30=[1,2,3,4,5,6,7,8,9,10]
my_list_31=[6,7,8,9,10,11,12,13,14,15]
my_bos_list=[]
for i in my_list_30:
    my_bos_list.append(i)
for i in my_list_31:
    if i not in my_bos_list:
        my_bos_list.append(i)
print(f" bos listenin içi= {my_bos_list}")







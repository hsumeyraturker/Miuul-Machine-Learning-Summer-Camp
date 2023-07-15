#Python Alıştırmalar#
###GÖREV 1: Verilen değerlerin veri yapılarını inceleyiniz###

x=8
type(x)

y=3.2
type(y)

z=8j+18
type(z)

a="Hello World"
type(a)

b=True
type(b)

c=23<22
type(c)

l=[1,2,3,4]
type(l)

d={"Name":"Jake","Age":27,"Address":"Downtown"}
type(d)

t=("Machine Learning","Data Science")
type(t)

s={"Python","Machine Learning","Data Science"}
type(s)

###GÖREV 2:Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.Virgül ve nokta yerine space koyunuz,kelime kelime ayırınız###

text="The goal is to turn data into information, and information into insight"
text.upper().replace(","," ").replace("."," ").split()

###GÖREV 3:Verilen listeye adımları uygulayınız###

lst=["D","A","T","A","S","C","I","E","N","C","E"]

#adım 1: listenin eleman sayısına bakın.#
len(lst)

#adım 2: sıfırıncı ve onuncu indeksteki elemanları çağırınız.#
lst[0]
lst[10]

#adım 3: verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.#
new_list=lst[0:4]
new_list

#adım 4: sekizinci indeksteki elemanı silin.#
lst.pop(8)
lst

#adım 5: yeni bir eleman ekleyin.#
lst.append("HST")
lst

#adım 6: sekizinci indeksse "N" elemanını tekrar ekleyin.#
lst.insert(8,"N")
lst

###GÖREV 4: Verilen sözcük yapısına adımalrı uygulayınız.###

dict={'Christian':["America",18],'Daisy':["England",12],'Antonio':["Spain",22],'Dante':["Italy",25]}

#adım 1: key değerlerine erişiniz.#

dict.keys()

#adım 2: value'lara erişiniz.#

dict.values()

#adım 3: daisy key'ine ait 12 değerini 13 olarak güncelleyin.#

dict.update({"Daisy":["England",13]})
dict

#adım 4: key değeri ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.#

dict.update(({"Ahmet":["Turkey",24]}))
dict

#adım 5: antonio'yu dictionary'den siliniz.#

dict.pop("Antonio")
dict

###GÖREV 5: Argüman olarak bir liste alan,listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyonu yazınız.###

l=[2,13,18,93,22]

def func(list):

    even_list=[]
    odd_list=[]

    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
            return even_list,odd_list
even,odd= func(l)

###GÖREV 6: Verilen listede mühendislik ve tıp fakültelerinde dereceye giren öğrencilerin isimleri bulunmaktadır.Sıarsaıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fskültesi öğrenci sırasına aittir.Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırın.#

ogrenciler=["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
for i,x in enumerate(ogrenciler):
    if i<3:
        i+=1
        print("Mühendsilik Fakültesi",i,".öğrenci",x)
    else:
        i-=2
        print("Tıp Fakültesi",i,".öğrenci",x)

###GÖREV 7: Verilen listelerde sırayla dersin kodu,kredisi ve kontenjan bilgileri yer alıyor.Zip kullanarak ders bilgilerini bastırınız.###

ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi=[3,4,2,4]
kontenjan=[30,75,150,25]

for ders_kodu,kredi,kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişiidir")

###GÖREV 8: Verilen 2 adet setten 1.küme 2.kümeyi kapsıyor ise ortak elemanlarını,eğer kapsamıyor ise 2.kümenin 1.kümeden farkını yazdıracak fonksiyonu tanımlayınız.###

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)
kume(kume2,kume1)



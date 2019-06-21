# Python Homework-1
## Bu Çalışmanın Amacı
info.txt dosyasında ad_soyad,not formatında bulunan bilgiler ile kişilerin not ortalamasını hesaplama ve sıralama yapmayı içermektedir.
## Dosyadan Okuma İşlemi
Python'da dosyayı okumak için önce **open** fonsiyonu ile açma işlemi yapılır. open fonksiyonu parametre olarak dosya adresini alır ve sonuç olaraksa bir dosya nesnesi döndürür. Okuma işlemi de bu dosya nesnesi üzerinden yapılır.
<code> with open(filename, 'r') as info_file:
		for line in info_file: </code>
## Kullanılan Fonksiyonlar 
* **extract_data** fonksiyonu parametre olarak dosya adı almaktadır. Bu fonksiyon .txt dosyasındaki verileri okuyup onları virgüle göre split ediyor. Bu verilerin ilk itemları name değişkenine, ikinci itemleri score değşkenine atıyor. Daha sonra her isme karşılık gelen notları student_data değişkenine append ediyor. Fonksiyon student_data itemlanı return ediyor. 

* **print_func** fonksiyonu, hesaplanan verilerin belirli formatta ekrana çıktı vermesini sağlamaktadır.


# SteelSub

**Bu araç, kullanıcıların verdiği bir URL üzerinden subdomain'leri brute force (güçlü saldırı) yöntemiyle bulmalarına olanak tanır. Belirtilen bir listeyle subdomain'ler kontrol edilir ve her geçerli subdomain bulunduğunda kullanıcıya bildirilir.**

## Özellikler
**-Kullanıcıdan protokol seçimi alınır (https:// veya http://).
-Belirtilen bir URL üzerinden subdomain'ler aranır.
-Bir dosyadan alınan liste ile her subdomain teker teker test edilir.
-Geçerli subdomain'ler bulunduğunda, kullanıcıya bildirilir.
-Gereksinimler
-Python 3.x
-requests kütüphanesi**

__Kütüphaneyi yüklemek için terminal üzerinden şu komutu kullanabilirsiniz:__
'pip install requests'

## Kullanım
- Kodu çalıştırın.
- Test edilecek URL'yi girin.
- Kullanmak istediğiniz protokolü seçin (https:// veya http://).
- Bir dosya yolu girerek subdomain listesine ait dosyayı belirtin. (Her bir subdomain'in tek bir satırda olması gerekir.)


## Örnek Çıktı
-'Test edilecek url: example.com'
-'Protokol seç:'
-'1 = https 2 = http (1/2): 1'
-'Listenin tam yolunu girin: subdomains.txt'
-'Subdomain Bulundu! ---> https://sub1.example.com'
-'Subdomain Bulundu! ---> https://sub2.example.com'

import requests

def req(url):
    try:
        response = requests.get(url) 
        if response.status_code == 200:
            return url  
    except requests.exceptions.RequestException as e:
        pass 
    return None 
url = input("Test edilecek url: ")
secim = input("Protokol seç: \n1 = https 2 = http (1/2): ")

if secim == "1":
    protokol = "https://"
elif secim == "2":
    protokol = "http://"
else:
    print("Geçersiz protokol seçimi! Varsayılan olarak 'https://' kullanılacak.")
    protokol = "https://"

list = input("Listenin tam yolunu girin: ")

try:
    with open(list, "r") as ListFile:
        for line in ListFile:
            word = line.strip()
            TestUrl = protokol + word + "." + url
            sonuc = req(TestUrl)
            if sonuc:
                print("Subdomain Bulundu! ---> " + sonuc)
except FileNotFoundError:
    print("Dosya bulunamadı. Lütfen dosya yolunu kontrol edin.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")

import requests
import json

api_key = "793cae92ab6464377563ed26"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz türü: ") #USD
alinan_doviz = input("alinan döviz türü: ") #TRY
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsun: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"][alinan_doviz])
print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz,miktar * sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))

import requests
import json
import time
import sqlite3

cookie = '[{"domain":".www.webmotors.com.br","expirationDate":1664724302,"hostOnly":false,"httpOnly":false,"name":"AMCV_3ADD33055666F1A47F000101%40AdobeOrg","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"359503849%7CMCIDTS%7C18538%7CMCMID%7C38151117039513061930695441774644378972%7CMCAAMLH-1602257102%7C4%7CMCAAMB-1602257102%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1601659502s%7CNONE%7CvVersion%7C5.0.1"},{"domain":".webmotors.com.br","expirationDate":1657206067,"hostOnly":false,"httpOnly":false,"name":"_gcl_au","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"1.1.1759321197.1649430068"},{"domain":"www.webmotors.com.br","expirationDate":1680966067,"hostOnly":true,"httpOnly":false,"name":"blueID","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"46408684-8cf9-4e29-95c5-981a9bb45e79"},{"domain":".webmotors.com.br","expirationDate":1680966068,"hostOnly":false,"httpOnly":false,"name":"_hjid","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"11c97562-b9a6-4ca0-8abf-28eaecd0ace4"},{"domain":".webmotors.com.br","expirationDate":1659878757,"hostOnly":false,"httpOnly":false,"name":"_fbp","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"fb.2.1649430068181.1652798386"},{"domain":".webmotors.com.br","expirationDate":1683126037,"hostOnly":false,"httpOnly":false,"name":"__gads","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"ID=56395566c3d5161e:T=1649430037:S=ALNI_MZ7x9dvvfNAHQSGTHauXkvGb-bmsw"},{"domain":".webmotors.com.br","expirationDate":1683637536,"hostOnly":false,"httpOnly":false,"name":"_hjSessionUser_278928","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"eyJpZCI6ImYzMDMzYTVhLTk4MTctNTBiZS05NTU4LTc0NTZhZTI4YzE3YyIsImNyZWF0ZWQiOjE2NDk0MzAwNjgxMzYsImV4aXN0aW5nIjp0cnVlfQ=="},{"domain":".webmotors.com.br","expirationDate":1713461711,"hostOnly":false,"httpOnly":false,"name":"_ga","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"GA1.3.974137033.1649430081"},{"domain":".webmotors.com.br","expirationDate":1680966086,"hostOnly":false,"httpOnly":false,"name":"_pxvid","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"b21c7217-b74c-11ec-b897-6565574e6947"},{"domain":".webmotors.com.br","expirationDate":1675088166,"hostOnly":false,"httpOnly":false,"name":"_cc_id","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"f94e3b9a453abeeb924318ebc77983a8"},{"domain":".webmotors.com.br","expirationDate":1683637552,"hostOnly":false,"httpOnly":false,"name":"_hjMinimizedPolls","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"799378"},{"domain":".webmotors.com.br","expirationDate":1652364916,"hostOnly":false,"httpOnly":false,"name":"panoramaId_expiry","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"1652364916484"},{"domain":".webmotors.com.br","expirationDate":1652364916,"hostOnly":false,"httpOnly":false,"name":"panoramaId","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"e96437fa24cc762839e77345e7494945a70255a4be9b3c3ccde0ea2bc402bf49"},{"domain":"www.webmotors.com.br","expirationDate":1659567505,"hostOnly":true,"httpOnly":false,"name":"WebMotorsLastSearches","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"%5B%7B%22route%22%3A%22carros-usados%2Festoque%2Fhonda%2Fcivic%2F20-16v-flexone-sport-4p-cvt%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros-usados%26marca1%3DHONDA%26modelo1%3DCIVIC%26versao1%3D2.0%252016V%2520FLEXONE%2520SPORT%25204P%2520CVT%22%7D%2C%7B%22route%22%3A%22carros-usados%2Festoque%2Fhonda%2Fcivic%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros-usados%26marca1%3DHONDA%26modelo1%3DCIVIC%22%7D%2C%7B%22route%22%3A%22carros-usados%2Festoque%2Fhonda%2Fcity%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros-usados%26marca1%3DHONDA%26modelo1%3DCITY%22%7D%2C%7B%22route%22%3A%22carros-usados%2Festoque%2Fhonda%2Fcity%2F15-sport-16v-flex-4p-manual%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros-usados%26marca1%3DHONDA%26modelo1%3DCITY%26versao1%3D1.5%2520SPORT%252016V%2520FLEX%25204P%2520MANUAL%22%7D%2C%7B%22route%22%3A%22carros-usados%2Festoque%2Fhonda%2Faccord%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros-usados%26marca1%3DHONDA%26modelo1%3DACCORD%22%7D%2C%7B%22route%22%3A%22carros%2Festoque%2Ftoyota%2Fcorolla%22%2C%22query%22%3A%22%3Festadocidade%3Destoque%26marca1%3DTOYOTA%26modelo1%3DCOROLLA%22%7D%2C%7B%22route%22%3A%22carros%2Festoque%2Ftoyota%2Fcorolla%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros%26marca1%3DTOYOTA%26modelo1%3DCOROLLA%26anunciante%3DPessoa%2520F%25C3%25ADsica%22%7D%2C%7B%22route%22%3A%22carros%2Festoque%2Ftoyota%2Fcorolla%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros%26marca1%3DTOYOTA%26modelo1%3DCOROLLA%26anunciante%3DLoja%257CPessoa%2520F%25C3%25ADsica%22%7D%2C%7B%22route%22%3A%22carros%2Festoque%2Ftoyota%2Fcorolla%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros%26marca1%3DTOYOTA%26modelo1%3DCOROLLA%26anunciante%3DLoja%22%7D%2C%7B%22route%22%3A%22carros%2Festoque%2Ftoyota%2Fcorolla%22%2C%22query%22%3A%22%3Ftipoveiculo%3Dcarros%26marca1%3DTOYOTA%26modelo1%3DCOROLLA%26anunciante%3DConcession%25C3%25A1ria%257CLoja%22%7D%5D"},{"domain":".webmotors.com.br","hostOnly":false,"httpOnly":false,"name":"at_check","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"true"},{"domain":"www.webmotors.com.br","expirationDate":1652106356,"hostOnly":true,"httpOnly":false,"name":"WebMotorsVisitor","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"1"},{"domain":".webmotors.com.br","hostOnly":false,"httpOnly":false,"name":"AMCVS_3ADD33055666F1A47F000101%40AdobeOrg","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"1"},{"domain":".webmotors.com.br","expirationDate":1683137944,"hostOnly":false,"httpOnly":false,"name":"__gpi","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"UID=000003eada173d1c:T=1649441944:RT=1652100022:S=ALNI_Mb1lGDmIpGCPBuH20r4gUFjMTA34w"},{"domain":".webmotors.com.br","hostOnly":false,"httpOnly":false,"name":"s_cc","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"true"},{"domain":".webmotors.com.br","hostOnly":false,"httpOnly":false,"name":"pxcts","path":"/","sameSite":"lax","secure":false,"session":true,"storeId":"0","value":"31b58a26-cf95-11ec-9f28-774e4e5a6d62"},{"domain":".webmotors.com.br","expirationDate":1652103508,"hostOnly":false,"httpOnly":false,"name":"_hjSession_278928","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"eyJpZCI6IjUxMzkwOTZlLTU3MGEtNGU4Zi1iM2U4LTAxZDY2ZTBkZjk3NSIsImNyZWF0ZWQiOjE2NTIxMDAwNjg0ODUsImluU2FtcGxlIjpmYWxzZX0="},{"domain":".webmotors.com.br","expirationDate":1652103508,"hostOnly":false,"httpOnly":false,"name":"_hjAbsoluteSessionInProgress","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"0"},{"domain":"www.webmotors.com.br","hostOnly":true,"httpOnly":false,"name":"WMLastFilterSearch","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"%7B%22car%22%3A%22carros-usados%2Festoque%3Flkid%3D1000%22%2C%22bike%22%3A%22motos%2Festoque%22%2C%22estadocidade%22%3A%22estoque%22%2C%22lastType%22%3A%22car%22%2C%22cookie%22%3A%22v3%22%2C%22ano%22%3A%7B%7D%2C%22preco%22%3A%7B%7D%2C%22marca%22%3A%22%22%2C%22modelo%22%3A%22%22%7D"},{"domain":"www.webmotors.com.br","hostOnly":true,"httpOnly":false,"name":"WebMotorsDataFormLeads","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"%7B%22dataForm%22%3A%7B%22uniqueId%22%3A41251810%2C%22listingType%22%3A%22U%22%2C%22vehicleType%22%3A%22car%22%2C%22idGuid%22%3A%226a225cf5-90ea-4aa6-b8c7-31239a80e85b%22%2C%22make%22%3A%22MITSUBISHI%22%2C%22makeId%22%3A26%2C%22model%22%3A%22ASX%22%2C%22modelId%22%3A3194%2C%22version%22%3A%222.0%20MIVEC%20FLEX%20HPE-S%20AWD%20CVT%22%2C%22versionId%22%3A348007%2C%22yearModel%22%3A2020%2C%22yearFabrication%22%3A2019%2C%22price%22%3A145990%2C%22storeName%22%3A%22Cardinal%20Alphaville%22%2C%22storeDocument%22%3A%2205582269000651%22%2C%22sellerId%22%3A3851054%2C%22sellerType%22%3A%22PJ%22%2C%22city%22%3A%22Barueri%22%7D%7D"},{"domain":".webmotors.com.br","hostOnly":false,"httpOnly":false,"name":"s_sq","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"%5B%5BB%5D%5D"},{"domain":".webmotors.com.br","expirationDate":1652104556,"hostOnly":false,"httpOnly":false,"name":"gpv_v39","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"%2Fwebmotors%2Fcomprar%2Fhomepage"},{"domain":".webmotors.com.br","expirationDate":1686265536,"hostOnly":false,"httpOnly":false,"name":"cto_bundle","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"1426819keXN6eUlvaSUyQnJ6WWdRdmhZcFk5STN6dFg0JTJGMXJBJTJGQWlEUEREejVDbXhDcjhYZG1OUUlrd1lRN2klMkZUeUZPeWNWUUdkckpFQXRNR3gzOHhUR0hxVlhYS2ZONzk4dXZJMlQlMkZ2JTJCYjVPOUhZOEl4SFlmQ1BGRG1rb0ZtaUNqa2JsaVBJJTJGWDk1dmphd0wxYkpkbjd1ZWFPeUd2bUtsWFM5QkNnT1dQaEtOYms4cyUzRA"},{"domain":".webmotors.com.br","expirationDate":1652102899,"hostOnly":false,"httpOnly":false,"name":"_px3","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"b1f99d9948be0729836855f9eb054abef10dc3976b91c3ee85e0706dc372b649:c/wDwn5PpvgmHB7aQYhMy77TwjYsjNRn3LsQ+Su8diQKYCrakOL3Duv8oxlctyMaCJZA+AFvCxgOgGSHpc4z6A==:1000:0DfsdocyadjgEZ3XMCB3TrzauqhHR/gMycqJUXz80gviyD68bNYnh1KAbV/giB0utn5/0dihP5mOzj1/vZvxRMY74+y1g0k0QoxhDrupypueYgHufa76y0pNiGgk+zsvBvBR6Ak6+MYSXGLIhebXz0VZ9wVYDwmo8rnG+0dyKaQ6F8wXXWMoxWNyDP+RNrVXEGNSXpk4+hKXMQZhAd+hww=="},{"domain":".webmotors.com.br","expirationDate":1715261155,"hostOnly":false,"httpOnly":false,"name":"AMCV_3ADD33055666F1A47F000101%40AdobeOrg","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"1176715910%7CMCIDTS%7C19122%7CMCMID%7C38151117039513061930695441774644378972%7CMCAAMLH-1652707555%7C4%7CMCAAMB-1652707555%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1652109955s%7CNONE%7CvVersion%7C5.4.0"},{"domain":".webmotors.com.br","expirationDate":1715347558,"hostOnly":false,"httpOnly":false,"name":"mbox","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"PC#3bd7fe3d6b1f455096fd341002a542ab.34_0#1715347558|session#a95a871f7124456f939c4d399809fa83#1652104616"}]'

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,pt;q=0.8",
    "cache-control": "max-age=0",
    "cookie": cookie,
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}

bigbase = []


## aqui escolhe quantas paginas vao ser lidas 

page = 1
while page < 3:
    url = f"https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros-usados%2Festoque%3Flkid%3D1000&actualPage={page}&displayPerPage=100"

    time.sleep(3)
    r = requests.get(url=url, headers=headers)
    r.status_code

    base = json.loads(r.text)

    bigbase += base['SearchResults']
    page += 1

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

for offer in bigbase:
    uniqueId = offer['UniqueId']
    maker = offer['Specification']['Make']['Value']
    model = offer['Specification']['Model']['Value']
    price = offer['Prices']['Price']
    version = offer['Specification']['Version']['Value']
    yearfabrication = offer['Specification']['YearFabrication']
    yearmodel = offer['Specification']['YearModel']
    bodytype = offer['Specification']['BodyType']
    odometer = offer['Specification']['Odometer']
    color = offer['Specification']['Color']['Primary']
    sellertype = offer['Seller']['SellerType']
    city = offer['Seller']['City']
    state = offer['Seller']['State']
    
    cursor.execute ("""INSERT INTO tb_veiculo (idunico, marca, modelo, valor_veic, versao_veic, ano_frab, ano_veic, carroceria, km_veic, cor, vendedor, cidade, estado) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?)""", (uniqueId, maker, model, price,version, yearfabrication, yearmodel,  bodytype, odometer, color, sellertype, city, state))

    print(uniqueId,maker, model, price, version, yearfabrication, yearmodel,  bodytype, odometer, color, sellertype, city, state)


## COLOCANDO OS DADOS NO BANCO

conn.commit()

for linha in cursor.fetchall():
    print(linha)

    
conn.close()
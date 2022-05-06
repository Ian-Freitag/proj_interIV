import requests
import json

cookie = 'AMCV_3ADD33055666F1A47F000101@AdobeOrg=359503849|MCIDTS|18538|MCMID|38151117039513061930695441774644378972|MCAAMLH-1602257102|4|MCAAMB-1602257102|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1601659502s|NONE|vVersion|5.0.1; _gcl_au=1.1.1759321197.1649430068; blueID=46408684-8cf9-4e29-95c5-981a9bb45e79; _hjid=11c97562-b9a6-4ca0-8abf-28eaecd0ace4; _fbp=fb.2.1649430068181.1652798386; __gads=ID=56395566c3d5161e:T=1649430037:S=ALNI_MZ7x9dvvfNAHQSGTHauXkvGb-bmsw; _hjSessionUser_278928=eyJpZCI6ImYzMDMzYTVhLTk4MTctNTBiZS05NTU4LTc0NTZhZTI4YzE3YyIsImNyZWF0ZWQiOjE2NDk0MzAwNjgxMzYsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.3.974137033.1649430081; _pxvid=b21c7217-b74c-11ec-b897-6565574e6947; _cc_id=f94e3b9a453abeeb924318ebc77983a8; _hjMinimizedPolls=799378; at_check=true; AMCVS_3ADD33055666F1A47F000101@AdobeOrg=1; s_cc=true; pxcts=c967031a-cc7d-11ec-ad68-50774e655249; panoramaId_expiry=1652364916484; panoramaId=e96437fa24cc762839e77345e7494945a70255a4be9b3c3ccde0ea2bc402bf49; AMCV_3ADD33055666F1A47F000101@AdobeOrg=1176715910|MCIDTS|19118|MCMID|38151117039513061930695441774644378972|MCAAMLH-1652396251|4|MCAAMB-1652396251|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1651798651s|NONE|vVersion|5.4.0; WebMotorsDataFormLeads={"dataForm":{"uniqueId":41071125,"listingType":"U","vehicleType":"car","idGuid":"e10592f8-ef4f-4271-b64d-95095c3328e1","make":"HONDA","makeId":16,"model":"CITY","modelId":3053,"version":"1.5 SPORT 16V FLEX 4P MANUAL","versionId":345073,"yearModel":2014,"yearFabrication":2013,"price":53890,"storeName":"AJC MULTIMARCAS","storeDocument":"26202669000150","sellerId":3859015,"sellerType":"PJ","city":"Santo André"}}; cto_bundle=oWi4iV9keXN6eUlvaSUyQnJ6WWdRdmhZcFk5STRCM3ZZQk0zYWpMcGxQZ3Y3VHJVZGxGSmVGeDJ6c0hxQ2d1T0Y5aTJlUU1uSkwlMkI3UWdGcnd3SWNscGhFSjAwcHliZ05HdDhpZkMzOEZWRUNiN1lIWkpMaG9sZzBGUEh6OXZEbkR0MGZsTGpHSjY3ZzViOFJieUFMYVVoRU54aXFHenI4VU8wQ0p4clpPWGVybzZZcThzJTNE; WMLastFilterSearch={"car":"carros-usados/estoque/honda/civic/20-16v-flexone-sport-4p-cvt?tipoveiculo=carros-usados&marca1=HONDA&modelo1=CIVIC&versao1=2.0%2016V%20FLEXONE%20SPORT%204P%20CVT","bike":"motos/estoque","estadocidade":"estoque","lastType":"car","cookie":"v3","ano":{},"preco":{},"marca":"HONDA","modelo":"CIVIC"}; WebMotorsLastSearches=[{"route":"carros-usados/estoque/honda/civic/20-16v-flexone-sport-4p-cvt","query":"?tipoveiculo=carros-usados&marca1=HONDA&modelo1=CIVIC&versao1=2.0%2016V%20FLEXONE%20SPORT%204P%20CVT"},{"route":"carros-usados/estoque/honda/civic","query":"?tipoveiculo=carros-usados&marca1=HONDA&modelo1=CIVIC"},{"route":"carros-usados/estoque/honda/city","query":"?tipoveiculo=carros-usados&marca1=HONDA&modelo1=CITY"},{"route":"carros-usados/estoque/honda/city/15-sport-16v-flex-4p-manual","query":"?tipoveiculo=carros-usados&marca1=HONDA&modelo1=CITY&versao1=1.5%20SPORT%2016V%20FLEX%204P%20MANUAL"},{"route":"carros-usados/estoque/honda/accord","query":"?tipoveiculo=carros-usados&marca1=HONDA&modelo1=ACCORD"},{"route":"carros/estoque/toyota/corolla","query":"?estadocidade=estoque&marca1=TOYOTA&modelo1=COROLLA"},{"route":"carros/estoque/toyota/corolla","query":"?tipoveiculo=carros&marca1=TOYOTA&modelo1=COROLLA&anunciante=Pessoa%20F%C3%ADsica"},{"route":"carros/estoque/toyota/corolla","query":"?tipoveiculo=carros&marca1=TOYOTA&modelo1=COROLLA&anunciante=Loja%7CPessoa%20F%C3%ADsica"},{"route":"carros/estoque/toyota/corolla","query":"?tipoveiculo=carros&marca1=TOYOTA&modelo1=COROLLA&anunciante=Loja"},{"route":"carros/estoque/toyota/corolla","query":"?tipoveiculo=carros&marca1=TOYOTA&modelo1=COROLLA&anunciante=Concession%C3%A1ria%7CLoja"}]; mbox=PC#3bd7fe3d6b1f455096fd341002a542ab.34_0#1715036306|session#aee0a3eef04c49bebc2496f2d0435d55#1651793224; s_sq=webmglobaldev=%26pid%3D%252Fwebmotors%252Fcomprar%252Fresultado%26pidt%3D1%26oid%3Dfunctionar%2528%2529%257B%257D%26oidt%3D2%26ot%3DP; __gpi=UID=000003eada173d1c:T=1649441944:RT=1651854469:S=ALNI_Mb1lGDmIpGCPBuH20r4gUFjMTA34w'
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

page = 1
while page < 5:
    url = f'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros-usados/estoque?{page}kid=1000'

    r = requests.get(url=url, headers=headers)
    r.status_code

    base = json.loads(r.text)

    bigbase += base['SearchResults']
    page += 1

for offer in bigbase:
    fabricante = offer['Specification']['Make']['Value']
    model = offer['Specification']['Model']['Value']
    preco = offer['Prices']['Price']
    version = offer['Specification']['Version']['Value']
    yearfabrication = offer['Specification']['YearFabrication']
    yearmodel = offer['Specification']['YearModel']

    print(fabricante, model, preco, version, yearfabrication, yearmodel)



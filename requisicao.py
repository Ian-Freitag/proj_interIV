import requests
from bs4 import BeautifulSoup

url = 'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros-usados/estoque?lkid=1000'

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,pt;q=0.8",
    "cache-control": "max-age=0",
    "cookie": 'at_check=true; AMCVS_3ADD33055666F1A47F000101@AdobeOrg=1; AMCV_3ADD33055666F1A47F000101@AdobeOrg=1176715910|MCIDTS|19112|MCMID|20375147638814100760063595025116409245|MCAAMLH-1651857973|4|MCAAMB-1651857973|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1651260373s|NONE|vVersion|5.4.0; WebMotorsVisitor=1; s_cc=true; _gcl_au=1.1.1763827827.1651253182; pxcts=7c4f6a37-c7e1-11ec-ac4e-6f6959634453; _pxvid=7c4f5b4a-c7e1-11ec-ac4e-6f6959634453; blueID=e5ad3959-099f-45cb-bf87-83ae02da68c4; _hjid=d914d458-7386-44ca-a246-c0e9b6d02dcb; _fbp=fb.2.1651253183639.188121532; _hjSessionUser_278928=eyJpZCI6IjU2NGU4ODgxLWZkZjgtNTAxZi04OWVmLTI3MWIwMjhiZDEyNSIsImNyZWF0ZWQiOjE2NTEyNTMxODMwNDIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_278928=eyJpZCI6IjVhY2RlODFiLTNmY2EtNDY1NS1hNjMyLWM1ZWRkYzYyZWY0NSIsImNyZWF0ZWQiOjE2NTEyNTMxODM2ODgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; cto_bundle=kF7BCF80enlSQmtCME5xd3FQNDExNFk5eHBvUHhLQjlZSWNoNDZCS25nOGc0SUU1Uk1CTFRzRENCbVYzaE10S0laYTh6cWVqQkZKa3B2R0VHUDZFcVBmWlZxZ0RWN2VUVFgweDNFMzl2WFp2cHdlbTZIcGFVSlR0M2dobDRybURuSUF1SHA2cEF0MGVoemxPd1dzOUk1REclMkYzQSUzRCUzRA; _cc_id=ae8908271d0ee1d10934eb626a7510b2; panoramaId_expiry=1651857984960; panoramaId=9b205110181ce2f17e2ad5832f084945a70267f186c592f76b48d7a4ee081520; WMLastFilterSearch={"car":"carros/estoque/toyota/corolla?estadocidade=estoque&marca1=TOYOTA&modelo1=COROLLA&idcmpint=t1:c17:m07:webmotors:modelo::toyota corolla&autocomplete=corolla&autocompleteTerm=TOYOTA COROLLA","bike":"motos/estoque","estadocidade":"estoque","lastType":"car","cookie":"v3","ano":{},"preco":{},"marca":"TOYOTA","modelo":"COROLLA"}; gpv_v39=/webmotors/comprar/resultado; s_sq=[[B]]; WebMotorsLastSearches=[{"route":"carros/estoque/toyota/corolla","query":"?estadocidade=estoque&marca1=TOYOTA&modelo1=COROLLA&autocompleteTerm=TOYOTA COROLLA"}]; mbox=session#328e02f1579d4203a61708075ecf8628#1651255034|PC#328e02f1579d4203a61708075ecf8628.34_0#1714498305; _px3=50060f1bf9beaf6394633d728d206a450ca99083e2deffe81dc3c622bc5d8b26:7LHdXENsrzlTOVg2zABvzUXrnRiVKDSNdf+jU/4qHLIz1MMKNKfRj7gxsBnh9A10CZZ1IhoVUILTrkWNYPKLRg==:1000:m4OCm7D0TMvb2ewuzRmAMhBcIkLbwJ6THsL90eDL/JBxGNNOquL4CGLeddgoc/0jQhi64nNDC8XROdlU3GurJhwHQg24RKDgv2skilg1xKsoSNCPWctjy1tyYr8I/hU3Ro8ZvZ5iRseAVODCtNJJeaR+Lm5Ug2BKb+yorUVN0W5DCVnU4aC4sLJ1ogBl/OOwSNV5wTFj/pHNqC738J49qw==',
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

r = requests.get(url=url, headers=headers)
r.status_code

print(r.text) 

from bs4 import BeautifulSoup

import requests

couponNum = '쿠폰넘버'
session = requests.Session()

url = "https://order.goobne.co.kr:8481/login/data_process.aspx"

# mode : nomemberloginproc 비회원 승인
payload="{\r\n    \"mode\":\"nomemberloginproc\"\r\n}"
headers = {
	'Content-Type': 'application/json'
}

response = session.request("POST", url, headers=headers, data=payload)
getSessionCookieNomember = session.cookies.get_dict()

# https://order.goobne.co.kr:8481/order/delivery.aspx
# 중간에 본인의 집주소 Cookie가 필요!
# 해당 사이트에서 주소찾기 후, ASP.NET_SessionId 하나 더 가져오기

# getSessionCookieMyaddress = session.cookies.get_dict()

url = "https://order.goobne.co.kr:8481/order/ecoupon_proc.aspx"

payload="{\r\n    \"mode\":\"isc_ck\",\r\n    \"channel\":\"giftishow\",\r\n    \"coupon_number\":\"" + str(couponNum) + "\"\r\n    }"
headers = {
	'Referer': 'https://order.goobne.co.kr:8481/order/ecoupon.aspx',
	'Cookie': 'ASP.NET_SessionId=' + getSessionCookieMyaddress['ASP.NET_SessionId'],
	'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# 결과값 출력!
# EX) {"ResultDt":{"ResultCode":"481","ResultMsg":"이미 에 에서 사용된 쿠폰입니다.","BrandCd":"","BrandNm":"","UseBranchId":"
#      ","UseBranchNm":"","UseDtm":" ","ProductCount":"","ProductList": { "ProductDt" : [{
#       "ProductId":"","ProductIdLink":"","ProductNm":"","ProductPrice":"","BalancePrice":""}] }} }
print(response.text['ResultDt']['ResultMsg'])
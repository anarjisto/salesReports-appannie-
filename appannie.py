__author__ = 'anarjisto'
import json
import urllib2

MY_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def sales(appID, date):
    url = "https://api.appannie.com/v1/accounts/" + str(
        appID) + "/sales?break_down=application+date&start_date=" + date + "&end_date=" + date + "&currency=USD"
    req = urllib2.Request(url)
    req.add_header('Authorization', 'bearer ' + MY_API_KEY)
    resp = urllib2.urlopen(req)
    content = resp.read()
    response = json.loads(content)
    revenue = 0.0
    for app in response["sales_list"]:
        revenue += float(app["revenue"]["app"]["promotions"])
        revenue += float(app["revenue"]["app"]["downloads"])
        revenue += float(app["revenue"]["app"]["updates"])
        revenue += float(app["revenue"]["app"]["refunds"])
    return revenue


req = urllib2.Request('https://api.appannie.com/v1/accounts')
req.add_header('Authorization', 'bearer ' + MY_API_KEY)
resp = urllib2.urlopen(req)
content = resp.read()
response = json.loads(content)
acts = response['account_list']
date = ""
try:
    date = response['account_list'][0]['last_sales_date']
except:
    print("seems like you have no accounts added on appannie")
revenue = 0.0
for account in acts:
    revenue += sales(account['account_id'], account['last_sales_date'])

print("total sales for " + date + " = " + str(revenue) + " USD")


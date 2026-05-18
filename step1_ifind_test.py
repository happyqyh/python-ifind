from iFinDPy import *
import pandas as pd

print("程序开始")

login_result = THS_iFinDLogin("grzqgf188 ","03sTd67H")
print("登录结果：", login_result)

data = THS_HistoryQuotes(
    "000001.SZ",
    "open,high,low,close",
    "period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB,fill:Previous",
    "2024-01-01",
    "2024-03-01"
)

table0 = data["tables"][0]
dates = table0["time"]
values = table0["table"]

df = pd.DataFrame(values)
df.insert(0, "date", dates)
df.insert(0, "thscode", table0["thscode"])

print(df)

df.to_csv("ifind_test.csv", index=False, encoding="utf-8-sig")

print("已生成 ifind_test.csv")
print("程序结束")
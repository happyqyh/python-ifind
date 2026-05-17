from iFinDPy import *

# 登录
login = THS_iFinDLogin('grzqgf188', '03sTd67H')
print("login =", login)

# 测试数据（平安银行收盘价）
data = THS_BD("000001.SZ", "ths_close_price_stock", "")
print(data)
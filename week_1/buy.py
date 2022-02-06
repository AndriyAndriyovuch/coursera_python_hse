price_dol = int(input())
price_cen = int(input())
item_num = int(input())

res_dol = (item_num * price_dol) + (item_num * price_cen // 100)
res_cen = item_num * price_cen % 100

print(res_dol, res_cen)

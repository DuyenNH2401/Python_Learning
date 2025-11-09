import datetime
name = "Alice"
age = 30
price = 12345.67
today = datetime.datetime.now()

print(f"Xin chào, tôi là {name:<10}. Tôi {age} tuổi.")
print(f"Giá sản phẩm: ${price:,.2f}")
print(f"Hôm nay là ngày {today:%A}, ngày {today.day} tháng {today.month} năm {today.year}")
"""
Tính xem còn bao nhiêu minutes thì tới tết
Đồng hồ hiện h giờ m phút định dạng 24 giờ và tết vào lúc 0h và 0p
"""

h, m = map(int, input().split())
if h > 0 and m > 0:
    count_hour = 24-h if m == 0 else 24-h-1
    minutes = count_hour * 60 + (60-m) if m>0 else count_hour * 60
    print(minutes)
else: print("0")

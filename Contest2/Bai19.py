"""
có n xu để mua bia
cứ 3 vỏ chai thì được 1 chai
hỏi người đó có bao nhiêu chai bia
"""
n = int(input())
count = n//28
them = count//3
du = count % 3
while True:
    if du >= 3:
        them +=1
        du-=3
    else: break
print(them+count)

nguyen = 10000
chuoi = "Hello"
thap_phan = 1.2
phuc = 1 + 2j
dung_sai = True
print(type(nguyen), type(chuoi), type(thap_phan), type(phuc), type(dung_sai), sep=" \n ")
#trong Python thì số nguyên rất lớn

#in ra số thập phân thứ n
e = 23.12845678
print()
#cách 1: round(a, n)
print(round(e,2))
#cách 2:
print(f"{e:.2f}")
#cách 3:print("%.nf" % e)
print("%.2f" % e)
print()


#Số phức var.real in ra phần thực var.imag in ra phần ảo
so_phuc = 3 + 5j
print(so_phuc.real)
print(so_phuc.imag)
print()

#muốn ghi sâu kí tự trên nhiều dòng ta có thể dùng """______"""
print("""xin chao
Viet nam""")
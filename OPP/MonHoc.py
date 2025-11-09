import csv
import os

ds_mon_hoc = []

class MonHoc:
    def __init__(self, ma_mon, ten_mon, so_tc):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.so_tc = so_tc
    #hiển thị môn học
    def show(self):
        return f"Mã môn học: {self.ma_mon}\nTên môn học: {self.ten_mon}\nSố tín chỉ: {self.so_tc}"

def main():
    try:
        while True:
            os.system("cls")
            print("1. Nhap danh sach mon hoc")
            print("2. Doc danh sach mon hoc tu tep")
            print("3. Hien thi danh sach mon hoc")
            print("4. Them mot mon hoc moi")
            print("5. Xoa mot mon hoc theo ma")
            print("6. Tim kiem mon hoc")
            print("7. Luu va thoat")
            choose = int(input("Lựa chọn chức năng(1-7): "))
            os.system('cls' if os.name == 'nt' else 'clear')

            match choose:
                case 1:
                    get_subject()
                    write_subject_to_file()
                case 2:
                    print("Danh sach mon hoc duoc doc tu tep la")
                    read_subject_from_file()
                    input()
                case 3:
                    show_subjects_lst()
                    input()
                case 4:
                    add_subject()
                case 5:
                    del_subject_byid()
                    input()
                case 6:
                    search_subject()
                    input()
                case 7:
                    write_subject_to_file()
                    break
    except:
        pass

def get_subject():
    n = int(input("Nhập số lượng môn học: "))
    for i in range(n):
        ma_mh = input("Nhập mã môn học: ")
        ten_mh = input("Nhập tên môn học: ")
        so_tc = int(input("Nhập số tín chỉ: "))
        mh = MonHoc(ma_mh, ten_mh, so_tc)
        ds_mon_hoc.append(mh)

def show_subjects_lst():
    print("Danh sách môn học là: ")
    for i in range(len(ds_mon_hoc)):
        print(f"-----Thong tin môn học {i + 1} -----")
        print(ds_mon_hoc[i].show())

def add_subject():
    print("Nhập vào thông tin môn học cần thêm")
    ma = input("Mã môn học: ")
    ten = input("Tên môn học: ")
    tc = int(input("Số tín chỉ: "))
    mh = MonHoc(ma, ten, tc)
    ds_mon_hoc.append(mh)

def del_subject_byid():
    id = str(input("Nhap id mon hoc"))
    for i in range(len(ds_mon_hoc)):
        if ds_mon_hoc[i].ma_mon == id:
            ds_mon_hoc.remove(ds_mon_hoc[i])
        else: print("ID bạn nhập không khớp với môn học trong danh sách")

def search_subject():
    check = False
    loai = -1
    while loai not in [1, 2, 3]:
        loai = int(input("""Bạn đang muốn tím kiếm thông tin gì:
    1. Mã môn học
    2. Tên môn học
    3. Số tín chỉ
    Chọn: """))

    if loai == 1:
        thong_tin = str(input("Nhập mã môn: "))
        for i in range(len(ds_mon_hoc)):
            if ds_mon_hoc[i].ma_mon == thong_tin:
                index = i
                check = True

    elif loai == 2:
        thong_tin = str(input("Nhập tên môn: "))
        for i in range(len(ds_mon_hoc)):
            if ds_mon_hoc[i].ten_mon == thong_tin:
                index = i
                check = True

    elif loai == 3:
        thong_tin = int(input("Số tín chỉ: "))
        for i in range(len(ds_mon_hoc)):
            if ds_mon_hoc[i].so_tc == thong_tin:
                index = i
                check = True

    if check:
        print(ds_mon_hoc[index].show())
    else:
        print("Thông tin bạn cung cấp không đúng!")

def write_subject_to_file():
    with open("MonHoc.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["stt","Ma_mon", "Ten_mon", "so_tin_chi"])
        for i in range(len(ds_mon_hoc)):
            writer.writerow([str(i+1), ds_mon_hoc[i].ma_mon, ds_mon_hoc[i].ten_mon, ds_mon_hoc[i].so_tc])

def read_subject_from_file():
    with open("MonHoc.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            stt, ma, ten, tc = row
            if stt == "stt":
                continue
            print(f"-----Đây là môn học thứ {stt}-----")
            print(f"Ma mon hoc: {ma}")
            print(f"Ten mon hoc: {ten}")
            print(f"So tin chi: {tc}")

if __name__ == '__main__':
    main()

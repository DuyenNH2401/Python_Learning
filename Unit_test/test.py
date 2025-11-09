def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = str(s)
    if len(s) > 1:
        num_place = -1
    else: return False

    if s.isalnum() and 2 <= len(s) <= 6:
        for index in range(len(s)):
            if s[index].isnumeric():
                num_place = index
                break
        if num_place != -1:
            head_sliced = s[0:num_place]
            tail_sliced = s[num_place:]

            if tail_sliced[0] == "0" or not tail_sliced.isnumeric():
                return False
            if not head_sliced.isalpha():
                return False

        else: return True
    else:
        return False
    return True


if __name__ == "__main__":
    main()

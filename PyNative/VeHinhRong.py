def draw_hollow_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

# Ví dụ: Vẽ hình chữ nhật rộng 10 và cao 5
draw_hollow_rectangle(3, 4
                      )

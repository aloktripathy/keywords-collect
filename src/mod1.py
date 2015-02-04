import human_size

while True :
    size = int(input("Size of the file: "))
    mode = True
    print(human_size.approximate_size(size, mode))
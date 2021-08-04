def main(num):
    data = []
    run = True
    while run:
        if (num % 2) == 0:
            num = num/2
        elif num == 1:
            run = False
        else:
            num = num*3+1

        data.append(num)

    return data

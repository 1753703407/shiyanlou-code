
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    x = [7, 17, 27, 37, 47, 57, 67,70,71,72,73,74,75,76, 77,78,79, 87, 97]
    for i in range(1, 101):
        if i % 7 == 0:
            continue
        elif i in x:
            continue
        else:
            print(i)

# This is a sample Python script.
from app import app

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def odd_count(number):
    array = []
    for i in range(1, number):
        if i % 2 != 0:
            array.append(i)
    return array

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    app.run(debug=True)
    # print(odd_count(100))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

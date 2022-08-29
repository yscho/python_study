import checkOS



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
    print('Hello, world!')

    print(checkOS.currentOS_fullname())
    print(checkOS.currentOS_shortname())

import platform



def currentOS_fullname():
    os_full_name = platform.platform()
    return os_full_name

def currentOS_shortname():
    os_full_name = platform.platform()
    os_short_name = os_full_name.split('-')
    return os_short_name[0]

if __name__ == '__main__':
    print(currentOS_fullname())
    print(currentOS_shortname())
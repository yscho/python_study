#출처: https://info-lab.tistory.com/230 [:: IT School ::]
class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    BRIGHT_END = '\033[0m'

    def COLOR_PRINT(self,str_tmp, color_tmp):
        print(color_tmp + str_tmp + self.RESET)

if __name__ == '__main__':
    print(Colors.RED + 'TEST' + Colors.RESET)
    #print(BRIGHT_YELLOW + 'TEST' + BRIGHT_END)
    print(Colors.RED + 'TE' + Colors.BLUE + 'ST' + Colors.RESET)


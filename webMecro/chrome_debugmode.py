import os,sys

chrome_path = r'C:\Program Files\Google\Chrome\Application'
chrome_option = r'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"'
def run_chrome_debug():
    os.chdir(chrome_path)
    print(chrome_option)
    os.system(chrome_option)

#https://doitgrow.com/38

if __name__ == '__main__':

    run_chrome_debug()
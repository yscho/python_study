import psutil
from psutil import AccessDenied

PROCNAME = "LgeInspectionAvn.exe"
# LgeInspectionAvn.exe
# IMTMemtool.exe

# 실행중인 프로세스를 순차적으로 검색

# print(psutil.cpu_percent())
def check_string(include_str, target_str):
    if include_str in target_str:
        print("include " + include_str + " FULL name : " + target_str)
        return 1
    else:
        return 0


for proc in psutil.process_iter():
    try:
        # if proc.name == PROCNAME:
        #print(proc)
        if check_string(PROCNAME, str(proc.name) ) :
          print(proc.pid)
          proc.kill()
    except (PermissionError, AccessDenied):
        print("Permission Error")

'''
    # 프로세스 이름을 ps_name에 할당
    ps_name = proc.name()
    # 실행 명령어와 인자(argument)를 리스트 형식으로 가져와 cmdline에 할당
    cmdline = proc.cmdline()
  #print('NAME:', ps_name, ' CMD:', cmdline)
'''

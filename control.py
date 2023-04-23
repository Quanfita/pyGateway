import subprocess
import sys
import os
import platform

system = platform.system()

def start():
    try:
        # 后台启动脚本
        subprocess.Popen(['python', 'server.py'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True if system == 'Windows' else False)
        print('tts.py 已启动')
    except Exception as e:
        print(e)

def stop():
    try:
        if system == 'Linux':
            # 查找并杀死脚本相关进程
            subprocess.Popen(['pkill', '-f', 'tts.py'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        elif system =='Windows':
            # 查找并杀死脚本相关进程
            os.system('taskkill /f /im python.exe /t /fi "IMAGE NAME eq server.py" >nul')
        print('tts.py 已停止')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 处理命令行参数
    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            start()
        elif sys.argv[1] == 'stop':
            stop()
        else:
            print('无效参数')
    else:
        print('用法: python manage.py {start|stop}')

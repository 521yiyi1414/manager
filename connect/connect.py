import  os
import  time
import pyautogui as pag
import win32gui, win32com.client
import win32con
import win32api
import random

def isConnected():
    exit_code = os.system('ping 166.111.139.12 -n 4')
    if(exit_code == 0):
        return True
    return False

def click_position(hwd, x_position, y_position):
    long_position = win32api.MAKELONG(x_position, y_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)

try:
    pag.FAILSAFE = False
    while True:
        win_mesg = win32gui.FindWindow(u'SRun3KUIMessageFrame',u'TUnet2018版')
        if(win_mesg):
            win32gui.PostMessage(win_mesg, win32con.WM_CLOSE, 0, 0)
        status = isConnected()
        if(status == False):
            print("net connected failure")
            screenWidth, screenHeight = pag.size()  #获取屏幕的尺寸
            #print(screenWidth,screenHeight)
            x,y = pag.position()   #获取当前鼠标的位置
            posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
            print(posStr)
            win = win32gui.FindWindow(u'{65C60B77-DF6D-8F6C-26BF-2A92E4B368E3}',u'TUnet2018版')
            if(win != 0):
                print(hex(win))
                left, top, right, bottom = win32gui.GetWindowRect(win)
                #print(left, top, right, bottom)
                parent_x = (right - left) / 2 + left
                parent_y = (bottom - top) * 0.65 + top
                print(parent_x,parent_y)
                #shell = win32com.client.Dispatch("WScript.Shell")
                #shell.SendKeys('%')
                #win32gui.SetForegroundWindow (win)
                win32gui.SendMessage(win, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
                win32gui.ShowWindow(win, 1)
                
                #pag.click(parent_x,parent_y,button='left')
                #click_position(win,int(parent_x),int(parent_y))
                win32gui.PostMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
                win32gui.PostMessage(win, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
            #time.sleep(1)
        else:
            randomx=random.randint(1,200)
            randomy=random.randint(1,200)
            print(randomx,randomy)
            pag.moveTo(randomx,randomy)
            print("net connected sucess")
            win_show = win32gui.FindWindow(u'{65C60B77-DF6D-8F6C-26BF-2A92E4B368E3}',u'TUnet2018版')
            if(win_show != 0):
                win32gui.ShowWindow(win_show, win32con.SW_MINIMIZE)
            time.sleep(5)
except KeyboardInterrupt:
    print('end....')




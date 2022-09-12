import ast
import atexit
import json
from time import sleep
import win32gui
import win32api
from ext_library import doNothing


''' App remembers window positions and monitor count at startup
     and then tries to recover it when montor count changes'''


def exit_handler():
    print('Exiting app')
    file = open(filename, 'w+')
    #file.write('monitor count = ')
    #file.write(str(monitorCount)+'\n')
    file.write(str(windowsPos))
    doNothing()



windowClassBlacklist = ['Progman', 'Windows.UI.Core.CoreWindow', 'RAIL_WINDOW']
windowTitleBlacklist = ['']


def checkIsWindowInBlacklist(hwnd):
    for className in windowClassBlacklist:
        if win32gui.GetClassName(hwnd) == className:
            #print(hex(hwnd), 'className skipped.......')
            return True
    for winTitle in windowTitleBlacklist:
        if win32gui.GetWindowText(hwnd) == winTitle:
            #print(hex(hwnd), win32gui.GetClassName(hwnd), 'winText skipped.......')
            return True
    return False


def addWindowHandleToList(hwnd, wndList: list):
    if win32gui.IsWindowVisible(hwnd) and not checkIsWindowInBlacklist(hwnd):
        wndList.append(hwnd)


def retrieveWindowPosition(windowHandle, windowPlacement):
    windowHandle = 0xf095c
    windowPlacement = (0, 1, (-32000, -32000), (-1, -1), (305, 95, 1693, 941))
    win32gui.ShowWindow(windowHandle, 1)
    win32gui.SetWindowPlacement(windowHandle, windowPlacement)


atexit.register(exit_handler)

filename = 'backToMon.settings'
file = open(filename,'r')
windowsPos={}
windowsPosStr = file.read()
file.close()
windowsPos=ast.literal_eval(windowsPosStr)
print(windowsPos)
sleep(5)
while 1:
    monitorCount = win32api.GetSystemMetrics(80)
    windowsList = []
    win32gui.EnumWindows(addWindowHandleToList, windowsList)
    winPos={}
    for winHandle in windowsList:
        winPos[winHandle]= win32gui.GetWindowPlacement(winHandle)
    windowsPos.update({monitorCount: winPos})
    print("Number of monitors", monitorCount)
    print(windowsPos)
    print("-----------------------------------------------------------")
    sleep(5)

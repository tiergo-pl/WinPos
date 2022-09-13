import ast
import atexit
import json
import yaml
from time import sleep
import win32gui
import win32api
from ext_library import doNothing


''' App remembers window positions and monitor count at startup
     and then tries to recover it when montor count changes'''


def exit_handler():
    print('Exiting app')
    # file = open(yaml_filename, 'w+')
    # #file.write('monitor count = ')
    # #file.write(str(monitorCount)+'\n')
    # file.write(str(windowsPos))
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
    # windowHandle = 0xf095c
    # windowPlacement = (0, 1, (-32000, -32000), (-1, -1), (305, 95, 1693, 941))
    win32gui.ShowWindow(windowHandle, 1)
    win32gui.SetWindowPlacement(windowHandle, windowPlacement)


atexit.register(exit_handler)

# filename = 'backToMon.settings'
yaml_filename = 'back_to_mon.yaml'
# file = open(filename,'r')
windowsPos={}
# windowsPosStr = file.read()
# file.close()
# windowsPos=ast.literal_eval(windowsPosStr)
# with open(yaml_filename,'r') as stream:
#     windowsPos = yaml.safe_load(stream)
print(windowsPos,'\n')
sleep(5)
while 1:
    monitorCount = win32api.GetSystemMetrics(80)
    desktop_resolution = {'width': win32api.GetSystemMetrics(78), 'height': win32api.GetSystemMetrics(79)}
    windowsList = []
    win32gui.EnumWindows(addWindowHandleToList, windowsList)
    winPos={}
    for winHandle in windowsList:
        winPos[winHandle] = {'window_title': win32gui.GetWindowText(winHandle),
                            'window_class': win32gui.GetClassName(winHandle),
                            'window_placement': win32gui.GetWindowPlacement(winHandle)}
    windowsPos.update({'monitorCount': monitorCount})
    windowsPos.update({'desktop_resolution': desktop_resolution})
    windowsPos.update({"windows_positions": winPos})
    with open(yaml_filename, 'w') as yaml_file:
        yaml.safe_dump(windowsPos, yaml_file, sort_keys=False)
    print("Number of monitors", monitorCount)
    print(windowsPos)
    print("-----------------------------------------------------------")
    break
    sleep(5)

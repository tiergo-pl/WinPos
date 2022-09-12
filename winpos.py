
from distutils.log import error
from time import sleep
import win32gui
import win32api

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


def retrieveWindowPosition():
    windowHandle = 0xf095c
    windowPlacement = (0, 1, (-32000, -32000), (-1, -1), (305, 95, 1693, 941))
    win32gui.ShowWindow(windowHandle, 1)
    win32gui.SetWindowPlacement(windowHandle, windowPlacement)


print('--------------------------------------------------')
windowsList = []
win32gui.EnumWindows(addWindowHandleToList, windowsList)
for winHandle in windowsList:
    print(hex(winHandle), win32gui.GetWindowText(winHandle), "| Class:", win32gui.GetClassName(
        winHandle), win32gui.GetClientRect(winHandle), win32gui.GetWindowPlacement(winHandle), win32api.MonitorFromWindow(winHandle))
monitorList = win32api.EnumDisplayMonitors()
print(monitorList)
print('Number of monitors:', win32api.GetSystemMetrics(80))
for monitor in list(monitorList):
    print('Monitor info:', win32api.GetMonitorInfo(monitor[0]))
try:
    retrieveWindowPosition()
except error as e:
    print('Exception:', type(e).__name__)

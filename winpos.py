
import win32gui
import win32api


def addWindowHandleToList(hwnd, wndList: list):
    if win32gui.IsWindowVisible(hwnd):
        wndList.append(hwnd)


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

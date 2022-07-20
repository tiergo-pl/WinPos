
import win32gui


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        print(hex(hwnd), win32gui.GetWindowText(hwnd), "| Class:",win32gui.GetClassName(hwnd), win32gui.GetClientRect(hwnd), win32gui.GetWindowPlacement(hwnd))

def addWindowHandleToList(hwnd, wndList: list):
    if win32gui.IsWindowVisible(hwnd):
        wndList.append(hwnd)


win32gui.EnumWindows(winEnumHandler, None)
print('--------------------------------------------------')
windowsList = []
win32gui.EnumWindows(addWindowHandleToList,windowsList)
for winHandle in windowsList:
    print(hex(winHandle), win32gui.GetWindowText(winHandle), "| Class:", win32gui.GetClassName(
        winHandle), win32gui.GetClientRect(winHandle), win32gui.GetWindowPlacement(winHandle))

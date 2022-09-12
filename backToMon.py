from time import sleep
import win32gui
import win32api


''' App remembers window positions and monitor count at startup
     and then tries to recover it when montor count changes'''
file = open('backToMon.settings', 'w')
try:
    while 1:
        monitorCount = win32api.GetSystemMetrics(80)
        print("Number of monitors", monitorCount)
        sleep(5)
except Exception as ex:
     file.write('monitor count = ', monitorCount, 'Exception:', ex)

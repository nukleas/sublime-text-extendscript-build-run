import win32com.client
import sys
import os
app = win32com.client.dynamic.Dispatch("InCopy.Application")
script = os.path.realpath(sys.argv[1])
print os.path.realpath(sys.argv[1])
app.DoScript(script, 1246973031)

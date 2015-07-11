import shutil
import datetime
import os
now = datetime.datetime.now()

import errno, os, stat, shutil

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise
#remove old back up
for f in os.listdir("E:\Windows Backup"):
    temp = "E:\Windows Backup\\" + f
    file_time = datetime.datetime.fromtimestamp(os.path.getmtime(temp))
    if file_time < now + datetime.timedelta(weeks=-4):
        shutil.rmtree(temp, ignore_errors=False, onerror=handleRemoveReadonly)
#backup
src = "C:\Users\Michael\Saved Games"
dst = "E:\\Windows Backup\\" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "\Saved Games"
shutil.copytree(src, dst)
src = "C:\Users\Michael\Desktop"
dst = "E:\\Windows Backup\\" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "\Desktop"
shutil.copytree(src, dst)
src = "C:\Users\Michael\Documents"
dst = "E:\\Windows Backup\\" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "\Documents"
shutil.copytree(src, dst)

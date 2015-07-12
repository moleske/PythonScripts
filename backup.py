import shutil
import datetime
import os
import errno, os, stat, shutil
import argparse

now = datetime.datetime.now()
parser = argparse.ArgumentParser()
parser.add_argument("directory", metavar='D', nargs='+', help="Directory(ies) to backup")
parser.add_argument("backup_location", metavar='B', help="Directory to make the backup in")
args = parser.parse_args()

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise
#remove old back up
for f in os.listdir(args.backup_location):
    temp = args.backup_location + f
    print temp
    file_time = datetime.datetime.fromtimestamp(os.path.getmtime(temp))
    if file_time < now + datetime.timedelta(weeks=-4):
        shutil.rmtree(temp, ignore_errors=False, onerror=handleRemoveReadonly)
#backup
for src in args.directory:
    dst = args.backup_location + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "\Documents"
    shutil.copytree(src, dst)

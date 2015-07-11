import os
import string
import re

ar = ['Episode 1','Episode 2','Episode 3', 'Episode 4', 'Episode 5', 'Episode 6', 'Episode 7', 'Episode 8', 'Episode 9']
dir = "E:\Stuff\TV\TVSHOWDIR"
files = os.listdir(dir)



for files in files:
    if files.endswith(".mkv"):
        strs = string.split(files, '.')
        name = ''
        pattern = '[S][0]'
        pattern2 = 'X264.*'
        for strs in strs:
            if re.match(pattern, strs):
                strs = string.replace(string.lstrip(strs, 'S0'), 'E', '')
                name = name + ' - ' + strs + ' - ' + ar[string.atoi(strs[1:])-1]
            elif strs == 'mkv' or strs == 'H' or strs == 'I' or strs == 'E' or strs == 'L' or strs == 'D' or strs == 'ini':
                name = name + '.' + strs
            elif strs == 'HDTV' or  re.match(pattern2, strs) or strs == '720p' or strs == 'WEBRip' or strs == 'x264-W4F' or strs == 'x264-KILLERS' or strs == 'PROPER':
                name = name
            else:
                name = name + ' ' + strs
        name = string.strip(name)
        #num = str(int(string.split(strs[0],'title')[1]) + 8)
    #    if int(num) < 10:
     #       num = '0' + num
      #  name = name + num + ' - ' + ar[int(num) - 1] + '.' + strs[1]
        print name
        os.rename(dir + '\\' + files, dir + '\\' + name)
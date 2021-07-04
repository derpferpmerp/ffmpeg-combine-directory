#!/usr/bin/python3

import os
import re
import subprocess
import sys


args = sys.argv[1::] if len(sys.argv) > 1 else False
fns = []
EXTENSIONS = ["mp4", "mov", "mkv", "webm", "avi", "flv"]
for f in os.listdir([args[0] if args else os.getcwd()][0]):
	if not [True for x in EXTENSIONS if x in f]:
		print(f'[DEV] Ignoring Item "{f}"')
		continue
	fext = (f.replace(re.sub("\\..*", "", f), "")[1::]).lower()
	if fext != "mp4" and fext in EXTENSIONS:
		tomp4 = re.sub("\\..*", ".mp4", f)
		subprocess.call(
			f'echo "Converting File {f} to .mp4"; ffmpeg-bar -i {f} {tomp4}', shell=True,
		)
	fns.append(f)

outstr = "MP4Box "
for fn in fns:
	outstr += f"-cat '{fn}' "
outstr += "output.mp4"
print(outstr)

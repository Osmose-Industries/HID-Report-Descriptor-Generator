import sys
import os

path = sys.argv[1]
if(not (os.path.exists(path) and os.path.isfile(path))):
    exit

file=open(path, "r")
lines=file.readlines()

bytesStr=""

for line in lines:
    line = line.strip()
    line = line.split("#")[0]
    line = line.replace(" ", "")
    for byteStr in line.split(","):
        byteStr=byteStr.removeprefix("0x")
        if(byteStr != ""):
            bytesStr += byteStr

with open("report_desc.bin", "wb") as binary_file:
    binary_file.write(bytes.fromhex(bytesStr))
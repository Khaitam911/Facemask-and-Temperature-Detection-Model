import socket
import cv2
import time
import subprocess
import os

Bash_script_location = os.path.join(os.getcwd(), "flirpi", "bash_scripts", "single_read_nc.sh")
img_location = "/mnt/ramdisk/temp.png"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
while True:
    start_time = time.time()
    # rc = subprocess.call("/home/tho/Lepton_Project/Test_folder/Test_bash.sh", shell=True)
    rc = subprocess.call(Bash_script_location, shell=True)
    img = cv2.imread(img_location, -1)
    b = bytearray(img)
    # sock.sendto(b, ("192.168.100.7", 5002))
    # sock.sendto(b, ("192.168.100.6", 5002))
    sock.sendto(b, ("192.168.31.255", 5002))
    time.sleep(0.08)
    end_time = time.time()
    # print("Frame sent in %.4f" % (end_time - start_time))

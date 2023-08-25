from model import model
import os
import time
i=0
class_ofmodel=0
#{'c2': 0, 'c0': 1, 'c7': 2, 'c4': 3, 'c3': 4, 'c9': 5, 'c8': 6, 'c5': 7, 'c1': 8, 'c6': 9}

while i<10:
    print("Foto captureing...")
    path_image=f"/home/omer/Desktop/rpi_proje/photo/image_{i}.jpg"

    os.system(f"raspistill -o {path_image}")
   
    print("Foto captured")
    print("Model working...")
    class_ofmodel=model(path_image)
    
    print("Result :")
    os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
        
    if class_ofmodel[0]==1:
        print("normal state")
        os.system("cansend can0 123#11")
        time.sleep(3)
        
    else:
        print("anormal state")
        os.system("cansend can0 123#22")
        time.sleep(3)
        

    os.system("sudo /sbin/ip link set can0 down")
        
    i=i+1

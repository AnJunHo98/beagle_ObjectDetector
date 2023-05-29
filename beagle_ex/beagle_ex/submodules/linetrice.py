from roboid import *
import roboidai as ai
import roboidai.lab as lab
cam = ai.Camera('ip0')
beagle = Beagle()

velocity = 30

def control_beagle(center_x, ref_x):
    diff= (center_x - ref_x)
    leftvel = velocity - 0.1* diff
    rightvel = velocity +0.1*diff
    beagle.wheels(leftvel, rightvel)
    wait(100)
    print(leftvel,rightvel)
    
while True:
    image = cam.read()
    if image is not None:
        width = image.shape[1]
        height = image.shape[0]
        output = image.copy()
        ref_x, _ = lab.find_blue_track_xy(image,output,window_height=50)
    
    control_beagle(width//2, ref_x)
    cam.show(output)
    
    if cam.check_key(10) == 'esc': break
    beagle.stop()
    #wait(100)
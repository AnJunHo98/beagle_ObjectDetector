from roboid import *

beagle = Beagle()

beagle.start_lidar()
beagle.wait_until_lidar_ready()
print('lidar is ready.')

# when hand found
def condition():
    return beagle.front_lidar() < 100

# move backward for 1 second after beep sound
def move():
    beagle.beep()
    beagle.move_backward()

while_do(condition, move)
wait(-1) # wait forever
dispose()
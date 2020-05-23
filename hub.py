from Laser import laser_base
from digitalio import DigitalInOut
import board
import rio_coms
import leds

xshut = laser_base.xshut
lasers = laser_base.vl53
enabled = True

xshut.append(DigitalInOut(board.D21))
xshut.append(DigitalInOut(board.D20))

laser_base.set_addresses()
#leds.setup(board.D0, 30)

while enabled:
    if rio_coms.disabled():
        enabled = False
    else:
        #leds.normal_Rotation(4)
        for i in range(len(lasers)):
            rio_coms.send_value(int(laser_base.distance(i)), i)


#leds.rainbow_cycle(0.01)
print("Que rainbow leds")
laser_base.reset_addresses()
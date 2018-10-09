import time
from car import *

#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =========================================for==============================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        pass


if __name__ == "__main__":
    try:
        # Example Of Front Servo Motor Control
        steering = front_wheels.Front_Wheels(db='config')
        steering.center_alignment()
        time.sleep(1)

        # Example Of Real Motor Control
        accelerator = rear_wheels.Rear_Wheels(db='config')
        accelerator.ready()
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)

        #case 1 (15cm)

        distance1 = -1
        distance2 = -1
        while True:
            accelerator.go_forward(30)
            distance2 = distance_detector.get_distance()
            print("distance is >> ", distance2)
            print("distance is >> ", distance1)
            if 0 < distance1 <= 15 and 0 < distance2 <= 15:
                accelerator.stop()
                break
            distance1 = distance2

        accelerator.go_backward(30)
        time.sleep(4)
        accelerator.stop()

        #case 2(20cm)

        distance1 = -1
        distance2 = -1
        while True:
            accelerator.go_forward(50)
            distance2 = distance_detector.get_distance()
            print("distance is >> ", distance2)
            print("distance is >> ", distance1)
            if 0 < distance1 <= 20 and 0 < distance2 <= 20:
                accelerator.stop()
                break
            distance1 = distance2

        accelerator.go_backward(30)
        time.sleep(4)
        accelerator.stop()

        #case 3(25cm)

        distance1 = -1
        distance2 = -1
        while True:
            accelerator.go_forward(70)
            distance2 = distance_detector.get_distance()
            print("distance is >> ", distance2)
            print("distance is >> ", distance1)
            if 0 < distance1 <= 25 and 0 < distance2 <= 25:
                accelerator.stop()
                break
            distance1 = distance2

        accelerator.go_backward(30)
        time.sleep(4)
        accelerator.stop()

        accelerator.power_down()

    except KeyboardInterrupt:
        accelerator.stop()
        accelerator.power_down()
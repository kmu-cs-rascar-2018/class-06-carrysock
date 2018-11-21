from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    def car_startup(self):


        while True:
            self.car.accelerator.go_forward(30)

            data = self.car.line_detector.read_digital()
            if data == [0, 0, 1, 0, 0]:
                self.car.steering.turn(90)
            elif data == [1, 0, 0, 0, 0]:
                self.car.steering.turn(55)
            elif data == [1, 1, 0, 0, 0]:
                self.car.steering.turn(60)
            elif data == [0, 1, 0, 0, 0]:
                self.car.steering.turn(80)
            elif data == [0, 1, 1, 0, 0]:
                self.car.steering.turn(80)
            elif data == [0, 0, 0, 0, 1]:
                self.car.steering.turn(125)
            elif data == [0, 0, 0, 1, 1]:
                self.car.steering.turn(120)
            elif data == [0, 0, 0, 1, 0]:
                self.car.steering.turn(100)
            elif data == [0, 0, 1, 1, 0]:
                self.car.steering.turn(100)
            elif data == [0, 0, 0, 0, 0]:
                self.car.steering.turn(55)
                self.car.accelerator.go_backward(30)


            distance = self.car.distance_detector.get_distance()
            print(distance)

            if 0 < distance <= 30:  # 장애물
                while True:
                    self.car.steering(110)
                    data = self.car.line_detector.read_digital()
                    if data!=[0,0,0,0,0]:
                        self.car.steering.turn(55)
                        break

                while True:
                    self.car.steering.turn(55)
                    data = self.car.line_detector.read_digital()
                    if data!= [0,0,0,0,0]:
                        self.car.steering.turn(110)
                        break





if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        myCar.drive_parking()

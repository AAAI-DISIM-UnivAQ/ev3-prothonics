import prothonics
import numpy as np
# eat=just increase the score
# vrep robot sensor takılacak yer , hocaya sor
# robotun dönüş haraketlerini ayarla
# herbir kare boyutunu optimal olarak ayarla


# if frontColorSensor==yellow:
#    move_forward()
#    eat()
# elif rightColorSensor==yellow:
#    turn_right()
#    move_forward()
#    eat()
# elif leftColorSensor==yellow:
#    turn_left()
#    move_forward()
#    eat()
# elif frontColorSensor==white:
#    move_forward()
# elif rightColorSensor==white:
#    turn_right()
#    move_forward()
# elif leftColorSensor==white:
#    turn_left()
#    move_forward()
# else: #frontColorSensor==red and rightColorSensor==red and leftColorSensor==red
#    turn_backward()


def map_decision_to_action(decision):
    switcher = {
        "MoveForward": move_forward,
        "MoveBackward": move_backward,
        "TurnRight": turn_right,
        "TurnLeft": turn_left,
        "Eat": eat
    }
    func = switcher.get(decision, lambda: "Undefined decision")
    func()


def move_forward():
    print("move forward")
    # tank fonk. çalıştırılacak


def turn_right():
    print("turn right")


def turn_left():
    print("turn left")


def move_backward():
    print("move backward")


def eat():
    print("eat")


color_sensor_front = 6  # ColorSensor(INPUT_3)
color_sensor_right = 6
color_sensor_left = 4
colors = ["Unknown", "Black", "Blue", "Green", "Yellow", "Red", "White",
          "Brown"]


def main():

    blindRobot = prothonics.Prothonics(1, 1)
    blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")

    # fstring -> string içerisinde variable çağırabilme
    blindRobot.useBrain().reactTo(
        f"perception(['{colors[color_sensor_front]}', '{colors[color_sensor_right]}', '{colors[color_sensor_left]}'])",  "takeDecision()")
    print("Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    decision = blindRobot.useBrain().useMemory().getAllDecisions()[0][0]

    for i in eval(decision):
        map_decision_to_action(i['D'])


if __name__ == '__main__':
    main()

import sys
import tty
import termios
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('teleop_turtle')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

    def publish_velocity(self, twist,direction):
        print(f"{direction} - Linear Velocity: {twist.linear.x}, Angular Velocity: {twist.angular.z}")
        self.publisher.publish(twist)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main(args=None):
    rclpy.init(args=args)
    teleop_turtle = TeleopTurtle()
    print("""
    ### Controle do Robô ###

    Use as seguintes teclas para controlar o robô:

        W
      A S D
        X

    Comandos:
    - W: Move o robô para frente.
    - A: Vira o robô para a esquerda.
    - X: Move o robô para trás.
    - D: Vira o robô para a direita.
    - S: Para o robô imediatamente.
    """)
    while True:
        keyPressed = getch()    
        if ord(keyPressed) == 3:
            break
        twist = Twist()
        match keyPressed:
            case "a":
                twist.linear.x = 0.0
                twist.angular.z = 1.0
                teleop_turtle.publish_velocity(twist, "Esquerda")
            case "d":
                twist.linear.x = 0.0
                twist.angular.z = -1.0
                teleop_turtle.publish_velocity(twist, "Direita")
            case "w":
                twist.linear.x = -0.2
                twist.angular.z = 0.0
                teleop_turtle.publish_velocity(twist, "Frente")
            case "x":
                twist.linear.x = 0.2
                twist.angular.z = 0.0
                teleop_turtle.publish_velocity(twist, "Trás")
            case "s":
                print("stop")
                twist.linear.x = 0.0
                twist.angular.z = 0.0
                teleop_turtle.publish_velocity(twist)
            
    rclpy.shutdown()
if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    main()
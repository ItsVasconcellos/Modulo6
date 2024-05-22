
import sys
import tty
import termios
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger

class KeyboardTeleop(Node):

    def __init__(self):
        super().__init__('teleop_turtle')
        self.velocity = self.create_publisher(Twist, "/velocity", 10)
        self.kill_client = self.create_client(Trigger, "kill_robot_service")

    def publish_velocity(self, twist):
        self.velocity.publish(twist)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
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
    rclpy.init()
    keyboard_telop_node = KeyboardTeleop()
    while rclpy.ok():

        keyPressed = getch()    
        if ord(keyPressed) == 3:
            break
        twist = Twist()
        match keyPressed:
            case "a":
                twist.linear.x = 0.0
                twist.angular.z = 1.0
                keyboard_telop_node.publish_velocity(twist)
            case "d":
                twist.linear.x = 0.0
                twist.angular.z = -1.0
                keyboard_telop_node.publish_velocity(twist)
            case "w":
                twist.linear.x = -0.2
                twist.angular.z = 0.0
                keyboard_telop_node.publish_velocity(twist)
            case "x":
                twist.linear.x = 0.2
                twist.angular.z = 0.0
                keyboard_telop_node.publish_velocity(twist)
            case "s":
                print("stop")
                twist.linear.x = 0.0
                twist.angular.z = 0.0
                keyboard_telop_node.publish_velocity(twist)

    keyboard_telop_node.kill_client.wait_for_service()
    request = Trigger.Request()
    future = keyboard_telop_node.kill_client.call_async(request)
    rclpy.spin_until_future_complete(keyboard_telop_node, future)
    response = future.result()
    if response.success:
        print("Robot killed successfully")
    else:
        print("Failed to kill robot")
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    keyboard_telop_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    main()
    
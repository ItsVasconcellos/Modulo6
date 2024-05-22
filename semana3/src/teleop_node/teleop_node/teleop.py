
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('teleop_turtle')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.velocity_client = self.create_subscription(Twist, '/velocity', self.velocity_callback, 10)
        self.current_velocity = Twist()
        self.direction = ""

    def velocity_callback(self, msg):
        if self.current_velocity != msg.data:
            self.current_velocity = msg.data
            self.find_direction()
            self.get_logger().info(f"{self.direction} - Linear Velocity: {self.current_velocitylinear.x}, Angular Velocity: {self.current_velocity.angular.z}")
            self.publisher.publish(self.current_velocity)

    def find_direction(self):
        if(self.current_velocity.x != 0):
            if(self.current_velocity.x > 0):
                self.direction = "Frente"
            else:
                self.direction = "Trás"
        else:
            if(self.current_velocity.z > 0):
                self.direction = "Direita"
            else:
                self.direction = "Esquerda"
            

def main(args=None):
    rclpy.init(args=args)
    teleop_turtle = TeleopTurtle()
    rclpy.spin(teleop_turtle)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

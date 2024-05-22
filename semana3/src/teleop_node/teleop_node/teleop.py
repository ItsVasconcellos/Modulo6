
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger


class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('teleop_turtle')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.velocity_client = self.create_subscription(Twist, '/velocity', self.velocity_callback, 10)
        self.current_velocity = Twist()
        self.direction = ""
        self.kill_robot_service = self.create_service(Trigger, 'kill_robot', self.kill_robot_callback)
        self.is_available = True

    def kill_robot_callback(self, request, response):
        # Add your code here to handle the kill_robot service request
        # For example, you can stop the robot's movement by setting the current_velocity to zero
        self.current_velocity.linear.x = 0.0
        self.current_velocity.angular.z = 0.0
        self.publisher.publish(self.current_velocity)
        response.success = True
        response.message = "Robot killed"
        self.is_available = False
        return response

    def velocity_callback(self, msg):
        print(msg)
        if self.is_available:
            self.current_velocity = msg
            self.find_direction()
            print((f"{self.direction} - Linear Velocity: {self.current_velocity.linear.x }, Angular Velocity: {self.current_velocity.angular.z}"))
            self.publisher.publish(self.current_velocity)

    def find_direction(self):
        if(self.current_velocity.linear.x != 0):
            if(self.current_velocity.linear.x > 0):
                self.direction = "Frente"
            else:
                self.direction = "Trás"
        else:
            if(self.current_velocity.angular.z > 0):
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

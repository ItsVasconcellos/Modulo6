import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time

class DrawingTurtle(Node):
    def __init__(self,turtle_name):
        super().__init__(turtle_name)
        self.turtle_name = turtle_name
        self.spawn_turtle = self.create_client(Spawn, '/spawn')
        self.kill_turtle = self.create_client(Kill, '/kill')
        self.set_pen = self.create_client(SetPen, f'/{self.turtle_name}/set_pen')
        self.draw = self.create_publisher(Twist, f'/{self.turtle_name}/cmd_vel',10)
        kill_original = self.kill_turtle.call_async(Kill.Request(name='turtle1'))

    def spawn(self):
        spawn = self.spawn_turtle.call_async(Spawn.Request(x=5.5, y=5.5, theta=0.0, name=self.turtle_name))
        rclpy.spin_until_future_complete(self, spawn)
        new_turtle_name = spawn.result().name
        print(new_turtle_name)

    def kill(self,name):
        kill = self.kill_turtle.call_async(Kill.Request(name=name))
        rclpy.spin_until_future_complete(self, kill)

    def set_pen_color(self):
        set_pen = self.set_pen.call_async(SetPen.Request(r=20, g=255, b=20, width=1, off=0))
        rclpy.spin_until_future_complete(self, set_pen)

    def draw_circle(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        for _ in range(10):
            self.draw.publish(msg)
            time.sleep(1)
    
    def draw_p(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        # Draw vertical line
        for _ in range(5):
            self.draw.publish(msg)
            time.sleep(1)
        # Stop
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.draw.publish(msg)
        time.sleep(1)
        # Draw horizontal line
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        for _ in range(3):
            self.draw.publish(msg)
            time.sleep(1)
        # Stop
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.draw.publish(msg)
        time.sleep(1)
        # Draw diagonal line
        msg.linear.x = 2.0
        msg.angular.z = -1.0
        for _ in range(3):
            self.draw.publish(msg)
            time.sleep(1)
        # Stop
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.draw.publish(msg)
        time.sleep(1)
        # Draw vertical line
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        for _ in range(5):
            self.draw.publish(msg)
            time.sleep(1)
        # Stop
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.draw.publish(msg)
        time.sleep(1)


def main(args=None):
    rclpy.init(args=args)
    draw_turtle = DrawingTurtle("VASC0")
    draw_turtle.spawn()
    draw_turtle.set_pen_color()
    draw_turtle.draw_circle()
    draw_turtle.kill(draw_turtle.turtle_name)

if __name__ == '__main__':
    main()
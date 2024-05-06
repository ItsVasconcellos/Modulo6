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
        self.set_pen = self.create_client(SetPen, '/teste/set_pen')

    def spawn(self):
        spawn = self.spawn_turtle.call_async(Spawn.Request(x=5.5, y=5.5, theta=0.0, name=self.turtle_name))
        rclpy.spin_until_future_complete(self, spawn)
        new_turtle_name = spawn.result().name
        print(new_turtle_name)

    def kill(self):
        kill = self.kill_turtle.call_async(Kill.Request(name=self.turtle_name))
        rclpy.spin_until_future_complete(self, kill)

    def set_pen(self):
        set_pen = self.set_pen.call_async(SetPen.Request(r=255, g=255, b=255, width=1, off=0))
        rclpy.spin_until_future_complete(self, set_pen)

def main(args=None):
    rclpy.init(args=args)
    draw_turtle = DrawingTurtle("VASC0")
    draw_turtle.spawn()

if __name__ == '__main__':
    main()
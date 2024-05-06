import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time

#Classe para criar uma tartaruga e manipular a mesma
class DrawingTurtle(Node):
    def __init__(self,turtle_name):
        super().__init__(turtle_name)
        self.turtle_name = turtle_name
        self.spawn_turtle = self.create_client(Spawn, '/spawn')
        self.kill_turtle = self.create_client(Kill, '/kill')
        self.set_pen = self.create_client(SetPen, f'/{self.turtle_name}/set_pen')
        self.draw = self.create_publisher(Twist, f'/{self.turtle_name}/cmd_vel',10)
        
    # Função para remover a tartaruga original do node
    def kill_original(self):
        kill = self.kill_turtle.call_async(Kill.Request(name='turtle1'))
        rclpy.spin_until_future_complete(self, kill)

    # Função para criar uma nova tartaruga
    def spawn(self):
        spawn = self.spawn_turtle.call_async(Spawn.Request(x=5.5, y=5.5, theta=0.0, name=self.turtle_name))
        rclpy.spin_until_future_complete(self, spawn)
        new_turtle_name = spawn.result().name
        print(new_turtle_name)

    # Função para remover a tartaruga
    def kill(self,name):
        kill = self.kill_turtle.call_async(Kill.Request(name=name))
        rclpy.spin_until_future_complete(self, kill)

    # Função para setar a cor da caneta
    def set_pen_color(self):
        set_pen = self.set_pen.call_async(SetPen.Request(r=20, g=255, b=20, width=1, off=0))
        rclpy.spin_until_future_complete(self, set_pen)

    # Função para desenhar um círculo
    def draw_circle(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        for _ in range(8):
            self.draw.publish(msg)
            time.sleep(1)
    
    # Função para desenhar a letra P
    def draw_p(self):
        msg = Twist()
        time.sleep(1)
        # Linha vertical
        msg.linear.y = 1.25
        msg.angular.z = 0.0
        for _ in range(2):
            self.draw.publish(msg)
            time.sleep(1)
        msg.linear.x = 0.5
        msg.angular.z = -2.0
        # Círculo do P
        for _ in range(3):
            self.draw.publish(msg)
            time.sleep(1)


def main(args=None):
    rclpy.init(args=args)
    # Instanciando a classe DrawingTurtle para desenhar o P do escudo do Palmeiras
    draw_turtle_p = DrawingTurtle("PalmeirasTurtle")
    draw_turtle_p.spawn()
    draw_turtle_p.kill_original()
    draw_turtle_p.set_pen_color()
    draw_turtle_p.draw_p()
    draw_turtle_p.kill(draw_turtle_p.turtle_name)

    # Instanciando a classe DrawingTurtle para desenhar um círculo
    draw_turtle_c = DrawingTurtle("CircleTurtle")
    draw_turtle_c.spawn()
    draw_turtle_c.set_pen_color()
    draw_turtle_c.draw_circle()
    draw_turtle_c.kill(draw_turtle_c.turtle_name)

if __name__ == '__main__':
    main()
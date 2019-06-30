import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Control(Node):
    def __init__(self):
        super().__init__("turtlebot3_burger")

        self.pub = self.create_publisher(Twist, "/cmd_vel")

        self.twist = Twist()

        l = 0.3
        a = 0.5

        while True:
            self.run(l, a)

    def run(self, l, a):
        self.twist.linear.x = float(l)
        self.twist.angular.z = float(a)

        self.pub.publish(self.twist)

def main():
    rclpy.init()

    node = Control()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
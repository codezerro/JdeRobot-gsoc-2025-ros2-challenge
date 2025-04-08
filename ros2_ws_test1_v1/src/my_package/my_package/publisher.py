import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'greeting_topic', 10)
        timer_period = 1.0  # Publish every 1 second
        self.timer = self.create_timer(timer_period, self.publish_message)
    
    def publish_message(self):
        msg = String()
        msg.data = 'Hello! ROS2 is fun.'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
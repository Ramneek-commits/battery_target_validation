import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped


class FakeTargetPublisher(Node):

    def __init__(self):
        super().__init__('fake_target_publisher')

        self.publisher_ = self.create_publisher(
            PoseStamped,
            '/battery_target',
            10
        )

        self.timer = self.create_timer(
            2.0,
            self.publish_target
        )

        self.get_logger().info(
            'Fake CV Target Publisher started'
        )

    def publish_target(self):

        msg = PoseStamped()

        msg.header.stamp = (
            self.get_clock().now().to_msg()
        )

        msg.header.frame_id = 'world'

        # Synthetic target representing future CV output
        msg.pose.position.x = 0.40
        msg.pose.position.y = 0.10
        msg.pose.position.z = 0.05

        # Neutral quaternion orientation
        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0

        self.publisher_.publish(msg)

        self.get_logger().info(
            'Published fake battery target: '
            'x=0.40, y=0.10, z=0.05'
        )


def main(args=None):

    rclpy.init(args=args)

    node = FakeTargetPublisher()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            'Fake Target Publisher stopped by user'
        )

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
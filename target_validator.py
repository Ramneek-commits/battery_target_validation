import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped


class TargetValidator(Node):

    def __init__(self):
        super().__init__('target_validator')

        self.subscription = self.create_subscription(
            PoseStamped,
            '/battery_target',
            self.validate_target,
            10
        )

        # Temporary development workspace limits.
        # These should later be aligned with the actual Gazebo scene.
        self.x_min = 0.10
        self.x_max = 0.80

        self.y_min = -0.50
        self.y_max = 0.50

        self.z_min = 0.00
        self.z_max = 0.60

        self.allowed_frames = ['world', 'base_link']

        self.get_logger().info(
            'Battery Target Validator started'
        )

    def validate_target(self, msg):

        x = msg.pose.position.x
        y = msg.pose.position.y
        z = msg.pose.position.z
        frame = msg.header.frame_id

        self.get_logger().info(
            f'Received target: frame={frame}, '
            f'x={x:.3f}, y={y:.3f}, z={z:.3f}'
        )

        errors = []

        # Coordinate frame validation
        if frame not in self.allowed_frames:
            errors.append(
                f'Unexpected coordinate frame: {frame}'
            )

        # Numerical validation
        if not all(math.isfinite(value) for value in [x, y, z]):
            errors.append(
                'Target contains invalid numerical values'
            )

        # Workspace validation
        if not self.x_min <= x <= self.x_max:
            errors.append(
                'X coordinate outside configured workspace'
            )

        if not self.y_min <= y <= self.y_max:
            errors.append(
                'Y coordinate outside configured workspace'
            )

        if not self.z_min <= z <= self.z_max:
            errors.append(
                'Z coordinate outside configured workspace'
            )

        # Final validation result
        if errors:
            self.get_logger().error('TARGET REJECTED')

            for error in errors:
                self.get_logger().error(
                    f'Reason: {error}'
                )

        else:
            self.get_logger().info('TARGET VALID')


def main(args=None):

    rclpy.init(args=args)

    node = TargetValidator()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            'Target Validator stopped by user'
        )

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
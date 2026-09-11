from setuptools import find_packages, setup

package_name = 'battery_target_validation'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(
        exclude=['test']
    ),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=[
        'setuptools'
    ],
    zip_safe=True,
    maintainer='Ramneek Singh Bhangu',
    maintainer_email='',
    description=(
        'ROS 2 target-pose validation layer for the '
        'E-Waste Battery Extraction simulation.'
    ),
    license='Apache-2.0',
    tests_require=[
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            (
                'target_validator = '
                'battery_target_validation.'
                'target_validator:main'
            ),
            (
                'fake_target_publisher = '
                'battery_target_validation.'
                'fake_target_publisher:main'
            ),
        ],
    },
)
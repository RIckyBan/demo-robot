from launch import LaunchDescription
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    gzserver_exe = launch.actions.ExecuteProcess(
        cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_init.so',
             launch.substitutions.LaunchConfiguration('world')],
        output='screen'
    )
    gzclient_exe = launch.actions.ExecuteProcess(
        cmd=['gzclient'],
        output='screen'
    )
    demo = launch_ros.actions.Node(
        package='demo_program',
        node_executable='demo',
        output='screen',
        # remappings=[
        #     ('cmd_vel', '/demo/cmd_vel'),
        #     ('laser_scan', '/demo/laser_scan')
        # ]
    )

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
          'world',
          default_value=['worlds/empty.world', ''],
          description='Gazebo world file'),
        gzserver_exe,
        gzclient_exe,
        demo
    ])

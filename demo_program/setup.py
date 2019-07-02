from setuptools import setup

package_name = 'demo_program'

setup(
    name=package_name,
    version='0.6.1',
    packages=[],
    py_modules=[
        'demo'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='rickyban',
    author_email='rickyban@hoge.com',
    maintainer='rickyban',
    maintainer_email='rickyban@hoge.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal publishers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo = demo:main',
        ],
    },
)
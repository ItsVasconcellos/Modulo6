from setuptools import find_packages, setup

package_name = 'drawing_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fvasconcellos',
    maintainer_email='fernando.asv@uol.com.br',
    description='O pacote é responsável por desenhar um escudo do palmeiras através do turtlesim.',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts':[
         'drawing_turtle = drawing_turtle.draw:main'
        ],
    },
)

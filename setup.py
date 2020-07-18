from setuptools import setup, find_packages

setup(
    name='pi-groot',
    version='0.0.1',
    author='Youngduk Suh',
    author_email='skyducks111@gmail.com',
    description='Smart farming tool for Raspberry pi.',
    url='https://github.com/skyducks/pi-groot',
    packages=find_packages(),
    scripts=['pi_groot'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'board',
        'adafruit-circuitpython-dht', # REF https://circuitpython.org/libraries
        'pyyaml',
        'elasticsearch>=7.0.0,<8.0.0',
        'pytz'
    ]
)

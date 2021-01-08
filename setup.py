from setuptools import setup
setup(
    name = 'AudibleTweetFun',
    version = '0.1.0',
    packages = ['AudibleTweetFun'],
    entry_points = {
        'console_scripts': [
            'AudibleTweetFun = AudibleTweetFun.__main__:main'
        ]
    })
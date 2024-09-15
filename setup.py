from setuptools import setup, find_packages

setup(
    name='AirdropLikeSoftware',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'zeroconf'
    ],
    entry_points={
        'console_scripts': [
            'airdrop=airdrop:main',
        ]
    },
)

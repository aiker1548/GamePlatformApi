from setuptools import setup, find_packages

setup(
    name='my_game_platform_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='API for interacting with Game Platform',
    author='aiker',
    author_email='None@email.com',
    url='https://github.com/aiker1548/GamePlatformApi.git',  # Укажите URL репозитория
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
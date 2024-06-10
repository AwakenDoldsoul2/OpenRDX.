  GNU nano 8.0                                                                                                      setup.py                                                                                                                
from setuptools import setup, find_packages

VERSION = "1.0"

setup(
    name="OpenRedirect",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "open_redirect_finder=main:main",
        ],
    },
    author="DheenaDina",
    author_email="dina2cas@gmail.com",
    description="A tool to find open redirection vulnerabilities in web applications",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)




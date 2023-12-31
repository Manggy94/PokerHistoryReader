import json
from pathlib import Path
from setuptools import setup, find_packages

install_requires = [
    "boto3",
    "python-dotenv"
    ]

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Natural Language :: French",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Games/Entertainment",
    "Topic :: Games/Entertainment :: Board Games"
]


def get_version():
    with open("version.json", "r") as f:
        version = json.load(f)
        return f"{version['major']}.{version['minor']}.{version['patch']}"


setup(
    name="pkrhistoryreader",
    version=get_version(),
    description="A Poker Package to read poker history files from S3 bucket",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    keywords="poker pkrhistory history pkr pkrhistoryreader pokerhistory reader",
    author="Alexandre MANGWA",
    author_email="alex.mangwa@gmail.com",
    url="https://github.com/manggy94/PokerHistoryreader",
    license_file='LICENSE.txt',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=["pytest", "pytest-cov", "coverage", "coveralls"],
)
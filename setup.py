from setuptools import setup


def readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

setup(
    name="beatsaver.py",
    version="0.0.1",
    author="Sirspam",
    author_email="xboxclone555@Gmail.com",
    description="An API wrapper for BeatSaver",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="beatsaber, beatsaver, API",
    url="https://github.com/Sirspam/beatsaver.py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["beatsaver", "beatsaver.models"],
    install_requires=["requests", "aiohttp", "python-dateutil"],
    license="MIT",
    python_requires=">=3.7",
)
from setuptools import setup, find_packages

setup(
    name="myws",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'myws=myws.cli:main',
        ],
    },
    author="Dev Mehta",
    author_email="dev.a.mehta30@gmail.com",
    description="Allowing users to create workspaces",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DevMehta-30/myws",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
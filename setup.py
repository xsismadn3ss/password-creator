from setuptools import setup, find_packages

setup(
    name="password creator",
    author="Abraham Artiga - xsismadness(Github)",
    description="CLI application to generate passwords",
    version="0.1",
    packages=find_packages(),
    install_requires=["click", "colorama"],
    entry_points={
        "console_scripts": [
            "password=cli:cli",
        ],
    },
)

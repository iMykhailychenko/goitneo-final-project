from setuptools import find_namespace_packages, setup

packages = find_namespace_packages()

setup(
    name="bot",
    version="0.1.0",
    description="Bot cli application",
    license="MIT",
    packages=packages,
    install_requires=["pydantic"],
    entry_points={"console_scripts": ["bot = cli.main:main"]},
)

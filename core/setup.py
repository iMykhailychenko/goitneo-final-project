from setuptools import find_namespace_packages, setup

packages = find_namespace_packages()
packages.append("core")

setup(
    name="core",
    version="0.1.0",
    description="Bot core application",
    license="MIT",
    packages=packages,
    install_requires=["pydantic"],
)

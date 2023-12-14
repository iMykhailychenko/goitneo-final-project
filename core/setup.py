from setuptools import find_namespace_packages, setup

setup(
    name="core",
    version="0.1.0",
    description="Bot core application",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["pydantic"],
)

from setuptools import find_packages, setup
from cicdtest1 import __version__

setup(
    name="cicdtest1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks Labs CICD Templates Sample Project",
    author="Khalili",
)

from setuptools import setup, find_packages

setup(
    name="peters-python-logger",
    version="0.1.0",
    py_modules=["peters-python-logger"],
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        peters-python-logger=peters-python-logger.peters-python-logger:main
    """,
)

from setuptools import setup

setup(
    name="pyneng",
    version="1.0",
    py_modules=["pyneng"],
    install_requires=[
        "Click",
        "pytest",
        "pytest-clarity",
        "pytest-json-report",
        "six",
    ],
    entry_points="""
        [console_scripts]
        pyneng=pyneng:cli
    """,
)

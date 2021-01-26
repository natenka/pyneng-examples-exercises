from setuptools import setup

setup(
    name="ptest",
    version="1.0",
    py_modules=["ptest"],
    install_requires=[
        "Click",
        "pytest",
        "pytest-clarity",
        "pytest-json-report",
        "six",
    ],
    entry_points="""
        [console_scripts]
        ptest=ptest:cli
    """,
)

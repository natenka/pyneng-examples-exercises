from setuptools import setup

setup(
    name="pyneng",
    version="1.3",
    py_modules=["pyneng"],
    install_requires=[
        "Click",
        "pytest",
        "pytest-clarity",
        "pytest-json-report",
        "six",
        "jinja2",
        "textfsm",
    ],
    entry_points="""
        [console_scripts]
        pyneng=pyneng:cli
    """,
)

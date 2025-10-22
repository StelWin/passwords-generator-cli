from setuptools import setup, find_packages

setup(
    name="newpass",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["newpass"],
    entry_points="""
        [console_scripts]
        newpass = newpass:main
    """,
)

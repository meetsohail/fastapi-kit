from setuptools import setup, find_packages

setup(
    name="fastapikit",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "fastapikit=fastapi_kit.cli:main",
        ],
    },
    python_requires=">=3.8",
)

import setuptools

setuptools.setup(
    name="api",
    version="0.1.0",
    packages=setuptools.find_packages(where="api"),
    package_dir={"": "api"},
    python_requires=">=3.6",
)

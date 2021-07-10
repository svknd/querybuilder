
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="svknd-query_builder",
    version="0.1.0",
    description="SVKND query builder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://svknd.id",
    author="Irvan Maulana",
    author_email="me@tukangremot.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["query_builder"],
    include_package_data=True,
    install_requires=[]
)

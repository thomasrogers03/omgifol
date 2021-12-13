import setuptools

setuptools.setup(
    name="omg",
    version="0.0.1",
    author="Fredrik Johansson",
    description="A Python library for Doom WAD files",
    url="https://github.com/AlexMax/omgifol",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["pillow==8.4.0"],
)

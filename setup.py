import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    "flask == 1.*",
    "python-dotenv == 0.21.*",
    "requests == 2.*",
]

DEV_REQUIREMENTS = [
    "flake8 == 6.*",
    "pytest == 7.*",
    "pytest-cov == 4.*",
    "vcrpy == 4.*",
]

setuptools.setup(
    name="Bond",
    version="0.3.0",
    description="The carrier integration for Bond on the EasyPost platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/justintime50/easypost-bond",
    author="Justintime50, bradleywalsh",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={"dev": DEV_REQUIREMENTS},
    python_requires=">=3.7",
)

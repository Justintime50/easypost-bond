import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'flask >= 1.1.2',
    'requests >= 1.0.0',
    'python-dotenv >= 0.10.0'
]

setuptools.setup(
    name='withbond',
    version='0.0.1',
    description='The carrier integration for WithBond on the EasyPost platform.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/withbond-easypost',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pylint >= 2.5.0',
        ]
    },
    python_requires='>=3.6',
)

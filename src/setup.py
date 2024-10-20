from setuptools import setup, find_packages

setup(
    name="svg-tool-functions",
    version="0.1.3",
    author="Fernando Pujaico Rivera",
    author_email="fernando.pujaico.rivera@gmail.com",
    description="Functions to work with svg",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/trucomanx/svg-tool-functions",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        # Adicione outros pacotes necessários aqui
    ],
    python_requires='>=3.6',

)


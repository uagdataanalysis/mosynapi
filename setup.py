import setuptools
from os import path
from io import open
from setuptools.command.install import install


class PostInstall(install):
    def run(self):
        install.run(self)
        import nltk
        nltk.download("punkt")

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'mosyn',
    version = '1.0.8',
    description = 'A morphological dictionary tool.',
    long_description=long_description,
    author = 'uagdataanalysis',
    author_email = 'uagdataanalysis@gmail.com',
    packages = setuptools.find_packages(),
    package_data = {'mosyn': ['dict/*.csv']},
    cmdclass = {'install': PostInstall},
    install_requires = [
        'nltk>=3.0'
    ],
    keywords = ['dictionary' , 'morphological', 'analysis'],
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent"
    ),
    url = 'https://github.com/uagdataanalysis/mosynapi',
    download_url = "https://github.com/uagdataanalysis/mosynapi/tarball/1.0.8",
    project_urls={
        'Bug Reports': 'https://github.com/uagdataanalysis/mosynapi/issues',
        'Source': 'https://github.com/uagdataanalysis/mosynapi/'
    }
)

import setuptools
from setuptools.command.install import install


class PostInstall(install):
    def run(self):
        install.run(self)
        import nltk
        nltk.download("punkt")

setuptools.setup(
    name = 'mosyn',
    packages = setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: Creative Commons",
        "Operating System :: OS Independent"
    ),
    version = '1.0.7',
    description = 'A morphological dictionary tool.',
    author = 'uagdataanalysis',
    author_email = 'uagdataanalysis@gmail.com',
    url = 'https://github.com/uagdataanalysis/mosynapi',
    download_url = "https://github.com/uagdataanalysis/mosynapi/tarball/1.0.6",
    package_data = {'mosyn': ['dict/*.csv']},
    keywords = ['dictionary' , 'morphological', 'analysis'],
    cmdclass = {'install': PostInstall},
    install_requires = [
        'nltk>=3.0'
    ]
)

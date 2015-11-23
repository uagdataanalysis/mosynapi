from setuptools import setup, find_packages
from setuptools.command.install import install as _install


class Install(_install):
    def run(self):
        _install.do_egg_install(self)
        import nltk
        nltk.download("punkt")

setup(
    name = 'mosyn',
    packages = find_packages(),
    version = '1.0.4',
    description = 'A morphological dictionary tool.',
    author = 'uagdataanalysis',
    author_email = 'uagdataanalysis@gmail.com',
    url = 'https://github.com/uagdataanalysis/mosynapi',
    download_url = "https://github.com/uagdataanalysis/mosynapi/tarball/1.0.4",
    package_data = {'mosyn': ['dict/*.csv']},
    keywords = ['dictionary' , 'morphological', 'analysis'],
    cmdclass = {'install': Install},
    install_requires = [
        'nltk>=3.0'
    ]
)

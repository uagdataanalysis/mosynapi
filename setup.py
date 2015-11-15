from setuptools import setup, find_packages
from setuptools.command.install import install as _install


class Install(_install):
    def run(self):
        _install.do_egg_install(self)
        import nltk
        nltk.download("punkt")

setup(
    name='mosyn',
    version='1.0.3',
    author='asaelt',
    author_email='art.torres.alv@gmail.com',
    url='https://github.com/uagdataanalysis/mosynapi',
    packages=find_packages(),
    package_data={'mosyn': ['dict/*.csv']},
    description='A morphological analysis tool.',
    cmdclass={'install': Install},
    install_requires=[
        'nltk>=3.0'
    ]
)

from setuptools import setup, find_packages
     
setup(name='my_math',
        version='1.0',
        author='Dominik Gerlach',
        author_email='dominikgeralch01@gmail.com',
        license='Free',
        description='This package contains 2 implementation for each gcd, factorial and diophantile equasion',
        packages=find_packages(include=['my_math']),
)
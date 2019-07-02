from setuptools import setup, find_packages


requirements = [r.strip() for r in open('requirements.txt').readlines() if '#' not in r]


setup(
    name='rosreestr-api',
    author='Greg Eremeev',
    author_email='gregory.eremeev@gmail.com',
    version='0.3.0',
    license='BSD',
    url='https://github.com/GregEremeev/rosreestr-api',
    install_requires=requirements,
    description='Toolset to work with rosreestr.ru/api',
    packages=find_packages(),
    extras_require={'dev': ['ipdb==0.12', 'pytest==4.6.3', 'httpretty==0.9.6']},
    classifiers=['Programming Language :: Python :: 3.7'],
    zip_safe=False,
    include_package_data=True
)

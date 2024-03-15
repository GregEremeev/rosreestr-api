from setuptools import setup, find_packages


requirements = [r.strip() for r in open('requirements.txt').readlines() if '#' not in r]


setup(
    name='rosreestr-api',
    author='Greg Eremeev',
    author_email='gregory.eremeev@gmail.com',
    version='1.0.0',
    license='BSD-3-Clause',
    url='https://github.com/GregEremeev/rosreestr-api',
    install_requires=requirements,
    description='Toolset to work with rosreestr.gov.ru/api and pkk.rosreestr.ru/api',
    packages=find_packages(),
    extras_require={'dev': ['ipdb>=0.13.2', 'pytest>=5.4.1', 'httpretty>=1.0.2']},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    zip_safe=False,
    include_package_data=True
)

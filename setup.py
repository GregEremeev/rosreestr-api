from setuptools import setup, find_packages


with open('requirements.txt') as f:
    # drop comments, including trailing ones, and blank lines
    requirements = [r.split('#', 1)[0].strip() for r in f]
requirements = [r for r in requirements if r]


setup(
    name='rosreestr-api',
    author='Greg Eremeev',
    author_email='gregory.eremeev@gmail.com',
    version='1.0.0',
    license='BSD-3-Clause',
    url='https://github.com/GregEremeev/rosreestr-api',
    install_requires=requirements,
    description='Toolset to work with lk.rosreestr.ru and nspd.gov.ru',
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

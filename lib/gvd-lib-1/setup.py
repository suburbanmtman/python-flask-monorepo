from distutils.core import setup


__version__ = '1.0.0'


setup(
    name='gvd-lib-1',
    version=__version__,
    description='Sample library 1',
    author='David Smith',
    url='https://gentlevalleydigital.com',
    packages=[
        'gvd_lib_1',
    ],
    install_requires=[
        'faker==14.2.0',
    ]
)

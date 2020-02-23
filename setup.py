import setuptools

setuptools.setup(
    name='atl_cache_warmer',
    version='0.1',
    packages=['atl_cache_warmer'],
    entry_points={
        'console_scripts': [
            'atlwarmer = atl_cache_warmer.cache_builder:main'
        ]
    },
    url='',
    license='',
    author='np-at',
    author_email='',
    description='',
    install_requires=['requests']
)

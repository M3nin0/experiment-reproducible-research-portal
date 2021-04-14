import os

from setuptools import find_packages, setup

docs_require = [
    'Sphinx>=2.2',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
    'sphinx_tabs.tabs',
    'sphinx_click'
]

tests_require = [
    'pytest==6.1.1'
]

extras_require = {
}
extras_require['all'] = [req for exts, reqs in extras_require.items() for req in reqs]

setup_requires = [
    'pytest-runner>=5.2',
]

install_requires = [
    'requests==2.25.1',
    'bagit==1.8.1',
    'emoji==1.2.0',
    'click==7.1.2'
]

packages = find_packages()

g = {}
with open(os.path.join('reprocli', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='reprocli',
    version=version,
    description=__doc__,
    keywords=['Reproducibility', 'Research Package'],
    license='MIT',
    author='INPE',
    author_email='felipe.carlos@inpe.br',
    url='https://github.com/M3nin0/datacube-reproducible-service',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'reprocli = reprocli.cli:cli'
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Console :: Curses  ',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
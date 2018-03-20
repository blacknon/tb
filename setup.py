import setuptools 

if __name__ == "__main__":
    setuptools.setup(
        name='tb',
        version='0.0.1',
        install_requires=['tabulate'],
        packages=setuptools.find_packages(),
        py_modules = ['tb'],
        entry_points={
            'console_scripts':[
                'tb = tb:main',
            ],
        },
    )

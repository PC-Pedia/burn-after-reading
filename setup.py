from setuptools import setup, find_packages

setup(
    name         = 'burn-after-reading',
    version      = '1.2',
    packages     = find_packages(),
    test_suite   = "burn.tests",
    install_requires = ['Flask>=0.11.1'],    
    zip_safe = False,
    include_package_data = True,
)

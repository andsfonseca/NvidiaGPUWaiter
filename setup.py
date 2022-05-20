from setuptools import find_packages, setup

setup(
    name='NvidiaGPUWaiter',
    version='0.1.3',    
    description='Method to detect idle GPU with certain conditions using nvidia-smi',
    url='https://github.com/andsfonseca/NvidiaGPUWaiter',
    author='Anderson Silva',
    author_email='andsfonseca@tecgraf.puc-rio.br',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    project_urls = {
        "Bug Tracker": "https://github.com/andsfonseca/NvidiaGPUWaiter/issues"
    }
)
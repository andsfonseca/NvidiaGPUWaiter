from setuptools import setup

setup(
    name='NvidiaGPUWaiter',
    version='0.1.1',    
    description='Method to detect idle GPU with certain conditions using nvidia-smi',
    url='https://github.com/andsfonseca/NvidiaGPUWaiter',
    author='Anderson Silva',
    author_email='andsfonseca@tecgraf.puc-rio.br',
    license='MIT',
    packages=['NvidiaGPUWaiter'],
    install_requires=[],
    project_urls = {
        "Bug Tracker": "https://github.com/andsfonseca/NvidiaGPUWaiter/issues"
    }
)
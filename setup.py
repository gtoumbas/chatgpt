from setuptools import setup, find_packages

setup(
    name='chatgpt',
    version='0.1',
    packages=find_packages(),
    description='A simple package to interact with the OpenAI API',
    author='George Toumbas',
    author_email='gtoumbas23@gmail.com"
    url='https://github.com/yourusername/your-package-name',
    install_requires=[
        'openai',
        'json',
        'importlib',
        'time',
        'sys'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
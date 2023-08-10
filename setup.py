from setuptools import setup

setup(
    name='chatgpt',
    version='0.1',
    packages=['chatgpt']
    description='A simple package to interact with the OpenAI API',
    author='George Toumbas',
    author_email='gtoumbas23@gmail.com',
    licesne='MIT',
    url='https://github.com/gtoumbas/chatgpt.git',
    install_requires=[
        'openai',
    ],
)
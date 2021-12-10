from setuptools import setup


setup(
    name="Pipe",
    url="https://github.com/vklokov/pipe-python",
    author="Vladimir Klokov",
    author_email="klokov.dev@gmail.com",
    packages=['pipe'],
    install_requires=[
      'requests >= 2.20; python_version >= "3.0"',
    ],
    version="0.1",
    license="MIT",
    description="Pipedrive API wrapper"
)

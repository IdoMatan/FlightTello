import io
import os
import re

from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


requirements = [
    'numpy==1.15.4',
    'opencv-python==4.2.0.32',
    'pygame==1.9.4',
    'scipy>=1.1.0',
    'matplotlib>=3.1.1'
    # , 'time'
]

requirements_dev = [
    'Pillow',
    'nose'
]


setup(
    name="Flight Tello",
    version="0.0.0",
    # url="https://github.com/...",
    license='**',
    author="Ido Glanz and Matan Weksler",
    author_email="**",
    description="Tello API Ready for reinforcement applications",
    long_description=read("README.md"),
    # packages=find_packages(exclude=('models', 'venv')),
    packages=['TelloControl'],

    install_requires=requirements,
    extras_require={
        'dev': requirements_dev
    },
)
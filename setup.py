from setuptools import setup


setup(
    name='SpotiPy',
    version='1.200',
    description='simple client for the Spotify Web API',
    author="@plamere",
    author_email="paul@echonest.com",
    url='http://github.com/plamere/spotipy',
    install_requires=['requests>=1.0', ],
    license='LICENSE.txt',
    py_modules=['spotipy', 'spotipy.oauth2'],)

FLASH-pyMAS
===========


.. image:: https://img.shields.io/pypi/v/flash_pymas.svg
        :target: https://pypi.python.org/pypi/flash_pymas

.. image:: https://img.shields.io/travis/andrei10t/flash_pymas.svg
        :target: https://travis-ci.com/andrei10t/flash_pymas

.. image:: https://readthedocs.org/projects/flash-pymas/badge/?version=latest
        :target: https://flash-pymas.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




MAS framework for monitoring and deployment


* Free software: GNU General Public License v3
* Documentation: https://flash-pymas.readthedocs.io.


Features
--------


How To
--------
Create a pem certificate for websockets: 
sudo openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem 
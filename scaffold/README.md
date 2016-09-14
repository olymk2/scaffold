Scaffold templating language
============================

Introduction
------------

Scaffold is a python templating language, that brings html into you code via calls to the framework, it heavily uses the concept of widgets or predefined html and javascript.

Features:

  * Consistent html markup avoiding errors like unclosed tags
  * No need for a seperate template language to learn
  * Reusuable code, with pre defined defaults
  * Caching of the generated pages via flat files
  * Usefull helper modules for validating and parsing

Installing
----------

You can install scaffold using pip using the example below.
```pip install --install -e bzr+lp:scaffold#egg=scaffold```
Or if you have a debian machine you can 
``` sudo add-apt-repository ppa:oly/ppa
sudo apt-get update && sudo apt-get install python-scaffold```

Source Code
-----------

The code is hosted on launchpad at this url [link](https://code.launchpad.net/~oly/scaffold/trunk).


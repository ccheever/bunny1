#!/usr/bin/python

__author__ = "ccheever"
__doc__ = """
A barebones bunny1 server that should be easy to modify for your own use
"""
__date__ = "Thu Feb 12 09:05:40 PST 2009"

import urlparse

import bunny1
from bunny1 import cherrypy
from bunny1 import Content
from bunny1 import q
from bunny1 import qp
from bunny1 import expose
from bunny1 import dont_expose
from bunny1 import escape
from bunny1 import HTML

class MyCommands(bunny1.Bunny1Commands):

    def your_command_here(self, arg):
        """this is where a description of your command goes"""
        return "http://www.example.com/?" % qp(arg)

    def another_command(self, arg):
        """this example will send content to the browser rather than redirecting"""
        raise HTML("some <u>html</u> " + escape("with some <angle brackets>"))


    # ... and you can add other commands by just defining more methods
    # in this class here

class MyBunny(bunny1.Bunny1):
    def __init__(self):
        bunny1.Bunny1.__init__(self, MyCommands(), bunny1.Bunny1Decorators())

if __name__ == "__main__":
    bunny1.main(MyBunny())



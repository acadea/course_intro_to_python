# third party modules are modules written by other developers
#
# Why?
# Using modules written by someone else means that we can leverage the skills and knowledge
# of someone specialised in other area without reinventing the wheels ourself
#
# Example:
# data analysis libraries -- extract useful statistical information from a data set
# charting libraries to easily build charts from data
# web dev libraries - build a web app with python

# How?
# Modules are often dependent on each other. Thus sometimes we also call them dependencies of a project
# It would be a pain to install modules manually.
# For eg.
# Module A needs Module B to work
# Module B needs Module C
# and etc..

# if we want to install A, that means we also need Module B and C and ...

# Solution:
# Use a dependency manager
# A dependency manager is a program that automatically detects and install all the required modules in our project
# So if we install A, the dependency manager should be able to take care of B and C for us
#
# Pip is the official dependency manager of python.
# we can browse for libraries / packages / modules on https://pypi.org/search/
# conda is the dependency manager provided by Anaconda
# it has more features than pip

# pip install bokeh
# pip uninstall bokeh


# once installed we can simply import it
import bokeh






"""Top-level package for Arbin Electrochemical Tools."""
from electrochem._version import __version__

__author__ = """Vincent Wu"""
__email__ = 'vincentwu@ucsb.edu'
__version__ = __version__ 

from electrochem.parse import (parseArbin, toDataframe, extractEchem, 
extractCycleEchem, generateSummary, generateEchemSummary, plotEchem)


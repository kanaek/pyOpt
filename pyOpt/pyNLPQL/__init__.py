#!/usr/bin/env python

try:
    from .pyNLPQL import NLPQL
    __all__ = ['NLPQL']
except:
    __all__ = []

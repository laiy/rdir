#!/usr/bin/python
# coding: utf-8
from rdir import rdir

__author__ = 'lhfcws'


#rdir.rdir("urllib")
#rdir.rdir(name="urllib", limit_deep=1)
#rdir.rdir("urllib.urlopen")
#rdir.rdir("urllib.urlopen", limit_deep=1)
# rdir.rdir("urllib.urlopen", limit_deep=2, mode=rdir.TREE, output="/Users/lhfcws/tree.html")
rdir.rdir('numpy.matrixlib.defmatrix.matrix.getH', limit_deep=1, mode=rdir.TREE, output="/Users/lhfcws/tree.html")

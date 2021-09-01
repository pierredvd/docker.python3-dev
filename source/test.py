#!/usr/bin/env python3

"""
    Un petit cartouche ?
"""

import os
import sys
import argparse

DS            = os.sep
CURRENT_DIR   = os.path.dirname(os.path.realpath(__file__))+DS


class Test():

    def __init__(self):

        parser = argparse.ArgumentParser(description='Return merged ansible inventories', usage='%(prog)s [options] [host|group]')
        parser.add_argument('--list' , action='store_true', help='Return list')
        parser.add_argument('--get' , type=ascii, metavar='<hostname>', help='Return one')
        
        if(len(sys.argv)==0):
            print("no argv")
            return            
        
        args = parser.parse_args(sys.argv[1:len(sys.argv)]).__dict__
        
        if args['list'] and args['get']!=None or args['list']==False and args['get']==None:
            print("Require one argument in (--get, --list)")
            return
        
        # Identify command line
        if args['list']==True:
            print("do --list")
            return            
        
        if args['get']!=None:
            print("do --get", args['get'])
            return

        return        

# Let's start !
Test()


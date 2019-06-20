# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:10:32 2019

@author: robot
"""



import logging

log = logging.getLogger()
log.setLevel(logging.INFO)
file = open('test.log','w') 
file.close()
handler = logging.FileHandler('test.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
            )
handler.setFormatter(formatter)
log.addHandler(handler)

log.info('log file is open')  
logging.shutdown()
log.removeHandler(handler)
log.info('log file should be closed')
#

#import logging
#
#def main():
#    log = logging.getLogger()
#    log.setLevel(logging.INFO)
#    fh = logging.FileHandler(filename='test.log')
#    fh.setLevel(logging.INFO)
#    formatter = logging.Formatter(
#                    fmt='%(asctime)s %(levelname)s: %(message)s',
#                    datefmt='%Y-%m-%d %H:%M:%S'
#                    )
#    fh.setFormatter(formatter)
#    log.addHandler(fh)
#
#    log.info('-------Start--------')
#    logging.shutdown()
#    log.info('this function is doing something')
#    log.info('this function is finished')
#    log.removeHandler(fh)
##    <--------------------------Add this line
#    del log,fh
#    
#    
#main()
#logging.close()
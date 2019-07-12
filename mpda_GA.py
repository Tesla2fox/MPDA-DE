import sys
import time
import logging
from  enum import Enum

from OptimizerGA import MPDA_Genetic_Alg

# class


def mpda_GA(insName,decodeType):
    pass
    optimizer = MPDA_Genetic_Alg(insName,decodeType)
    optimizer.run()




if __name__ == '__main__':

    # log = logging.getLogger()
    # log.setLevel(logging.INFO)
    # # file = open('test.log', 'w')
    # # file.close()
    # handler = logging.FileHandler('test.log')
    # handler.setLevel(logging.INFO)
    # formatter = logging.Formatter(
    #     fmt='%(asctime)s %(levelname)s: %(message)s',
    #     datefmt='%Y-%m-%d %H:%M:%S'
    # )
    # handler.setFormatter(formatter)
    # log.addHandler(handler)
    # log.info('log file is open')
    # logging.shutdown()
    # log.removeHandler(handler)
    # log.info('log file should be closed')

    print(sys.argv)
    if len(sys.argv) != 3:
        raise Exception('argv no right')

    if sys.argv[2] == '1':
        decode_type = DecoderType.back
    elif sys.argv[2] == '2':
        decode_type = DecoderType.no_back
    else:
        # log.error('need decoder Type')
        raise Exception('need decoder Type')
    insName = sys.argv[1]
    #
    #
    #
    # time.sleep(100)
    print('main')
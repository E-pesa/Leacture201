import threading
import logging
import time

def theardign_fuunction(name):
    logging.info(f"Therding {name} starting,")
    time.sleep(2)
    logging.info(f"Therading {name} Ending")

if __name__ == '__main__':
    formater = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formater,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main before creating")
    x = threading.Thread(target=theardign_fuunction, args=(1,))
    logging.info("Main before start threading")
    x.start()
    logging.info("Main : waitning for threading to finish")
    x.join()
    logging.info("Main ending")
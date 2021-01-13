from war import War
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    war = War()
    war.generate()
    war.start_battle()

import multiprocessing
from productos_server import run_productos_server
from mysql_server import run_mysql

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_productos_server)
    p2 = multiprocessing.Process(target=run_mysql)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

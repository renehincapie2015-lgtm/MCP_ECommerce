import multiprocessing
from fastmcp_mysql import run_mysql_server
from servidorMCPProductos import run_productos_server

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_mysql_server)
    p2 = multiprocessing.Process(target=run_productos_server)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
 
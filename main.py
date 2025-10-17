import multiprocessing
from fastmcp_mysql import run_mysql_server
from servidorMCPProductos import run_productos_server

if __name__ == "__main__":
    print("antes multiprocessing run_mysql_server")
    p1 = multiprocessing.Process(target=run_mysql_server)
    print("antes multiprocessing run_productos_server")
    p2 = multiprocessing.Process(target=run_productos_server)

    print("antes p1.start")
    p1.start()
    print("antes p2.start")
    p2.start()

    print("antes p1.join")
    p1.join()
    print("antes p2.join")
    p2.join()

from fastmcp import FastMCP
import mysql.connector
from typing import Dict, List, Any

mcp = FastMCP()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="luza0609",
        database="bd_ecommerce_cse642"
    )

@mcp.tool(name="listar_productos", description="Lista todos los productos disponibles.")
def listar_productos(_: Dict[str, Any]) -> List[Dict[str, Any]]:
    def run():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return productos
    return run()

@mcp.tool(
    name="consultar_producto_por_id",
    description="Consulta un producto por su ID."
)
def consultar_producto_por_id(params: Dict[str, Any]) -> Dict[str, Any]:
    def run():
        producto_id = params.get("id")
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        return producto if producto else {"error": "Producto no encontrado"}
    return run()

if __name__ == "__main__":
    mcp.run()

from fastmcp import FastMCP
from typing import Dict, List, Any

mcp = FastMCP()

@mcp.tool(name="listar_productos", description="Lista todos los productos disponibles.")
def listar_productos(_: Dict[str, Any]) -> List[Dict[str, Any]]:
    def run():
        query = "SELECT * FROM productos"
        return mcp.mysql.query(query)
    return run()

@mcp.tool(name="consultar_producto_por_id", description="Consulta un producto por su ID.")
def consultar_producto_por_id(params: Dict[str, Any]) -> Dict[str, Any]:
    def run():
        producto_id = params.get("id")
        query = "SELECT * FROM productos WHERE id = %s"
        resultado = mcp.mysql.query(query, (producto_id,))
        return resultado[0] if resultado else {"error": "Producto no encontrado"}
    return run()

if __name__ == "__main__":
    mcp.run()

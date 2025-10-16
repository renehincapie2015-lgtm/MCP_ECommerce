from fastmcp import FastMCP
from typing import Dict, List, Any

mcp = FastMCP("Servidor MCP de Productos")

@mcp.tool(name="listar_productos", description="Lista todos los productos disponibles.")
def listar_productos(_: Dict[str, Any]) -> List[Dict[str, Any]]:
        query = "SELECT * FROM productos"
        return mcp.mysql.query(query)

@mcp.tool(name="consultar_producto_por_id", description="Consulta un producto por su ID.")
def consultar_producto_por_id(params: Dict[str, Any]) -> Dict[str, Any]:
        producto_id = params.get("id")
        query = "SELECT * FROM productos WHERE id = %s"
        resultado = mcp.mysql.query(query, (producto_id,))
        return resultado[0] if resultado else {"error": "Producto no encontrado"}

def run_productos_server():
    mcp.run()
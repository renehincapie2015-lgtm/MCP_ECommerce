from fastmcp import FastMCP
from typing import Dict, List, Any

mcp = FastMCP("Servidor MCP de Productos")

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

@mcp.tool(name="probar_conexion_mysql", description="Verifica si la conexión a MySQL está activa.")
def probar_conexion_mysql(_: Dict[str, Any]) -> Dict[str, Any]:
    def run():
        try:
            resultado = mcp.mysql.query("SELECT 1")
            return {"estado": "conectado", "resultado": resultado}
        except Exception as e:
            return {"estado": "error", "detalle": str(e)}
    return run()

if __name__ == "__main__":
    mcp.run()

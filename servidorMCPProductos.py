from fastmcp import FastMCP
from sqlalchemy import create_engine, text
from typing import Dict, List, Any

engine = create_engine("mysql+pymysql://root:luza0609@localhost:3306/bd_ecommerce_cse642")

mcp = FastMCP()

@mcp.tool(name="listar_productos", description="Lista todos los productos disponibles.")
def listar_productos(_: Dict[str, Any]) -> List[Dict[str, Any]]:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM productos"))
        return [row._asdict() for row in result]

@mcp.tool(
    name="consultar_producto_por_id",
    description="Consulta un producto por su ID."
)
def consultar_producto_por_id(params: Dict[str, Any]) -> Dict[str, Any]:
    producto_id = params["id"]
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM productos WHERE id = :id"), {"id": producto_id})
        row = result.fetchone()
        return row._asdict() if row else {"error": "Producto no encontrado"}

if __name__ == "__main__":
    mcp.run()

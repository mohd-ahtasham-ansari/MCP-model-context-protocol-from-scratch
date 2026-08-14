from mcp.server.fastmcp import FastMCP
mcp = FastMCP("math-server")

@mcp.tool
def add(a:int,b:int)->int:
    """
    Adds two integers
    """
    return a + b

@mcp.tool
def sub(a:int,b:int)->int:
    """
    Subtracts two integers
    """
    return a - b

@mcp.tool
def mul(a:int,b:int)->int:
    """
    Multiplies two integers
    """
    return a * b

@mcp.tool
def div(a:int,b:int)->int:
    """
    Divides two integers
    """
    return a / b

@mcp.tool
def power(a:int,b:int)->int:
    """
    Raises a to the power of b
    """
    return a ** b

@mcp.tool
def mod(a:int,b:int)->int:
    """
    Returns the remainder of a divided by b
    """
    return a % b

##the transport="stdio" argument tells the server to :

#use Standard input and output (stdin/stdout) to recieve and respond to tool functions calls

if __name__ == "__main__":
    mcp.run(transport="stdio")
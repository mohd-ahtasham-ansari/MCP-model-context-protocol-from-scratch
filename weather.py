from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
async def get_weather(weather:str)->str:
    """
    get the locations weather
    """
    return "the weather is cold and rainy"

if __name__=="__main__":
    mcp.run(transport="streamable-http")

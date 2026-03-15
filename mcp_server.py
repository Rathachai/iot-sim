from fastmcp import FastMCP
import requests

# Initialize FastMCP Server
mcp = FastMCP("IoT_Dashboard_Controller")

BASE_URL = "http://127.0.0.1:5050"

# --- SENSOR TOOLS (Box 1-6: Read Only) ---

@mcp.tool()
def get_temperature():
    """Read Temperature from Box 1 (Celsius)."""
    response = requests.get(f"{BASE_URL}/box1/read")
    return response.json().get("box1")

@mcp.tool()
def get_humidity():
    """Read Humidity from Box 2 (%)."""
    response = requests.get(f"{BASE_URL}/box2/read")
    return response.json().get("box2")

@mcp.tool()
def get_wind_speed():
    """Read Wind Speed from Box 3."""
    response = requests.get(f"{BASE_URL}/box3/read")
    return response.json().get("box3")

@mcp.tool()
def get_light_level():
    """Read Light Intensity from Box 4."""
    response = requests.get(f"{BASE_URL}/box4/read")
    return response.json().get("box4")

@mcp.tool()
def check_movement():
    """Check Movement detection status from Box 5 (on/off)."""
    response = requests.get(f"{BASE_URL}/box5/read")
    return response.json().get("box5")

@mcp.tool()
def check_wetness():
    """Check Wet/Rain detection status from Box 6 (on/off)."""
    response = requests.get(f"{BASE_URL}/box6/read")
    return response.json().get("box6")


# --- ACTUATOR TOOLS (Box 7-12: Write Only) ---

@mcp.tool()
def update_display_a(content: str):
    """Write any text or data to Display A (Box 7)."""
    response = requests.post(f"{BASE_URL}/box7/write/{content}")
    return response.json()

@mcp.tool()
def update_display_b(content: str):
    """Write any text or data to Display B (Box 8)."""
    response = requests.post(f"{BASE_URL}/box8/write/{content}")
    return response.json()

@mcp.tool()
def control_bulb_a(level: int):
    """Set Bulb A (Box 9) brightness. Levels: 0 (Off), 1, 2, 3 (Max)."""
    if level < 0 or level > 3: return "Error: Level must be 0-3"
    response = requests.post(f"{BASE_URL}/box9/write/{level}")
    return response.json()

@mcp.tool()
def control_bulb_b(level: int):
    """Set Bulb B (Box 10) brightness. Levels: 0 (Off), 1, 2, 3 (Max)."""
    if level < 0 or level > 3: return "Error: Level must be 0-3"
    response = requests.post(f"{BASE_URL}/box10/write/{level}")
    return response.json()

@mcp.tool()
def control_fan_a(speed: int):
    """Set Fan A (Box 11) speed. Levels: 0 (Off), 1, 2, 3, 4, 5 (Max)."""
    if speed < 0 or speed > 5: return "Error: Speed must be 0-5"
    response = requests.post(f"{BASE_URL}/box11/write/{speed}")
    return response.json()

@mcp.tool()
def control_fan_b(speed: int):
    """Set Fan B (Box 12) speed. Levels: 0 (Off), 1, 2, 3, 4, 5 (Max)."""
    if speed < 0 or speed > 5: return "Error: Speed must be 0-5"
    response = requests.post(f"{BASE_URL}/box12/write/{speed}")
    return response.json()

if __name__ == "__main__":
    #mcp.run()
    mcp.run(transport="http", host="0.0.0.0", port=8000)
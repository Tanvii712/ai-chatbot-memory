# tools.py

def weather_tool(city: str):
    return f"Weather in {city}: 30°C, sunny"

def news_tool():
    return "Latest news: AI is growing rapidly"

def calculator_tool(expr: str):
    try:
        return str(eval(expr))
    except:
        return "Error in calculation"
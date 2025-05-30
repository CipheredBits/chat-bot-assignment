def parse_query(user_query):
    """
    Analyze the user's query string and determine the intent:
    - 'sustainability' for eco-friendly queries
    - 'profitability' for investment/growth queries
    - 'general' for other queries or fallback
    
    Returns a string indicating the intent.
    """
    query = user_query.lower()

    # Keywords for sustainability
    sustainability_keywords = ["eco-friendly", "green", "sustainable", "environment", "energy use", "eco", "climate", "sustainability"]

    # Keywords for profitability
    profitability_keywords = ["profit", "profitable", "price trend", "growth", "rising", "invest", "investment", "market cap", "long-term", "best coin", "price", "trending", "top"]

    # Check if query is about sustainability
    if any(word in query for word in sustainability_keywords):
        return "sustainability"

    # Check if query is about profitability
    elif any(word in query for word in profitability_keywords):
        return "profitability"

    else:
        # fallback for other/general queries
        return "general"

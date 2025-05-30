# dataset
cryptocurrencies = [
    {"name": "Algorand", "eco_friendly_score": 10},
    {"name": "Cardano", "eco_friendly_score": 9},
    {"name": "Stellar", "eco_friendly_score": 8},
    {"name": "Nano", "eco_friendly_score": 7},
    {"name": "Solana", "eco_friendly_score": 7},
    {"name": "Tezos", "eco_friendly_score": 6},
    {"name": "Ethereum", "eco_friendly_score": 4},
    {"name": "Bitcoin", "eco_friendly_score": 2}
]

def handle_sustainability_query(query):
    query = query.lower()
    
    eco_keywords = ["eco-friendly", "green", "sustainable", "environment", "eco"]
    if any(keyword in query for keyword in eco_keywords):
        most_eco = max(cryptocurrencies, key=lambda x: x["eco_friendly_score"])
        
        if "most" in query or "top" in query or "best" in query:
            return f"The most eco-friendly cryptocurrency is {most_eco['name']} with a sustainability score of {most_eco['eco_friendly_score']}/10."
        else:
            sorted_cryptos = sorted(cryptocurrencies, key=lambda x: x["eco_friendly_score"], reverse=True)
            response = "Here are cryptocurrencies ranked by eco-friendliness:\n"
            for crypto in sorted_cryptos:
                response += f"- {crypto['name']}: {crypto['eco_friendly_score']}/10\n"
            return response
    else:
        return "I can only provide information about eco-friendly cryptocurrencies. Please ask about 'green' or 'sustainable' coins."

print(get_sustainable_crypto("Which is the most eco-friendly coin?"))
print("\n")
print(get_sustainable_crypto("Show me sustainable cryptocurrencies"))
print("\n")
print(get_sustainable_crypto("What's the price of Bitcoin?"))

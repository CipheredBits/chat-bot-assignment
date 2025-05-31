crypto_profitability = [
    {"name": "Bitcoin", "price_trend": "rising", "market_cap": "high"},
    {"name": "Ethereum", "price_trend": "stable", "market_cap": "high"},
    {"name": "Cardano", "price_trend": "rising", "market_cap": "medium"},
    {"name": "Dogecoin", "price_trend": "falling", "market_cap": "low"},
    {"name": "Polkadot", "price_trend": "rising", "market_cap": "medium"},
]

def get_profitable_crypto(query):
    query = query.lower()

    investment_keywords = ["invest", "growth", "profit", "make money", "price", "best crypto", "rising"]

    if any(keyword in query for keyword in investment_keywords):
        
        profitable_cryptos = [
            crypto for crypto in crypto_profitability
            if crypto["price_trend"] == "rising" and crypto["market_cap"] in ["high", "medium"]
        ]

        if not profitable_cryptos:
            return "Sorry, I couldn’t find any cryptocurrencies currently showing profitable trends."

        response = "Here are some cryptocurrencies with rising trends and solid market cap:\n"
        for crypto in profitable_cryptos:
            response += f"- {crypto['name']} (Trend: {crypto['price_trend']}, Market Cap: {crypto['market_cap']})\n"

        top = profitable_cryptos[0]
        response += f"\n💡 Recommendation: Consider investing in {top['name']} — it's showing positive growth and has a good market position! 🚀"
        return response
    else:
        return "I can help you find profitable cryptocurrencies. Try asking about investments, growth, or rising trends!"

# Example test
print(get_profitable_crypto("What crypto should I invest in for growth?"))
print("\n")
print(get_profitable_crypto("Show me rising cryptocurrencies"))
print("\n")
print(get_profitable_crypto("Tell me about Ethereum's price"))

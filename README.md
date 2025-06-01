# chat-bot-assignment
#Fallback Logic

Test also the fall back logic

# Sample profitability dataset
crypto_profitability = [
    {"name": "Bitcoin", "price_trend": "rising", "market_cap": "high"},
    {"name": "Ethereum", "price_trend": "stable", "market_cap": "high"},
    {"name": "Cardano", "price_trend": "rising", "market_cap": "medium"},
    {"name": "Dogecoin", "price_trend": "falling", "market_cap": "low"},
    {"name": "Polkadot", "price_trend": "rising", "market_cap": "medium"},
]

def get_profitable_crypto(query):
    query = query.lower().strip()

    # Keywords
    investment_keywords = ["invest", "growth", "profit", "make money", "price", "best crypto", "rising"]
    crypto_related_keywords = ["crypto", "coin", "bitcoin", "ethereum", "blockchain", "dogecoin", "cardano", "polkadot"]

    if not query:
        return "Nyx: 🤖 It seems you didn't type anything. Try asking something like 'Which crypto is rising?'"

    if any(keyword in query for keyword in investment_keywords):
        profitable_cryptos = [
            crypto for crypto in crypto_profitability
            if crypto["price_trend"] == "rising" and crypto["market_cap"] in ["high", "medium"]
        ]

        if not profitable_cryptos:
            return "Nyx: Sorry, I couldn’t find any cryptocurrencies currently showing profitable trends."

        response = "Nyx: Here are some cryptocurrencies with rising trends and solid market cap:\n"
        for crypto in profitable_cryptos:
            response += f"- {crypto['name']} (Trend: {crypto['price_trend']}, Market Cap: {crypto['market_cap']})\n"

        top = profitable_cryptos[0]
        response += f"\n💡 Recommendation: Consider investing in {top['name']} — it's showing positive growth and has a good market position! 🚀"
        return response

    elif any(word in query for word in crypto_related_keywords):
        # Crypto-related but no investment intent detected
        return "Nyx: I see you're asking about crypto! Try asking about investments or profitable trends. For example:\n- 'Which crypto is growing fast?'\n- 'Where should I invest now?'"

    else:
        # Off-topic or confusing input
        return "Nyx: 🤔 I'm a crypto chatbot, so I might not be able to help with that. Try asking about cryptocurrencies, investments, or market trends."

# 🧪 Test function
def run_test():
    test_queries = [
        "What crypto should I invest in for growth?",
        "Show me rising cryptocurrencies",
        "Tell me about Ethereum's price",
        "Hi Nyx!",
        "What's your favorite color?",
        "",
        "Help me make money with crypto",
        "Are there falling cryptos?",
        "What's the weather like today?",
        "Best crypto to make profit?",
        "Do you like pizza?",
        "Tell me about blockchain"
    ]

    print("🧪 Chatbot Test Results:\n")
    for i, query in enumerate(test_queries, 1):
        print(f"Test {i}: You → {query}")
        print(get_profitable_crypto(query))
        print("-" * 60)

# Run the test
run_test()

# Run Test Function 

Here is the run test function

# Sample profitability dataset
crypto_profitability = [
    {"name": "Bitcoin", "price_trend": "rising", "market_cap": "high"},
    {"name": "Ethereum", "price_trend": "stable", "market_cap": "high"},
    {"name": "Cardano", "price_trend": "rising", "market_cap": "medium"},
    {"name": "Dogecoin", "price_trend": "falling", "market_cap": "low"},
    {"name": "Polkadot", "price_trend": "rising", "market_cap": "medium"},
]

def get_profitable_crypto(query):
    query = query.lower().strip()

    # Keywords indicating investment intent
    investment_keywords = ["invest", "growth", "profit", "make money", "price", "best crypto", "rising"]

    # Basic check for empty input
    if not query:
        return "Nyx: I didn't catch that. Could you type something about crypto investments or trends?"

    # Check for investment intent
    if any(keyword in query for keyword in investment_keywords):
        profitable_cryptos = [
            crypto for crypto in crypto_profitability
            if crypto["price_trend"] == "rising" and crypto["market_cap"] in ["high", "medium"]
        ]

        if not profitable_cryptos:
            return "Nyx: Sorry, I couldn’t find any cryptocurrencies currently showing profitable trends."

        response = "Nyx: Here are some cryptocurrencies with rising trends and solid market cap:\n"
        for crypto in profitable_cryptos:
            response += f"- {crypto['name']} (Trend: {crypto['price_trend']}, Market Cap: {crypto['market_cap']})\n"

        top = profitable_cryptos[0]
        response += f"\n💡 Recommendation: Consider investing in {top['name']} — it's showing positive growth and has a good market position! 🚀"
        return response
    else:
        # Fallback for unrelated or unsupported queries
        return "Nyx: I specialize in crypto profitability advice. Try asking things like:\n- 'Which crypto is rising?'\n- 'What’s the best coin to invest in now?'"

# 🧪 Test function
def run_test():
    test_queries = [
        "What crypto should I invest in for growth?",
        "Show me rising cryptocurrencies",
        "Tell me about Ethereum's price",
        "Hi Nyx!",
        "What's your favorite color?",
        "",
        "Help me make money with crypto",
        "Are there falling cryptos?",
        "What's the weather like today?",
        "Best crypto to make profit?"
    ]

    print("🧪 Chatbot Test Results:\n")
    for i, query in enumerate(test_queries, 1):
        print(f"Test {i}: You → {query}")
        print(get_profitable_crypto(query))
        print("-" * 60)

# Run the test
run_test()

# Cryptopia Chatbot – Updated to handle specific coin queries + intent

# Cryptocurrency database
cryptos = [
    {"name": "Bitcoin", "profitability": "high", "sustainability": "low"},
    {"name": "Ethereum", "profitability": "medium", "sustainability": "medium"},
    {"name": "Cardano", "profitability": "medium", "sustainability": "high"},
    {"name": "Solana", "profitability": "high", "sustainability": "medium"},
    {"name": "Nano", "profitability": "low", "sustainability": "high"},
]

# Normalize and index coin names
coin_names = [crypto["name"].lower() for crypto in cryptos]

# Detect intent: general advice vs coin-specific
def parse_query(query):
    query = query.lower()
    matched_coins = [coin for coin in coin_names if coin in query]

    if matched_coins:
        return "coin_info", matched_coins[0]

    elif any(word in query for word in ["eco", "green", "environment", "sustain", "climate"]):
        return "sustainability", None

    elif any(word in query for word in ["profit", "invest", "money", "gain", "grow"]):
        return "profitability", None

    else:
        return "unknown", None

# Give advice on sustainability
def handle_sustainability_query():
    sustainable = [c["name"] for c in cryptos if c["sustainability"] == "high"]
    if sustainable:
        return f"🌱 These cryptocurrencies are considered eco-friendly: {', '.join(sustainable)}.\n⚠️ *Not financial advice.*"
    else:
        return "❌ Sorry, I couldn't find any sustainable coins."

# Give advice on profitability
def handle_profitability_query():
    profitable = [c["name"] for c in cryptos if c["profitability"] == "high"]
    if profitable:
        return f"📈 These coins are known for high profitability: {', '.join(profitable)}.\n⚠️ *Not financial advice.*"
    else:
        return "❌ Sorry, no highly profitable coins found."

# Analyze specific coin
def analyze_specific_coin(coin_name):
    for crypto in cryptos:
        if crypto["name"].lower() == coin_name:
            return (
                f"🔍 Here's what I found about {crypto['name']}:\n"
                f"📈 Profitability: {crypto['profitability'].capitalize()}\n"
                f"🌿 Sustainability: {crypto['sustainability'].capitalize()}\n"
                f"⚠️ *Please do your own research before investing.*"
            )
    return f"❌ Sorry, I couldn't find data for '{coin_name}'."

# Chat loop
print(" Welcome to Cryptopia — your crypto sustainability & profitability advisor!")
print("💬 Ask about any coin, or type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Cryptopia: Goodbye! Stay smart in your crypto journey.")
        break

    intent, coin = parse_query(user_input)

    if intent == "sustainability":
        print("Cryptopia:", handle_sustainability_query())
    elif intent == "profitability":
        print("Cryptopia:", handle_profitability_query())
    elif intent == "coin_info":
        print("Cryptopia:", analyze_specific_coin(coin))
    else:
        print("Cryptopia:  I can help you with crypto sustainability and profitability. Try asking about a specific coin like 'Tell me about Cardano'.")


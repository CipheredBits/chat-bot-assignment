# Step 1: Define Cryptopia's personality
print("👋 Hello! I’m Cryptopia, your first AI-powered financial sidekick!")
print("I’m here to help you analyze crypto profitability and sustainability.")
print("Type 'exit' anytime to end our chat.\n")

# Step 2: Create user input system + chatbot loop
while True:
    user_input = input("💬 Which cryptocurrency do you want advice on? ")

    if user_input.lower() == 'exit':
        print("👋 Goodbye! Remember, always do your own research. Stay smart!")
        break
    else:
        print(f"🔍 Got it! You asked about {user_input}. Let me analyze it for you...\n")
        

# Cryptopia – A Cryptocurrency Advice Chatbot

Cryptopia is a simple, rule-based Python chatbot that helps users make sense of cryptocurrency choices based on **profitability** and **sustainability**. It offers educational, non-financial advice to curious investors or beginners looking for eco-friendly or profitable crypto coins.

> ⚠️ Disclaimer: Cryptopia does **not** provide real-time data or financial advice. It is a learning project built for demonstration purposes only.

---

## 💡 Features

-  Understands questions about specific coins (e.g., "Is Ethereum sustainable?")
-  Recommends eco-friendly cryptocurrencies
-  Suggests coins known for high profitability
-  Gracefully handles unclear or unrelated questions
-  Interactive chat loop in the terminal

---

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Clone the repo or copy the code into a `.py` file.
3. Run it in the terminal:

```bash
python cryptopia_chatbot.py
```

4. Type your question (e.g., *"Which coin is most sustainable?"* or *"Tell me about Bitcoin"*).
5. Type `exit` to end the chat.

---

## Team Contributions

### 🔹priscillanzula
- Designed the bot's tone and personality (friendly + professional)
- Built the user input system and chatbot loop (`while True:` interaction)

### 🔹 Doreenmongina
- Implemented the sustainability logic
- Created `handle_sustainability_query()` to recommend eco-friendly coins

### 🔹golibemartha
- Implemented the profitability logic
- Created `handle_profitability_query()` for investment-related questions

### 🔹 YewandeMorris
- Handled confusing or vague user input
- Wrote fallback messages and helped test weird edge cases

### 🔹 CipheredBits
- Set up GitHub repo + folder structure
- Created `parse_query()` for intent detection (coin name, sustainability, or profitability)
- Integrated and cleaned up the final chatbot logic
- Wrote this README and ensured project readiness for submission

---



## ✅ Sample Interactions

```
You: Which coin is most eco-friendly?
Cryptopia: 🌱 These cryptocurrencies are considered eco-friendly: Cardano, Nano.

You: Tell me about Ethereum
Cryptopia:
🔍 Here's what I found about Ethereum:
📈 Profitability: Medium
🌿 Sustainability: Medium
```

---

## 📝 Notes

- This chatbot is fully offline and uses a fixed list of cryptocurrencies.
- It was built during our group specialization project in the **AI for Software Engineers** track.
- Ideal for showcasing logic-based bots, Python conditionals, and basic intent detection.

---



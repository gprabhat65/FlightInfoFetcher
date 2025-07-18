# ✈️ FlightInfoFetcher — Two-Agent System with Function Calling & Structured Output

## 📌 Project Overview
`FlightInfoFetcher` is a lightweight, modular two-agent system designed to handle **airline flight queries** using structured reasoning. It supports:
- 📦 **Structured output** in JSON
- 🧠 **Modular architecture** with independent agents
- ⚙️ **Custom function calling** to simulate intelligent coordination between agents

---

## 🤖 System Architecture

### 🔹 1. **Info Agent**
- Reads from `flight_data.json`
- Retrieves flight details like:
  - ✈️ Flight Name
  - 🛫 Source & Destination
  - 🕑 Departure & Arrival Times
  - 🪪 Airline Operator
- Returns structured **JSON** responses

### 🔹 2. **QA Agent**
- Accepts user queries in natural language
- Parses the query to identify the flight name
- Calls the **Info Agent** with appropriate arguments
- Returns a neatly formatted and structured JSON result

---

## 🧑‍💻 Technologies Used
- Python 3.11
- JSON for data storage
- Environment Variables for API keys (via `.env` file)
- OpenAI API (optional / for advanced LLM integration)

---

## 📂 Project Structure


---

## ⚙️ Setup Instructions

### ✅ Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Anaconda](https://www.anaconda.com/) (for environment management)
- [PyCharm (optional)](https://www.jetbrains.com/pycharm/) — IDE of choice

### 📦 Installation via Conda

```bash
# Step 1: Create a conda environment
conda create -n problem1_env python=3.11

# Step 2: Activate the environment
conda activate problem1_env

# Step 3: Install dependencies
pip install -r requirements.txt


# In the activated environment
python agent_system.py


Enter flight name: AI202
{
  "flight": "AI202",
  "source": "Delhi",
  "destination": "Mumbai",
  "departure": "10:30 AM",
  "arrival": "12:45 PM",
  "airline": "Air India"
}

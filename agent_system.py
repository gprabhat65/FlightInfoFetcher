import json
import re
import os
from pathlib import Path

# Define the path to the JSON file relative to the script location
SCRIPT_DIR = Path(__file__).parent
FLIGHT_DATA_FILE = SCRIPT_DIR / "flight_data.json"


def load_flight_data() -> dict:
    if not FLIGHT_DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find '{FLIGHT_DATA_FILE}'. "
            f"Please ensure it is in the same directory as '{__file__}'."
        )

    with open(FLIGHT_DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Error decoding '{FLIGHT_DATA_FILE}': {e}. "
                f"Check the file for valid JSON syntax.",
                e.doc, e.pos
            )


def get_flight_info(flight_number: str) -> dict:
    flight_data = load_flight_data()
    return flight_data.get(flight_number, {"flight_number": flight_number, "status": "Not found"})


def info_agent_request(flight_number: str) -> str:
    flight_data = get_flight_info(flight_number)
    return json.dumps(flight_data)


def qa_agent_respond(user_query: str) -> str:
    # Extract flight number from query using regex
    match = re.search(r"Flight (\w+)", user_query, re.IGNORECASE)
    if not match:
        return json.dumps({"answer": "Please provide a valid flight number."})

    flight_number = match.group(1)
    flight_info_json = info_agent_request(flight_number)
    flight_info = json.loads(flight_info_json)

    # Construct response based on query intent
    if "when" in user_query.lower() or "depart" in user_query.lower():
        if flight_info["status"] == "Not found":
            return json.dumps({"answer": f"Flight {flight_number} not found in database."})
        return json.dumps({
            "answer": f"Flight {flight_number} departs at {flight_info['departure_time']} "
                      f"to {flight_info['destination']}. Current status: {flight_info['status']}."
        })
    elif "status" in user_query.lower():
        if flight_info["status"] == "Not found":
            return json.dumps({"answer": f"Flight {flight_number} not found in database."})
        return json.dumps({"answer": f"The status of Flight {flight_number} is {flight_info['status']}."})
    else:
        return json.dumps({"answer": "Sorry, I can only respond to departure time or status queries."})


# Test cases
if __name__ == "__main__":
    try:
        # Test get_flight_info
        print("get_flight_info('AI123'):", json.dumps(get_flight_info("AI123"), indent=2))
        print("get_flight_info('AI456'):", json.dumps(get_flight_info("AI456"), indent=2))
        print("get_flight_info('AI999'):", json.dumps(get_flight_info("AI999"), indent=2))
        print("get_flight_info('XYZ789'):", json.dumps(get_flight_info("XYZ789"), indent=2))

        # Test info_agent_request
        print("info_agent_request('AI123'):", info_agent_request("AI123"))
        print("info_agent_request('AI999'):", info_agent_request("AI999"))

        # Test qa_agent_respond
        test_queries = [
            "When does Flight AI123 depart?",
            "What is the status of Flight AI999?",
            "What time does Flight AI456 depart?",
            "What is the status of Flight XYZ789?",
            "Invalid query without flight number"
        ]
        for query in test_queries:
            print(f"qa_agent_respond('{query}'):", qa_agent_respond(query))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
"""
Garden Advice App (Console)

Issue #1:
- user input instead of hardcoded values
- advice stored in dictionaries
- functions for clean, modular code
"""

from typing import Dict

SEASON_ADVICE: Dict[str, str] = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "autumn": "Clear fallen leaves and prepare soil with compost.",
    "spring": "Start planting and watch for early pests.",
}

PLANT_ADVICE: Dict[str, str] = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests and ensure consistent watering.",
    "herb": "Harvest regularly to encourage growth.",
    "shrub": "Prune lightly to maintain shape and remove dead branches.",
}


def normalise(text: str) -> str:
    """Lowercase and strip whitespace for consistent matching."""
    return text.strip().lower()


def get_input(prompt: str) -> str:
    """Get input from the user and normalise it."""
    return normalise(input(prompt))


def give_advice(season: str, plant_type: str) -> str:
    """Return advice for the given season and plant type."""
    season_msg = SEASON_ADVICE.get(season, "No advice for this season.")
    plant_msg = PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return f"{season_msg}\n{plant_msg}"


def main() -> None:
    """Main program flow."""
    print("🌱 Garden Advice App")
    season = get_input("Enter the season (summer/winter/autumn/spring): ")
    plant_type = get_input("Enter the plant type (flower/vegetable/herb/shrub): ")

    print("\n--- Your Gardening Advice ---")
    print(give_advice(season, plant_type))


if __name__ == "__main__":
    main()
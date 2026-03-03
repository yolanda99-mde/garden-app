"""
Garden Advice App (Console)

Issue #2 improvements:
- Defensive input validation (keeps asking until valid)
- Plant recommendations by season
- Better documentation
"""

from typing import Dict, List

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

RECOMMENDATIONS: Dict[str, List[str]] = {
    "summer": ["Lavender", "Rosemary", "Tomatoes", "Marigolds"],
    "winter": ["Kale", "Spinach", "Garlic", "Winter pansies"],
    "autumn": ["Broccoli", "Cabbage", "Swiss chard", "Alyssum"],
    "spring": ["Basil", "Lettuce", "Strawberries", "Petunias"],
}


def normalise(text: str) -> str:
    """Lowercase and strip whitespace for consistent matching."""
    return text.strip().lower()


def ask_choice(prompt: str, options: List[str]) -> str:
    """Ask until the user types a valid option."""
    options_display = ", ".join(options)
    while True:
        value = normalise(input(f"{prompt} ({options_display}): "))
        if value in options:
            return value
        print(f"Invalid choice. Please enter one of: {options_display}")


def build_advice(season: str, plant_type: str) -> str:
    """Build advice message with seasonal recommendations."""
    season_msg = SEASON_ADVICE[season]
    plant_msg = PLANT_ADVICE[plant_type]
    recs = RECOMMENDATIONS.get(season, [])
    rec_msg = f"Plants that thrive in {season}: {', '.join(recs)}" if recs else ""
    return "\n".join([season_msg, plant_msg, rec_msg]).strip()


def main() -> None:
    """Main program flow."""
    print("🌱 Garden Advice App")
    season = ask_choice("Enter the season", ["summer", "winter", "autumn", "spring"])
    plant_type = ask_choice("Enter the plant type", ["flower", "vegetable", "herb", "shrub"])

    print("\n--- Your Gardening Advice ---")
    print(build_advice(season, plant_type))


if __name__ == "__main__":
    main()
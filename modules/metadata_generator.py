def generate_metadata(coin_name, purpose, audience):
    """
    Generate metadata for a new cryptocurrency coin.
    Includes basic information like coin name, purpose, and target audience.
    """
    metadata = {
        "coin_name": coin_name,
        "purpose": purpose,
        "target_audience": audience,
        "symbol": coin_name[:3].upper(),
        "launch_date": "2024-10-20",
        "description": f"{coin_name} is designed to revolutionize {purpose} for {audience}."
    }
    return metadata

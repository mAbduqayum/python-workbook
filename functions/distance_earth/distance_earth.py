import math


def distance_earth(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    # Convert to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Earth's radius in kilometers
    R = 6371
    distance = R * c

    return distance


if __name__ == "__main__":
    # Test your function
    distance_earth(0, 0, 0, 0)  # 0.0
    distance_earth(40.7128, -74.0060, 34.0522, -118.2437)  # ~5574 km

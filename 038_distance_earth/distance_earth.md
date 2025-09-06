# Exercise: Distance Between Two Points on Earth

Write a program that calculates the distance between two points on Earth's surface using the great circle distance formula.

## Task
- Read latitude and longitude of first point (as `float`)
- Read latitude and longitude of second point (as `float`)
- Calculate and display the distance in kilometers

## Examples
**Example 1:**
```
Enter latitude of first point: 49.2827
Enter longitude of first point: -123.1207
Enter latitude of second point: 45.5152
Enter longitude of second point: -122.6784
Distance: 312.46 km
```

**Example 2:**
```
Enter latitude of first point: 40.7128
Enter longitude of first point: -74.0060
Enter latitude of second point: 51.5074
Enter longitude of second point: -0.1278
Distance: 5570.85 km
```

**Example 3:**
```
Enter latitude of first point: 35.6762
Enter longitude of first point: 139.6503
Enter latitude of second point: 37.7749
Enter longitude of second point: -122.4194
Distance: 8267.25 km
```

## Formula
`distance = 6371.01 × arccos(sin(lat1) × sin(lat2) + cos(lat1) × cos(lat2) × cos(lon1 - lon2))`

## Note
- Use `.2f` formatting to display 2 decimal places
- Convert degrees to radians using `math.radians()`
- Use `math.acos()`, `math.sin()`, `math.cos()`
- `6371.01` is Earth's average radius in kilometers
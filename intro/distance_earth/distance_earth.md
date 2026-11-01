# Exercise: Distance Between Two Points on Earth

Write a program that calculates the distance (in kilometers) between two points on Earth's surface, given each point's latitude and longitude in degrees, using the great circle distance formula.

## Examples

**Example 1: Dushanbe to Khujand (Tajikistan)**

```
Enter first latitude: 38.5598
Enter first longitude: 68.7870
Enter second latitude: 40.2789
Enter second longitude: 69.6210
```

```
Distance: 204.14 km
```

## Formula

First convert every coordinate from degrees to radians, then:

`distance = 6371.01 × arccos(sin(lat1) × sin(lat2) + cos(lat1) × cos(lat2) × cos(lon1 - lon2))`

where `lat1, lat2, lon1, lon2` are the radian values, and `6371.01` is
Earth's average radius in kilometers.

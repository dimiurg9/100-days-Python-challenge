"""
unitt test for the simple method
"""

def calculate_average(numbers):
    avg = sum(numbers)/len(numbers)
    print(avg)
    return avg

def test_calculate_average():
    # potitive
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([-1, 2, 3, 4, 5]) == 2.6



test_calculate_average()
#ChatGPT assisted math file for testing functions

def calculate_y_coordinate(value):
    """
    Calculate y coordinate based on given value.

    Arguments:
    value -- the input value (between 0 and 50)

    Returns:
    y_coordinate -- the calculated y coordinate
    """
    slope = (498-280) / 50
    y_coordinate = slope * value + 280
    return y_coordinate

for value in range(0, 51):
    y_coordinate = calculate_y_coordinate(value)
    print(f"Value: {value}, Y coordinate: {y_coordinate}")

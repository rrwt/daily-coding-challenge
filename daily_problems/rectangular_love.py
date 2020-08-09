"""
Write a function to find the rectangular intersection of two given love rectangles.
Love rectangles are always "straight" and never "diagonal.
More rigorously: each side is parallel with either the x-axis or the y-axis.
They are defined as dictionaries ↴ like this:
  my_rectangle = {
    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,
}
"""


def find_range_overlap(point1, length1, point2, length2):
    # Find the highest start point and lowest end point.
    # The highest ("rightmost" or "upmost") start point is
    # the start point of the overlap.
    # The lowest end point is the end point of the overlap.
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    # Return null overlap if there is no overlap
    if highest_start_point >= lowest_end_point:
        return None, None

    # Compute the overlap length
    overlap_length = lowest_end_point - highest_start_point

    return highest_start_point, overlap_length


def find_rectangular_overlap(rect1, rect2):
    # Get the x and y overlap points and lengths
    x_overlap_point, overlap_width = find_range_overlap(
        rect1["left_x"], rect1["width"], rect2["left_x"], rect2["width"]
    )
    y_overlap_point, overlap_height = find_range_overlap(
        rect1["bottom_y"], rect1["height"], rect2["bottom_y"], rect2["height"]
    )

    # Return null rectangle if there is no overlap
    if not overlap_width or not overlap_height:
        return {
            "left_x": None,
            "bottom_y": None,
            "width": None,
            "height": None,
        }

    return {
        "left_x": x_overlap_point,
        "bottom_y": y_overlap_point,
        "width": overlap_width,
        "height": overlap_height,
    }

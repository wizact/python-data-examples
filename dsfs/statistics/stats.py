import math
from collections import Counter
from typing import List

import matplotlib.pyplot as plt
from scratch.linear_algebra import sum_of_squares

num_friends: List[float] = [
    100,
    49,
    50,
    23,
    25,
    33,
    3,
    5,
    7,
    50,
    48,
    49,
    7,
    7,
    5,
    3,
    3,
    3,
    3,
    7,
]

friend_counts = Counter(num_friends)


def plot_friends():
    """plot the number of friends people have"""
    xs = range(101)
    xy = [friend_counts[i] for i in xs]
    plt.title("Histogram of friends count")
    plt.xlabel("number of friends")
    plt.ylabel("number of people")

    plt.bar(xs, xy)
    plt.axes([0, 101, 0, 10])
    plt.show()


num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
largest_value = sorted_values[-1]
smallest_value = sorted_values[0]


def mean(xs: List[float]) -> float:
    """Returns the mean of elements in an array"""
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    """Returns the element in the middle of a sorted array"""
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """Returns the avg of the two elements in the middle of a sorted array"""
    sorted_xs = sorted(xs)
    hi_point = len(xs) // 2
    return (sorted_xs[hi_point - 1] + sorted_xs[hi_point]) / 2


def media(xs: List[float]) -> float:
    """Returns the middle-most value of xs"""
    return _median_even(xs) if len(xs) % 2 == 0 else _median_odd(xs)


def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in xs"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def mod(xs: List[float]) -> List[float]:
    """Returns the most common values"""
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.values() if count == max_count]


def data_range(xs: List[float]) -> float:
    """Returns the diff between the largest and smallest value"""
    return max(xs) - min(xs)


def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    xs_bar = mean(xs)
    return [x - xs_bar for x in xs]


def variance(xs: List[float]) -> float:
    """Returns the avg squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least 2 elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / n - 1

def std_deviation(xs: List[float]) -> float:
    """Returns the standard deviation of a sample"""
    return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

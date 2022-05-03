import pandas as pd
from cydets.algorithm import detect_cycles


def main():
    series = pd.Series([0, 1, 0, 0.5, 0, 1, 0, 0.5, 0, 1, 0])
    print(series)
    print(detect_cycles(series))


main()
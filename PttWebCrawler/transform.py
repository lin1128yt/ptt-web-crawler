import pandas as pd
import numpy as np
import json
import yaml
import sys


def main():
    # print command line arguments

    filename = sys.argv[1]
    print(filename)
    data = yaml.load(open(filename))

    df = pd.DataFrame(data)
    df.to_csv(f"{filename}.csv", encoding='utf-8', index=False)


if __name__ == "__main__":
    main()

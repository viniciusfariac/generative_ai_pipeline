from extract import extract_users
from transform import generate_news
from load import load_users
import pandas as pd

def main():
    path = "data/users.csv"
    df = extract_users(path)

    print(df.head())


if __name__ == "__main__":
    main()
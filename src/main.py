from extract import extract_users
from transform import generate_news


def main():
    path = "data/users.csv"
    df = extract_users(path)
    generate_news(df)
    df.to_csv("data/users.csv", index=False)


if __name__ == "__main__":
    main()
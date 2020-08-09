import psycopg2


from aws_learn.sql.Constants import RDS_URL, RDS_PORT, RDS_USERNAME, RDS_PASSWORD


def connect(database: str):
    print(RDS_URL, RDS_PORT, database, RDS_USERNAME, RDS_PASSWORD)

    x = f"postgresql://{RDS_URL}/TEST?user={RDS_USERNAME}&password={RDS_PASSWORD}"

    return psycopg2.connect(x)


if __name__ == "__main__":
    "postgresql:///mydb?user=other&password=secret"

    print("hi")
    connection = connect("TEST")
    breakpoint()
    pass

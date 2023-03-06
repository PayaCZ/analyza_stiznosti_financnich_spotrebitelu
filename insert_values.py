import csv
import psycopg2


if __name__ == "__main__":

    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="petulilinka",
        host="localhost",
        port="5432",
    )

    cur = conn.cursor()  

    with open(
        "C:/Users/Uzivatel/Desktop/financial_consumer_complaints.csv",
        "r",
    ) as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        for row in reader:
            cur.execute(
                "INSERT INTO financial_consumer_complaints VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                row,
            )

    conn.commit()
    conn.close()
    print("1 = Closed / 0 = Open: ", "--", conn.closed, "--")

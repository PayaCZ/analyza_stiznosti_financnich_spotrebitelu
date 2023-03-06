import os
import psycopg2

from psycopg2 import sql

if __name__ == "__main__":

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DATABASE", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "petulilinka"),
    )

    with conn, conn.cursor() as cur:
        create_test_stiznosti_2_table_query = sql.SQL(
            """
            DROP TABLE IF EXISTS financial_consumer_complaints;
            CREATE TABLE financial_consumer_complaints
            (
                Complaint_ID INT PRIMARY KEY,
                Date_Sumbited VARCHAR(150),
                Product VARCHAR(150),
                Sub_product VARCHAR(150),
                Issue VARCHAR(150),
                Sub_issue VARCHAR(150),
                Company_public_response VARCHAR(150),
                Company VARCHAR(150),
                State VARCHAR(150),
                ZIP_code VARCHAR(150),
                Tags VARCHAR(150),
                Consumer_consent_provided VARCHAR(150),
                Submitted_via VARCHAR(150),
                Date_Received VARCHAR(150),
                Company_response_to_consumer VARCHAR(150),
                Timely_response VARCHAR(150),
                Consumer_disputed VARCHAR(150)
            );
            """
        )

        print(create_test_stiznosti_2_table_query.as_string(cur))
        cur.execute(create_test_stiznosti_2_table_query)
        print("financial_consumer_complaints table created")

    conn.close()
    print("1 = Closed / 0 = Open: ", "--", conn.closed, "--")

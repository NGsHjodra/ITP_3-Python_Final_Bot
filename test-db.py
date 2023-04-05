import logging
import os

import psycopg2
from dotenv import load_dotenv

def main():
    # load environment variables
    load_dotenv()

    # connect to the PostgreSQL server
    logging.info('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(host=os.getenv('POSTGRES_HOST_EXTERNAL'),
                            database=os.getenv('POSTGRES_DB'),
                            user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD'))

    logging.info('Connected.')

    # create table products
    logging.info('Creating table...')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS history')
    
    # create table of name and url
    cur.execute('CREATE TABLE history ( name TEXT, url TEXT )')

    # create sample data
    logging.info('Creating sample data...')
    sample_data = [ 
        ('NGs#203', 'https://www.youtube.com/watch?v=QH2-rsat'),
        ('NGs#204', 'https://www.youtube.com/watch?v=QH2-Tastwu3'),
        ('NGs#205', 'https://www.youtube.com/watch?v=QH2-atrsat')
    ]

    # insert a new products
    logging.info('Inserting data...')
    for data in sample_data:
        cur.execute('INSERT INTO history (name, url) VALUES (%s, %s)', data)

    conn.commit()

    # display the products
    logging.info('Displaying data...')
    cur.execute('SELECT * FROM history')
    rows = cur.fetchall()
    for row in rows:
        logging.info(row)

    # close the communication with the PostgreSQL
    cur.close()
    conn.close()
    logging.info('Done.')

if __name__ == "__main__":
    format = "SRV: %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%F-%H-%M-%S")

    main()
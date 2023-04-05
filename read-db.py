import logging
import os
import socket

import psycopg2
from dotenv import load_dotenv

def main():
    # load environment variables
    load_dotenv()

    # connect to the PostgreSQL server
    logging.info('Connecting to the PostgreSQL database...')
    DOCKER_HOST = socket.gethostbyname('docker.for.mac.localhost')  # Use the IP address of your Docker host here
    conn = psycopg2.connect(host=DOCKER_HOST,
                            database=os.getenv('POSTGRES_DB'),
                            user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD'))

    logging.info('Connected.')

    # create table products
    logging.info('Creating table...')
    cur = conn.cursor()
    
    # display the products
    logging.info('Displaying data...')
    cur.execute('SELECT * FROM history') # WHERE name = %s', ('NGs#203',)
    rows = cur.fetchall()
    for row in rows:
        logging.info(repr(row[0]) + ' ' + repr(row[1]))

    # close the communication with the PostgreSQL
    cur.close()
    conn.close()
    logging.info('Done.')

if __name__ == "__main__":
    format = "SRV: %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%F-%H-%M-%S")

    main()
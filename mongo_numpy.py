from pymongo import MongoClient
from configparser import RawConfigParser
import numpy as np
from pprint import pprint


def array_from_task(dbname, colname):
    client = MongoClient()
    db = client[dbname]
    col = db[colname]

    return





def main():
    config = RawConfigParser()
    config.read('data_handler.properties')
    dbname = config.get('DatabaseSection', 'database.dbname')
    colname = config.get('DatabaseSection', 'database.colname')
    array_from_task(dbname, colname)
    return


if __name__ == "__main__":
    main()


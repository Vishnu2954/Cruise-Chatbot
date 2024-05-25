import mysql.connector

db_config = {
    'user': 'root',
    'password': 'Vishnu_2954',
    'host': 'localhost',
    'database': 'cruise',
}

def get_precaution(disease):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = "SELECT Precaution FROM precaution_remedy WHERE Disease = %s"
        cursor.execute(query, (disease,))
        result = cursor.fetchone()
        cursor.close()
        cnx.close()

        if result:
            return result[0]
        else:
            return None  # Return None if no result found

    except mysql.connector.Error as err:
        return f"Error: {err}"

def get_remedy(disease):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = "SELECT Remedy FROM precaution_remedy WHERE Disease = %s"
        cursor.execute(query, (disease,))
        result = cursor.fetchone()
        cursor.close()
        cnx.close()

        if result:
            return result[0]
        else:
            return None

    except mysql.connector.Error as err:
        return f"Error: {err}"

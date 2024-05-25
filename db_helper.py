import csv

def get_precaution(disease):
    try:
        with open('precaution_remedy.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Disease'] == disease:
                    return row['Precaution']
        return None 

    except FileNotFoundError:
        return "Error: CSV file not found"
    except Exception as e:
        return f"Error: {e}"

def get_remedy(disease):
    try:
        with open('precaution_remedy.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Disease'] == disease:
                    return row['Remedy']
        return None  

    except FileNotFoundError:
        return "Error: CSV file not found"
    except Exception as e:
        return f"Error: {e}"

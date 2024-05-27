import pandas as pd

def get_precaution(disease):
    try:
        df = pd.read_excel('precaution_remedy.xlsx')
        row = df[df['Disease'] == disease]
        if not row.empty:
            return row.iloc[0]['Precaution']
        else:
            return None 

    except FileNotFoundError:
        return "Error: Excel file not found"
    except Exception as e:
        return f"Error: {e}"

def get_remedy(disease):
    try:
        df = pd.read_excel('precaution_remedy.xlsx')
        row = df[df['Disease'] == disease]
        if not row.empty:
            return row.iloc[0]['Remedy']
        else:
            return None 
            
    except FileNotFoundError:
        return "Error: Excel file not found"
    except Exception as e:
        return f"Error: {e}"

def get_causes(disease):
    try:
        df = pd.read_excel('precaution_remedy.xlsx')
        row = df[df['Disease'] == disease]
        if not row.empty:
            return row.iloc[0]['Causes']
        else:
            return None 

    except FileNotFoundError:
            return "Error: Excel file not found"
    except Exception as e:
            return f"Error: {e}"

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, FileResponse 
import pickle
import uvicorn
import db_helper
app = FastAPI()

with open('svm_rbf.pkl', 'rb') as f:
    svm, vectorizer, le = pickle.load(f)

@app.get("/cruise")
async def cruise():
    with open("cruise.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    query_text = payload['queryResult']['queryText']

    if intent == "disease.finder":
        return disease_finder(query_text, payload)
    elif intent == "disease.precaution":
        parameters = payload['queryResult']['parameters']
        return disease_precaution(parameters)
    elif intent == "disease.remedy":
        parameters = payload['queryResult']['parameters']
        return disease_remedy(parameters)
     elif intent == "disease.causes":
        parameters = payload['queryResult']['parameters']
        return disease_causes(parameters)
    return JSONResponse({})

def disease_finder(query_text: str, payload: dict):
    predicted_disease = predict_disease(query_text)
    fulfillment_text = payload['queryResult']['fulfillmentText']
    response_text = fulfillment_text.replace("$predicted_disease", predicted_disease)
    print("Response text:", response_text)
    payload['queryResult']['fulfillmentText'] = response_text
    return JSONResponse(content={"fulfillmentText": response_text})

def predict_disease(symptoms: str):
    symptoms_vec = vectorizer.transform([symptoms])
    predicted_disease_encoded = svm.predict(symptoms_vec)
    predicted_disease = le.inverse_transform(predicted_disease_encoded)[0]
    return predicted_disease

def disease_precaution(parameters: dict):
    disease_types = parameters['disease-types']
    if isinstance(disease_types, str):
        disease_types = [disease_types]

    precautions = []
    for disease in disease_types:
        precaution = db_helper.get_precaution(disease)
        if precaution:
            precautions.append(f"{precaution}")
        else:
            precautions.append(f"No precautions found for {disease}.")

    return JSONResponse(content={"fulfillmentText": " ".join(precautions)})

def disease_remedy(parameters: dict):
    disease_types = parameters['disease-types']
    if isinstance(disease_types, str):
        disease_types = [disease_types]

    remedies = []
    for disease in disease_types:
        remedy = db_helper.get_remedy(disease)
        if remedy:
            remedies.append(f"{remedy}")
        else:
            remedies.append(f"No remedies found for {disease}.")

    return JSONResponse(content={"fulfillmentText": " ".join(remedies)})

def disease_causes(parameters: dict):
    disease_types = parameters['disease-types']
    if isinstance(disease_types, str):
        disease_types = [disease_types]

    causes = []
    for disease in disease_types:
        cause = db_helper.get_remedy(disease)
        if cause:
            causes.append(f"{cause}")
        else:
            causes.append(f"No causes found for {disease}.")

    return JSONResponse(content={"fulfillmentText": " ".join(causes)})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

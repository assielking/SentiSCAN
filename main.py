from fastapi import Body, FastAPI,UploadFile,File,Depends, HTTPException, status, Request, Form
from typing import Optional
from pydantic import BaseModel
from joblib import load
from PIL import Image
import uvicorn
from colorama import init
from fastapi.security import APIKeyHeader
import hashlib 
from fastapi.responses import HTMLResponse ,StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import asyncio
from fastapi.responses import FileResponse
from io import BytesIO
import tempfile
from fastapi.responses import JSONResponse
import base64

loadel_model = load('emotions.joblib')

app = FastAPI()

class InputData(BaseModel):
    # Structure des données d'entrée
    comments : str

class OutputData(BaseModel):
    # Structure des données de sortie
    prediction: str



@app.post("/analyse")
async def sentiment( data : InputData):

    input_text = data.comments

    prediction = loadel_model.predict([input_text])

    return prediction[0]
    
#-------------------------Interface web--------------------------
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

#chargement de chaque page---------------------------------------
 
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("page.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def predict_p(request: Request):
    
    # Convertir la donnée d'entrée en tableau numpy
    
    form_data = await request.form()
    x =form_data["comment"]
    
    comment =str(x)
    # Faire la prédiction en utilisant le modèle entraîné
    prediction = loadel_model.predict([comment])

    # Créer l'objet de réponse
    msg = prediction[0]
    sent = msg
    return templates.TemplateResponse("page.html", {"request": request, "sent": msg})


if __name__=='__main__':
    init()
    uvicorn.run(app,host="127.0.0.1",port=8000)
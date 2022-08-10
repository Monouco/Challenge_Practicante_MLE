from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema.RequestData import RequestData
from modules.RequestDataModules import probEnfermedadCardiaca
import pickle


#inicializando el api
app = FastAPI()

app.add_middleware(
    CORSMiddleware,    
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#instanciando variable global pipe
with open("artifacts/pipe_file.pkl", "rb") as file:
    pipe = pickle.load(file)

#ruta del servicio
@app.post("/probEnfermedadCardiaca")
async def prob_enfermedad_cardiaca(request : RequestData):
    return probEnfermedadCardiaca(request, pipe)

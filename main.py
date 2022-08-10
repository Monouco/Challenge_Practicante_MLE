from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle
from pydantic import BaseModel
from sklearn.pipeline import Pipeline

#inicializando el api
app = FastAPI()
#instanciando variable global pipe
with open("pipe_file.pkl", "rb") as file:
    pipe = pickle.load(file)

app.add_middleware(
    CORSMiddleware,    
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#creando la clase del request
class RequestData(BaseModel):
    age:            int
    sex:            str
    chestPainType:  str
    restingBP:      int
    cholesterol:    int
    fastingBS:      int
    restingECG:     str
    maxHR:          int
    exerciseAngina: str
    oldpeak:        float
    stSlope:        str

    def toDataFrame(self):
        requestDict = {
            'Age':              [self.age],
            'Sex':              [self.sex],
            'ChestPainType':    [self.chestPainType],
            'RestingBP':        [self.restingBP],
            'Cholesterol':      [self.cholesterol],
            'FastingBS':        [self.fastingBS],
            'RestingECG':       [self.restingECG],
            'MaxHR':            [self.maxHR],
            'ExerciseAngina':   [self.exerciseAngina],
            'Oldpeak':          [self.oldpeak],
            'ST_Slope':         [self.stSlope]
        }
        return pd.DataFrame(requestDict)


#creando la funcion que calcula la probabilidad
def probEnfermedadCardiaca(request):
    inputData = request.toDataFrame()
    prob = pipe.predict_proba(inputData)[:,1]
    prob = {"prob": round(float(prob), 2)}  
    return prob

#funcion que carga el modelo preentrenado
@app.on_event("startup")
async def startup_event():
    with open("pipe_file.pkl", "rb") as file:
        pipe = pickle.load(file)

@app.post("/probEnfermedadCardiaca")
async def prob_enfermedad_cardiaca(request : RequestData):
    return probEnfermedadCardiaca(request)

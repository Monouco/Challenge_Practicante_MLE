from pydantic import BaseModel

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
    sTSlope:        str
    
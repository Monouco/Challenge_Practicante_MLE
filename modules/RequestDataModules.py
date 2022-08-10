import pandas as pd

#creando la funcion que calcula la probabilidad
def probEnfermedadCardiaca(request, pipe):
    reqDict = request.dict()
    inputData = pd.DataFrame([reqDict.values()], columns=reqDict.keys())
    #prediciendo la probabilidad
    prob = pipe.predict_proba(inputData)[:,1]
    prob = {"prob": round(prob.item(), 4)} 
    return prob
try:
    from config_dev import firebaseClient, user, auth

except:
    from config_prod import firebaseClient, user, auth

db = firebaseClient.database()

def WriteInitialValue(symbols, initialvalue):
    
    user_n = auth.refresh(user["refreshToken"])
    data = {"initialValue" : initialvalue}
    db.child(symbols).update(data,user_n["idToken"])

def GetInitialValue(symbols):

    # res = db.get().val()[symbols]
    # lasted_data = list(res.keys())[-1]
    # res_data = res[lasted_data]
    # print(res_data)

    #Value เริ่มต้น
    try:
        res = db.get(user_n["idToken"]).val()[symbols]["initialValue"]
        return res
    
    except KeyError:
        WriteInitialValue(symbols = symbols, initialvalue = 0)
        res = db.get(user["idToken"]).val()[symbols]["initialValue"]
        return res


def UpdateBotSetting(key,value):

    user_n = auth.refresh(user["refreshToken"])

    if key == "RUN":
        data = {"RUN": value}
        db.child("BOTSETTING").update(data,user_n["idToken"])

    elif key == "Positionsize":
        data = {"Positionsize": value}
        db.child("BOTSETTING").update(data,user_n["idToken"])

def GetDataBotSetting(key):
    res = db.get(user_n["idToken"]).val()["BOTSETTING"][key]
        return res


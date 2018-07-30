
def setPropositionType(object):

    if (object.is_universal == True and object.is_affirmative == True):
            object.type = "A"
    elif (object.is_universal == True and object.is_affirmative == False):
            object.type = "I"
    elif (object.is_universal == False and object.is_affirmative == True):
            object.type = "E"
    else:
            object.type = "O"


def setConclusionType(object,object2,object3):

    if  (object.type == "A" and object2.type == "A"):
        object3.type = "A"
    elif (object.type == "E" and object2.type == "A"):
        object3.type = "E"
    elif (object.type == "A" and object2.type == "I"):
        object3.type = "I"
    elif (object.type == "E" and object2.type == "I"):
        object3.type = "O"
    elif (object.type == "A" and object2.type == "E"):
        object3.type = "E"
    elif (object.type == "A" and object2.type == "O"):
        object3.type = "O"
    elif (object.type == "O" and object2.type == "A"):
        object3.type = "O"
    elif (object.type == "A" and object2.type == "A"):
        object3.type = "I"
    elif (object.type == "A" and object2.type == "E"):
        object3.type = "O"
    elif (object.type == "E" and object2.type == "A"):
        object3.type = "O"

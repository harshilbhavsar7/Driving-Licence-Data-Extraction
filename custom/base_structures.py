

## some basic functions to create structures

def get_predicts(result,class_names):
    predicts=[]
    for res,cname in zip(result,class_names):
        r=list(res[0])
        r.append(cname)
        predicts.append(r)
    print(predicts)
    return predicts
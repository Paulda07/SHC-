import boto3
def run_model(path):
    file = open(path, 'r') 
    text = file.read()
    client = boto3.client(service_name='comprehendmedical', region_name='us-east-1')
    result = client.detect_entities(Text= text)
    entities = result['Entities']
    flag = False
    names = []
    for entity in entities:
        if entity['Type']== 'NAME' and flag is False:
            flag = True
            print('Entity', entity)
            names.append(entity['Text'])
    med_con = []
    for entity in entities:
        if entity['Category']== 'MEDICAL_CONDITION':
            temp = entity['Traits']
            if len(temp) == 0:
                continue
            if len (temp) == 3 :
                temp = temp[2]
                if temp['Name'] == 'NEGATION':
                    continue
            if len (temp) == 2:
                temp = temp[1]
                if temp['Name'] == 'NEGATION':
                    continue
            if len(temp) == 1:
                temp = temp[0]
                if temp['Name'] == 'NEGATION' or temp['Name'] == 'SIGN' or temp['Name'] == 'SYMPTOM' or temp['Score']<0.75:
                    continue
            if entity['Text'] in med_con:
                continue
            med_con.append(entity['Text'])
            #print (entity)
            
    #print(med_con)
        
    dic = {names[0]: med_con}
    print (dic)
    return dic


    
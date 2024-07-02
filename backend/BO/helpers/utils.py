def boolean_converter(dict={}, list=[]):
    if dict:
        for i in dict:
            if dict[i] == 'true':
                dict[i] = True
            elif dict[i] == 'false':
                dict[i] = False
        return dict
    
    elif list:
        for l in list:
            if l == 'true':
                l = True
            elif l == 'false':
                l = False
        return list
    

def boolean_to_yes_or_no(dict={}):
    for i in dict:
        if type(dict[i]) == bool:  
            if dict[i] == True:
                dict[i] = 'S'
            elif dict[i] == False:
                dict[i] = 'N'
    return dict
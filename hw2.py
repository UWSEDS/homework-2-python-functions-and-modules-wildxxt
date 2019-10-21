import pandas as pd

def read_url(url):
    data = pd.read_csv(url)
    return data

def test_create_dataframe(data, col_list):
    check1 = (data.columns.tolist() == col_list)
    
    check2 = True
    true_col_list = data.columns.tolist();
    tp = type(true_col_list[0])
    for ele in true_col_list:
        if(type(ele) != tp):
            check2 = False
        
    check3 = (len(data)>=10)
    
    if((check1 and check2) and check3):
        return True
    return False
       
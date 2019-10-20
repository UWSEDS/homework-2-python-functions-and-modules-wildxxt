import pandas as pd

url = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
data = pd.read_csv(url)
# print(type(data))

col_list = data.columns.tolist()

def test_create_dataframe(data, col_list):
    check1 = (data.columns.tolist() == col_list)
    
    check2 = True
    tp = type(col_list[0])
    for ele in col_list:
        if(type(ele) != tp):
            check2 = False
        
    check3 = (len(data)>=10)
    
    if((check1 and check2) and check3):
        return True
    return False
       
test_create_dataframe(data, col_list)
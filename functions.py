import pandas as pd

def read_and_filter(fileName):
    df = pd.read_csv("downloads/%s"%fileName, index_col=False, header=1)
    df = df[['year','week','VCI','TCI','VHI','%Area_VHI_LESS_15','%Area_VHI_LESS_35']]
    df = df[(df['VHI']>=0)]
    return df

def max_VHI(df, year):
    yr=df[df['year']==int(year)] #max VHI
    max1 = max(yr.VHI)
    return max1

def min_VHI(df, year):
    yr=df[df['year']==int(year)] #min VHI
    min1 = min(yr.VHI)
    return min1

def extreme_drought_area(df, percent):
    a=df[(df['%Area_VHI_LESS_15']>=int(percent))] #search for extreme drought
    return a

def moderate_drought_area(df, percent):
    a=df[(df['%Area_VHI_LESS_35']>=int(percent))] #search for moderate drought
    return a

def add_task(df):
    ar = df[(df['year']>=2000) & (df['VHI']>=15) & (df['VHI']<=35)]
    print ar

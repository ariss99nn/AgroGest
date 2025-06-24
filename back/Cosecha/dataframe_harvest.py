import pandas as pd
from .models import Classification, Harvest_Type, Harvest, Harvest_Details

def dataframe_Classification():
    queryset = Classification.objects.all().values(
        'id', 'variety', 'classification', 'details', 'estimated_value', 'created_at'
    )
    df = pd.DataFrame(list(queryset))
    
    return df

def dataframe_Harvest_Type():
    queryset = Harvest_Type.objects.all().values(
        'id', 'name', 'start_date', 'end_date', 'classification', 'season', 'created_at'
    )
    
    df = pd.DataFrame(list(queryset))
    return df

def dataframe_Harvest():
    queryset = Harvest.objects.all().values(
        'id', 'name', 'quantity', 'harvest_method', 'type', 'season', 'latitude', 'longitude', 'created_at'
    )
    
    df = pd.DataFrame(list(queryset))
    return df

def dataframe_Harvest_Details():
    queryset = Harvest_Details.objects.all().values(
        'id', 'classification', 'estimated_price', 'profit_margin', 'overall_quality', 'diagram_data', 'created_at'
    )
    
    df = pd.DataFrame(list(queryset))
    return df
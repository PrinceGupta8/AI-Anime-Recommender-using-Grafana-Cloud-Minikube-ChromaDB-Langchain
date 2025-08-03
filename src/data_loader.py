import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_data:str,processed_data:str):
        self.original_data=original_data
        self.processed_data=processed_data

    def save_and_load_data(self):
        df=pd.read_csv(self.original_data,encoding="ISO-8859-1",on_bad_lines="skip").dropna()
        required_cols = {'Name' , 'Genres','sypnopsis'}
        missing=required_cols-set(df.columns)
        if missing:
            raise ValueError(f"{missing} column is missing")
        df['Combined_cols']=("Title: " + df['Name'] + " Generes: " + df['Genres'] +  "Oveview: " + df['sypnopsis'])
        df[['Combined_cols']].to_csv(self.processed_data,encoding="ISO-8859-1",index=False)
        return self.processed_data
    
    
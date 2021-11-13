import json
import pandas as pd
from pandas.core.indexes.base import Index

class BMICalculator():
    def __init__(self) -> None:
        pass
    
    def get_input(self):
        input_path="/home/pkumarre/code-13112021-pavankumarreddy/input/input.json"
        with open(input_path,'r') as input_file:
            input = json.loads(input_file.read())
        input_df = pd.json_normalize(input)
        return input_df
        
    def bmi_calculator(self,df):
        df['BMI'] = df["WeightKg"]/(df["HeightCm"]/100)
        df.loc[df['BMI']<=18.4, 'BMI Range(kg/m2)'] = '18.4 and below'
        df.loc[df['BMI'].between(18.5, 24.9, inclusive=True), 'BMI Range(kg/m2)'] = '18.5 - 24.9'
        df.loc[df['BMI'].between(25, 29.9, inclusive=True), 'BMI Range(kg/m2)'] = '25 - 29.9'
        df.loc[df['BMI'].between(30, 34.9, inclusive=True), 'BMI Range(kg/m2)'] = '30 - 34.9'
        df.loc[df['BMI'].between(35, 39.9, inclusive=True), 'BMI Range(kg/m2)'] = '35 - 39.9'
        df.loc[df['BMI']>=40, 'BMI Range(kg/m2)'] = '40 and above'

        
        df.loc[df['BMI Range(kg/m2)']=='18.4 and below', 'Health risk'] = 'Malnutrition risk'
        df.loc[df['BMI Range(kg/m2)']=='18.5 - 24.9', 'Health risk'] = 'Low risk'
        df.loc[df['BMI Range(kg/m2)']=='25 - 29.9', 'Health risk'] = 'Enhanced risk'
        df.loc[df['BMI Range(kg/m2)']=='30 - 34.9', 'Health risk'] = 'Medium risk'
        df.loc[df['BMI Range(kg/m2)']=='35 - 39.9', 'Health risk'] = 'High risk'
        df.loc[df['BMI Range(kg/m2)']=='40 and above', 'Health risk'] = 'Very high risk'

        
        df.loc[df['BMI Range(kg/m2)']=='18.4 and below', 'BMI Category'] = 'Underweight'
        df.loc[df['BMI Range(kg/m2)']=='18.5 - 24.9', 'BMI Category'] = 'Normal weight'
        df.loc[df['BMI Range(kg/m2)']=='25 - 29.9', 'BMI Category'] = 'Overweight'
        df.loc[df['BMI Range(kg/m2)']=='30 - 34.9', 'BMI Category'] = 'Moderately obese'
        df.loc[df['BMI Range(kg/m2)']=='35 - 39.9', 'BMI Category'] = 'Severely obese'
        df.loc[df['BMI Range(kg/m2)']=='40 and above', 'BMI Category'] = 'Very severely obese'
        return df

    def over_weight_count(self,df):
        filter_df = df['BMI Range(kg/m2)'].isin(["Overweight"])
        return filter_df.sum()


if __name__=="__main__":
    bmi = BMICalculator()
    input_df = bmi.get_input();
    bmi_df = bmi.bmi_calculator(input_df)
    print("BMI calculator dataframe after all transformations\n\n",bmi_df)
    overweight_df = bmi.over_weight_count(bmi_df)
    print("Total Number of overweight people from the inputs-->",overweight_df)


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
class DataCleaningClass:
    def data_info(self,data):
        cols,dtype,nulls,duplicates,uniques=[],[],[],[],[]
        for col in data.columns:
            cols.append(col)
            dtype.append(data[col].dtype)
            nulls.append(data[col].isnull().sum())
            duplicates.append(data.duplicated().sum())
            uniques.append(data[col].nunique())
        data=pd.DataFrame(
            {"Column":cols,"Data Type":dtype,"No of Null":nulls,"No of Uniques":uniques,"Duplicates":duplicates}
        )
        return data
    def replace_outliers_with_fences(self,data,num_cols):
        for col in num_cols:
            Q1= data[col].quantile(0.25)
            Q3= data[col].quantile(0.75)
            IQR=Q3-Q1
            lower_fence=Q1-1.5*IQR
            upper_fence=Q3+1.5*IQR
            lower_outliers=data[data[col]<lower_fence][col].values
            upper_outliers=data[data[col]>upper_fence][col].values
            data[col].replace(upper_outliers,upper_fence,inplace=True)
            data[col].replace(lower_outliers,lower_fence,inplace=True)
        return data
    def columns_histplot(self,data):
        c=3
        r=math.ceil(len(data.columns)/c)
        plt.figure(figsize=(20,5*r))
        for index,column in enumerate(data.columns,start=1):
            plt.subplot(r, c, index )
            plt.title(f"Histogram of {column}",fontsize=14,color="darkblue")
            sns.histplot(data[column], kde=True,color="red")
        plt.show()
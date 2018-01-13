import pandas as pd
import numpy as np
import geocoder
#For reading excel sheet
#here sheetname=0 means first sheet in Excel
sheet_1 = pd.read_excel("D:\KEPY tableau\Seagate - on Keyur_s Drive\Fraud Project\Spend Data\FY17_Q1_Spend_by_payment.xlsx",sheetname=0)

#It creates data frame for good output
df = pd.DataFrame(sheet_1)

#It gives distinct buyers Array.
buyers = df.Buyer.unique()
len(buyers)

#To combine data using space from multiple columns
df["V_Full_Address"] = df["V_ADDRESS_LINE1"].map(str) + " " + df["V_CITY"].map(str) + " " + df["V_STATE"].map(str) + " " + df["V_ZIP"].map(str) + " " + df["V_COUNTRY"].map(str)

#adding transaction number 
#np.arrange() generate numbersss.
df["Transaction Number1"] = pd.Series(np.arange(len(df)), index=df.index)
df.set_index("Transaction Number", inplace = True)

#this line only consider this two columns and saves into the DF1
df1 = pd.DataFrame(np.array(df[['Item Description','Payment Amount USD']]))
print(df1)

#changing column name for particular column
df= df.rename(columns = {"Full Name" : "Buyer Name"})

#dropping Item Description columns
#Note: axis=1 denotes that we are referring to a column, not a row
df1.drop('Item Description', axis=1)
df = df.drop(df.columns[3:], axis = 1)

#dropping null values row wise for Full Address column 
df.dropna(axis = 0 , subset=['Full Address'], how = 'any', inplace = True)

#dropping duplicate values and returns only first value 
df.drop_duplicates(subset = "English Name", keep = 'first', inplace = True)

#filling space in Null values at specific column. Here FN column selected
df = df.fillna({"FN":""})

#for removing double space
df.postcode = df.postcode.str.replace('  ', ' ')

#used to remove whitespaces from particular column
df['Full Name'] = df['Full Name'].str.strip()

#For Loop iterate row wise. It returns whole row in row variable and index of row in index variable
a = 0
for index, row in df.iterrows():
  g = geocoder.google(row[0], key=api)
  df.iloc[a, df.columns.get_loc('B_lat')] = g.lat
  df.iloc[a, df.columns.get_loc('B_lang')] = g.lng
  a = a + 1

#This line checking duplicated values and returns true in new column df1['duplicated']
df1['duplicated'] = df1.duplicated([0],keep=False)
df1['is_duplicated'].sum()

#splitting in to data
df["LN"]= df["Buyer"].str.split(",", expand= True).get(0)
df["FN"]= df["Buyer"].str.split(",", expand= True).get(1)

#merge two columns
df['Buyer Name'] = df[['FN', 'LN']].apply(lambda x: ' '.join(x), axis=1)

#join on df and df1. Here is left join and column name "Buyer Name"
Final_Buyer = df.merge(df1, left_on = "Buyer Name", right_on = "Buyer Name", how = "left")

#It changes column name in the data frame
df1.columns = ['Item Description', 'Payment Amount USD', 'duplicated']

#For exporting data to excel
df1.to_excel(r"D:\KEPY tableau\Seagate - on Keyur_s Drive\untitled\kepy1.xlsx")

#It creates group of item description and then payment amount usd in the grouped data
grouped = df.groupby(['Item Description','Payment Amount USD'])

#For printing Selected multiple columns
df[['Item Description','Buyer','Payment Amount USD']].head(2)

print("done")
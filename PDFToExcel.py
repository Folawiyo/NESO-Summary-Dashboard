import pandas as pd
import tabula
import os 


#Get list of files 

path = r"C:\Users\user\Desktop\Fola\Data Analysis\Smarterise\Resource Materials\Resource materials\Project 1\Webscraping"
#os.chdir(raw_input("C:\Users\user\Desktop\Fola\Data Analysis\Smarterise\Resource Materials\Resource materials\Project 1\Webscraping").replace("\\", ""))
Allfiles = os.listdir(path)

Pdffiles = []
for file in Allfiles:
    if file.endswith(".pdf"):
        if os.path.getsize(file) > 1024 :
            Pdffiles.append(file)

i =0
NewDF = pd.DataFrame ( columns = ['Date','Peak Generation', 'Lowest Generation', 'Daily Energy Generation'])

#Read all pdfs

for file in Pdffiles:    
    df = tabula.read_pdf(file, pages ='all')

    DF = pd.DataFrame (df[0])
    
    DF2 = pd.DataFrame.to_numpy (DF)
    #print(DF)
    
    #tabula.convert_into("DailyOperationalRpt02-02-20.pdf", "DailyOperationalRpt02-02-20.csv", output_format="csv")
    
    PeakGeneration = float(DF2[1,1].split('M',1)[0].replace(',',''))
    DailyEnergyGeneration = float(DF2[3,1].split('M',1)[0].replace(',',''))
    Date = DF2[1,0].split()[-1]
    

    
    NewDF.loc[i] = [Date, PeakGeneration,LowestGeneration,DailyEnergyGeneration]
    i=i+1
    
#Write NewDF to Excel 
NewDF.to_excel("NewData.xlsx")    
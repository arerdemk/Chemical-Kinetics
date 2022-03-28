from tkinter.ttk import Treeview
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import gspread
from tkinter import *
from pandastable import Table,TableModel


win=Tk()
win.geometry('800x800')

listbox_data=Listbox(win,height=25,width=60)
listbox_data.place(x=0,y=0)



sheet_id='1B2Tm7H9Te8pbxRSDsHUdpDf8YIwREjXs75K6fnce90s'
gc=gspread.service_account('tubitak-121z085.json')
sh=gc.open_by_key(sheet_id)
worksheet=sh.sheet1

with open('GCN.txt') as f:
    lines=f.readlines()
    for row in lines:
        readdata=row.rstrip('\n')
        listbox_data.insert(END,readdata)

        def createplot():
            res=worksheet.get(listbox_data.get(ANCHOR))
            create_df=pd.DataFrame(res,columns=['min','cm','mL (H2+CO2)','mL (H2)','TOF h-1'])
            df=create_df.iloc[3:,:]

            # dflabel=Label(win,text=TableModel.getSampleData(listbox_data.get(ANCHOR)))
            # dflabel.place(x=500,y=0)

            time=df['min'].astype(float)
            gasxx=df['mL (H2)'].astype(float)
            gas=np.subtract(6,gasxx*22.4/1000)

            lngas=np.log(gas)
            inversed=np.divide(1,gas)

            fig, (ax1,ax2,ax3)=plt.subplots(1,3,num=listbox_data.get(ANCHOR))
            ax1.plot(time,gas,marker='o',color='g')
            ax1.set(xlabel='min',ylabel='[A]')

            ax2.plot(time,lngas,marker='o',color='b')
            ax2.set(xlabel='min',ylabel='ln[A]')

            ax3.plot(time,inversed,marker='o',color='r')
            ax3.set(xlabel='min',ylabel='1/[A]')

            plt.suptitle(listbox_data.get(ANCHOR))

            plt.show()


selectbutton=Button(win,text='Select',command=createplot)
selectbutton.place(x=220,y=460)

win.mainloop()

# #EXAMPLE 20-8 Graphing Data to Determine the Order of a Reaction Petrucci Chemical Kinetics pg:941
# min=[0,5,10,15,25]
# gas=[1,0.63,0.46,0.36,0.25]


# df=pd.DataFrame({
#     'min':[0,5,10,15,25],
#     '[A]':[1.0,0.63,0.46,0.36,0.25]
# })


# df['ln[A]']=np.log(gas)
# df['1/[A]']=np.divide(1,gas)

# time=df['min']
# a=df['[A]']
# lna=df['ln[A]']
# inverse=df['1/[A]']

# #=====TANGENT LINE====
# #Buna loc fonksiyonu gelece1!!!!
# # tangetkarsi=np.subtract(inverse.tail(1),inverse.head(1))
# # tangentkomsu=np.subtract(time.tail(1),time.head(1))

# # tangentline=np.divide(tangetkarsi,tangentkomsu)

# #lna df[] degistir
# def createplotxxx():
#     fig,(ax1,ax2,ax3)=plt.subplots(1,3)
#     ax1.plot(df['min'],df['[A]'],marker='o',color='g')
#     ax1.set(xlabel='min',ylabel='[A]')

#     ax2.plot(df['min'],df['ln[A]'],marker='o',color='b')
#     ax2.set(xlabel='min',ylabel='ln[A]')

#     ax3.plot(df['min'],df['1/[A]'],marker='o',color='r')
#     ax3.set(xlabel='min',ylabel='1/[A]')

#     plt.suptitle('EXAMPLE 20-8 Graphing Data to Determine the Order of a Reaction Petrucci Chemical Kinetics pg:941')
#     plt.show()



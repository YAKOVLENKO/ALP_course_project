from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
root=Tk()
root.title(u'HFind')
root.geometry('1350x750+85+20')
root.resizable(False, False)
#fra1 = Frame(myWind,width=500,height=100,bg="green")

#canvas.create_line(200,50,300,50,width=3,fill="blue")



group_Info = LabelFrame(root, padx=200, pady=330,  bg='white')
group_Info.pack()
group_Info.place(x=901, y=35)
button1=Button(group_Info, bg='white', relief='flat')
button1.pack()

group_Graph = LabelFrame(root,padx=275, pady=230, labelanchor='n',bg='white')
group_Graph.pack()
group_Graph.place(x=323, y=235)
button3=Button(group_Graph, bg='white', relief='flat')
button3.pack()


group_Base = LabelFrame(root,padx=130, pady=330, labelanchor='n',bg='white')
group_Base.pack()
group_Base.place(x=35, y=35)
button2=Button(group_Base, bg='white', relief='flat')
button2.pack()

group_GraphSet = LabelFrame(root,padx=275, pady=80, labelanchor='n',bg='white')
group_GraphSet.pack()
group_GraphSet.place(x=323, y=35)
button4=Button(group_GraphSet, bg='white', relief='flat')
button4.pack()

BSaveTo=Button(text='Сохранить профиль', relief='groove', width='25')
BSaveTo.pack()
BSaveTo.place(x=918, y=690)

BChange=Button(text='Изменить', relief='groove', width='25')
BChange.pack()
BChange.place(x=1115, y=690)

BInfoType=Button(root,text='Дополнительная информация',width=53, relief='groove')
BInfoType.pack()
BInfoType.place(x=918, y=655)

BMyBase=Label(text='Сохраненные профили', relief='groove', padx=69, bg='white', font='arial 9')
BMyBase.pack()
BMyBase.place(x=35, y=50)

BSearch=Button(text='Найти', relief='groove', width='31', padx=4)
BSearch.pack()
BSearch.place(x=57, y=130)

LFid = LabelFrame(root, fg='grey', labelanchor='nw', text='id', bg='white')
LFid.pack()
LId=Label(LFid, text='id',width=24,height=2, fg='light grey', bg='white', relief='flat', padx=4)
LId.pack()
LFid.place(x=1115, y=190)

LFSocSites=Frame(root, bg='lightgrey', padx=2, pady=2)
LFSocSites.pack()
LFSocSites.place(x=1115, y=50)

LFAddVk=LabelFrame(LFSocSites, fg='grey', labelanchor='nw', text='VK', bg='white')
LFAddVk.pack()
LAddVk=Label(LFAddVk, text='vk.com/',width=24,height=2, fg='light grey', bg='white', relief='flat', padx=2)
LAddVk.pack()


LFAddFB=LabelFrame(LFSocSites, fg='grey', labelanchor='nw', text='Facebook', bg='white')
LFAddFB.pack()
LAddFB=Label(LFAddFB, text='facebook.com/',width=24,height=2, fg='light grey', bg='white', relief='flat', padx=2)
LAddFB.pack()


LFFName = LabelFrame(root, fg='grey', labelanchor='nw', text='Имя', bg='white')
LFFName.pack()
LFName=Label(LFFName,text='Имя',width=53,height=2, fg='light grey', bg='white', relief='flat')
LFName.pack()
LFFName.place(x=918, y=250)

LFLName = LabelFrame(root, fg='grey', labelanchor='nw', text='Фамилия', bg='white')
LFLName.pack()
LLName=Label(LFLName,text='Фамилия',width=53, height=2, fg='light grey', bg='white', relief='flat')
LLName.pack()
LFLName.place(x=918, y=310)

LFMName = LabelFrame(root, fg='grey', labelanchor='nw', text='Отчество', bg='white')
LFMName.pack()
LMName=Label(LFMName,text='Отчество',width=53,height=2, fg='light grey', bg='white', relief='flat')
LMName.pack()
LFMName.place(x=918, y=370)

LFBDate = LabelFrame(root,  bg='grey', relief='flat', bd=1)
LFBDate.pack()
LFBDate.place(x=990, y=439)

#LBDateText=Label(LFBDate,text='Дата рождения:', width=20, height=2, font='arial 8', fg='grey', bg='white', relief='flat')
#LBDateText.pack()

LFBDay = LabelFrame(root, fg='grey', labelanchor='nw', text='дд', bg='white')
LFBDay.pack()
LBDay=Label(LFBDay,text='дд',width=5,height=2, fg='light grey', bg='white', relief='flat')
LBDay.pack()
LFBDay.place(x=1115, y=430)

LFBMonth = LabelFrame(root, fg='grey', labelanchor='nw', text='мм', bg='white')
LFBMonth.pack()
LBMonth=Label(LFBMonth,text='мм',width=5,height=2, fg='light grey', bg='white', relief='flat')
LBMonth.pack()
LFBMonth.place(x=1164, y=430)

LFBYear = LabelFrame(root, fg='grey', labelanchor='nw', text='гггг', bg='white')
LFBYear.pack()
LBYear=Label(LFBYear,text='гггг',width=11,height=2, fg='light grey', bg='white', relief='flat')
LBYear.pack()
LFBYear.place(x=1213, y=430)

LFCity = LabelFrame(root, fg='grey', labelanchor='nw', text='Город', bg='white')
LFCity.pack()
LCity=Label(LFCity,text='Город',width=25,height=2, fg='light grey', bg='white', relief='flat')
LCity.pack()
LFCity.place(x=918, y=490)

LFCountry = LabelFrame(root, fg='grey', labelanchor='nw', text='Страна', bg='white')
LFCountry.pack()
LCountry=Label(LFCountry,text='Страна',width=25,height=2, fg='light grey', bg='white', relief='flat')
LCountry.pack()
LFCountry.place(x=1115, y=490)

LFMobile = LabelFrame(root, fg='grey', labelanchor='nw', text='Телефон', bg='white')
LFMobile.pack()
LMobile=Label(LFMobile,text='Телефон',width=53,height=2, fg='light grey', bg='white', relief='flat')
LMobile.pack()
LFMobile.place(x=918, y=550)

LFSearchContacts = LabelFrame(root, fg='grey', labelanchor='nw', text='Поиск', bg='white')
LFSearchContacts.pack()
TSearchContacts=Text(LFSearchContacts,font='courier 10',height=1, width=28,relief='flat',wrap=WORD)
TSearchContacts.pack()
LFSearchContacts.place(x=57, y=80)

TSearchSite=Text(root, font='courier 10', height=1, width=36,relief='groove', wrap=WORD)
TSearchSite.pack()
TSearchSite.place(x=901, y=7)

BSearchSite=Button(root, relief='groove', width=15,pady=1, font='courier 8', text='Поиск')
BSearchSite.pack()
BSearchSite.place(x=1200, y=5)

root.mainloop()
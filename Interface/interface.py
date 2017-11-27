import vk
from tkinter import *
from Core.Modules.VK.VK import Profile

class MyWindow:
    vk_profile = Profile()
    root = Tk()


    group_Info = LabelFrame(root,
                            padx=200,
                            pady=330,
                            bg='white')

    group_Info_B = Button(group_Info,
                          bg='white',
                          relief='flat')

    group_Graph = LabelFrame(root,
                             padx=275,
                             pady=230,
                             labelanchor='n',
                             bg='white')

    group_Graph_B = Button(group_Graph,
                           bg='white',
                           relief='flat')

    group_Base = LabelFrame(root,
                            padx=130,
                            pady=330,
                            labelanchor='n',
                            bg='white')

    group_Base_B = Button(group_Base,
                          bg='white',
                          relief='flat')

    group_GraphSet = LabelFrame(root,
                                padx=275,
                                pady=80,
                                labelanchor='n',
                                bg='white')

    group_GraphSet_B = Button(group_GraphSet,
                              bg='white',
                              relief='flat')

    BSaveTo = Button(text='Сохранить профиль',
                     relief='groove',
                     width='25')

    BChange = Button(text='Изменить',
                     relief='groove',
                     width='25')

    BInfoType = Button(root,
                       text='Дополнительная информация',
                       width=53,
                       relief='groove')

    BMyBase = Label(text='Сохраненные профили',
                    relief='groove',
                    padx=69,
                    bg='white',
                    font='arial 9')

    BSearch = Button(text='Найти',
                     relief='groove',
                     width='31',
                     padx=4)

    LFid = LabelFrame(root,
                      fg='grey',
                      labelanchor='nw',
                      text='id',
                      bg='white')

    LId = Label(LFid,
                text='id',
                width=24,
                height=2,
                fg='light grey',
                bg='white',
                relief='flat',
                padx=4)

    LFSocSites = Frame(root,
                       bg='lightgrey',
                       padx=2,
                       pady=2)

    LFAddVk = LabelFrame(LFSocSites,
                         fg='grey',
                         labelanchor='nw',
                         text='VK',
                         bg='white')

    LAddVk = Label(LFAddVk,
                   text='vk.com/',
                   width=24,
                   height=2,
                   fg='light grey',
                   bg='white',
                   relief='flat',
                   padx=2)

    LFAddFB = LabelFrame(LFSocSites,
                         fg='grey',
                         labelanchor='nw',
                         text='Facebook',
                         bg='white')

    LAddFB = Label(LFAddFB,
                   text='facebook.com/',
                   width=24,
                   height=2,
                   fg='light grey',
                   bg='white',
                   relief='flat',
                   padx=2)

    LFFName = LabelFrame(root,
                         fg='grey',
                         labelanchor='nw',
                         text='Имя',
                         bg='white')

    TFName = Entry(LFFName,
                   width=44,
                   bd=9,
                   bg='white',
                   relief='flat',
                   font='courier 10',
                   disabledbackground='white')

    LFLName = LabelFrame(root,
                         fg='grey',
                         labelanchor='nw',
                         text='Фамилия',
                         bg='white')

    TLName = Entry(LFLName,
                   width=44,
                   bd=9,
                   bg='white',
                   relief='flat',
                   font='courier 10',
                   disabledbackground='white')

    LFMName = LabelFrame(root,
                         fg='grey',
                         labelanchor='nw',
                         text='Отчество',
                         bg='white')

    TMName = Entry(LFMName,
                   width=44,
                   bd=9,
                   bg='white',
                   relief='flat',
                   font='courier 10',
                   disabledbackground='white')

    LFBDay = LabelFrame(root,
                        fg='grey',
                        labelanchor='nw',
                        text='дд',
                        bg='white')

    TBDay = Entry(LFBDay,
                  width=3,
                  bd=9,
                  bg='white',
                  relief='flat',
                  font='courier 10',
                  disabledbackground='white')

    LFBMonth = LabelFrame(root,
                          fg='grey',
                          labelanchor='nw',
                          text='мм',
                          bg='white')

    TBMonth = Entry(LFBMonth,
                    width=3,
                    bd=9,
                    bg='white',
                    relief='flat',
                    font='courier 10',
                    disabledbackground='white')

    LFBYear = LabelFrame(root,
                         fg='grey',
                         labelanchor='nw',
                         text='гггг',
                         bg='white')

    TBYear = Entry(LFBYear,
                   width=8,
                   bd=9,
                   bg='white',
                   relief='flat',
                   font='courier 10',
                   disabledbackground='white')

    LFCity = LabelFrame(root,
                        fg='grey',
                        labelanchor='nw',
                        text='Город',
                        bg='white')

    TCity = Entry(LFCity,
                  width=20,
                  bd=9,
                  bg='white',
                  relief='flat',
                  font='courier 10',
                  disabledbackground='white')

    LFCountry = LabelFrame(root,
                           fg='grey',
                           labelanchor='nw',
                           text='Страна',
                           bg='white')


    TCountry = Entry(LFCountry,
                     width=20,
                     bd=9,
                     bg='white',
                     relief='flat',
                     font='courier 10',
                     disabledbackground='white')

    LFMobile = LabelFrame(root,
                          fg='grey',
                          labelanchor='nw',
                          text='Телефон',
                          bg='white')

    TMobile = Entry(LFMobile,
                    width=44,
                    bd=9,
                    bg='white',
                    relief='flat',
                    font='courier 10',
                    disabledbackground='white')

    LFSearchContacts = LabelFrame(root,
                                  fg='grey',
                                  labelanchor='nw',
                                  text='Поиск',
                                  bg='white')

    TSearchContacts = Text(LFSearchContacts,
                           font='courier 10',
                           height=1,
                           width=28,
                           relief='flat',
                           wrap=WORD)
    TSearchSite = Entry(root,
                        font='courier 10',
                        width=36,
                        relief='groove')

    BSearchSite = Button(root,
                         relief='groove',
                         width=15,
                         pady=1,
                         font='courier 8',
                         text='Поиск')

    BCareer = Button(root,
                     text='Карьера',
                     width=53,
                     relief='groove')

    BEducation = Button(root,
                        text='Образование',
                        width=53,
                        relief='groove')

    BRelatives = Button(root,
                        text='Родственные связи',
                        width=53,
                        relief='groove')

    BInterests = Button(root,
                        text='Интересы',
                        width=53,
                        relief='groove')
    BLikes = Button(root,
                    text='Недавние лайки',
                    width=53, relief='groove')

    LFContacts = LabelFrame(root,
                            fg='grey',
                            padx=2,
                            pady=2,
                            text='Контакты',
                            labelanchor='nw',
                            bg='white')

    LFTwitter = LabelFrame(LFContacts,
                           fg='grey',
                           labelanchor='nw',
                           text='Twitter',
                           bg='white')

    ETwitter = Entry(LFTwitter,
                     width=43,
                     bd=11,
                     bg='white',
                     disabledbackground='white',
                     relief='flat',
                     font='courier 10')

    LFInstagram = LabelFrame(LFContacts,
                             fg='grey',
                             labelanchor='nw',
                             text='Instagram',
                             bg='white')

    EInstagram = Entry(LFInstagram,
                       width=43,
                       bd=11,
                       bg='white',
                       disabledbackground='white',
                       relief='flat',
                       font='courier 10')

    LFSkype = LabelFrame(LFContacts,
                         fg='grey',
                         labelanchor='nw',
                         text='Skype',
                         bg='white')

    ESkype = Entry(LFSkype,
                   width=43,
                   bd=11,
                   bg='white',
                   disabledbackground='white',
                   relief='flat',
                   font='courier 10')



    LBigInfo = Label(root)
    TBigInfo = Text(LBigInfo, height=12, width=44, padx=2)
    SBigInfo = Scrollbar(LBigInfo, command=TBigInfo.yview)

    BFindLikes = Button(LBigInfo,
                        text='Обновить',
                        width=35,
                        relief='sunken')

    label_first_infoW = [LFid, LFFName, LFLName, LFMName, LFBDay, LFBMonth, LFBYear, LFMobile, LFCity, LFCountry]
    entry_first_infoW = [TLName, TFName, TMName, TBDay, TBMonth, TBYear, TCity, TCountry, TMobile]

    label_second_infoW = [LFContacts, LFTwitter, LFSkype, LFInstagram, LBigInfo]
    entry_second_infoW = [ETwitter, ESkype, EInstagram]

    bunntons_second_infoW = [LBigInfo, BCareer, BInterests, BLikes, BRelatives, BEducation]


    def __init__(self):

        self.root.title(u'HFind')
        self.root.geometry('1350x750+85+20')
        self.root.resizable(False, False)
        self.set_default_W()

        self.BSearchSite.bind('<Button-1>', self.bind_search_user)
        self.BSearchSite.place(x=1200, y=5)
        self.TSearchSite.place(x=901, y=7)

        self.set_buttons_infoW()
        self.set_entry()
        self.set_infoW()
        self.pack_first_infoW()
        self.root.mainloop()


    def set_text(self, field, text):
        field.delete(0, END)
        field.insert(0, text)
        return

    def set_infoW(self):
        for i in self.entry_first_infoW:
            i.pack()
        self.LAddFB.pack()
        self.LAddVk.pack()
        self.LId.pack()
        self.ETwitter.pack()
        self.EInstagram.pack()
        self.ESkype.pack()
        self.block_entry()

    def pack_first_infoW(self):

        self.LFid.place(x=1115, y=190)

        self.LFSocSites.place(x=1115, y=50)

        self.LFAddVk.pack()

        self.LFAddFB.pack()

        self.LFFName.place(x=920, y=250)

        self.LFLName.place(x=920, y=310)

        self.LFMName.place(x=920, y=370)

        self.LFBDay.place(x=1100, y=430)

        self.LFBMonth.place(x=1154, y=430)

        self.LFBYear.place(x=1208, y=430)

        self.LFCity.place(x=920, y=490)

        self.LFCountry.place(x=1112, y=490)

        self.LFMobile.place(x=920, y=550)

    def forget_first_infoW(self):
        self.LFSocSites.pack()
        self.LFid.pack()
        self.LFAddVk.pack()
        self.LFAddFB.pack()
        self.LFSocSites.pack_forget()
        self.LFid.pack_forget()
        self.LFAddVk.pack_forget()
        self.LFAddFB.pack_forget()

        for i in self.label_first_infoW:
            i.pack()
            i.pack_forget()

    def forget_second_infoW(self):

        for i in self.label_second_infoW:
            i.pack()
            i.pack_forget()

        for i in self.bunntons_second_infoW:
            i.pack()
            i.pack_forget()

    def pack_second_infoW(self):
        self.LFTwitter.pack()

        self.BFindLikes.pack()

        self.LFInstagram.pack()

        self.LFSkype.pack()
        self.LFContacts.place(x=918, y=450)
        self.TBigInfo['yscrollcommand'] = self.SBigInfo.set
        self.SBigInfo.pack(fill=Y, side=RIGHT)
        self.TBigInfo.pack()
        self.LBigInfo.place(x=918, y=210)

        self.BCareer.bind('<Button-1>', self.bind_career)
        self.BCareer.place(x=918, y=50)

        self.BInterests.bind('<Button-1>', self.bind_interests)
        self.BInterests.place(x=918, y=80)

        self.BLikes.bind('<Button-1>', self.bind_likes)
        self.BLikes.place(x=918, y=110)

        self.BRelatives.bind('<Button-1>', self.bind_relations)
        self.BRelatives.place(x=918, y=140)

        self.BEducation.bind('<Button-1>', self.bind_education)
        self.BEducation.place(x=918, y=170)



    def block_entry(self):

        for i in self.entry_first_infoW:
            i.config(state=DISABLED)
        for i in self.entry_second_infoW:
            i.config(state=DISABLED)
        self.TBigInfo.config(state=DISABLED)

    def unblock_entry(self):
        for i in self.entry_first_infoW:
            i.config(state=NORMAL)
        for i in self.entry_second_infoW:
            i.config(state=NORMAL)
        self.TBigInfo.config(state=NORMAL)

    def set_entry(self):
        self.TFName.insert(END, self.vk_profile.fname)
        self.TLName.insert(END, self.vk_profile.lname)
        self.TMName.insert(END, self.vk_profile.mname)
        self.TBDay.insert(END, self.vk_profile.birth_day)
        self.TBMonth.insert(END, self.vk_profile.birth_month)
        self.TBYear.insert(END, self.vk_profile.birth_year)
        self.TMobile.insert(END, self.vk_profile.mobile_phone)
        self.TCity.insert(END, self.vk_profile.city)
        self.TCountry.insert(END, self.vk_profile.country)
        self.EInstagram.insert(END, self.vk_profile.instagram)
        self.ESkype.insert(END, self.vk_profile.skype)
        self.ETwitter.insert(END, self.vk_profile.twitter)
        self.LId['text'] = self.vk_profile.id

    def clear_entry(self):
        for i in self.entry_first_infoW:
            i.delete(0, 'end')
        for i in self.entry_second_infoW:
            i.delete(0, 'end')

    def set_buttons_infoW(self):

        self.BSaveTo.bind('<Button-1>', self.bind_save)
        self.BSaveTo.place(x=918, y=690)

        self.BChange.bind("<Button-1>", self.bind_change)
        self.BChange.place(x=1115, y=690)

        self.BInfoType.bind('<Button-1>', self.bind_another_info)
        self.BInfoType.pack()
        self.BInfoType.place(x=918, y=655)

    def set_default_W(self):

        self.group_Info.pack()
        self.group_Info.place(x=901, y=35)
        self.group_Info_B.pack()

        self.group_Graph.pack()
        self.group_Graph.place(x=323, y=235)
        self.group_Graph_B.pack()

        self.group_Base.pack()
        self.group_Base.place(x=35, y=35)
        self.group_Base_B.pack()

        self.group_GraphSet.pack()
        self.group_GraphSet.place(x=323, y=35)
        self.group_GraphSet_B.pack()

    def bind_change(self, event):
        if self.BChange['text'] == 'Изменить':
            self.BChange['text'] = 'Отмена'
            self.BSaveTo['text'] = 'Сохранить изменения'
            self.unblock_entry()
        else:
            self.BChange['text'] = 'Изменить'
            self.BSaveTo['text'] = 'Сохранить профиль'
            self.clear_entry()
            self.set_entry()
            self.block_entry()

    def bind_save(self, event):
        pass
        if self.BSaveTo['text'] == 'Сохранить профиль':
            pass
        else:
            self.BChange['text'] = 'Изменить'
            self.BSaveTo['text'] = 'Сохранить профиль'
            self.vk_profile.fname=self.TFName.get()
            self.vk_profile.lname = self.TLName.get()
            self.vk_profile.mname = self.TMName.get()
            self.vk_profile.birth_day = self.TBDay.get()
            self.vk_profile.birth_month = self.TBMonth.get()
            self.vk_profile.birth_year = self.TBYear.get()
            self.vk_profile.city = self.TCity.get()
            self.vk_profile.country = self.TCountry.get()
            self.vk_profile.mobile_phone = self.TMobile.get()
            self.vk_profile.instagram = self.EInstagram.get()
            self.vk_profile.skype = self.ESkype.get()
            self.vk_profile.twitter = self.ETwitter.get()
            self.clear_entry()
            self.set_entry()
            self.block_entry()

    def bind_another_info(self, event):
        if self.BInfoType['text'] == 'Дополнительная информация':
            self.BInfoType['text'] = 'Основная информация'
            self.forget_first_infoW()
            self.pack_second_infoW()
        else:
            self.BInfoType['text'] = 'Дополнительная информация'
            self.forget_second_infoW()
            self.pack_first_infoW()

    def bind_career(self, event):
        if self.TBigInfo['state'] == 'disabled':
            self.TBigInfo.config(state=NORMAL)
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.career)
            self.TBigInfo.config(state=DISABLED)
        else:
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.career)
        self.BFindLikes['relief'] = 'sunken'

    def bind_education(self, event):
        if self.TBigInfo['state'] == 'disabled':
            self.TBigInfo.config(state=NORMAL)
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.education)
            self.TBigInfo.config(state=DISABLED)
        else:
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.education)
        self.BFindLikes['relief'] = 'sunken'

    def bind_relations(self, event):
        if self.TBigInfo['state'] == 'disabled':
            self.TBigInfo.config(state=NORMAL)
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.relatives)
            self.TBigInfo.config(state=DISABLED)
        else:
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.relatives)
        self.BFindLikes['relief'] = 'sunken'

    def bind_likes(self, event):
        self.BFindLikes['relief'] = 'groove'
        if self.TBigInfo['state'] == 'disabled':
            self.TBigInfo.config(state=NORMAL)
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.likes)
            self.TBigInfo.config(state=DISABLED)
        else:
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.likes)

    def bind_interests(self, event):
        if self.TBigInfo['state'] == 'disabled':
            self.TBigInfo.config(state=NORMAL)
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.interests)
            self.TBigInfo.config(state=DISABLED)
        else:
            self.TBigInfo.delete('1.0', END)
            self.TBigInfo.insert(1.0, self.vk_profile.interests)
        self.BFindLikes['relief'] = 'sunken'

    def bind_search_user(self, event):

            self.vk_profile.set_data(self.TSearchSite.get(), '7f8a5df12a5633ee0496fd3e8c22cc3d565eb75a9cf4a4d36616840af3bcc4bd064c8b69a08085123a70d')
            self.unblock_entry()
            self.clear_entry()
            self.set_entry()
            self.block_entry()

    def bind_find_likes(self, event):
        if self.TBigInfo['state'] == 'disabled':
            self.TBigInfo.config(state=NORMAL)
            self.TBigInfo.delete('1.0', END)
            self.vk_profile.vk_data.get__likes(5)
        else:
            pass
a = MyWindow()





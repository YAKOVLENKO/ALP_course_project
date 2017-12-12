import vk
from tkinter import *
from Core.Modules.VK.VK import Profile
from Core.DataBase import Base
from Interface.Graphs.graphs import Graph
from PIL import ImageTk, Image
import os

class MyWindow:
    vk_profile = Profile()
    root = Tk()
    data_base = Base.MySavedProfiles()
    token = ''
    api = ''
    user_graph = Graph()

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
                width=21,
                height=2,
                fg='light grey',
                bg='white',
                relief='flat',
                padx=5)


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
                                  text='Сохраненные контакты',
                                  bg='white')

    TSearchContacts = Entry(LFSearchContacts,
                           font='courier 10',
                           width=28,
                           relief='groove')
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

    TokEntry = Entry(root,
                     bg='light grey',
                     font='courier 15',
                     width=42,
                     show="*",
                     relief='groove')
    TokInfo = Label(root,
                    text='Введите токен:',
                    relief='flat',
                    bg='white',
                    font='courier 13')
    TokButton = Button(root,
                       text='Ввод',
                       width=71,
                       padx=2,
                       relief='groove')


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

    # =
    LFFriendsGraph = LabelFrame(root,
                         fg='grey',
                         labelanchor='nw',
                         text='Граф "Общие друзья"',
                         bg='white',
                                padx=250,
                                pady=25
                                )

    LFFGButton = Button(LFFriendsGraph,
                        bg='white',
                        relief='flat')

    #LFBondsGraph =
    LFGroupsGraph =LabelFrame(root,
                         fg='grey',
                         labelanchor='nw',
                         text='Граф "Аудитория групп"',
                         bg='white',
                         padx=250,
                        pady=100)

    LFGGButton = Button(LFGroupsGraph,
                        bg='white',
                        relief='flat')

    BFriendsGraph = Button(root,
                        text='Построить',
                        width=65,
                        relief='groove')

    BFriendsGraph_info = Text(root,
                              font='courier 10',
                              width=57,
                              padx=2,
                              bg='light grey',
                              bd=2,
                              relief='flat',
                              height=1)


    BGroupsGraph = Button(root,
                        text='Построить',
                        width=65,
                        relief='groove')

    ChBGroupGraph_Entry1 = Entry(root,
                                 font='courier 10',
                                 width=20,
                                 bd=2,
                                 relief='groove')
    ChBGroupGraph_Entry2 = Entry(root,
                                 font='courier 10',
                                 width=20,
                                 bd=2,
                                 relief='groove'
                                 )
    ChBGroupGraph_Entry3 = Entry(root,
                                 font='courier 10',
                                 width=20,
                                 bd=2,
                                 relief='groove'
                                 )
    ChBGroupGraph_Entry4 = Entry(root,
                                 font='courier 10',
                                 width=20,
                                 bd=2,
                                 relief='groove'
                                 )
    ChBGroupGraph_Entry5 = Entry(root,
                                 font='courier 10',
                                 width=20,
                                 bd=2,
                                 relief='groove'
                                 )
    ChBGroupGraph_Entry6 = Entry(root,
                                 font='courier 10',
                                 width=20,
                                 bd=2,
                                 relief='groove'
                                 )

    Entries_ofGroupGraph = [ChBGroupGraph_Entry1, ChBGroupGraph_Entry2, ChBGroupGraph_Entry3,
                            ChBGroupGraph_Entry4, ChBGroupGraph_Entry5, ChBGroupGraph_Entry6]

    ChBGroupGraph_Info1 = Text(root,
                               font='courier 8',
                               bg='light grey',
                               width=49,
                               padx=5,
                               bd=2,
                               relief='flat',
                               state='disabled',
                               height=3
                                 )

    ChBGroupGraph_frame = Frame(root,
                                bg='lightgrey',
                                padx=2,
                                pady=2)
    ChBGroupGraph_button1 = Button(ChBGroupGraph_frame,
                                   text='Вариант 1',
                                   width=10,
                                   relief='groove')
    ChBGroupGraph_button2 = Button(ChBGroupGraph_frame,
                                   text='Вариант 2',
                                   width=10,
                                   relief='groove')

    ChBGroupGraph_CounterText = Entry(root,
                                      font='courier 10',
                                      width=20,
                                      bd=2,
                                      relief='groove')

    ChBGroupGraph_Counter = Entry(root,
                                  font='courier 10',
                                  width=3,
                                  bd=2,
                                  relief='groove')
    ChBGroupGraph_Info2 = Text(root,
                               font='courier 8',
                               width=49,
                               padx=5,
                               bg='light grey',
                               bd=2,
                               relief='flat',
                               state='disabled',
                               height=6)
    LFSelectPerson1 = Label(root,
                            bg='light grey')
    LFSelectPerson2 = Label(root,
                            bg='light grey')
    LFSelectPerson3 = Label(root,
                            bg='light grey')
    LFSelectPerson4 = Label(root,
                            bg='light grey')
    LFSelectPerson5 = Label(root,
                            bg='light grey')
    LFSelectPerson6 = Label(root,
                            bg='light grey')
    EBlankForContact1 = Entry(LFSelectPerson1,
                              font='courier 10',
                              width=28,
                              bd=2,
                              relief='groove')
    EBlankForContact2 = Entry(LFSelectPerson2,
                              font='courier 10',
                              width=28,
                              bd=2,
                              relief='groove')
    EBlankForContact3 = Entry(LFSelectPerson3,
                              font='courier 10',
                              width=28,
                              bd=2,
                              relief='groove')
    EBlankForContact4 = Entry(LFSelectPerson4,
                              font='courier 10',
                              width=28,
                              bd=2,
                              relief='groove')
    EBlankForContact5 = Entry(LFSelectPerson5,
                              font='courier 10',
                              width=28,
                              bd=2,
                              relief='groove')
    EBlankForContact6 = Entry(LFSelectPerson6,
                              font='courier 10',
                              width=28,
                              bd=2,
                              relief='groove')
    EBlankForId1 = Entry(LFSelectPerson1,
                              font='courier 10',
                              width=28,
                              bd=2,
                              relief='groove')
    EBlankForId2 = Entry(LFSelectPerson2,
                         font='courier 10',
                         width=28,
                         bd=2,
                         relief='groove')
    EBlankForId3 = Entry(LFSelectPerson3,
                         font='courier 10',
                         width=28,
                         bd=2,
                         relief='groove')
    EBlankForId4 = Entry(LFSelectPerson4,
                         font='courier 10',
                         width=28,
                         bd=2,
                         relief='groove')
    EBlankForId5 = Entry(LFSelectPerson5,
                         font='courier 10',
                         width=28,
                         bd=2,
                         relief='groove')
    EBlankForId6 = Entry(LFSelectPerson6,
                         font='courier 10',
                         width=28,
                         bd=2,
                         relief='groove')
    BSelectPerson1 = Button(LFSelectPerson1,
                           text='Выбрать',
                           width=31,
                           relief='groove')
    BSelectPerson2 = Button(LFSelectPerson2,
                            text='Выбрать',
                            width=31,
                            relief='groove')
    BSelectPerson3 = Button(LFSelectPerson3,
                            text='Выбрать',
                            width=31,
                            relief='groove')

    BSelectPerson4 = Button(LFSelectPerson4,
                            text='Выбрать',
                            width=31,
                            relief='groove')

    BSelectPerson5 = Button(LFSelectPerson5,
                            text='Выбрать',
                            width=31,
                            relief='groove')

    BSelectPerson6 = Button(LFSelectPerson6,
                            text='Выбрать',
                            width=31,
                            relief='groove')



    EBlankForContacts = [EBlankForContact1,
                         EBlankForContact2,
                         EBlankForContact3,
                         EBlankForContact4,
                         EBlankForContact5,
                         EBlankForContact6]

    EBlankForIds = [EBlankForId1,
                    EBlankForId2,
                    EBlankForId3,
                    EBlankForId4,
                    EBlankForId5,
                    EBlankForId6]

    BSelectPersons = [BSelectPerson1,
                      BSelectPerson2,
                      BSelectPerson3,
                      BSelectPerson4,
                      BSelectPerson5,
                      BSelectPerson6]

    LFSelectPersons = [LFSelectPerson1,
                       LFSelectPerson2,
                       LFSelectPerson3,
                       LFSelectPerson4,
                       LFSelectPerson5,
                       LFSelectPerson6]

    IPhoto = ImageTk.PhotoImage(Image.open("SavedPictures\\static.jpg"))
    LPhoto = Label(image=IPhoto)





    def __init__(self):

        self.root.title(u'HFind')
        self.root.geometry('1350x750+85+20')
        self.root.resizable(False, False)
        self.set_default_W()

        self.BSearchSite.place(x=1200, y=5)
        self.TSearchSite.place(x=901, y=7)
        self.BSearchSite.bind('<Button-1>', self.bind_search_user)
        self.pack_graphW()
        self.set_buttons_infoW()
        self.set_entry()
        self.set_infoW()
        self.pack_first_infoW()
        self.pack_tokenW()
        self.pack_searchContacts()
        self.root.mainloop()

    def pack_searchContacts(self):
        self.LFSearchContacts.place(x=57, y=50)
        self.TSearchContacts.pack()
        self.BSearch.place(x=57, y=100)
        self.BSearch.bind('<Button-1>', self.bind_searchContacts)
        self.BSelectPerson1.bind('<Button-1>', self.bind_selectPerson1)
        self.BSelectPerson2.bind('<Button-1>', self.bind_selectPerson2)
        self.BSelectPerson3.bind('<Button-1>', self.bind_selectPerson3)
        self.BSelectPerson4.bind('<Button-1>', self.bind_selectPerson4)
        self.BSelectPerson5.bind('<Button-1>', self.bind_selectPerson5)
        self.BSelectPerson6.bind('<Button-1>', self.bind_selectPerson6)


    def pack_tokenW(self):
        self.TokButton.place(x=350, y=130)
        self.TokEntry.place(x=350, y=90)
        self.TokInfo.place(x=350, y=50)
        self.TokButton.bind('<Button-1>', self.bind_token)

    def pack_graphW(self):
        self.LFFriendsGraph.place(x=349, y=520)
        self.LFGroupsGraph.place(x=349,y=250)
        self.LFFGButton.pack()
        self.LFGGButton.pack()

        self.ChBGroupGraph_Entry1.place(x=480, y=330)
        self.ChBGroupGraph_Entry1['state'] = NORMAL
        self.set_text(self.ChBGroupGraph_Entry1, 'Группа1')

        self.ChBGroupGraph_Entry2.place(x=480, y=370)
        self.set_text(self.ChBGroupGraph_Entry2, 'Группа2')
        self.ChBGroupGraph_Entry2['state'] = NORMAL

        self.ChBGroupGraph_Entry3.place(x=480, y=410)
        self.set_text(self.ChBGroupGraph_Entry3, 'Группа3')
        self.ChBGroupGraph_Entry3['state'] = NORMAL

        self.ChBGroupGraph_Entry4.place(x=670, y=330)
        self.set_text(self.ChBGroupGraph_Entry4, 'Группа4')
        self.ChBGroupGraph_Entry4['state'] = NORMAL

        self.ChBGroupGraph_Entry5.place(x=670, y=370)
        self.set_text(self.ChBGroupGraph_Entry5, 'Группа5')
        self.ChBGroupGraph_Entry5['state'] = NORMAL

        self.ChBGroupGraph_Entry6.place(x=670, y=410)
        self.set_text(self.ChBGroupGraph_Entry6, 'Группа6')
        self.ChBGroupGraph_Entry6['state'] = NORMAL

        self.ChBGroupGraph_Info1.place(x=480, y=271)
        self.ChBGroupGraph_Info1['state'] = NORMAL
        self.ChBGroupGraph_Info1.delete(1.0, END)
        self.ChBGroupGraph_Info1.insert(1.0,
                                        'Показывает, насколько велико количество общих\nучастников, являющихся друзьями данного\nпользователя, в выбранных группах.')
        self.ChBGroupGraph_Info1['state'] = DISABLED

        self.ChBGroupGraph_Counter['state'] = DISABLED


        self.ChBGroupGraph_frame.place(x=370,y=270)
        self.ChBGroupGraph_button1.pack()
        self.ChBGroupGraph_button1.bind('<Button-1>', self.bind_groupGraphF)
        self.ChBGroupGraph_button2.pack()
        self.ChBGroupGraph_button2.bind('<Button-1>', self.bind_groupGraphS)
        self.BGroupsGraph.place(x=374, y=450)
        self.BGroupsGraph.bind('<Button-1>', self.bind_buildGraphGroups)

        self.BFriendsGraph.place(x=374,y=573)
        self.BFriendsGraph.bind('<Button-1>', self.bind_buildGraphFriends)
        self.BFriendsGraph_info.place(x=374,y=543)
        self.BFriendsGraph_info.insert(1.0, 'Отображает круг общения человека')
        self.BFriendsGraph_info['state'] = DISABLED

    def add_lineToVk(self):

        session = vk.Session(access_token=self.token)
        self.api = vk.API(session)
        try:
            self.api.account.getCounters(filter='messages')
            return 1
        except:
            return 0

    def getUserId(self, link):
        try:
            id = link
            if 'vk.com/' in link:  # проверяем эту ссылку
                id = link.split('/')[-1]  # если да, то получаем его последнюю часть
            if not id.replace('id', '').isdigit():  # если в нем после отсечения 'id' сами цифры - это и есть id
                id = self.api.utils.resolveScreenName(screen_name=id)[
                    'object_id']  # если нет, получаем id с помощью метода API
            else:
                id = id.replace('id', '')
            return int(id)
        except: pass

    def set_text(self, field, text):
        field.delete(0, END)
        field.insert(0, text)
        return

    def set_infoW(self):
        for i in self.entry_first_infoW:
            i.pack()
        self.LId.pack()
        self.ETwitter.pack()
        self.EInstagram.pack()
        self.ESkype.pack()
        self.block_entry()

    def pack_first_infoW(self):

        self.LFid.place(x=1130, y=190)

        self.LFFName.place(x=920, y=250)

        self.LFLName.place(x=920, y=310)

        self.LFMName.place(x=920, y=370)

        self.LFBDay.place(x=1100, y=430)

        self.LFBMonth.place(x=1154, y=430)

        self.LFBYear.place(x=1208, y=430)

        self.LFCity.place(x=920, y=490)

        self.LFCountry.place(x=1112, y=490)

        self.LFMobile.place(x=920, y=550)

        self.LPhoto.place(x=920, y=43)

    def forget_first_infoW(self):
        self.LPhoto.place_forget()
        for i in self.label_first_infoW:
            i.place_forget()

    def forget_second_infoW(self):

        for i in self.label_second_infoW:
            i.place_forget()

        for i in self.bunntons_second_infoW:
            i.place_forget()

    def pack_second_infoW(self):
        self.LFTwitter.pack()

        self.BFindLikes.pack()
        self.BFindLikes.bind('<Button-1>', self.bind_updateLikes)

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
        if self.BSaveTo['text'] == 'Сохранить профиль' and self.vk_profile.id != 'id':
            try:
                if self.data_base.findUser(self.vk_profile.id):
                    diff = self.data_base.findDiff(self.vk_profile)
                    self.data_base.updateUserData(self.vk_profile.id, diff)
                else:
                    self.data_base.addFrom(self.vk_profile)
            except:
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
        try:
            if not self.data_base.findUser(self.vk_profile.id):
                try:
                    os.remove('SavedPictures\\'+self.vk_profile.id +'.jpg')
                except:
                    pass
        except:
            self.data_base.tableCreation()

        request = self.TSearchSite.get()
        id = self.getUserId(request)
        if self.data_base.findUser(id):
            self.data_base.getFromTo(self.vk_profile, id)
            self.unblock_entry()
            self.clear_entry()
            self.set_entry()
            self.block_entry()
            self.setPhoto()
        else:
            try:
                self.vk_profile.set_data(request, self.token)
                #self.IPhoto['file'] = 'C:\\Учеба\CursRab\\Interface\\' + self.vk_profile.fname + '_' + self.vk_profile.lname + '.bmp'
                self.setPhoto()
                self.LPhoto['image'] = self.IPhoto
                self.unblock_entry()
                self.clear_entry()
                self.set_entry()
                self.block_entry()
            except:
                pass

    def bind_find_likes(self, event):
        if self.TBigInfo['state'] == 'disabled':
            self.TBigInfo.config(state=NORMAL)
            self.TBigInfo.delete('1.0', END)
            self.vk_profile.vk_data.get__likes(5)
        else:
            pass

    def bind_token(self, event):
        self.token = self.TokEntry.get()

        if self.add_lineToVk():
            self.TokInfo['text'] = 'Соединение установлено'

        else: self.TokInfo['text'] = 'Неверный токен, попробуйте еще раз!'

    def bind_updateLikes(self, event):
        if self.vk_profile.id != 'id' and self.BFindLikes['relief'] != 'sunken':
            self.vk_profile.get_likes(self.api, self.token)
            if self.TBigInfo['state'] == 'disabled':
                self.TBigInfo.config(state=NORMAL)
                self.TBigInfo.delete('1.0', END)
                self.TBigInfo.insert(1.0, self.vk_profile.likes)
                self.TBigInfo.config(state=DISABLED)
            else:
                self.TBigInfo.delete('1.0', END)
                self.TBigInfo.insert(1.0, self.vk_profile.likes)

    def bind_groupGraphF(self, event):
        self.ChBGroupGraph_Entry1.place(x=480, y=330)
        self.ChBGroupGraph_Entry1['state'] = NORMAL
        self.set_text(self.ChBGroupGraph_Entry1, 'Группа1')

        self.ChBGroupGraph_Entry2.place(x=480, y=370)
        self.set_text(self.ChBGroupGraph_Entry2, 'Группа2')
        self.ChBGroupGraph_Entry2['state'] = NORMAL

        self.ChBGroupGraph_Entry3.place(x=480, y=410)
        self.set_text(self.ChBGroupGraph_Entry3, 'Группа3')
        self.ChBGroupGraph_Entry3['state'] = NORMAL

        self.ChBGroupGraph_Entry4.place(x=670, y=330)
        self.set_text(self.ChBGroupGraph_Entry4, 'Группа4')
        self.ChBGroupGraph_Entry4['state'] = NORMAL

        self.ChBGroupGraph_Entry5.place(x=670, y=370)
        self.set_text(self.ChBGroupGraph_Entry5, 'Группа5')
        self.ChBGroupGraph_Entry5['state'] = NORMAL

        self.ChBGroupGraph_Entry6.place(x=670, y=410)
        self.set_text(self.ChBGroupGraph_Entry6, 'Группа6')
        self.ChBGroupGraph_Entry6['state'] = NORMAL

        self.ChBGroupGraph_Info1.place(x=480, y=271)
        self.ChBGroupGraph_Info1['state'] = NORMAL
        self.ChBGroupGraph_Info1.delete(1.0, END)
        self.ChBGroupGraph_Info1.insert(1.0, 'Показывает, насколько велико количество общих\nучастников, являющихся друзьями данного\nпользователя, в выбранных группах.')
        self.ChBGroupGraph_Info1['state'] = DISABLED

        self.ChBGroupGraph_Counter['state'] = DISABLED
        self.ChBGroupGraph_CounterText.place_forget()
        self.ChBGroupGraph_Counter.place_forget()
        self.ChBGroupGraph_Info2.place_forget()

    def bind_groupGraphS(self, event):

        self.ChBGroupGraph_Entry1.place_forget()
        self.ChBGroupGraph_Entry1['state'] = DISABLED

        self.ChBGroupGraph_Entry2.place_forget()
        self.ChBGroupGraph_Entry1['state'] = DISABLED

        self.ChBGroupGraph_Entry3.place_forget()
        self.ChBGroupGraph_Entry1['state'] = DISABLED

        self.ChBGroupGraph_Entry4.place_forget()
        self.ChBGroupGraph_Entry1['state'] = DISABLED

        self.ChBGroupGraph_Entry5.place_forget()
        self.ChBGroupGraph_Entry1['state'] = DISABLED

        self.ChBGroupGraph_Entry6.place_forget()
        self.ChBGroupGraph_Entry1['state'] = DISABLED

        self.ChBGroupGraph_Info1.place_forget()

        self.ChBGroupGraph_Info2.place(x=480, y=271)
        self.ChBGroupGraph_Info2['state'] = NORMAL
        self.ChBGroupGraph_Info2.delete(1.0, END)
        self.ChBGroupGraph_Info2.insert(1.0,
                                        'Показывает, насколько велико количество общих\nучастников, являющихся друзьями'
                                        ' данного\nпользователя, в группах пользователя.\nКоличество групп по умолчанию'
                                        ': 10\nВнимание! Большее количество групп приводит\nк большему времени ожидания.')
        self.ChBGroupGraph_Info2['state'] = DISABLED
        self.ChBGroupGraph_Counter.place(x=650, y=380)
        self.ChBGroupGraph_Counter['state'] = NORMAL
        self.ChBGroupGraph_CounterText.place(x=480, y=380)
        self.ChBGroupGraph_CounterText['state'] = NORMAL
        self.set_text(self.ChBGroupGraph_CounterText, 'Количество групп:')
        self.ChBGroupGraph_CounterText['state'] = DISABLED

    def bind_buildGraphFriends(self, event):
            self.user_graph.make_friendsGraph(self.vk_profile.get_commonFriends(self.api, self.token))
            self.user_graph.show_friendsGraph()

    def bind_buildGraphGroups(self, event):
        if self.ChBGroupGraph_Counter['state'] == NORMAL:
            if self.ChBGroupGraph_Counter.get() == '': count = 10
            else: count = int(self.ChBGroupGraph_Counter.get())
            self.user_graph.make_groupGraph(self.vk_profile.fname, self.vk_profile.lname,
                                            self.vk_profile.getInfo_fromCountOfGroups(self.api,count))
            self.user_graph.show_groupGraph_common()
        else:
            found_groups = []
            for i in self.Entries_ofGroupGraph:
                found_groups.append(i.get())
            self.user_graph.make_groupGraphSix(self.vk_profile.fname, self.vk_profile.lname,
                                               self.vk_profile.getInfo_fromGroups(self.api, found_groups))
            self.user_graph.show_groupGraph_common()

    def bind_searchContacts(self, event):

        word = self.TSearchContacts.get().split()
        contacts = [[],[]]
        try:
            #contacts = self.data_base.findSame(word)
            for k in word:
                tmp_contacts = self.data_base.findSame(k)
                for ko in range(0, len(tmp_contacts[0])):
                    if tmp_contacts[1][ko] not in contacts[1]:
                        contacts[0].append(tmp_contacts[0][ko])
                        contacts[1].append(tmp_contacts[1][ko])

            counter = 0
            for p in word:
                for po in range(0, len(contacts[0])):
                    if p.lower() not in contacts[0][po - counter].lower():
                        contacts[0].remove(contacts[0][po - counter])
                        contacts[1].remove(contacts[1][po - counter])
                        counter += 1
        except:
            return
        for g in range(0, 6):
            self.EBlankForIds[g].pack_forget()
            self.EBlankForContacts[g].pack_forget()
            self.BSelectPersons[g].pack_forget()
            self.LFSelectPersons[g].place_forget()
        if len(contacts[0]) > 0:
            for i in range(0, len(contacts[0])):
                if i > 5:
                    break
                self.EBlankForContacts[i]['state'] = NORMAL
                self.EBlankForIds[i]['state'] = NORMAL
                self.EBlankForContacts[i].delete(0, 'end')
                self.EBlankForIds[i].delete(0, 'end')
                self.EBlankForContacts[i].insert(END, contacts[0][i])
                self.EBlankForIds[i].insert(END, contacts[1][i])
                self.EBlankForContacts[i]['state'] = DISABLED
                self.EBlankForIds[i]['state'] = DISABLED
                self.LFSelectPersons[i].place(x=57, y=150 + i * 80)
                self.EBlankForIds[i].pack()
                self.EBlankForContacts[i].pack()
                self.BSelectPersons[i].pack()

    def bind_selectPerson1(self, event):
        self.deletePhoto()
        id = self.EBlankForId1.get()
        self.data_base.getFromTo(self.vk_profile, id)
        self.fill_entry()
        self.setPhoto()

    def bind_selectPerson2(self, event):
        self.deletePhoto()
        id = self.EBlankForId2.get()
        self.data_base.getFromTo(self.vk_profile, id)
        self.fill_entry()
        self.setPhoto()

    def bind_selectPerson3(self, event):
        self.deletePhoto()
        id = self.EBlankForId3.get()
        self.data_base.getFromTo(self.vk_profile, id)
        self.fill_entry()
        self.setPhoto()

    def bind_selectPerson4(self, event):
        self.deletePhoto()
        id = self.EBlankForId4.get()
        self.data_base.getFromTo(self.vk_profile, id)
        self.fill_entry()
        self.setPhoto()

    def bind_selectPerson5(self, event):
        self.deletePhoto()
        id = self.EBlankForId5.get()
        self.data_base.getFromTo(self.vk_profile, id)
        self.fill_entry()
        self.setPhoto()

    def bind_selectPerson6(self, event):
        self.deletePhoto()
        id = self.EBlankForId6.get()
        self.data_base.getFromTo(self.vk_profile, id)
        self.fill_entry()
        self.setPhoto()

    def fill_entry(self):
        self.unblock_entry()
        self.clear_entry()
        self.set_entry()
        self.block_entry()

    def setPhoto(self):
        try:
            self.IPhoto = ImageTk.PhotoImage(Image.open(
                "SavedPictures\\" + str(self.vk_profile.id) + ".jpg"))
            self.LPhoto['image'] = self.IPhoto
        except:
            self.IPhoto = ImageTk.PhotoImage(Image.open(
                "SavedPictures\\static.jpg"))
            self.LPhoto['image'] = self.IPhoto

    def deletePhoto(self):
        if not self.data_base.findUser(self.vk_profile.id):
            try:
                path = 'SavedPictures\\'+str(self.vk_profile.id) +'.jpg'
                os.remove(path)
            except:
                pass

myW = MyWindow()




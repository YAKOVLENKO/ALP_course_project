
import vk, time, requests
import urllib.request



class Vk_data:
    access = ''
    vk_api = ''
    data_profile = ''
    user_id = ''
    data_groups = ''
    def __init__(self, site, token):
        self.access = token
        session = vk.Session(access_token = self.access)
        self.vk_api = vk.API(session)
        self.user_id = self.getUserId(site)

        try:
            self.data_profile = self.vk_api.users.get(user_ids = self.user_id, fields = "about,activities,bdate,"
                                                                                     "books,career,city,connections,"
                                                                                     "contacts,country,education,games,"
                                                                                     "home,"
                                                                                     "town,interests,maiden_name,military,"
                                                                                     "movies,music,nickname,occupation,"                                                                                     
                                                                                     "photo_200,quotes,relatives,"
                                                                                     "relation,schools,sex,site,status,tv,"
                                                                                     "universities")
            self.data_groups = self.vk_api.groups.get(user_id = self.user_id, extended = 1, fields = 'name,status,description')[1:]
        except:

            self.data_profile = requests.get('https://api.vk.com/method/users.get?fields=about,activities,bdate,books,'
                                         'career,city,connections,contacts,country,education,games,home,town,interests,'
                                         'maiden_name,military,movies,music,nickname,occupation,movies,music,nickname,'
                                         'occupation,personal,photo_200,quotes,relatives,relation,'
                                             'schools,sex,site,'
                                         'status,tv,universities&user_id='+str(self.user_id))
            self.data_profile = self.data_profile.json()['response']
            self.data_groups = requests.get('https://api.vk.com/method/users.getSubscriptions?extended=1&fields=name, status, description&user_id=' + str(self.user_id))
            self.data_groups = self.data_groups.json()['response']
        self.change__relatives()
        self.set_birthday()
        self.change__city()
        self.change__country()
        self.change__career()
        self.change__universities()
        self.change__schools()
        self.downloadSave_picture()

    def getUserId(self, link):
        try:
            id = link
            if 'vk.com/' in link:
                id = link.split('/')[-1]
            if not id.replace('id', '').isdigit():
                id = self.vk_api.utils.resolveScreenName(screen_name=id)['object_id']
            else:
                id = id.replace('id', '')
            return int(id)
        except:
            pass

    def change__relatives(self):
        if 'relatives' in self.data_profile[0]:
            for relate in self.data_profile[0]['relatives']:
                if not ('name' in relate):
                    uid_data = self.vk_api.users.get(user_ids=relate['uid'])[0]
                    relate.update({'name': uid_data['first_name'] + ' ' + uid_data['last_name']})

    def change__city(self):
        if 'city' in self.data_profile[0]:
            #self.data_profile[0]['city'] = self.vk_api.database.getCitiesById(city_ids=self.data_profile[0]['city'])
            #self.data_profile[0]['city'] = self.data_profile[0]['city'][0]['name']
            try:
                time.sleep(1)
                self.data_profile[0]['city'] = requests.post(
                            'https://api.vk.com/method/execute?access_token=' + self.access +
                            '&code=return API.database.getCitiesById({"city_ids":' + str(self.data_profile[0]['city'])+'});').json()['response'][0]['name']
            except: pass

    def change__universities(self):
        if 'universities' in self.data_profile[0]:
            for i in self.data_profile[0]['universities']:

                #i['country'] = self.vk_api.database.getCountriesById(country_ids=i['country'])
                time.sleep(1)
                i['country'] = requests.post(
                    'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCountriesById({"country_ids":' + str(
                        i['country']) + '});').json()['response'][0]['name']

                #i['city'] = self.vk_api.database.getCitiesById(city_ids=i['city'])
                time.sleep(1)
                i['city'] = requests.post(
                    'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCitiesById({"city_ids":' + str(
                        i['city']) + '});').json()['response'][0]['name']

    def change__schools(self):
        if 'schools' in self.data_profile[0]:
            for i in self.data_profile[0]['schools']:
                time.sleep(1)
                i['country'] = requests.post(
                    'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCountriesById({"country_ids":' + str(
                        i['country']) + '});').json()['response'][0]['name']
                time.sleep(1)
                i['city'] = requests.post(
                    'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCitiesById({"city_ids":' + str(
                        i['city']) + '});').json()['response'][0]['name']

    def change__career(self):
        if 'career' in self.data_profile[0]:
            for i in self.data_profile[0]['career']:
                if 'group_id' in i:
                    name = self.vk_api.groups.getById(group_id=i['group_id'])[0]['name']
                    i.update({'vk': name})
                time.sleep(1)
                i['country_id'] = requests.post(
                        'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCountriesById({"country_ids":' + str(i['country_id'])+'});')
                i['country_id'] = i['country_id'].json()['response'][0]['name']
                    #self.vk_api.database.getCountriesById(country_ids=i['country_id'])
                time.sleep(1)
                i['city_id'] = i['city_id'] = requests.post(
                        'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCitiesById({"city_ids":' + str(i['city_id'])+'});')
                i['city_id'] = i['city_id'].json()['response'][0]['name']
                    #self.vk_api.database.getCitiesById(city_ids=i['city_id'])

    def change__country(self):
        if 'country' in self.data_profile[0]:
            try:
                time.sleep(1)
                a = self.data_profile[0]['country']
                self.data_profile[0]['country'] = requests.post(
                            'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCountriesById({"country_ids":' + str(self.data_profile[0]['country'])+'});')
                self.data_profile[0]['country'] = self.data_profile[0]['country'].json()['response'][0]['name']
                    #self.data_profile[0]['country'] = self.vk_api.database.getCountriesById(country_ids=self.data_profile[0]['country'])
            except:
                try:
                    self.data_profile[0]['country'] = self.vk_api.database.getCountriesById(
                        country_ids=self.data_profile[0]['country'])
                    self.data_profile[0]['country'] = self.data_profile[0]['country'][0]
                except:
                    self.data_profile[0]['country'] = 'Страна'

    def set_birthday(self):
        info = ''
        year = ''
        month = ''
        day = ''
        try:
            info = self.data_profile[0]['bdate']
        except:
            pass

        if len(info) != 10 and len(info) != 9:
            name = self.data_profile[0]['first_name'] + ' ' + self.data_profile[0]['last_name']
            try:

                    for ydate in range(-2003, -1950):
                        ydate *= -1
                        ans = ''
                        try:
                            time.sleep(1)
                            ans = self.vk_api.users.search(q=name,
                                                           count=1000,
                                                           birth_year=ydate)
                        except vk.exceptions.VkAPIError as text:
                            if str(text)[:2] == '6.':
                                time.sleep(1)
                                continue
                        if ans[0] != 0:
                            for answer in ans[1:]:
                                if answer['uid'] == self.data_profile[0]['uid']:
                                    year = ydate
                                    break
                        if year != '':
                            break

                    if (info != ''):
                        self.data_profile[0]['bdate'] = info + '.' + str(year)

                    else:
                        for ddate in range(1, 32):
                            try:
                                time.sleep(1)
                                ans = self.vk_api.users.search(q=name,
                                                               count=1000,
                                                               birth_day=ddate,
                                                               birth_year=year)
                            except vk.exceptions.VkAPIError as text:
                                if str(text)[:2] == '6.':
                                    time.sleep(1)
                            if ans[0] != 0:
                                for answer in ans[1:]:
                                    if answer['uid'] == self.data_profile[0]['uid']:
                                        day = ddate
                                        break
                            if day != '':
                                break
                        for mdate in range(1, 13):
                            try:
                                time.sleep(1)
                                ans = self.vk_api.users.search(q=name,
                                                               count=1000,
                                                               birth_day=day,
                                                               birth_year=year,
                                                               birth_month=mdate)
                            except vk.exceptions.VkAPIError as text:
                                if str(text)[:2] == '6.':
                                    time.sleep(1)
                            if ans[0] != 0:
                                for answer in ans[1:]:
                                    if answer['uid'] == self.data_profile[0]['uid']:
                                        month = mdate
                                        break
                            if month != '':
                                break
                        self.data_profile[0].update({'bdate': str(day) + '.' + str(month) + '.' + str(year)})
            except: pass

    def downloadSave_picture(self):
        data = self.data_profile[0]
        url = data['photo_200']
        urllib.request.urlretrieve(url, '..\\Interface\\SavedPictures\\'+str(data['uid']) + '.jpg')


# 15 января в 2 дня АЯП

#B = Vk_data('https://vk.com/id394728714', 'f29548559f34a82cae2f3ec9578c4af5526a5fd60ca77a2bed80517b20af636c53d335bee5fe9bbc0265b')
#B.set_data('yakovlenko_anna', 'd550e01849aae9307c1263ddb24ec5b6a48d3c9f10df200cfefcbc36c14f9f903f97d28ac9d8ea2af9142')
#print(B.data_profile)





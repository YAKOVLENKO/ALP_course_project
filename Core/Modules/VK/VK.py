from urllib.request import urlretrieve
import vk, os, time, math, requests
import urllib.request
import threading

# requests все-таки добавлю, так как библиотрека для работы с VK не позволяет работать без access_token. Работа без
# acess_token позволяет просматривать пользователей, у которых данный пользователь находится в black_list (если,
# конечно, аккаунт не скрыт настройками приватноси)
# add: если найдутся способы узнать информацию более удобным способом, я его применю


# count это количество запросов (и количество постов = 100 * count постов)

def getUserId(link, vkapi):
    try:
        id = link
        if 'vk.com/' in link: # проверяем эту ссылку
            id = link.split('/')[-1]  # если да, то получаем его последнюю часть
        if not id.replace('id', '').isdigit(): # если в нем после отсечения 'id' сами цифры - это и есть id
            id = vkapi.utils.resolveScreenName(screen_name = id)['object_id'] # если нет, получаем id с помощью метода API
        else:
            id = id.replace('id', '')
        return int(id)
    except:
        pass

class Vk_data:
    access = ''
    vk_api = ''
    data_profile = ''
    user_id = ''
    data_groups = ''
    def __init__(self, site, token):
        try:
            self.access = token
            session = vk.Session(access_token = self.access)
            self.vk_api = vk.API(session)
            self.user_id = getUserId(site, self.vk_api)

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
        except:
            pass


    def change__relatives(self):
        if 'relatives' in self.data_profile[0]:
            for i in self.data_profile[0]['relatives']:
                if not ('name' in i):
                    uid_data = self.vk_api.users.get(user_ids=i['uid'])[0]
                    i.update({'name': uid_data['first_name'] + ' ' + uid_data['last_name']})

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
                self.data_profile[0]['country'] = requests.post(
                            'https://api.vk.com/method/execute?access_token=' + self.access + '&code=return API.database.getCountriesById({"country_ids":' + str(self.data_profile[0]['country'])+'});')
                self.data_profile[0]['country'] = self.data_profile[0]['country'].json()['response'][0]['name']
                    #self.data_profile[0]['country'] = self.vk_api.database.getCountriesById(country_ids=self.data_profile[0]['country'])
            except:
                pass

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
            #lname = self.data_profile[0]['last_name']
            try:

                    for i in range(-2003, -1950):
                        i *= -1
                        ans = ''
                        try:
                            ans = self.vk_api.users.search(q=name, count=1000, birth_year=i)
                        except vk.exceptions.VkAPIError as text:
                            if str(text)[:2] == '6.':
                                time.sleep(1)
                                continue
                        if ans[0] != 0:
                            for j in ans[1:]:
                                if j['uid'] == self.data_profile[0]['uid']:
                                    year = i
                                    break
                        if year != '':
                            break

                    if (info != ''):
                        self.data_profile[0]['bdate'] = info + '.' + str(year)

                    else:
                        for i in range(1, 32):
                            try:
                                ans = self.vk_api.users.search(q=name, count=1000, birth_day=i,
                                                               birth_year=year)
                            except vk.exceptions.VkAPIError as text:
                                if str(text)[:2] == '6.':
                                    time.sleep(1)
                            if ans[0] != 0:
                                for j in ans[1:]:
                                    if j['uid'] == self.data_profile[0]['uid']:
                                        day = i
                                        break
                            if day != '':
                                break
                        for i in range(1, 13):
                            try:
                                ans = self.vk_api.users.search(q=name, count=1000, birth_day=day,
                                                               birth_year=year,
                                                               birth_month=i)
                            except vk.exceptions.VkAPIError as text:
                                if str(text)[:2] == '6.':
                                    time.sleep(1)
                            if ans[0] != 0:
                                for j in ans[1:]:
                                    if j['uid'] == self.data_profile[0]['uid']:
                                        month = i
                                        break
                            if month != '':
                                break
                        self.data_profile[0].update({'bdate': str(day) + '.' + str(month) + '.' + str(year)})
            except: pass

    def downloadSave_picture(self):
        data = self.data_profile[0]
        url = data['photo_200']
        urllib.request.urlretrieve(url, '..\\Interface\\SavedPictures\\'+data['first_name']+ '_' + data['last_name'] + '.jpg')



class Profile:
    vk_data = ''
    groups = ''
    id = 'id'
    fname = 'Имя'
    lname = 'Фамилия'
    mname = 'Отчество'
    birth_day = 'дд'
    birth_month = 'мм'
    birth_year = 'гггг'
    city = 'Город'
    country = 'Страна'
    mobile_phone = 'Телефон'
    skype = 'skype.com/'
    instagram = 'instagram.com/'
    facebook = 'facebook.com/'
    twitter = 'twitter.com/'
    career = 'Места работы'
    education = 'Места учебы'
    interests = 'Интересы'
    relatives = 'Родственные связи'
    likes = 'Понравившиеся посты'

    def __int__(self):
        pass

    def set_data(self, site, access):
        try:
            self.vk_data = Vk_data(site, access)
            data = self.vk_data.data_profile[0]
            self.id = data['uid']
            self.fname = data['first_name']
            self.lname = data['last_name']

            self.groups = self.vk_data.data_groups



            try:
                self.birth_day = data['bdate'].split('.')[0]
                self.birth_month = data['bdate'].split('.')[1]
                self.birth_year = data['bdate'].split('.')[2]
            except:
                self.birth_day = 'дд'
                self.birth_month = 'мм'
                self.birth_year = 'гггг'

            if 'nickname' in data:
                self.mname = data['nickname']
            else:
                self.mname = 'Отчество'

            if 'city' in data and not str(data['city']).isdigit():
                self.city = data['city']
            else:
                self.city = 'Город'

            if 'mobile_phone' in data:
                self.mobile_phone = data['mobile_phone']
            else:
                self.mobile_phone = 'Телефон'

            if 'instagram' in data:
                self.instagram = data['instagram']
            else:
                self.instagram = 'instagram.com/'

            if 'skype' in data:
                self.skype = data['skype']
            else:
                self.skype = 'skype.com/'


            if 'career' in data:
                self.career = ''
                for i in data['career']:
                    if 'vk' in i:
                        self.career += 'Место работы: ' + i['vk'] + '\n' + 'Страна: ' + i['country_id'] + '\n' + 'Город: ' \
                                       + i['city_id'] + '\n'

                    else:
                        self.career += 'Место работы: ' + i['company'] + '\n' + 'Страна: ' + i['country_id'] + '\n' \
                                       + 'Город: ' + i['city_id'] + '\n'

                    self.career += 'Годы работы: '
                    if 'from' in i:
                        self.career += str(i['from']) + ' - '
                    else:
                        self.career += 'Неизвестно - '
                    if 'until' in i:
                        self.career += str(i['until']) + '\n'
                    else:
                        self.career += 'неизвестно\n'
                    self.career += 'Должность: '
                    if 'position' in i:
                        self.career += i['position'] + '\n\n'
                    else:
                        self.career += 'Неизвестно\n\n'
                if self.career == '':
                    self.career = 'Места работы'


            else:
                self.career = 'Места работы'


            if 'schools' in data and len(data['schools']) != 0:
                self.education = ''
                for i in data['schools']:
                    self.education += i['name'] + '\n' + 'Страна: ' + i['country'] + '\n' + 'Город: ' + \
                                          i['city'] + '\n' + 'Годы обучения: '
                    if 'year_from' in i:
                        self.education += str(i['year_from']) + ' - '
                    else:
                        self.education += 'Неизвестно - '
                    if 'year_to' in i:
                        self.education += str(i['year_to']) + ' - '
                    else:
                        self.education += 'неизвестно\n'
                    self.education += 'Класс: '
                    if 'class' in i:
                        self.education += str(i['class']) + '\n\n'
                    else:
                        self.education += 'Неизвестно\n\n'
            else:
                self.education = 'Места учебы'
            if 'universities' in data and len(data['universities']) != 0:
                if self.education == 'Места учебы':
                    self.education = ''
                for i in data['universities']:
                    self.education += i['name'] + '\n'
                    if 'faculty_name' in i:
                        self.education += i['faculty_name'] + '\n'
                    else:
                            self.education += 'Факультет: неизвестно\n'
                    if 'chair_name' in i:
                            self.education += i['chair_name'] + '\n'
                    else:
                        self.education += 'Кафедра: неизвестно\n'
                    self.education += 'Страна: ' + i['country'] + '\n'
                    self.education += 'Город: ' + i['city'] + '\n'
                    if 'education_form' in i:
                        self.education += i['education_form'] + '\n'
                    else:
                        self.education += 'Отделение: неизвестно\n'
                    if 'education_status' in i:
                        self.education += i['education_status'] + '\n\n'
                    else:
                        self.education += '\n'

            if 'relatives' in data:
                for i in data['relatives']:
                    if i['type'] == 'parent':
                        self.relatives += 'Родитель:' + i['name'] + '\n\n'
                    if i['type'] == 'sibling':
                        self.relatives += 'Брат/сестра' + i['name'] + '\n\n'
            else:
                self.relatives = 'Родственные связи'

            try:
                self.interests = self.InterestsSearch()
            except:
                self.interests = 'Интересы'

            if 'country' in data:
                self.country = data['country']
                if self.country == []:
                   self.country = ''
            else:
                pass
        except:
            pass

    def InterestsSearch(self):
        try:
            info_about_groups = self.vk_data.data_groups
            full = 0
            interests_list = ''
            interests_dict = {
                'Мультипликация, комиксы': [0, 'манхв', 'аниме', 'anime', 'маньху', 'manhua', 'manhwa', 'манга', 'manga',
                                            'манге', 'мангу', 'комикс', 'мультф', 'мультик'],
                'Юмор, мемы': [0, 'мем', 'mem', 'юмор', 'смех', 'смешн', 'прикол', '4ch', '2ch'],
                'Кино, сериалы': [0, 'кино', 'фильм', 'сериал'],
                'Игры, киберспорт': [0, 'игр', 'game', 'гейм'],
                'Спорт': [0, ' спорт', 'sport', 'фитнес'],
                'Социальные сети': [0, 'tumblr', 'instagram', 'twitter', 'insta', 'facebook', 'тамблер', 'тумблер', 'инста',
                                    'фэйсбук', 'фейсбук'],
                'Наука': [0, 'наук', 'science', 'физик', 'хими', 'биолог'],
                'Искусство': [0, 'art', 'арт', 'искусств', 'худож', 'рису', 'рисов'],
                'IT': [0, 'программи', 'java', 'c++', 'python', 'комп'],
                'Красота': [0, 'бьюти', 'beauty', 'красот'],
                'Музыка': [0, 'music', 'песн', 'музык'],
                'Животные': [0, 'cat', 'кошк', 'собак', 'кот'],
                'Общение': [0, 'знакомств', 'друз']
            }

            for z in info_about_groups[1:]:
                for y in interests_dict:
                    for x in interests_dict[y]:
                        try:
                            if x != interests_dict[y][0] and (x in z['name'].lower() or x in z['status'].lower() or x
                            in z['description'].lower()):
                                interests_dict[y][0] += 1
                                full += 1
                                break

                        except KeyError:
                            try:
                                if x != interests_dict[y][0] and x in z['description'].lower():
                                    interests_dict[y][0] += 1
                                    full += 1
                                    break
                            except:
                                continue
            for i in interests_dict.keys():
                percent = interests_dict[i][0] * 100 / full
                if percent > 15:
                    interests_list += i + ', '
            return interests_list.title()
        except:
            pass


    def get_likes(self, vk_api, token):
        try:
            count = 5
            counter = 0
            try:
                data_groups = vk_api.groups.get(user_id=self.id, extended=0)
            except:
                data_groups = requests.get('https://api.vk.com/method/users.getSubscriptions?user_id=' + str(self.id))
                data_groups = data_groups.json()['response']['groups']['items']
            data_groups = ['-' + str(x) for x in data_groups]
            posts = []
            is_liked = []

            newsfeed = vk_api.newsfeed.get(filters='post', source_ids=', '.join(data_groups), count=100, timeout=10)

            for x in newsfeed['items']:
                posts.append([x['post_id'], x['source_id']])
            if count != 1:
                for i in range(count - 1):
                    next_from = newsfeed['new_from']
                    kwargs = {
                        'from': next_from,
                        'filters': 'post',
                        'source_ids': ', '.join(data_groups),
                        'count': 100,
                        'timeout': 10
                    }
                    newsfeed = vk_api.newsfeed.get(**kwargs)

                    for x in newsfeed['items']:
                        posts.append([x['post_id'], x['source_id']])
                    time.sleep(0.35)

            for i in range(0, len(posts) // 25):
                i = i * 25
                text = 'https://api.vk.com/method/execute?access_token=' + token + '&code=return ['
                for g in range(0, 25):
                    g = g + i
                    post = posts[g]
                    text = text + 'API.likes.isLiked({"user_id":' + str(
                        self.id) + ',"type":"post", "owner_id":"' + str(
                        post[1]) + \
                           '", "item_id":"' + str(post[0]) + '"}),'
                text = text[0:-1] + ']' \
                                    ';'
                result = \
                requests.post(text).json()[
                    'response']
                # print(result)
                time.sleep(0.35)
                for i in result:
                    if i == 1:
                        is_liked.append('vk.com/wall-{0}_{1}'.format(-posts[counter][1], posts[counter][0]))
                    counter += 1
            self.likes = is_liked
        except:
            pass

    def get_commonFriends(self, vk_api, token):
        try:

            common_friends = []
            names = []
            ids = []
            groups_ids = []
            result = []
            for i in vk_api.friends.get(user_id=self.id, count=1000, fields='first_name,last_name,deactivated'):
                if not 'deactivated' in i:
                    ids.append(i['uid'])
                    names.append(i['first_name'] + '\n' + i['last_name'])

            for g in range(0, math.ceil(len(names)/100)):
                g *= 100
                groups_ids.append(ids[g:g+100])



            for k in range(0, len(groups_ids)):
                text = 'https://api.vk.com/method/execute?access_token=' + token + '&code=return ['
                text += 'API.friends.getMutual({"source_uid":' + str(self.id) + ',"target_uids":' + str(groups_ids[k])+ '}),'
                #result.append(vk_api.friends.getMutual(source_uid=self.id, target_uids=groups_ids[k]))
                text = text[0:-1] + '];'
                result.append(requests.post(text).json()['response'][0])

            counter=0
            for l in result:
                for m in l:
                    common_friends.append([self.fname+'\n'+self.lname, names[counter],m['common_count']])
                    counter += 1
            return common_friends
        except:
            pass

    def getInfo_fromCountOfGroups(self, vk_api, count = 10):
        try:
            personal_card = []
            persons = []
            answer = []
            for i in vk_api.friends.get(user_id=self.id, count=10000, fields='deactivated'):
                if not 'deactivated' in i:
                    persons.append(i['uid'])
            for g in vk_api.groups.get(user_id=self.id, count=count, extended=1)[1:]:
                personal_card.append([g['name'], g['gid'], 0])
            for w in range(0, count):
                answer.append([])
                for p in range(0, math.ceil(len(persons) / 500)):
                    p *= 500
                    time.sleep(1)
                    answ = vk_api.groups.isMember(group_id=personal_card[w][1], user_ids=
                        persons[p:p + 500])
                    answer[w] += answ

                for k in range(0, len(persons)):
                    if answer[w][k]['member']:
                        personal_card[w][2] += 1
            return personal_card
        except:
            pass

    def getInfo_fromGroups(self, vk_api, groups):
        try:
            personal_card = []
            persons = []
            for i in vk_api.friends.get(user_id=self.id, count=10000, fields='deactivated'):
                if not 'deactivated' in i:
                    persons.append(i['uid'])

            groups_counter = 0
            for g in groups:
                personal_card.append([[], 0])
                if 'vk.com/' in g:  # проверяем эту ссылку
                    g = g.split('/')[-1]  # если да, то получаем его последнюю часть
                if 'club' in g:
                    g = g.replace('club', '')
                try:
                    personal_card[groups_counter][0] = vk_api.groups.getById(group_id=g)[0]['name']
                    for p in range(0, math.ceil(len(persons) / 500)):
                        p *= 500
                        time.sleep(1)
                        for l in vk_api.groups.isMember(group_id=g, user_ids=
                            persons[p:p + 500]):
                            if l['member'] == 1:
                                personal_card[groups_counter][1] += 1
                    groups_counter += 1

                except:
                    personal_card.pop()
            return personal_card
        except:
            pass


# 15 января в 2 дня АЯП

#B = Vk_data('https://vk.com/id394728714', 'f29548559f34a82cae2f3ec9578c4af5526a5fd60ca77a2bed80517b20af636c53d335bee5fe9bbc0265b')
#B.set_data('yakovlenko_anna', 'd550e01849aae9307c1263ddb24ec5b6a48d3c9f10df200cfefcbc36c14f9f903f97d28ac9d8ea2af9142')
#print(B.data_profile)





from urllib.request import urlretrieve
import vk, os, time, math, requests

# requests все-таки добавлю, так как библиотрека для работы с VK не позволяет работать без access_token. Работа без
# acess_token позволяет просматривать пользователей, у которых данный пользователь находится в black_list (если,
# конечно, аккаунт не скрыт настройками приватноси)
# add: если найдутся способы узнать информацию более удобным способом, я его применю


# count это количество запросов (и количество постов = 100 * count постов)

def getUserId(link, vkapi):
    id = link
    if 'vk.com/' in link: # проверяем эту ссылку
        id = link.split('/')[-1]  # если да, то получаем его последнюю часть
    if not id.replace('id', '').isdigit(): # если в нем после отсечения 'id' сами цифры - это и есть id
        id = vkapi.utils.resolveScreenName(screen_name = id)['object_id'] # если нет, получаем id с помощью метода API
    else:
        id = id.replace('id', '')
    return int(id)

class Vk_data:
    access = ''
    vk_api = ''
    data_profile = ''
    data_profile__w = '' # для данных без авторизации
    user_id = ''
    data_groups = ''

    def __init__(self, site, token, year1, year2):
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
        self.set_birthday(year1, year2)
        self.change__sex()
        self.change__city()
        self.change__country()

    def change__sex(self):
        try:
            if self.data_profile[0]['sex'] == 1:
                self.data_profile[0]['sex'] = 'женский'
            else:
                self.data_profile[0]['sex'] = 'мужской'
        except:
            pass

    def change__city(self):
        try:
            self.data_profile[0]['city'] = self.vk_api.database.getCitiesById(city_ids=self.data_profile[0]['city'])
            self.data_profile[0]['city'] = self.data_profile[0]['city'][0]['name']
        except:
            pass

    def change__country(self):
        try:
            self.data_profile[0]['country'] = self.vk_api.database.getCountriesById(country_ids=self.data_profile[0]['country'])
        except:
            pass


    def get__likes(self, count):
        try:
            data_groups = self.vk_api.groups.get(user_id = self.user_id, extended = 0)
        except:
            data_groups = requests.get('https://api.vk.com/method/users.getSubscriptions?user_id='+str(self.user_id))
            data_groups = data_groups.json()['response']['groups']['items']
        data_groups = ['-' + str(x) for x in data_groups]
        is_liked = []
        newsfeed = self.vk_api.newsfeed.get(filters = 'post', source_ids = ', '.join(data_groups), count = count, timeout = 10)
        try:
            for i in newsfeed['items']:
                if self.vk_api.likes.isLiked(user_id = self.user_id, type = 'post', owner_id = str(i['source_id']),
                                        item_id = i['post_id']) == 1:
                    is_liked.append('vk.com/wall{0}_{1}'.format(i['source_id'], i['post_id']))
                time.sleep(0.3)
        except:
            is_liked.append('Упс! Кажется, данный пользователь давно ничего не лайкал!')
        return is_liked

    def set_birthday(self, year1, year2):
        info = ''
        year = ''
        month = ''
        day = ''
        try:
            info = self.data_profile[0]['bdate']
        except:
            pass

        if len(info) != 10 and len(info) != 9:
            print(len(info))
            fname = self.data_profile[0]['first_name']
            lname = self.data_profile[0]['last_name']
            for i in range(year1, year2 + 1):
                try:
                    ans = self.vk_api.users.search(q=fname + ' ' + lname, count=1000, birth_year=i)
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
                        ans = self.vk_api.users.search(q=fname + ' ' + lname, count=100, birth_day=i, birth_year=year)
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
                        ans = self.vk_api.users.search(q=fname + ' ' + lname, count=50, birth_day=day, birth_year=year,
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

    def get__data_profile(self):
        return self.data_profile

    def get__data_groups(self):
        return self.data_groups

    def get__vk_api(self):
        return self.vk_api
    def get__user_id(self):
        return self.user_id

class Interests: #todo задать определенный процент для выведения на экран

    interests = ''

    def __init__(self, acc_name):
        pass






    def get__interests(self):
        return self.interests

class Profile:
    id = ''
    fname = ''
    lname = ''
    sex = ''
    birth_day = ''
    birth_month = ''
    birth_year = ''
    city = ''
    country = ''
    mobile_phone = ''
    home_phone = ''
    skype = ''
    instagram = ''
    status = ''
    career = ''
    military = ''
    education = ''
    relation = ''
    personal = ''
    interests = ''
    relatives = ''

    def __init__(self, acc_name):
        data = acc_name.get__data_profile()[0]
        self.id = data['uid']
        self.fname = data['first_name']
        self.lname = data['last_name']
        try:
            self.sex = data['sex']
        except:
            pass

        try:
            self.birth_day = data['bdate'].split('.')[0]
        except:
            pass

        try:
            self.birth_month = data['bdate'].split('.')[1]
        except:
            pass

        try:
            self.birth_year = data['bdate'].split('.')[2]
        except:
            pass

        try:
            self.city = data['city']
            if self.city == []:
                self.city = ''
            self.city = self.city[0]['name']
        except:
            pass

        try:
            self.mobile_phone = data['mobile_phone']
        except:
            pass

        try:
            self.instagram = data['instagram']
        except:
            pass

        try:
            self.skype = data['skype']
        except:
            pass

        try:
            self.status = data['status']
        except:
            pass

        try:
            self.career = data['career']
        except:
            pass

        try:
            self.military = data['military']
        except:
            pass

        try:
            self.education = data['education']
        except:
            pass

        try:
            self.relation = data['relation']
        except:
            pass

        try:
            self.personal = data['personal']
        except:
            pass

        try:
            self.relatives = data['relatives']
        except:
            pass

        try:
            self.interests = self.InterestsSearch(acc_name)
        except:
            pass

        try:
            self.country = data['country']
            if self.country == []:
               self.country = ''
            self.country = self.country[0]['name']
        except:
            pass


    def gett(self):
        return [self.country, self.id, self.fname, self.lname, self.sex, self.birth_day, self.birth_month, self.birth_year, self.city,
                self.mobile_phone, self.home_phone, self.skype, self.instagram, self.status, self.career, self.military,
                self.education, self.relation, self.personal, self.interests, self.relatives]

    def InterestsSearch(self, acc_name):
        info_about_groups = acc_name.get__data_groups()
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
            'Животные': [0, 'cat', 'кошк', 'собак', 'кот']
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



    def search_city(self):
        pass





for x in range(1000):
    A = Vk_data('https://vk.com/frost_voltage', '', 1990, 1999)
    print(A.get__data_profile(), '\n')
    time.sleep(3)



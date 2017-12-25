
import time, math, requests
from Core.Modules.VK.VK import Vk_data

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
    twitter = 'twitter.com/'
    career = 'Места работы'
    education = 'Места учёбы'
    interests = 'Интересы'
    relatives = 'Родственные связи'
    likes = 'Понравившиеся посты'

    def __init__(self):
        pass

    def set_data(self, site, access):
            self.vk_data = Vk_data(site, access)
            data = self.vk_data.data_profile[0]
            self.id = data['uid']
            self.fname = data['first_name']
            self.lname = data['last_name']

            self.groups = self.vk_data.data_groups

            self.likes = 'Недавние лайки'

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
            if 'occupation' in data and self.education == 'Места учебы' and data['occupation']['type'] == ('school' or 'university'):

                self.education = data['occupation']['name']
            if 'relatives' in data:
                for i in data['relatives']:
                    self.relatives = ''
                    if i['type'] == 'parent':
                        self.relatives += 'Родитель: ' + i['name'] + '\n\n'
                    if i['type'] == 'sibling':
                        self.relatives += 'Брат/сестра: ' + i['name'] + '\n\n'
            else:
                self.relatives = 'Родственные связи'

            try:
                self.interests = self.interests_search()
            except:
                self.interests = 'Интересы'

            if 'country' in data:
                self.country = data['country']
                if self.country == []:
                   self.country = ''
            else:
                pass


    def interests_search(self):
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

            for g_info in info_about_groups[1:]:
                for interest in interests_dict:
                    for search_word in interests_dict[interest]:
                        try:
                            if search_word != interests_dict[interest][0] and (search_word in g_info['name'].lower()
                                                                               or search_word in g_info['status'].lower()
                                                                               or search_word in g_info['description'].lower()):
                                interests_dict[interest][0] += 1
                                full += 1
                                break

                        except KeyError:
                            try:
                                if search_word != interests_dict[interest][0] and search_word in g_info['description'].lower():
                                    interests_dict[interest][0] += 1
                                    full += 1
                                    break
                            except:
                                continue
            for i_keys in interests_dict.keys():
                percent = interests_dict[i_keys][0] * 100 / full
                if percent > 15:
                    interests_list += i_keys + ', '
            return interests_list.title()
        except:
            pass

    def get_likes(self, vk_api, token):
        try:
            count = 10
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

    def get_commonFriends(self, vk_api, token, id=-1234):
        try:
            if id == -1234:
                id = self.id
            common_friends = []
            names = []
            ids = []
            friend_ids = []
            result = []
            for friend in vk_api.friends.get(user_id=id, count=1000, fields='first_name,last_name,deactivated'):
                if not 'deactivated' in friend:
                    ids.append(friend['uid'])
                    names.append(friend['first_name'] + '\n' + friend['last_name'])

            for number in range(0, math.ceil(len(names)/100)):
                number *= 100
                friend_ids.append(ids[number:number+100])



            for group_ids in range(0, len(friend_ids)):
                text = 'https://api.vk.com/method/execute?access_token=' + token + '&code=return ['
                text += 'API.friends.getMutual({"source_uid":' + str(id) + ',"target_uids":' + str(friend_ids[group_ids])+ '}),'
                #result.append(vk_api.friends.getMutual(source_uid=self.id, target_uids=groups_ids[k]))
                text = text[0:-1] + '];'
                result.append(requests.post(text).json()['response'][0])

            counter=0
            for mass in result:
                for obj in mass:
                    common_friends.append([self.fname+'\n'+self.lname, names[counter],obj['common_count']])
                    counter += 1
            return [common_friends,ids]
        except:
            pass

    def getInfo_fromCountOfGroups(self, vk_api, count = 10):
        try:
            personal_card = []
            persons = []
            answer = []
            for friend in vk_api.friends.get(user_id=self.id, count=10000, fields='deactivated'):
                if not 'deactivated' in friend:
                    persons.append(friend['uid'])
            for group in vk_api.groups.get(user_id=self.id, count=count, extended=1)[1:]:
                personal_card.append([group['name'], group['gid'], 0])
            for number in range(0, count):
                answer.append([])
                for person_number in range(0, math.ceil(len(persons) / 500)):
                    person_number *= 500
                    time.sleep(1)
                    answ = vk_api.groups.isMember(group_id=personal_card[number][1], user_ids=
                        persons[person_number:person_number + 500])
                    answer[number] += answ

                for person_number in range(0, len(persons)):
                    if answer[number][person_number]['member']:
                        personal_card[number][2] += 1
            return personal_card
        except:
            pass

    def getInfo_fromGroups(self, vk_api, groups):
        try:
            personal_card = []
            persons = []
            for friend in vk_api.friends.get(user_id=self.id, count=10000, fields='deactivated'):
                if not 'deactivated' in friend:
                    persons.append(friend['uid'])

            groups_counter = 0
            for group in groups:
                personal_card.append([[], 0])
                if 'vk.com/' in group:
                    group = group.split('/')[-1]
                if 'club' in group:
                    group = group.replace('club', '')
                try:
                    personal_card[groups_counter][0] = vk_api.groups.getById(group_id=group)[0]['name']
                    for number in range(0, math.ceil(len(persons) / 500)):
                        number *= 500
                        time.sleep(1)
                        for l in vk_api.groups.isMember(group_id=group, user_ids=
                            persons[number:number + 500]):
                            if l['member'] == 1:
                                personal_card[groups_counter][1] += 1
                    groups_counter += 1

                except:
                    personal_card.pop()
            return personal_card
        except:
            pass


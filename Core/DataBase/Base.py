import sqlite3,os


class MySavedProfiles:
    db_path = '..\\Core\\DataBase\\DB.sqlite3'
    ProfileSaves = 'ProfileSaves'


    def __init__(self):
        #os.remove(self.db_path)
        self.conn = sqlite3.connect(self.db_path,check_same_thread=False)
        self.cursor = self.conn.cursor()
        #self.tableCreation()

        pass

    def tableCreation(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE "+ self.ProfileSaves+" ("
                          "id TEXT, "
                          "fname TEXT,"
                          " lname TEXT,"
                          " mname TEXT, "
                          "birth_day TEXT,"
                          " birth_month TEXT, "
                          "birth_year TEXT,"
                          "city TEXT,"
                          "country TEXT,"
                          "mobile_phone TEXT,"
                          "skype TEXT,"
                          "instagram TEXT,"
                          "facebook TEXT,"
                          "twitter TEXT,"
                          "career TEXT,"
                          "education TEXT,"
                          "interests TEXT,"
                          "relatives TEXT);")
        self.conn.commit()
        cursor.close()


    def addFrom(self,person):
        '''
        INSERT
        INTO
        db2mapper_table_config(`table_name`, `downloaded`, `table_columns`)
        VALUES('%s', % i, '%s')
        '''
        cursor = self.conn.cursor()
        values = (person.id,
                  person.fname,
                  person.lname,
                  person.mname,
                  person.birth_day,
                  person.birth_month,
                  person.birth_year,
                  person.city,
                  person.country,
                  person.mobile_phone,
                  person.skype,
                  person.instagram,
                  person.facebook,
                  person.twitter,
                  person.career,
                  person.education,
                  person.interests,
                  person.relatives)

        cursor.execute("INSERT INTO " + self.ProfileSaves+" VALUES (?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?,"
                                                                    "?"
                                                                    ")",
                                                                    values)
        self.conn.commit()

        cursor.close()


        pass

    def getFromTo(self, person, id):
        cursor = self.conn.cursor()
        for raw in self.conn.execute("SELECT * FROM " + self.ProfileSaves + " WHERE id=? LIMIT 1", (id,)):
            person.id = raw[0]
            person.fname = raw[1]
            person.lname= raw[2]
            person.mname = raw[3]
            person.birth_day = raw[4]
            person.birth_month = raw[5]
            person.birth_year = raw[6]
            person.city = raw[7]
            person.country = raw[8]
            person.mobile_phone = raw[9]
            person.skype = raw[10]
            person.instagram = raw[11]
            person.facebook = raw[12]
            person.twitter = raw[13]
            person.career = raw[14]
            person.education = raw[15]
            person.interests = raw[16]
            person.relatives = raw[17]
        cursor.close()


    def updateUserData(self,id,changeArr):

        cursor = self.conn.cursor()
        for i in changeArr.keys():
            self.conn.execute("UPDATE "+self.ProfileSaves+" SET " +str(i)+ " = '"+str(changeArr[i])+"' WHERE id = " + str(id) + ";")

        self.conn.commit()
        cursor.close()

        pass

    def findUser(self, id):
        cursor = self.conn.cursor()
        find = self.conn.execute("SELECT EXISTS(SELECT 1 FROM "+self.ProfileSaves+" WHERE id='"+str(id)+"')")
        cursor.close()
        return find.fetchone()[0]

    def findDiff(self, person):
        cursor = self.conn.cursor()
        difference = {}
        for raw in self.conn.execute("SELECT * FROM " + self.ProfileSaves + " WHERE id=? LIMIT 1", (person.id,)):
            if (raw[1] != person.fname):
                difference.update({'fname':person.fname})
            if (raw[2] != person.lname):
                difference.update({'lname': person.lname})
            if (raw[3] != person.mname):
                difference.update({'mname': person.mname})
            if (raw[4] != person.birth_day):
                difference.update({'birth_day': person.birth_day})
            if (raw[5] != person.birth_month):
                difference.update({'birth_month': person.birth_month})
            if (raw[6] != person.birth_year):
                difference.update({'birth_year': person.birth_year})
            if (raw[7] != person.city):
                difference.update({'city': person.city})
            if (raw[8] != person.country):
                difference.update({'country': person.country})
            if (raw[9] != person.mobile_phone):
                difference.update({'mobile_phone': person.mobile_phone})
            if (raw[10] != person.skype):
                difference.update({'skype': person.skype})
            if (raw[11] != person.instagram):
                difference.update({'instagram': person.instagram})
            if (raw[12] != person.facebook):
                difference.update({'facebook': person.facebook})
            if (raw[13] != person.twitter):
                difference.update({'twitter': person.twitter})
            if (raw[14] != person.career):
                difference.update({'career': person.career})
            if (raw[15] != person.education):
                difference.update({'education': person.education})
            if (raw[16] != person.interests):
                difference.update({'interests': person.interests})
            if (raw[17] != person.relatives):
                difference.update({'relatives': person.relatives})
        cursor.close()
        return difference



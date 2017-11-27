import sqlite3,os


class MySavedProfiles:
    db_path = 'Core\\DataBase\\DB.sqlite3'
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

    def getFromTo(self,id):
        result = {}
        cursor = self.conn.cursor()
        for raw in self.conn.execute("SELECT * FROM " + self.ProfileSaves + " WHERE id=? LIMIT 1", (id,)):
            result['id'] = raw[0]
            result['fname'] = raw[1]
            result['lname'] = raw[2]
            result['mname'] = raw[3]
            result['birth_day'] = raw[4]
            result['birth_month'] = raw[5]
            result['birth_year'] = raw[6]
            result['city'] = raw[7]
            result['country'] = raw[8]
            result['mobile_phone'] = raw[9]
            result['skype'] = raw[10]
            result['instagram'] = raw[11]
            result['facebook'] = raw[12]
            result['twitter'] = raw[13]
            result['career'] = raw[14]
            result['education'] = raw[15]
            result['interests'] = raw[16]
            result['relatives'] = raw[17]
        cursor.close()
        return result

    def updateUserData(self,id,changeArr):

        cursor = self.conn.cursor()
        for i in changeArr.keys():
            print("UPDATE "+self.ProfileSaves+" SET " +str(i)+ " = "+str(changeArr[i])+" WHERE id = '" + str(id) + "';")
            self.conn.execute("UPDATE "+self.ProfileSaves+" SET " +str(i)+ " = '"+str(changeArr[i])+"' WHERE id = " + str(id) + ";")

        self.conn.commit()
        cursor.close()

        pass




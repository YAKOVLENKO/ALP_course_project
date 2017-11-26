import sqlite3


class MySavedProfiles:
    db_path = ''
    ProfileSaves = 'ProfileSaves'


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.tableCreation()

        pass

    def tableCreation(self):
        self.conn.execute("CREATE TABLE"+ self.ProfileSaves+"("
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
                          "relatives TEXT)")


    def addFrom(self,person):
        '''
        INSERT
        INTO
        db2mapper_table_config(, , )
        VALUES('%s', % i, '%s')
        '''
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

        self.conn.execute("INSERT INTO" + self.ProfileSaves+"VALUES (?,"
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

        pass

    def getFromTo(self,id, person):
        data = self.conn.execute("SELECT * FROM" + self.ProfileSaves + "WHERE id=?", (id,))




    def updateUserData(self,str):
        pass



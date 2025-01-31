from flask import jsonify

from model.login import LoginDAO


class Login:
    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['lid'] = t[0]
            D['eid'] = t[1]
            D['username'] = t[2]
            D['password'] = t[3]
            result.append(D)

        return result

    def make_json_one(self, login):
        result = {}
        result['lid'] = login[0]
        result['eid'] = login[1]
        result['username'] = login[2]
        result['password'] = login[3]

        return result

    def make_json_login(self, login):
        result = {}
        result['lid'] = login[0]
        result['eid'] = login[1]
        result['username'] = login[2]
        result['password'] = login[3]
        result['position'] = login[4]

        return result

    def signUp(self, data):
        hid = data['hid']
        fname = data['fname']
        lname = data['lname']
        age = data['age']
        position = data['position']
        salary = data['salary']
        username = data['username']
        password = data['password']

        dao = LoginDAO()
        signup = dao.signUp(hid, fname, lname, age, position, salary, username, password)
        if not signup:
            return jsonify("Your username already exists, please try again"), 404
        else:
            result = self.make_json_login(signup)
            return result

    def getValidLogin(self, data):
        username = data['username']
        password = data['password']
        dao = LoginDAO()
        login = dao.getValidLogin(username, password)
        if not login:
            return jsonify("User Not Found - Try Sign Up"), 404
        else:
            result = self.make_json_login(login)
            return result

    def getAllLogins(self):
        model = LoginDAO()
        result = model.getAllLogins()
        answer = self.make_json(result)
        return answer

    def getLoginById(self, lid):
        dao = LoginDAO()
        login = dao.getLoginById(lid)
        if not login:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(login)
            return result

    def addLogIn(self, data):
        eid = data['eid']
        username = data['username']
        password = data['password']
        dao = LoginDAO()
        login = dao.addNewLogin(eid, username, password)
        if not login:
            return jsonify("Employee already has account"), 200
        else:
            result = self.make_json_one(login)
            return result

    def updateLogInById(self, lid, data):
        dao = LoginDAO()
        login = dao.updateLoginById(lid, data)

        if not login:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(login)
            return result

    def deleteLogInById(self, lid):
        dao = LoginDAO()
        login = dao.deleteLoginById(lid)
        if not login:
            return jsonify("Not Found"), 404
        else:
            result = "Successfully deleted login with ID " + str(login) + "!"
            return result
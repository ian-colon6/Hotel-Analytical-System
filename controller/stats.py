from flask import jsonify

from model.stats import StatsDAO
class Stats:

    def make_access_json(self, acc):
        result = {}
        result['access'] = acc[0]
        return result

    def make_revenue_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['chid'] = t[0]
            D['cname'] = t[1]
            D['revenue'] = t[2]
            result.append(D)
        return result

    def make_least_room_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['chid'] = t[0]
            D['cname'] = t[1]
            D['room_amount'] = t[2]
            result.append(D)
        return result

    def make_highest_paid_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['eid'] = t[0]
            D['hid'] = t[1]
            D['fname'] = t[2]
            D['lname'] = t[3]
            D['age'] = t[4]
            D['position'] = t[5]
            D['salary'] = t[6]
            result.append(D)

        return result

    def make_cap_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['hid'] = t[0]
            D['hname'] = t[1]
            D['hcity'] = t[2]
            D['total_cap'] = t[3]
            result.append(D)
        return result

    def make_res_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['hid'] = t[0]
            D['hname'] = t[1]
            D['hcity'] = t[2]
            D['reservation_count'] = t[3]
            D['percentile_rank'] = t[4]
            result.append(D)
        return result

    def make_discount_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['clid'] = t[0]
            D['fname'] = t[1]
            D['lname'] = t[2]
            D['memberyear'] = t[3]
            D['res_cost'] = t[4]
            D['discount'] = t[5]
            result.append(D)
        return result

    def make_least_reserve_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['rid'] = t[0]
            D['days_unavailable'] = t[1]
            result.append(D)
        return result

    def make_credit_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['clid'] = t[0]
            D['fname'] = t[1]
            D['lname'] = t[2]
            D['reservation_count'] = t[3]
            result.append(D)
        return result

    def make_handicaproom_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['rid'] = t[0]
            D['hid'] = t[1]
            D['rname'] = t[2]
            D['rtype'] = t[3]
            D['ishandicap'] = t[4]
            D['total_reservations'] = t[5]
            result.append(D)
        return result

    def make_room_type_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['rtype'] = t[0]
            D['reserved'] = t[1]
            result.append(D)
        return result



    def make_least_guests_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['rid'] = t[0]
            D['ratio'] = t[1]
            result.append(D)
        return result

    def make_payment_method_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['payment'] = t[0]
            D['total_reservations'] = t[1]
            D['percent'] = t[2]
            result.append(D)
        return result

    def make_profit_month_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['chid'] = t[0]
            D['reservation_month'] = t[1]
            D['total_reservation'] = t[2]
            result.append(D)
        return result

    def CheckGlobalAccess(self, eid):
        dao = StatsDAO()
        access = dao.CheckGlobalAccess(eid)
        return access

    def CheckLocalAccess(self, hid, eid):
        dao = StatsDAO()
        access = dao.CheckLocalAccess(hid, eid)
        return access


    def getTopRevenue(self):
        dao = StatsDAO()
        chain = dao.getTopRevenue()
        result = self.make_revenue_json(chain)
        return result

    def getLeastRooms(self):
        dao = StatsDAO()
        chain = dao.getLeastRooms()
        result = self.make_least_room_json(chain)
        return result


    def getHighestPaid(self, hid):
        dao = StatsDAO()
        employee = dao.getHighestPaid(hid)
        if not employee:
            return jsonify("Not Found"), 404
        else:
            result = self.make_highest_paid_json(employee)
            return result

    def getTopHotelCap(self):
        dao = StatsDAO()
        hotel = dao.getTopHotelCap()
        result = self.make_cap_json(hotel)
        return result

    def getTopHotelRes(self):
        dao = StatsDAO()
        hotel = dao.getTopHotelRes()
        result = self.make_res_json(hotel)
        return result

    def getTopCreditClient(self, hid):
        dao = StatsDAO()
        client = dao.getTopCreditClient(hid)
        result = self.make_credit_json(client)
        return result

    def getTopClientDiscount(self, hid):
        dao = StatsDAO()
        client = dao.getTopClientDiscount(hid)
        result = self.make_discount_json(client)
        return result

    def getTopHandicapRoom(self, hid):
        dao = StatsDAO()
        hotel = dao.getMostReservedHandicap(hid)
        result = self.make_handicaproom_json(hotel)
        return result

    def getLeastReserve(self, hid):
        dao = StatsDAO()
        ru = dao.getLeastReserve(hid)
        if not ru:
            return jsonify("Not Found"), 404
        else:
            result = self.make_least_reserve_json(ru)
            return result

    def getRoomType(self, hid):
        dao = StatsDAO()
        hotel = dao.getRoomType(hid)
        result = self.make_room_type_json(hotel)
        return result

    def getLeastGuests(self, hid):
        dao = StatsDAO()
        hotel = dao.getLeastGuests(hid)
        result = self.make_least_guests_json(hotel)
        return result

    def getProfitMonth(self):
        dao = StatsDAO()
        chain = dao.getProfitMonth()
        result = self.make_profit_month_json(chain)
        return result

    def getPaymentMethod(self):
        dao = StatsDAO()
        chain = dao.getPaymentMethod()
        result = self.make_payment_method_json(chain)
        return result
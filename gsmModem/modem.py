import huaweisms.api.user as user
import huaweisms.api.sms as sms
import huaweisms.api.ussd as ussd
from db import Connection
import logging
import jsonify

class Miamala:

    ctx = user.quick_login("admin", "admin")
    meseji = sms.get_sms(ctx,1,1,qty=10,unread_preferred=True)
    data = Connection()

    def save_miamala(self):
        """miamala ilio ingia kwenye account"""
        for ujumbe in self.meseji['response']['Messages']['Message']:
            if "HaloPesa" in ujumbe["Phone"]:
                muamala = ujumbe['Content'].split(' ')
                if "Transaction" and "received" in muamala:
                    try:
                        self.Transaction_id = muamala[2]
                        amount = muamala[muamala.index("received") + 1]
                        phone = muamala[muamala.index('number') + 1]
                        sender = muamala[muamala.index('from') + 1] + " " + muamala[muamala.index('from') + 2]
                        time = muamala[muamala.index('time') + 2]
                        date = muamala[muamala.index('time') + 1]
                        query = f"""INSERT INTO watu.miamla (transaction_id,amout,phone,sender,time,date)
                               values ({self.Transaction_id},{amount},{phone},{sender},{time},{date}) """
                    except Exception as e:
                        logging.INFO("Error in muamala")
                        pass
                    finally:
                        self.data.run_query(query)


    def watu_details(self):
        """get information of people"""
        query = "SELECT * FROM watu.people"
        watu = self.data.run_query(query)
        return jsonify(watu)


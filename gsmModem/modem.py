import huaweisms.api.user as user
import huaweisms.api.sms as sms
import huaweisms.api.ussd as ussd
import logging

ctx = user.quick_login("admin", "admin")
meseji = sms.get_sms(ctx,1,1,qty=10,unread_preferred=True)

if __name__ == "__main__":
    for ujumbe in meseji['response']['Messages']['Message']:
        if "HaloPesa" in ujumbe["Phone"]:
            muamala = ujumbe['Content'].split(' ')
            try:
                if "Transaction" and "received" in muamala:
                    Transaction_id = muamala[2]
                    amount = muamala[muamala.index("received") +1]
                    phone = muamala[muamala.index('number') + 1]
                    sender = muamala[muamala.index('from') + 1] + " " + muamala[muamala.index('from') + 2]
                    time = muamala[muamala.index('time')+2]
                    date = muamala[muamala.index('time')+1]
            except Exception as e:
                logging.INFO('error in transaction')
            finally:
                print(Transaction_id,amount,phone,sender,date,time)


    def check_payment(transaction_number):
        """check if a given transaction ID: exists"""
        try:
            if transaction_number == Transaction_id:
                """check if amount sent is equal to price tag"""
                pricetag = None
                if pricetag == amount:
                    sms.send_sms(ctx,dest=phone,msg=f"{sender} thanks for your donation :)")
                else:
                    sms.send_sms(ctx,dest=phone,msg="{sender} The amount you have sent is low")
            else:
                print("Please Enter the correct Transaction id")

        except Exception as e:
            pass



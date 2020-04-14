import huaweisms.api.user as user
import huaweisms.api.sms as sms
import huaweisms.api.ussd as ussd

ctx = user.quick_login("admin", "admin")
meseji = sms.get_sms(ctx,1,1,qty=10,unread_preferred=True)


for ujumbe in meseji['response']['Messages']['Message']:
    if "HaloPesa" in ujumbe["Phone"]:
        muamala = ujumbe['Content'].split('Transcation ID:')
        print(muamala)

if __name__ == '__main__':
    sms.send_sms(ctx,dest='0768090083',msg="hello this is test")
    ussd.send(ctx,msg='*150*88#')
    ussd.status(ctx)


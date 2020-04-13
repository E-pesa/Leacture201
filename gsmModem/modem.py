import huaweisms.api.user as user
import huaweisms.api.sms as sms

ctx = user.quick_login("admin", "admin")
meseji = sms.get_sms(ctx,1,1,qty=10,unread_preferred=True)


for ujumbe in meseji['response']['Messages']['Message']:
    if "HaloPesa" in ujumbe["Phone"]:
        muamala = ujumbe['Content'].split('Transaction')
        print(muamala)


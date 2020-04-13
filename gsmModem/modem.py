import huaweisms.api.user as user
import huaweisms.api.sms as sms

ctx = user.quick_login("admin","admin")
print(ctx)
if __name__ == "__main__":
    print(sms.get_sms(ctx,1,1,1,unread_preferred=True))
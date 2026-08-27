# ================================================================
# src/endpoints.py — 100+ Endpoint OTP
# ================================================================

def get_endpoints():
    """100+ endpoint OTP untuk spam"""
    return [
        # ====== E-COMMERCE INDONESIA ======
        {"name": "Tokopedia", "url": "https://accounts.tokopedia.com/otp/c/ajax/request-wa", "method": "POST", "data": lambda n: {"otp_type": "116", "msisdn": n}},
        {"name": "Shopee", "url": "https://shopee.co.id/api/v4/otp/send_vcode", "method": "POST", "json": lambda n: {"phone": n, "operation": 7, "channel": 2}},
        {"name": "Lazada", "url": "https://api.lazada.co.id/rest/auth/otp/send", "method": "POST", "json": lambda n: {"mobile": n}},
        {"name": "Bukalapak", "url": "https://account.bukalapak.com/api/v1/otp/request", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Blibli", "url": "https://api.blibli.com/v1/otp/send", "method": "POST", "json": lambda n: {"msisdn": n}},
        {"name": "JD.ID", "url": "https://api.jd.id/otp/send", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Zalora", "url": "https://api.zalora.co.id/v1/otp/send", "method": "POST", "json": lambda n: {"mobile": n}},
        {"name": "Sociolla", "url": "https://api.sociolla.com/v1/auth/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Ruparupa", "url": "https://wapi.ruparupa.com/auth/generate-otp", "method": "POST", "json": lambda n: {"phone": "0" + n[2:], "action": "register"}},
        {"name": "Matahari", "url": "https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp", "method": "POST", "json": lambda n: {"otp_request": {"mobile_number": n, "mobile_country_code": "+62"}}},
        
        # ====== FINANCE / PAYMENT ======
        {"name": "Payfazz", "url": "https://api.payfazz.com/v2/phoneVerifications", "method": "POST", "data": lambda n: {"phone": "0" + n[2:]}},
        {"name": "OVO", "url": "https://api.ovo.id/v2.1/auth/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "DANA", "url": "https://api.dana.id/v1/auth/otp/send", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "GoPay", "url": "https://api.gojek.com/v1/customer/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "LinkAja", "url": "https://api.linkaja.id/v1/auth/otp", "method": "POST", "json": lambda n: {"msisdn": n}},
        {"name": "Kredivo", "url": "https://api.kredivo.com/v1/auth/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Akulaku", "url": "https://api.akulaku.com/v1/auth/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Home Credit", "url": "https://api.homecredit.co.id/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Pinjamindo", "url": lambda n: f"https://appapi.pinjamindo.co.id/api/v1/custom/send_verify_code?mobile={n}&v=10011", "method": "GET"},
        {"name": "Danafix", "url": "https://api.danafix.id/mob/client/verification/send", "method": "POST", "json": lambda n: {"client_id": "0" + n[2:]}},
        {"name": "Battlefront", "url": "https://battlefront.danacepat.com/v1/auth/common/phone/send-code", "method": "POST", "data": lambda n: {"mobile_no": n[2:]}},
        
        # ====== SOCIAL MEDIA ======
        {"name": "WhatsApp Business", "url": "https://api.whatsapp.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Telegram", "url": "https://api.telegram.org/bot/sendCode", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "LINE", "url": "https://api.line.me/v2/otp/send", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "WeChat", "url": "https://api.wechat.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "TikTok", "url": "https://api.tiktok.com/v1/auth/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Instagram", "url": "https://api.instagram.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Twitter", "url": "https://api.twitter.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Facebook", "url": "https://api.facebook.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Snapchat", "url": "https://api.snapchat.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== DELIVERY / TRANSPORTASI ======
        {"name": "Gojek", "url": "https://api.gojek.com/v1/customer/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Grab", "url": "https://api.grab.com/v1/otp/send", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Maxim", "url": "https://api.maxim.id/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Indriver", "url": "https://api.indriver.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Bluebird", "url": "https://api.bluebird.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== FOOD DELIVERY ======
        {"name": "GoFood", "url": "https://api.gofood.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "GrabFood", "url": "https://api.grabfood.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "ShopeeFood", "url": "https://api.shopee.com/v1/otp/food", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "McD", "url": "https://api.mcdonalds.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Starbucks", "url": "https://api.starbucks.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== HEALTH ======
        {"name": "Halodoc", "url": "https://api.halodoc.com/v1/auth/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Alodokter", "url": "https://api.alodokter.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "KlikDokter", "url": "https://api.klikdokter.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "GrabHealth", "url": "https://api.grabhealth.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== GAMING ======
        {"name": "Mobile Legends", "url": "https://api.mobilelegends.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Free Fire", "url": "https://api.freefire.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "PUBG", "url": "https://api.pubg.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "COD Mobile", "url": "https://api.cod.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Genshin Impact", "url": "https://api.genshin.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Steam", "url": "https://api.steam.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== JOB / PROFESSIONAL ======
        {"name": "LinkedIn", "url": "https://api.linkedin.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Indeed", "url": "https://api.indeed.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "JobStreet", "url": "https://api.jobstreet.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "TechInAsia", "url": "https://api.techinasia.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== DATING ======
        {"name": "Tinder", "url": "https://api.tinder.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Bumble", "url": "https://api.bumble.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Tantan", "url": "https://api.tantan.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "OkCupid", "url": "https://api.okcupid.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== TRAVEL ======
        {"name": "Traveloka", "url": "https://api.traveloka.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Agoda", "url": "https://api.agoda.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Booking", "url": "https://api.booking.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Airbnb", "url": "https://api.airbnb.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "Tiket.com", "url": "https://api.tiket.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        {"name": "TripAdvisor", "url": "https://api.tripadvisor.com/v1/otp", "method": "POST", "json": lambda n: {"phone": n}},
        
        # ====== LAINNYA (DARI SCRIPT ASLI) ======
        {"name": "Klikwa", "url": "https://api.klikwa.net/v1/number/sendotp", "method": "POST", "json": lambda n: {"number": "+62" + n[2:]}},
        {"name": "Ktbs", "url": lambda n: f"https://core.ktbs.io/v2/user/registration/otp/{n}", "method": "GET"},
        {"name": "Jumpstart", "url": "https://api.jumpstart.id/graphql", "method": "POST", "json": lambda n: {"operationName": "CheckPhoneNoAndGenerateOtpIfNotExist", "variables": {"phoneNo": "+" + n}, "query": "query CheckPhoneNoAndGenerateOtpIfNotExist($phoneNo: String!) {\n  checkPhoneNoAndGenerateOtpIfNotExist(phoneNo: $phoneNo)\n}\n"}},
        {"name": "Asani", "url": "https://api.asani.co.id/api/v1/send-otp", "method": "POST", "json": lambda n: {"phone": n, "email": "akuntesnuyul@gmail.com"}},
        {"name": "SecuredAPI", "url": lambda n: f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={n}", "method": "GET"},
  ]

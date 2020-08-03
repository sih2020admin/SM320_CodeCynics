#Basic
from flask import Flask , render_template,url_for,request,jsonify,redirect,json
from datetime import datetime,date,timedelta
#API
from flask_cors import CORS
from bson import ObjectId
from flask_pymongo import PyMongo
import ast
#ML
import joblib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app=Flask(__name__)

app.config["MONGO_DBNAME"]="try2db"
app.config["MONGO_URI"]="mongodb://127.0.0.1:27017/try2db"

mongo=PyMongo(app)
CORS(app)
db= mongo.db.try2db

#Containers
cont=joblib.load('pkl/cont/Container.pkl')
car=joblib.load('pkl/cont/Car.pkl')
#Dry
bauxite=joblib.load('pkl/dry/Bauxite_In_Bulk.pkl')
black=joblib.load('pkl/dry/Black_Matpe.pkl')
coking=joblib.load('pkl/dry/Coking_Coal.pkl')
crimson=joblib.load('pkl/dry/Crimson_Lentils.pkl')
fly=joblib.load('pkl/dry/Fly_Ash_In_Jumbo_Bags.pkl')
industrial=joblib.load('pkl/dry/Industrial_Salt.pkl')
iol=joblib.load('pkl/dry/Iron_Ore_Lumps.pkl')
iop=joblib.load('pkl/dry/Iron_Ore_Pellets.pkl')
murite=joblib.load('pkl/dry/Murite_Of_Potash.pkl')
nitro=joblib.load('pkl/dry/Nitro_Phosphate_With_Potash.pkl')
pet=joblib.load('pkl/dry/Pet_Coal.pkl')
silica=joblib.load('pkl/dry/Silica_Sand.pkl')
soda=joblib.load('pkl/dry/Soda_Ash.pkl')
steam=joblib.load('pkl/dry/Steam_Coal.pkl')
steel_pipes=joblib.load('pkl/dry/Steel_Pipes.pkl')
steel_rails=joblib.load('pkl/dry/Steel_Rails.pkl')
stone=joblib.load('pkl/dry/Stone_Stone_Chips.pkl')
urea=joblib.load('pkl/dry/Urea.pkl')
#Liquid
acetic=joblib.load('pkl/liq/Acetic_Acid.pkl')
hexadecene=joblib.load('pkl/liq/Alpha_Plus_1_Hexadecene.pkl')
tetradecene=joblib.load('pkl/liq/Alpha_Plus_1_Tetradecene.pkl')
c2024=joblib.load('pkl/liq/Alpha_Plus_C2024.pkl')
dodecene=joblib.load('pkl/liq/Alpha_Plus_Rna_01_Dodecene_C12H14.pkl')
bitumen=joblib.load('pkl/liq/Bitumen.pkl')
carbon_black=joblib.load('pkl/liq/Carbon_Black_Feed_Stock.pkl')
#palm_kernel=joblib.load('pkl/liq/Crude_Palm_Kernel_Oil.pkl')
palm=joblib.load('pkl/liq/Crude_Palm_Oil.pkl')
petroleum=joblib.load('pkl/liq/Crude_Petroleum_Oil.pkl')
soyabean=joblib.load('pkl/liq/Crude_Soyabean_Oil.pkl')
sunflower=joblib.load('pkl/liq/Crude_Sunflower_Oil.pkl')
dea=joblib.load('pkl/liq/Denatured_Ethyl_Alcohol.pkl')
diethylene_glycol=joblib.load('pkl/liq/Diethylene_Glycol.pkl')
gas_oil_hsd=joblib.load('pkl/liq/Gas_Oil_Hsd.pkl')
heavy_white_oil=joblib.load('pkl/liq/Heavy_White_Oil.pkl')
hsd=joblib.load('pkl/liq/High_Speed_Diesel.pkl')
butane=joblib.load('pkl/liq/Lpg_Butane.pkl')
propane=joblib.load('pkl/liq/Lpg_Propane.pkl')
methanol=joblib.load('pkl/liq/Methanol.pkl')
methyl_tert_butyl_ether=joblib.load('pkl/liq/Methyl_Tertiary_Butyl_Ether.pkl')
motor=joblib.load('pkl/liq/Motor_Spirit.pkl')
naphtha=joblib.load('pkl/liq/Naphtha.pkl')
olefins=joblib.load('pkl/liq/Olefins_c13_All_Isomers_Alpha_Plus_c2428.pkl')
rbd=joblib.load('pkl/liq/RBD_Palm_Stearin.pkl')
split_rbd=joblib.load('pkl/liq/Split_RBD_Palm_Stearin_Fatty_Acid.pkl')


switcher={
    "Containers":cont ,
    "CAR":car,
    "BAUXITE IN BULK":bauxite,
    "BLACK MATPE":black,
    "COKING COAL":coking,
	"CRIMSON LENTILS":crimson,
	"FLY ASH IN JUMBO BAGS":fly,
	"INDUSTRIAL SALT":industrial,
    "IRON ORE LUMPS":iol,
    "IRON ORE PELLETS":iop,  
    "MURITE OF POTASH":murite,
    "NITRO PHOSPHATE WITH POTASH":nitro, 
    "PET COKE":pet,
	"SILICA SAND":silica, 
	"SODA ASH":soda,
	"STEAM COAL":steam,
	"STEEL PIPES":steel_pipes,
	"STEEL RAILS":steel_rails,
	"STONE / STONE CHIPS":stone,
	"UREA":urea,
	"ACETIC ACID":acetic,
	"ALPHAPLUS 1 HEXADECENE":hexadecene,
	"ALPHAPLUS 1-TETRADECENE": tetradecene,
	"ALPHAPLUS C-20/24":c2024,
	"ALPHAPLUS(R) NAO 1 - DODECENE (C12H24)":dodecene,
    "BITUMEN":bitumen,
	"CARBON BLACK FEED STOCK":carbon_black,
	#"CRUDE PALM KERNEL OIL":palm_kernel,
	"CRUDE PALM OIL":palm,
    "CRUDE PETROLEUM OIL":petroleum,
	"CRUDE SOYABEAL OIL" :soyabean,
    "CRUDE SUNFLOWER OIL":sunflower,
	"DENATURED ETHYL ALCOHOL":dea,
	"DIETHYLENE GLYCOL":diethylene_glycol,
	"GAS OIL (HSD)":gas_oil_hsd,
	"HEAVY WHITE OIL":heavy_white_oil,
	"HIGH SPEED DIESEL":hsd,
	"LPG BUTANE" :butane,
	"LPG PROPANE":propane,
	"METANOL":methanol,
	"METHYL TERTIARY BUTYL ETHER":methyl_tert_butyl_ether,
	"MOTOR SPIRIT":motor,
	"NAPHTHA":naphtha,
	"OLEFINS(C13+ALL ISOMERS)ALPHAPLUS (R)C24-28":olefins,
	"RBD PALM STEARIN":rbd,
	"SPLIT RBD PALM STEARIN FATTY ACID":split_rbd }

rate={
    "Containers":260 ,
    "CAR":260,
    "BAUXITE IN BULK":34,
    "BLACK MATPE":59,
    "COKING COAL":90,
	"CRIMSON LENTILS":59,
	"FLY ASH IN JUMBO BAGS":59,
	"INDUSTRIAL SALT":29,
    "IRON ORE LUMPS":34,
    "IRON ORE PELLETS":34,  
    "MURITE OF POTASH":59,
    "NITRO PHOSPHATE WITH POTASH":59, 
    "PET COKE":49,
	"SILICA SAND":49, 
	"SODA ASH":29,
	"STEAM COAL":60,
	"STEEL PIPES":39,
	"STEEL RAILS":39,
	"STONE / STONE CHIPS":49,
	"UREA":59,
	"ACETIC ACID":75,
	"ALPHAPLUS 1 HEXADECENE":75,
	"ALPHAPLUS 1-TETRADECENE": 75,
	"ALPHAPLUS C-20/24":75,
	"ALPHAPLUS(R) NAO 1 - DODECENE (C12H24)":75,
    "BITUMEN":75,
	"CARBON BLACK FEED STOCK":75,
	#"CRUDE PALM KERNEL OIL":palm_kernel,
	"CRUDE PALM OIL":56,
    "CRUDE PETROLEUM OIL":104,
	"CRUDE SOYABEAL OIL" :56,
    "CRUDE SUNFLOWER OIL":56,
	"DENATURED ETHYL ALCOHOL":104,
	"DIETHYLENE GLYCOL":75,
	"GAS OIL (HSD)":104,
	"HEAVY WHITE OIL":104,
	"HIGH SPEED DIESEL":104,
	"LPG BUTANE" :350,
	"LPG PROPANE":350,
	"METANOL":104,
	"METHYL TERTIARY BUTYL ETHER":59,
	"MOTOR SPIRIT":104,
	"NAPHTHA":104,
	"OLEFINS(C13+ALL ISOMERS)ALPHAPLUS (R)C24-28":104,
	"RBD PALM STEARIN":56,
	"SPLIT RBD PALM STEARIN FATTY ACID":56 }

        
current_time = datetime.now()
@app.template_filter("jsonit")
def jsonit(s):
    return json.loads(s)





@app.route('/berth',methods=['POST','GET'])
def berth():
    return render_template('berth_res.html')

@app.route('/',methods=['POST','GET'])
def dashboard():
    if request.method=="POST":
        return 'Success'
    
    else:
        max_prod=1000000
        current=[]
        expected=[]
        upcoming=[]
        instances=[]
        current_revenue=[]
        current_weight=[]
        percent_revenue=[]
        percent_weight=[]
        percent_ratios=[]
        final_ratio=[]
        productivity=[]
        time_dist=[]
        diff=[]

        new_productivity=[]
        for i in db.find():
            tepm=json.loads(i['data']['details'])
            temp_time=datetime.strptime(tepm['eta'],'%Y-%m-%dT%H:%M')
            if('status' in i):
                current.append(i)
            elif((temp_time-current_time).total_seconds()<=86400):
                expected.append(i)
            
            else:
                upcoming.append(i)
            #instances.append()
        for i in current:
            current_revenue.append(json.loads(i["data"]["details"])["revenue"])
            current_weight.append(sum(list(map(lambda x:float(x), json.loads(i["data"]["details"])['Weight']))))
        total_revenue=sum(current_revenue)
        total_weight=sum(current_weight)
        for i in range(len(current_revenue)):
            percent_revenue.append((current_revenue[i])/total_revenue)
            percent_weight.append((current_weight[i])/total_weight)
            percent_ratios.append(percent_revenue[i]/percent_weight[i])
        percent_ratios_sum=sum(percent_ratios)
        for i in range(len(current_revenue)):
            final_ratio.append(percent_ratios[i]/percent_ratios_sum)
            productivity.append(final_ratio[i]*max_prod)
            time_dist.append(current_weight[i]/productivity[i])
        
        if len(expected)>0:
            min_time=time_dist.index(min(time_dist))
            # time_dist2=time_dist.copy()
            # time_dist2.pop(min_time)
            # current[min_time]
            for i in range(len(productivity)):
                if i==min_time:
                    pass 
                else:
                    com_no=json.loads(current[i]["data"]["details"])["Count"]-1
                    for j in range(com_no):
                        com_prod=[]
                        com_prod.append(switcher[json.loads(current[i]["data"]['details'])["Commodities"][j]].predict([[float(json.loads(current[i]["data"]['details'])["Weight"][j])]])[0])
                    com_prod_sum=sum(com_prod)
                    # new_productivity[i]= com_prod_sum if com_prod_sum<productivity[i] else productivity[i]
                    if(com_prod_sum<productivity[i]):
                        diff.append(productivity[i]-com_prod_sum)
                        new_productivity.insert(i,com_prod_sum)
                    else:
                        new_productivity.insert(i,productivity[i])
            new_productivity.insert(min_time, productivity[min_time]+sum(diff))
        final_productivity=new_productivity if len(new_productivity)>0 else productivity


        return render_template('dashboard.html',final_productivity=final_productivity,current=current,expected=expected,upcoming=upcoming,instances=instances)


@app.route('/check',methods=['POST','GET'])
def check():
    if request.method=='POST':
        types=request.form['type']
        count=float(request.form['count'])
        commodities=request.form['com'].replace(']','').replace('[','').replace('"','').split(",")
        eta=request.form['eta']
        weight=request.form['w'].replace(']','').replace('[','').replace('"','').split(",")
        coeff=24/(count-1)
        data=[]
        price=0
        time=0
        for i in range(len(commodities)):
            prod=switcher[commodities[i]].predict([[float(weight[i])]])[0]
            time=time+(coeff*(float(weight[i])/prod))
            price=price+(rate[commodities[i]]*float(weight[i]))
            data.append(prod)
        tat=datetime.strftime(datetime.strptime(eta,'%Y-%m-%dT%H:%M')+timedelta(hours=time) ,'%Y-%m-%dT%H:%M')
        return jsonify({
        'prod':data,
        'time':time,
        'tat':tat,
        'Name': types,
        "Count":count,
        "Commodities":commodities,
        "Weight":weight,
        "eta":eta,
        'revenue':price
        })
    
@app.route('/change',methods=['POST'])
def change():
    if request.method=='POST':
        eta=request.form['eta']
        end=request.form['end']
        endtime=datetime.strptime(end,'%Y-%m-%dT%H:%M')
        etatime=datetime.strptime(eta,'%Y-%m-%dT%H:%M')
        #final=endtime-etatime
        return jsonify({
             'time':endtime,
             'eta':etatime,
             #'final':final
        })

      

@app.route('/save',methods=['POST'])
def saveinfo():
    if request.method=="POST":
        all_data=request.form.copy()
        db.insert_one({
            "data":all_data
        })
        return jsonify({
            "status":"Success"
        })


@app.route('/current',methods=['POST','GET','PUT','DELETE'])
def current():
        id=request.form['id']
        db.update_one({
            "_id":ObjectId(id)
        },
        {"$set":{
         "status":'current',
         "berth":request.form['berth'],
         "ActualTime":current_time
        }
        })
        return jsonify({"status":'Success'})

@app.route('/remove',methods=['POST'])
def remove():
    id=request.form['id']
    db.delete_one({
        "_id":ObjectId(id)
    })
    return jsonify({"Message":"removed!"})


@app.route('/info',methods=['GET','POST'])
def info():
    if request.method=='POST':
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        vesselname = request.form['name']
        vesselname = vesselname.upper()
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.vesselfinder.com/vessels")

        search = driver.find_element_by_id("advsearch-name")
        search.clear()
        search.send_keys(vesselname)
        search.send_keys(Keys.RETURN)

        try:
            resultslist = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, vesselname))
            )
            resultslist.click()

            information1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text2"))
            )
            information2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text1"))
            )

            info1=information1.text
            info2=information2.text
            info=info1+"\n"+info2
        finally:
            driver.quit()        
        return jsonify({
            "info":info
        })    






if __name__ == '__main__':
    app.run(debug=True)
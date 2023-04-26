#Import necessary libraries
import sqlite3
#import pyttsx3
#global e
details = ""
#e=pyttsx3.init() #for text to speach 
#e.setProperty("rate",130)
from flask import Flask, render_template, request
#import pickle
import numpy as np
import os


#database connection
con = sqlite3.connect("user.db")
print("database connected successfully")


# for ml model loading & predicting
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


# set model file path
#model_diabetes = pickle.load(open("model.pkl","rb"))

filepath = 'tea_model.hdf5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

#method for predict the result
global result
def diceas_predict(diceas_image):
  test_image = load_img(diceas_image, target_size = (180, 180)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)#/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  global result
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', max(result))
  
  pred = np.argmax(result, axis=1)
  print(pred[0])
  if pred==0:
      details1 = "The treatment for algal spot on tea leaves involves a combination of cultural practices and chemical controls"
      details2 = "Cultural Practices: Good plant hygiene is essential to control algal spot disease. It is important to maintain proper spacing between the tea bushes and provide adequate air circulation to reduce humidity levels. Prune the infected leaves and remove them from the plant to prevent further spread of the disease"
      details3 = "Fungicide Sprays: A preventive fungicide spray is usually recommended to control the disease. Copper-based fungicides are commonly used to control algal spot on tea leaves. Fungicides should be applied before the appearance of the disease symptoms or at the early stages of the disease. Fungicide application should be done in accordance with the manufacturer's instructions"
      details4 = "Organic Control: There are a few organic methods to control the disease. Baking soda and neem oil are organic fungicides that can be used to control algal spot. Mix a tablespoon of baking soda and a tablespoon of neem oil in a gallon of water, and spray it on the tea bushes"
      details5 = "Regular Monitoring: Regular monitoring of the tea bushes is essential to identify the disease at an early stage. The earlier the disease is detected, the easier it is to control it. Inspect the leaves and shoots regularly for signs of the disease and take prompt action when you detect any symptoms."
      details6 = "It is important to note that the best method to prevent algal spot is to maintain good plant hygiene and environmental conditions. By adopting a preventive approach and regular monitoring, you can keep your tea bushes healthy and free from algal spot"
      etc = "Algal spot is a common disease in tea plants caused by the fungus Cephaleuros virescens. It typically appears as small, greenish-brown spots on the leaves of tea plants, and can eventually cause the leaves to turn yellow and drop prematurely, reducing the yield and quality of the tea. "
      return "algal_spot", 'result.html',details1,details2,details3,details4,details5,details6,etc
       
  elif pred==1:
      details1 = "Brown blight is a fungal disease that affects tea leaves and can cause significant damage to tea plantations."
      details2 = "Fungicide Application: Fungicides can be used to control brown blight on tea leaves. A copper-based fungicide or a fungicide containing mancozeb can be effective in controlling the disease. Fungicides should be applied as per the manufacturer's instructions, and the application should be timed to coincide with the early stages of the disease. Repeat applications may be necessary depending on the severity of the disease."
      details3 = "Pruning: Infected leaves and shoots should be pruned to prevent the spread of the disease. Pruning should be done carefully, and the infected material should be disposed of properly to avoid spreading the disease to other parts of the plantation."
      details4 = "Cultural Practices: Good plant hygiene is essential to control brown blight disease. It is important to maintain proper spacing between the tea bushes and provide adequate air circulation to reduce humidity levels. Regular removal of weeds and debris from the plantation can also help to control the disease"
      details5 = "Soil Management: The fungus that causes brown blight can survive in the soil, so soil management is important to prevent the disease from recurring. Proper soil drainage, regular aeration, and soil amendment can help to keep the soil healthy and prevent the disease from reoccurring."
      details6 = "Organic Control: Some organic methods can be used to control brown blight. Garlic extract, neem oil, and baking soda are effective organic fungicides that can be used to control the disease. Mix one tablespoon of garlic extract or neem oil or baking soda in a gallon of water and spray it on the tea bushes."+"\n\nIt is important to note that prevention is the best way to control brown blight. Adopting good plant hygiene, regular monitoring, and prompt treatment can help to keep the disease under control and prevent significant damage to the tea plantation."+"\n"
      etc = "Brown blight is a fungal disease that affects tea plants, caused by the fungus Exobasidium vexans. It typically appears as brown or red circular patches on the leaves and can cause defoliation, reducing the yield and quality of tea. "
      return "brown_blight", 'result.html',details1,details2,details3,details4,details5,details6,etc
        
  elif pred==2:
      details1 = "Gray blight is a fungal disease that affects tea leaves and can cause significant damage to tea plantations."
      details2 = "Fungicide Application: Fungicides can be used to control gray blight on tea leaves. A copper-based fungicide or a fungicide containing mancozeb can be effective in controlling the disease. Fungicides should be applied as per the manufacturer's instructions, and the application should be timed to coincide with the early stages of the disease. Repeat applications may be necessary depending on the severity of the disease."
      details3 = "Pruning: Infected leaves and shoots should be pruned to prevent the spread of the disease. Pruning should be done carefully, and the infected material should be disposed of properly to avoid spreading the disease to other parts of the plantation."
      details4 = "Cultural Practices: Good plant hygiene is essential to control gray blight disease. It is important to maintain proper spacing between the tea bushes and provide adequate air circulation to reduce humidity levels. Regular removal of weeds and debris from the plantation can also help to control the disease."
      details5 = "Soil Management: The fungus that causes gray blight can survive in the soil, so soil management is important to prevent the disease from recurring. Proper soil drainage, regular aeration, and soil amendment can help to keep the soil healthy and prevent the disease from reoccurring."
      details6 = "Organic Control: Some organic methods can be used to control gray blight. Garlic extract, neem oil, and baking soda are effective organic fungicides that can be used to control the disease. Mix one tablespoon of garlic extract or neem oil or baking soda in a gallon of water and spray it on the tea bushes."+"\n"
      etc = "Gray blight is a fungal disease that affects tea plants, caused by the fungus Pestalotiopsis theae. It typically appears as grayish spots on the leaves and can cause defoliation, reducing the yield and quality of tea. "
      return "gray_blight", 'result.html',details1,details2,details3,details4,details5,details6,etc
        
  elif pred==3:
      details1 = "\nits healthy leaf"
      details2=details3=details4=details5=details6=""
      return "healthy", 'result.html',details1,details2,details3,details4,details5,details6
       
  elif pred==4:
      details1 = "Helopeltis is a common pest that affects tea plants, and it can cause significant damage to the leaves and shoots."
      details2 = "Insecticide Application: Insecticides can be used to control helopeltis infestation on tea leaves. A variety of insecticides are available, including synthetic and organic options. It is important to choose an insecticide that is effective against helopeltis and is safe for the tea bushes. Follow the manufacturer's instructions for application rates and timing."
      details3 = "Pruning: Infested leaves and shoots should be pruned to prevent the spread of the pest. Pruning should be done carefully, and the infected material should be disposed of properly to avoid spreading the pest to other parts of the plantation."
      details4 = "Good plant hygiene is essential to control helopeltis infestation. It is important to maintain proper spacing between the tea bushes and provide adequate air circulation to reduce humidity levels. Regular removal of weeds and debris from the plantation can also help to control the pest"
      details5 = "Beneficial Insects: Some beneficial insects, such as ladybugs and lacewings, can help to control helopeltis infestation. These insects can be introduced to the plantation to feed on the helopeltis and reduce their population."
      details6 = "Traps: Sticky traps can be used to trap and kill adult helopeltis. These traps can be placed in strategic locations on the plantation to attract and capture the pest."+"\n\nIt is important to note that prevention is the best way to control helopeltis infestation. Adopting good plant hygiene, regular monitoring, and prompt treatment can help to keep the pest under control and prevent significant damage to the tea plantation."+"\n"
      etc = "Helopeltis is a genus of insect pests that can cause damage to tea plants. The most common species is Helopeltis theivora, also known as the tea mosquito bug. It feeds on the tender shoots and young leaves of tea plants, causing a reduction in yield and quality of the tea."
      return "helopeltis", 'result.html',details1,details2,details3,details4,details5,details6,etc
        
  elif pred==5:
      details1 = "Red spot is a fungal disease that affects tea leaves and can cause significant damage to tea plantations."
      details2 = "Fungicide Application: Fungicides can be used to control red spot on tea leaves. A copper-based fungicide or a fungicide containing mancozeb can be effective in controlling the disease. Fungicides should be applied as per the manufacturer's instructions, and the application should be timed to coincide with the early stages of the disease. Repeat applications may be necessary depending on the severity of the disease."
      details3 = "Pruning: Infected leaves and shoots should be pruned to prevent the spread of the disease. Pruning should be done carefully, and the infected material should be disposed of properly to avoid spreading the disease to other parts of the plantation."
      details4 = "Good plant hygiene is essential to control red spot disease. It is important to maintain proper spacing between the tea bushes and provide adequate air circulation to reduce humidity levels. Regular removal of weeds and debris from the plantation can also help to control the disease."
      details5 = "Soil Management: The fungus that causes red spot can survive in the soil, so soil management is important to prevent the disease from recurring. Proper soil drainage, regular aeration, and soil amendment can help to keep the soil healthy and prevent the disease from reoccurring."
      details6 = "Organic Control: Some organic methods can be used to control red spot. Garlic extract, neem oil, and baking soda are effective organic fungicides that can be used to control the disease. Mix one tablespoon of garlic extract or neem oil or baking soda in a gallon of water and spray it on the tea bushes."+"\n\nIt is important to note that prevention is the best way to control red spot. Adopting good plant hygiene, regular monitoring, and prompt treatment can help to keep the disease under control and prevent significant damage to the tea plantation."+"\n"
      etc = "Red spot is a fungal disease that affects tea plants, caused by the fungus Mycena citricolor. It typically appears as small, reddish-brown spots on the leaves and can cause defoliation, reducing the yield and quality of tea"
      return "red_spot", 'result.html',details1,details2,details3,details4,details5,details6,etc
        



# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/index", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
#this method for login page
@app.route("/loginpage", methods = ['GET','POST'])
def loginpage():
     return render_template('login.html')

# this method for registration page
@app.route("/registerpage", methods = ['GET','POST'])
def registerpage():
     return render_template('register.html')    

#this method for landing page
@app.route("/", methods = ['GET','POST'])
def landingpage():
     return render_template('landingpage.html')

@app.route("/diabetes", methods = ['GET','POST'])
def diabetes():
    return render_template('diabetes.html')

  

# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
       # get the file from user 
        file = request.files['image'] # get input values from form inputs using there name attribute
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        # store the image  on server
        file_path = os.path.join('static/', filename)
        file.save(file_path)
        print(file_path)

        print("@@ Predicting class......")
        pred, output_page,details1,details2,details3,details4,details5,details6,etc = diceas_predict(diceas_image=file_path)
        #e.say(pred+"predicted and the accuracy is "+str(max(result[0])))
        #e.runAndWait()   
        return render_template(output_page,etcc=etc,doctor1=details1,doctor2=details2,doctor3=details3,doctor4=details4,doctor5=details5,doctor6=details6, pred_output = pred, user_image = file_path,pred_output_ac=max(result[0]))

# method for get the user login details from the login form
@app.route("/login", methods = ['GET','POST'])
def login():
     count = 0
     if request.method == 'POST':
       # get the user name from login form 
        name = request.form.get('name') # get input values from form inputs using there name attribute
        password = request.form.get('pass')
        cursor = con.execute("select * from user where name = '"+name+"' and password='"+password+"'")
        if name=="admin" and password=="admin":
           res = con.execute("select * from user")
           resli = []
           for r in res:
               resli.append(r)

           res = con.execute("select * from contact")
           res_c = []
           for r in res:
               res_c.append(r)   
           return render_template("admin.html",results=resli,results_c=res_c)
        for row in cursor:
          count = count + 1
        if count>0:
          print("login successfully")
          #e.say("login successfully")
          #e.runAndWait()
          return render_template("index.html")
        else:
          print("please register with our app !")
          #e.say("please register with our app !")
          #e.runAndWait()
          return render_template("login.html",message="incorrect password or username. try to sing up")
        print("@@ Input posted = ",name)      

# method for get the user register details from the register form
@app.route("/register", methods = ['GET','POST'])
def register():
     count = 0
     if request.method == 'POST':
       # get the user name from login form 
        name = request.form.get('username') # get input values from form inputs using there name attribute
        password = request.form.get('password')
        email = request.form.get('email')
        nic = request.form.get('nic')
        dob = request.form.get('dob')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        con.execute("insert into user values('"+name+"','"+password+"','"+email+"','"
                    +nic+"','"+dob+"','"+phonenumber+"','"+address+"')")
        con.commit()
        #e.say("hi "+name+" thank you for register with us !")
        #e.runAndWait()
        return render_template("index.html")


@app.route("/contact", methods = ['GET','POST'])
def successd():
     #return render_template("success.html")
     count = 0
     if request.method == 'POST':
       # get the user name from login form 
        name = request.form.get('firstname') # get input values from form inputs using there name attribute
        email = request.form.get('email')
        mess = request.form.get('subject')

        con.execute("insert into contact values('"+name+"','"+email+"','"+mess+"')")
        con.commit()
        #e.say("hi "+name+" thank you for register with us !")
        #e.runAndWait()
        return render_template("success.html")


@app.route("/diabetes_predict", methods = ['GET','POST'])
def diabetes_predict():
     count = 0
     if request.method == 'POST':
       # get the user name from login form 
        Pregnancies = request.form.get('Pregnancies') # get input values from form inputs using there name attribute
        Glucose = request.form.get('Glucose')
        BloodPressure = request.form.get('BloodPressure')
        SkinThickness = request.form.get('SkinThickness')
        Insulin = request.form.get('Insulin')
        BMI = request.form.get('BMI')
        DiabetesPedigreeFunction = request.form.get('DiabetesPedigreeFunction')
        Age = request.form.get('Age')
        pred = model_diabetes.predict([[int(Pregnancies),int(Glucose),int(BloodPressure),int(SkinThickness)
                                        ,int(Insulin),float(BMI),float(DiabetesPedigreeFunction)
                                        ,int(Age)]])
        print(pred)
        if pred<0.5:
          text = "congratulation you don't have diabetes"
          #e.say("congratulation you don't have diabetes")
          #e.runAndWait()
        else:
          text = "you have diabetes .. !"
          #e.say("you have diabetes ")
          #e.runAndWait()
        return render_template("diabetes_result.html",result=text)

      
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=1001) 
    
    

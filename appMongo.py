########################## FOR MONGODB CODE############################
from flask import Flask
from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin
import json
from bson import json_util
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os,sys



app = Flask(__name__)
CORS(app)     #, resources={r"/boeing/*": {"origins": "http://localhost:5000"}}

app.config['CORS_HEADERS'] = 'application/json'
app.config['MONGO_DBNAME'] = 'supplier_collection'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/supplier_collection'

mongo = PyMongo(app)

######################## Get All User###################################
@app.route('/boeing/suppliers',methods=['GET'])
@cross_origin(origin='*')
def getAllSuppliers():
    try:
        user = mongo.db.supplier_info
        output = []
        for supplier in user.find():
            user_details = {
                # 'id' : u.ObjectId('_id'),
                'supplier_name' :supplier['supplier_name'],
				'assessment_type' :supplier['assessment_type'],
                'assessment_date' :supplier['assessment_date'],
                'certifications' :supplier['certifications'],
                'capabilities' :supplier['capabilities'],
                'strength' :supplier['strength'],
                'risk' :supplier['risk']
            }
            output.append(user_details)
        return jsonify({'Users':output,'StatusCode':'200'})
    except Exception, e:
		return str(e)    

######################## Find One User##############################
@app.route('/boeing/supplier/<string:name>', methods=['GET'])
def getByName(name):
    try:
        user = mongo.db.supplier_info
        output = []
        data = user.find({'supplier_name' : name})
        for supplier in data:
            if supplier > 0: 
                user_details = {
                    'supplier_name' :supplier['supplier_name'],
                    'assessment_type' :supplier['assessment_type'],
                    'assessment_date' :supplier['assessment_date'],
                    'certifications' :supplier['certifications'],
                    'capabilities' :supplier['capabilities'],
                    'strength' :supplier['strength'],
                    'risk' :supplier['risk']
                }
                output.append(user_details)
            else:
                output = "No Data Found"
            
        return jsonify({'StatusCode':'200','User':output})
    except Exception, e:
		return str(e) 


######################## Find By Id ##############################
@app.route('/boeing/supplierId/<string:id>', methods=['GET'])
def getById(id):
    try:
        user = mongo.db.supplier_info
        output = []
        data = user.find({'_id' : ObjectId(id)})
        for supplier in data:
            if supplier == 0:
                output = "No Data Found" 
            else:
                user_details = {
                    'supplier_name' :supplier['supplier_name'],
                    'assessment_type' :supplier['assessment_type'],
                    'assessment_date' :supplier['assessment_date'],
                    'certifications' :supplier['certifications'],
                    'capabilities' :supplier['capabilities'],
                    'strength' :supplier['strength'],
                    'risk' :supplier['risk']
                }
                output.append(user_details)
        return jsonify({'status':'200','User':output})
    except Exception, e:
		return str(e) 

######################## Delete By Id ##############################
@app.route('/boeing/delId/<string:id>', methods=['POST'])
def deleteById(id):
    try:
        user = mongo.db.supplier_info
        user.remove({'_id' : ObjectId(id)})

        return jsonify({'Status':'OK','message':'data deleted succesfully'})

    except Exception, e:
		return str(e)

######################## Add data  ###################################################
@app.route('/boeing/post', methods=['POST'])
def postData():
    try:
        user = mongo.db.supplier_info
        # json_data = request.json

        # name = json_data['name']       
        # Address = json_data['Address']
        # user_info = {
        #     name : request.form['name'],
        #     Address : request.form['Address']    
        # }
        supplier_data = request.form.to_dict()
        user.insert_one(supplier_data)
        # for key in f.keys():
        #     for value in f.getlist(key):
        #         print (key,":",value)
               
        # supplier_name = request.form['supplier_name']
        # assessment_type = request.form['assessment_type']
        # assessment_date = request.form['assessment_date']
        # certifications = request.form['certifications']
        # capabilities = request.form['capabilities']
        # strengths = request.form['strengths']
        # risk = request.form['risk']

        # user.insert_one({'supplier_name':supplier_name,'assessment_type':assessment_type,'assessment_date':assessment_date,'certifications':certifications,
        # 'capabilities':capabilities,'strengths':strengths,'risk':risk})

        # user.insert_one(user_info)
        return jsonify({'Status':'OK','message':'data inserted succesfully'});

    except Exception, e:
		return str(e) 

########################## Update Data  #################################################
@app.route('/boeing/update/<string:id>', methods=['POST'])
def updateData(id):
    try:
        user = mongo.db.supplier_info

        # json_data = request.json
        # name = json_data['name']   
        # Address = json_data['Address']
        supplier_data = request.form.to_dict()
        user.update({'_id':ObjectId(id)},{'$set':supplier_data})

        # supplier_name = request.form['supplier_name']
        # assessment_type = request.form['assessment_type']
        # assessment_date = request.form['assessment_date']
        # certifications = request.form['certifications']
        # capabilities = request.form['capabilities']
        # strengths = request.form['strengths']
        # risk = request.form['risk']
        
        # user.update({'_id':ObjectId(id)},{'$set':{'supplier_name':supplier_name,'assessment_type':assessment_type,'assessment_date':assessment_date,'certifications':certifications,
        # 'capabilities':capabilities,'strengths':strengths,'risk':risk}})
        
        return jsonify({'Status':'OK','message':'data update succesfully'})

    except Exception, e:
		return str(e)

######################## Get only Supplier Name ##############################
@app.route('/boeing/search',methods=['GET'])
def getAllSuppliersName():
    try:
        user = mongo.db.supplier_info
        output = []
        data = user.find({},{'supplier_name':1,'_id':0})
        for supplier in data:
            user_details = {
                'supplier_name' :supplier['supplier_name']
            }
            output.append(user_details)
        return jsonify({'Users':output,'StatusCode':'200'})
    except Exception, e:
		return str(e) 


if __name__ == '__main__':
    # port = int(os.environ.get("PORT",5000))
    app.run(debug=True)
    # app.run(host = '192.168.0.102', port = port,debug=True)
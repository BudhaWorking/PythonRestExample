##############################FOR MYSQL CODE###############################


from flask import Flask, json, request, jsonify
from flask_api import FlaskAPI
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admins@123'
app.config['MYSQL_DATABASE_DB'] = 'pythondemo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

#####################################################################################
@app.route("/")
def hello():
    return "<h1><center>Welcome to Boeing Supplier Comparison!</center></h1>"

################################[ GetAllData ]#####################################################
@app.route("/getAllData", methods=['GET'])
def getAllData():
    try:

        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from supplier_info")
        data = cursor.fetchall()
        print(data)
        items_list=[];
        for item in data:
                i = {
                     'Supplier_id':item[0],
                     'Assessment_date':item[1],
                     'Supplier_name':item[2],
                     'Supplier_abbr':item[3],
                     'Country':item[4],
                     'State':item[5],
                     'City':item[6],
                     'Assess_team_name':item[7],
                     'Assess_team_title':item[8],
                     'Engg_function':item[9],
                     'Engg_sub_function':item[10],
                     'Assessment_type':item[11],
                     'Capabilities':item[12],
                     'Certifications':item[13],
                     'Pre_aero_experienc':item[14],
                     'Strengths':item[15],
                     'Risk_Awareness':item[16],
                     'Observations':item[17],

                }
                items_list.append(i)

        return jsonify({'StatusCode':'200','Items':items_list})
    except Exception as e:
        return {'error': str(e)}         
    #return jsonify({'result':data})

###################################[ GetData by Id ]###########################################################
@app.route("/getById/<int:id>", methods=['GET'])
def getById(id):
    try:
        cursor = mysql.connect().cursor()
        query = "SELECT * from supplier_info WHERE Supplier_id = %s"
        cursor.execute(query,(id))
        data = cursor.fetchall()
        print(data)
        items_list=[];
        for item in data:
                i = {
                     'Supplier_id':item[0],
                     'Assessment_date':item[1],
                     'Supplier_name':item[2],
                     'Supplier_abbr':item[3],
                     'Country':item[4],
                     'State':item[5],
                     'City':item[6],
                     'Assess_team_name':item[7],
                     'Assess_team_title':item[8],
                     'Engg_function':item[9],
                     'Engg_sub_function':item[10],
                     'Assessment_type':item[11],
                     'Capabilities':item[12],
                     'Certifications':item[13],
                     'Pre_aero_experienc':item[14],
                     'Strengths':item[15],
                     'Risk_Awareness':item[16],
                     'Observations':item[17],

                }
                items_list.append(i)

        return jsonify({'StatusCode':'200','Items':items_list})
    except Exception as e:
        return {'error': str(e)}

################################[ GetData by Name ]#############################################
@app.route("/getByName/<string:name>", methods=['GET'])
def getByName(name):
    try:
        cursor = mysql.connect().cursor()
        query = "SELECT * from supplier_info WHERE Supplier_name = %s"
        cursor.execute(query,(name))
        data = cursor.fetchall()
        print(data)
        items_list=[];
        for item in data:
                i = {
                     'Supplier_id':item[0],
                     'Assessment_date':item[1],
                     'Supplier_name':item[2],
                     'Supplier_abbr':item[3],
                     'Country':item[4],
                     'State':item[5],
                     'City':item[6],
                     'Assess_team_name':item[7],
                     'Assess_team_title':item[8],
                     'Engg_function':item[9],
                     'Engg_sub_function':item[10],
                     'Assessment_type':item[11],
                     'Capabilities':item[12],
                     'Certifications':item[13],
                     'Pre_aero_experienc':item[14],
                     'Strengths':item[15],
                     'Risk_Awareness':item[16],
                     'Observations':item[17],

                }
                items_list.append(i)

        return jsonify({'StatusCode':'200','Items':items_list})
    except Exception as e:
        return {'error': str(e)}  

#########################################[ Creating supplier ]#################################################################
@app.route("/add", methods=['POST'])
def post():

        try:

            req_json = request.get_json()
            conn = mysql.connect()
            cursor = conn.cursor()

            #query = """insert into pythondemo.supplier_info (Assessment_date,Supplier_name,Supplier_abbreviation,Country,State_Territory,City,Assess_team_name,Assess_team_title,Engineering_function,Engineering_sub_function,Assessment_type,Capabilities,Certifications,Pre_aero_experienc,Strengths,RiskAwareness,Observations) VALUES (%(Assessment_date)s, %(Supplier_name)s, %(Supplier_abbreviation)s, %(Country)s, %(State)s, %(City)s, %(Assess_team_name)s, %(Assess_team_title)s, %(Eng_function)s, %(Eng_sub_function)s, %(Assessment_type)s, %(Capabilities)s, %(Certifications)s, %(Pre_aero_experienc)s, %(Strengths)s, %(RiskAwareness)s, %(Observations)s)""" 
            cursor.execute("insert into supplier_info (Assessment_date,Supplier_name,Supplier_abbr,Country,State,City,Assess_team_name,Assess_team_title,Engg_function,Engg_sub_function,Assessment_type,Capabilities,Certifications,Pre_aero_experience,Strengths,Risk_Awareness,Observations) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(req_json['Assessment_date'], req_json['Supplier_name'], req_json['Supplier_abbr'],req_json['Country'], req_json['State'],req_json['City'], req_json['Assess_team_name'], req_json['Assess_team_title'],req_json['Eng_function'], req_json['Eng_sub_function'], req_json['Assessment_type'], req_json['Capabilities'], req_json['Certifications'], req_json['Pre_aero_experienc'],req_json['Strengths'], req_json['RiskAwareness'], req_json['Observations']))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                return json.dumps({'StatusCode':200,'Message': 'Data insert Successfully'})
            else:
                return json.dumps({'StatusCode':1000,'error': str(data[0])})
        except Exception as e:
            return {'error': str(e)}

#################################################[Delete data]##########################################################
@app.route("/delete/<int:id>", methods=['DELETE']) 
def delete(id):
        try: 
            req_json = request.get_json()

            conn = mysql.connect()
            cursor = conn.cursor()
            query = "DELETE FROM supplier_info WHERE Supplier_id = %s"
            # sql = cursor.execute("DELETE FROM supplier_info WHERE Supplier_id = %s", (req_json['id']))
            cursor.execute(query,(id))
            conn.commit()
            return jsonify({'StatusCode':'200','Message': ' Data deleted Successfully!!'})

        except Exception as e:
            return jsonify({'error': str(e)})

#########################################################################################################
# @app.route("/delete", methods=['DELETE']) 
# def deleteSupplier():
#         try: 
#             req_json = request.get_json()

#             conn = mysql.connect()
#             cursor = conn.cursor()
#             sql = cursor.execute("DELETE FROM supplier_info WHERE Supplier_id = %s" , (req_json['id']))
#             conn.commit()
#             return jsonify({'StatusCode':'200','Message': ' Data deleted Successfully!!'})

#         except Exception as e:
#             return jsonify({'error': str(e)})

###############################################[ Update data ]##############################################################
@app.route("/updateData/<int:id>", methods=['POST'])
def updateData(id):
    try:

        req_json = request.get_json()
        
        a = req_json['Assessment_date']
        b = req_json['Supplier_name']
        c = req_json['Supplier_abbr']
        d = req_json['Country']
        e = req_json['State']
        f = req_json['City']
        g = req_json['Assess_team_name']
        h = req_json['Assess_team_title']
        i = req_json['Eng_function']
        j = req_json['Eng_sub_function']
        k = req_json['Assessment_type']
        l = req_json['Capabilities']
        m = req_json['Certifications']
        n = req_json['Pre_aero_experienc']
        o = req_json['Strengths']
        p = req_json['RiskAwareness']
        q = req_json['Observations']

        print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("""update supplier_info set Assessment_date = %s, Supplier_name = %s, Supplier_abbr = %s, Country = %s, State = %s, City = %s, Assess_team_name = %s, Assess_team_title = %s, Engg_function = %s, Engg_sub_function = %s, Assessment_type = %s, Capabilities = %s, Certifications = %s, Pre_aero_experience = %s, Strengths = %s, Risk_Awareness = %s, Observations = %s WHERE Supplier_id=%s""", (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,id))
        # query = "update supplier_info set Assessment_date = %s, Supplier_name = %s, Supplier_abbr = %s, Country = %s, State = %s, City = %s, Assess_team_name = %s, Assess_team_title = %s, Engg_function = %s, Engg_sub_function = %s, Assessment_type = %s, Capabilities = %s, Certifications = %s, Pre_aero_experience = %s, Strengths = %s, Risk_Awareness = %s, Observations = %s where Supplier_id = '%s'"
        # query = """update supplier_info set Assessment_date = %(req_json['Assessment_date'])s, Supplier_name = %(req_json['Supplier_name'])s, Supplier_abbr = %(req_json['Supplier_abbr'])s, Country = %(req_json['Country'])s, State = %(req_json['State'])s, City = %(req_json['City'])s, Assess_team_name = %(req_json['Assess_team_name'])s, Assess_team_title = %(req_json['Assess_team_title'])s, Engg_function = %(req_json['Eng_function'])s, Engg_sub_function = %(req_json['Eng_sub_function'])s, Assessment_type = %(req_json['Assessment_type'])s, Capabilities = %(req_json['Capabilities'])s, Certifications = %(req_json['Certifications'])s, Pre_aero_experience = %(req_json['Pre_aero_experienc'])s, Strengths = %(req_json['Strengths'])s, Risk_Awareness = %(req_json['RiskAwareness'])s, Observations = %(req_json['Observations'])s where Supplier_id =%s"""
        # cursor.execute(query,(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,id))
        # query = """update supplier_info set Assessment_date = %s, Supplier_name = %s, Supplier_abbr = %s, Country = %s, State = %s, City = %s, Assess_team_name = %s, Assess_team_title = %s, Engg_function = %s, Engg_sub_function = %s, Assessment_type = %s, Capabilities = %s, Certifications = %s, Pre_aero_experience = %s, Strengths = %s, Risk_Awareness = %s, Observations = %s where Supplier_id = '%s',[id]"""
        # cursor.execute("update supplier_info set Assessment_date = %s, Supplier_name = %s, Supplier_abbr = %s, Country = %s, State = %s, City = %s, Assess_team_name = %s, Assess_team_title = %s, Engg_function = %s, Engg_sub_function = %s, Assessment_type = %s, Capabilities = %s, Certifications = %s, Pre_aero_experience = %s, Strengths = %s, Risk_Awareness = %s, Observations = %s where Supplier_id = %s", (req_json['Assessment_date'], req_json['Supplier_name'], req_json['Supplier_abbr'],req_json['Country'], req_json['State'],req_json['City'], req_json['Assess_team_name'], req_json['Assess_team_title'],req_json['Eng_function'], req_json['Eng_sub_function'], req_json['Assessment_type'], req_json['Capabilities'], req_json['Certifications'], req_json['Pre_aero_experienc'],req_json['Strengths'], req_json['RiskAwareness'], req_json['Observations']))
        # data = cursor.fetchall()
        # print(data)
        conn.commit()
        query = "SELECT * from supplier_info WHERE Supplier_id = %s"
        cursor.execute(query,(id))
        data = cursor.fetchall()
        items_list=[];
        for item in data:
                i = {
                     'Supplier_id':item[0],
                     'Assessment_date':item[1],
                     'Supplier_name':item[2],
                     'Supplier_abbr':item[3],
                     'Country':item[4],
                     'State':item[5],
                     'City':item[6],
                     'Assess_team_name':item[7],
                     'Assess_team_title':item[8],
                     'Engg_function':item[9],
                     'Engg_sub_function':item[10],
                     'Assessment_type':item[11],
                     'Capabilities':item[12],
                     'Certifications':item[13],
                     'Pre_aero_experienc':item[14],
                     'Strengths':item[15],
                     'Risk_Awareness':item[16],
                     'Observations':item[17],

                }
                items_list.append(i)

        return jsonify({'StatusCode':'200','Items':items_list,'Message': ' Data Successfully Updated!!!!'})   #'Items':items_list,
    except Exception as e:
        return {'error': str(e)}  




if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import jsonify
from flask import request
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)
empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]

#Syour_rest_server_port = 9090
# # The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
# eureka_client.init(eureka_server="http://your-eureka-server-peer1,http://your-eureka-server-peer2",
#                    app_name="your_app_name",
#                    instance_port=your_rest_server_port)
#

# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server='http://localhost:8761/eureka,'
                                                 "http://localhost:8761,"
                                                 "127.0.0.1:8761,"
                                                 # "http://CGSCLXR48708381.in623.corpintra.net:8761,"
                                                 # "http://CGSCLXR48708381.in623.corpintra.net:8761/eureka,"
                                                 "http://localhost:8761,"
                                                 "http://127.0.0.1:8761/eureka,"
                                                 "http://127.0.0.1:8761",
                                app_name="python-service",
                                instance_port=5000)


@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})
@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ]
    return jsonify({'emp':usr})
@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    return jsonify({'emp':em[0]})
@app.route('/empdb/employee',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)
@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
       abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})
if __name__ == '__main__':
 app.run()
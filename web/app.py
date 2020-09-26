#Assignmment By Hitensh Kharva
# Contact - 9930933909
#Email - khitansh@gmail.com

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]



def countTokens(url):
    tokens = users.find({
        "URL":url
    })[0]["Tokens"]
    return tokens


class API_URL(Resource):
    def post(self):
        #Step 1 is to get posted data by the user
        postedData = request.get_json()


        url = postedData["url"]
        users.insert({
            "URL": url,
            "Tokens":6
        })

        retJson = {
            "status": 200,
            "msg": "You successfully added a URL"
        }
        return jsonify(retJson)



    def put(self):
        #Step 1 get the posted data
        postedData = request.get_json()

        old_url = postedData["oldurl"]
        new_url = postedData["newurl"]

        num_tokens = countTokens(old_url)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        users.update({
            "URL":old_url
        }, {
            "$set":{
                "URL":new_url,
                "Tokens":num_tokens-1
                }
        })

        retJson = {
            "status":200,
            "msg":"URL saved successfully"
        }
        return jsonify(retJson)

    def delete(self):
        #Step 1 get the posted data
        postedData = request.get_json()

        url = postedData["url"]

        #Verify user has enough tokens

        num_tokens = countTokens(url)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        users.update({
            "URL":url
        }, {
            "$set":{
                "Tokens":num_tokens-1
                }
        })
        users.delete_one({"URL":url})

        retJson = {
            "status":200,
            "msg":"URL deleted successfully"
        }
        return jsonify(retJson)

class Get(Resource):
    def post(self):
        postedData = request.get_json()

        url = postedData["url"]


        num_tokens = countTokens(url)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        users.update({
            "URL":url
        }, {
            "$set":{
                "Tokens":num_tokens-1
                }
        })

        url = users.find({
            "URL": url
        })[0]['URL']
        retJson = {
            "status":200,
            "URL": str(url)
        }

        return jsonify(retJson)




api.add_resource(API_URL, '/api')
api.add_resource(Get, '/goto')


if __name__=="__main__":
    app.run(host='0.0.0.0')

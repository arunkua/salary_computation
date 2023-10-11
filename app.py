from flask_restful import Resource,Api
from flask import Flask,jsonify, make_response, request
import pandas as pd

app=Flask(__name__)
api=Api(app)

df=pd.read_csv("s3://talentprofile/arun_ml_work/salary_testing/modified_data.csv")


class InternalSalaryAPI(Resource):
    def get(self):
        query = request.args.get("query")
        res=dict()
        try:
            res['Average_Salary']=df[df['input_job_title']==query]['Average_salary'].values[0]
            res['title']=query
            status_code=200
            result = {"status" : "success",
                                        "salary" : res}

        except:
            status_code=400
            result = {"status" : "error",
                                        "salary" :""}
        return make_response(jsonify(result), status_code)

api.add_resource(InternalSalaryAPI,'/salary_testing')

if __name__=='__main__':
    app.run()

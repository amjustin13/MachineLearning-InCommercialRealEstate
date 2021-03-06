import flask
import json
from flask import request, jsonify, Response
import tensorflow as tf
import tensorflow_text
import numpy as np
app = flask.Flask(__name__)
app.config["DEBUG"] = True

model = None
# bos_class_names = ["Amendment_to_a_Long_Form", "Certificate_of_Occupancy", "Electrical_Fire_Alarms", "Electrical_Low_Voltage", "Electrical_Permit", "Electrical_Temporary_Service", "Erect_New_Construction", "Excavation_Permit", "Foundation_Permit", "Gas_Permit", "Long_Form_Alteration_Permit", "Plumbing_Permit", "Short_Form_Bldg_Permit", "Use_of_Premises"]
four_class_names = ["building_permit", "electrical_permit",
                    "plumbing_permit", "mechanical_permit"]

# change here to run the appropriate model
RUN_BINARY = False
if RUN_BINARY:
    model = tf.saved_model.load("../binary_model")
else:
    model = tf.saved_model.load("../latest")


@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

# Get permit result
# if id is provided, return certain result.
# Otherwise, return all
#  /permit?id= <id>
@app.route('/permit', methods=['GET'])
def getPermit():
    with open('dummy.json', 'r') as jsonfile:
        permitData = json.loads(jsonfile.read())
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return json.dumps(permitData)

    for permit in permitData:
        if permit['id'] == id:
            return jsonify(permit)


"""
expected request body:
{
    "instances": ["sample input string", "another sample input string"]
}

output: list of predictions 
"""
@app.route('/predict', methods=['GET'])
def predict():
    input = None
    try:
        input = request.get_json()['instances']
        if len(input) == 0:
            raise
        input = tf.constant(input)
    except:
        return Response("Invalid input. Please send JSON with a key of 'instances' and a value of a list of input strings", 400)
    res = model(input)
    ret = []
    if RUN_BINARY:
        res = res.numpy()
        for out in res:
            if out < .5:
                ret.append('post_construction')
            else:
                ret.append('pre_construction')
    else:
        max_ind = np.argmax(res.numpy(), axis=1)
        for idx in max_ind:
            ret.append(four_class_names[idx])
    return jsonify(ret)


if __name__ == '__main__':
    app.run(debug=True)

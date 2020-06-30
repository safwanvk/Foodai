from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='78742f93a0874e6c93db0aa67f5bb25e')
model = app.models.get('tomato')
response = model.predict_by_url(url='https://5.imimg.com/data5/KV/QI/MY-31387320/potato-onion-tomato-500x500.png')
print(response)

print("hrrrr")

arrs=(response["outputs"][0]["data"]["concepts"])


for m in arrs:
    name=(m["name"])
    value=(m["value"])
    print(name,type(value))

# # riss.kiran@gmail.com
# #
# # rissstaff

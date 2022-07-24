import pymongo
client = pymongo.MongoClient("mongodb+srv://deepaksaini:Cal84707@deepak.nds9up5.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
d={
    'name':'deepak',
    'emailid': 'deepksaini30@gmail',
    'surname':'saini'
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
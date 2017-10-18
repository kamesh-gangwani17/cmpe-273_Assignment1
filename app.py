import rocksdb
import uuid
import subprocess
import json
from flask import Flask, request, Response
app = Flask(__name__)

@app.route("/api/v1/scripts", methods=['GET','POST'])
def firstend():
	if request.method == 'POST':
		# extension =os.path.splitext(data_file.ext)	
		#Flask_path="/api/1/scripts"
		#file.save(os.path.join("Flask_path"+uniqueNo))

		db = rocksdb.DB("assign1.db", rocksdb.Options(create_if_missing=True))
		dataStore = request.files['data']
		uniqueNo = str(uuid.uuid4())
		#datastore = data_post.write()
		#newdata = datastore+uniqueNo
		#print gettype(data)


		#f=open('uniqueNo.dat','w+')
		#f.write( %s    %s  %(uniqueNo,dataStore))
		db.put(uniqueNo.encode(), dataStore.read())
		return Response(json.dumps({"script-id": uniqueNo}),status = 200)





    

	

@app.route("/api/v1/scripts/<scid>")
def secondend(scid):
    	db = rocksdb.DB("assign1.db", rocksdb.Options(create_if_missing=True))
	#result= subprocess.check_output("python3","-c",datastore.encode())
    	return Response(subprocess.check_output(["python3.6", "-c", db.get(scid.encode()) ]) )

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')



	

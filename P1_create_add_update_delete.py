#This is a tutorial to use firebase from python. 

#Add a project: by going to firebase website ans google login.
#Fill details: Make the project 
#Go to Data base on the side menu. 
#Use Test mode if your app is in develping stage as it allows anyone to chage data (without authentification)
#Click Done: Wait for setting up....
#Choose real time data base on the top for real time work.
#Now go to rules and make red and write : true (If you want to read and write.) and publish.  
#Now our firebase is ready to use and database id set up :D

#We import the library used: 
from firebase import firebase 

#Now we make a object: 
#FirebaseApplication requires 2 parameters: database url of database and auth. (Can be None in test mode)
firebase = firebase.FirebaseApplication('https://traffic-light-mini.firebaseio.com/' , None) 

#Adding data:
data = {
    'name' : 'Pranjal', 
    'rollNum' : 22 
}

#Now to put this data dictionary we use: post() method: takes the path and the values to be added in form of python dictinary
#firebase.post('try', data)
#We can also use the patch() method to avoid the random key generated: (url , dictionary to be patched)
result = firebase.patch('https://traffic-light-mini.firebaseio.com' + '', {'id': 4 , 'ok':{'Nice':10}})
#post() returns the key of the added data. 

#Getting data from firebase: get() method: (path)
result = firebase.get('/id' , '')
print(result)
result = firebase.get('/ok','')
print(result)

#To update data: put() : (path till the attribute(Not included) , attribute to be changed , new value)
firebase.put('' , 'id' , 5)

#To delete: delete() : (path , attribute)
firebase.delete('/ok' , 'Nice') #Also if a attribute/key has no value to is also deleted. 

# myName = 'levan'
# myAge = 30
# myLocation = 'New York'

# print(f'My name is {myName}, I am {myAge} years old, and I live in {myLocation}.')


# newNumber =  5 * myAge + 20 
# myAge = (newNumber -20) / 5
# print(newNumber)
# print(myAge)


import flask
from flask import Flask , render_template , request
import requests
app = Flask(__name__)
@app.route('/' , methods=['GET', 'POST'])

def wheather_test():
    if request.method == 'POST':
        enter_city = request.form['city']
        api_key1 = "d4ee7e6f2ca75bd1e12ed71fb794226b"
        urll = f"https://api.openweathermap.org/data/2.5/weather?q={enter_city}&appid={api_key1}&units=metric"
        responsess = requests.get(urll)
    
   
    
    if responsess.json()['cod'] == '404':
        render_template('index.html', data= 'data not found')
    else:
        data = responsess.json()['weather'][0]['main']
        temperature = round(responsess.json()['main']['temp'])
        print(data,temperature)
        return render_template('index.html' , data=data , temperature=temperature) 

    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

import requests

url='http://api.openweathermap.org/data/2.5/weather?appid=e2151b0ea0d7ee610b4d2795865eac8a&q=Amsterdam'

json_data = requests.get(url).json()
format_add = json_data ['main']['temp']
weather = str(round((format_add - 273), 1))

patterns = {
    "Do you remember (.*)":"Of course I remember {}",
    "do you remember (.*)":"Of course I remember {}",
    "'member (.*)":"Oh I 'member {}",
    "I feel (.*)":"Why do you feel {}?",
    "Do you like (.*)":"Of course I like {}",
    "do you like (.*)":"Of course I like {}",

}

qalist = {
  '':'',
  'Hello':'Hello!',
  'Hello!':'Hello!',
  'Hey':'Hello!',
  'Hey!':'Hello!',
  'hey':'Hello!',
  'Hi':'Hello!',
  'Hi!':'Hello!',
  'How is it going?':'I am good, how are you?',
  'How is it going':'I am fine, how are you?',
  'how is it going?' : 'I am good, how are you?',
  'how is it going' : 'I am fine, how are you?',
  'Good!':'Nice!',
  'Good':'Nice!',
  'Hola':'Hey!',
  'hola':'Hey!',
  'good':'Nice!',
  'good!':'Nice!',
  'How is the weather?': 'The temperature is ' + weather + 'C',
  'how is the weather?': 'The temperature is ' + weather + 'C',
  'How is the weather': 'The temperature is ' + weather + 'C',
  'how is the weather': 'The temperature is ' + weather + 'C',
  'How warm is it today?': 'The temperature is ' + weather + 'C',
  'how warm is it today?': 'The temperature is ' + weather + 'C',
  'How warm is it today': 'The temperature is ' + weather + 'C',
  'how warm is it today': 'The temperature is ' + weather + 'C',
  'What is the weather?': 'The temperature is ' + weather + 'C',
  'what is the weather?': 'The temperature is ' + weather + 'C',
  'What is the weather': 'The temperature is ' + weather + 'C',
  'what is the weather': 'The temperature is ' + weather + 'C',
  'How warm is it?': 'The temperature is ' + weather + 'C',
  'how warm is it': 'The temperature is ' + weather + 'C',
  'how warm is it?': 'The temperature is ' + weather + 'C',
  'How warm is it': 'The temperature is ' + weather + 'C',
  'What is your name?':'My name is soofbot.',
  'what is your name?':'My name is soofbot.',
  'what is your name':'My name is soofbot.',
  'What is your name':'My name is soofbot.',
  'how are you called':'My name is soofbot.',
  'how are you called?':'My name is soofbot.',
  'How are you called':'My name is soofbot.',
  'How are you called?':'My name is soofbot.',
}
# tkinter handles the GUI
import tkinter as tk

# requests handles form data
import requests

# get weather function that pulls in the city from the user input
# uses requests library
def get_weather(city):

	# weather API key
	weather_key = '95e250fdb99b46b3e2286b339f7b1ca4'

	# using openweathermap API to get weather
	url = 'https://api.openweathermap.org/data/2.5/weather'

	# using imperial since I'm in the US
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}

	# hits the weather API and the paramaters we defined
	response = requests.get(url, params=params)

	# gets weather from the API as a json file, we have tons of extra info in here but I'm only displaying a small bit of it
	weather = response.json()
	label['text'] = format_response(weather)
	print('text')

# function that displays only the data we want from the JSON file
def format_response(weather):

	# creates string to display
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)

	# if it's unable to display the string it shows an error message
	except:
		final_str = 'Error: Please try again'

	return final_str

# uses tkinter library
# root window that holds the GUI
root = tk.Tk()

# sets size of GUI
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

# background of GUI
background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# defines the frame, and it's adjustable because of 'rel'
frame = tk.Frame(root, bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# user input form for city
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

# get weather button, this declares what the button will look like
button = tk.Button(frame, text="Submit", font=40, command=lambda: get_weather(entry.get()))

# get weather button being placed in UI
button.place(relx=0.7, relheight=1, relwidth=0.3)

# this shows the lower frame where the weather information is displayed
lower_frame = tk.Frame(root, bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

# end of root window that holds the GUI
root.mainloop()
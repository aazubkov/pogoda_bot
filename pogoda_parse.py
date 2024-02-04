import json
import requests


url = "https://weatherapi-com.p.rapidapi.com/current.json"
url1 = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"59.938951,30.315635", 'lang':'ru'}
querystring1 = {"q":"59.938951,30.315635", "days":"2", 'lang':'ru'}

headers = {
	"X-RapidAPI-Key": "f6d548cf49msh5bcf3706714bd9ep1446a3jsn4dd5073b1b86",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


def get_pogoda_zavtra():
	response1 = requests.get(url1, headers=headers, params=querystring1)
	msg = f'<b><u>Прогноз погоды в С-Петербурге на завтра.</u></b>\n\n'
	for h in range(9, 20, 5):
		next_day_hour = json.loads(response1.content)['forecast']['forecastday'][1]['hour'][h]
		hour_temp = next_day_hour['temp_c']
		hour_wind = next_day_hour['wind_kph']
		hour_nebo = next_day_hour['condition']['text']
		hour_chance_of_rain = next_day_hour['chance_of_rain']
		hour_chance_of_snow = next_day_hour['chance_of_snow']
		tm = f'<b>{h}:00</b>.'
		t = f'🌡️ {hour_temp}°С  '
		c = f'<i>{hour_nebo}</i>  '
		w = f'💨 {hour_wind} км/ч  '
		r = f'☔ {hour_chance_of_rain}%  '
		s = f'❄️ {hour_chance_of_snow}%. '
		msg += tm + t + c + w + r + s + '\n'
	return msg


# def get_pogoda_segodnia():
	# response = requests.get(url, headers=headers, params=querystring)
	# cur_day = json.loads(response.content)['current']
	# temp = cur_day['temp_c']
	# wind = cur_day['wind_kph']
	# nedo = cur_day['condition']['text']
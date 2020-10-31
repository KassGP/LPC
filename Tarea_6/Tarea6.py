import requests
import os
from bs4 import BeautifulSoup

def get_soup(url) -> BeautifulSoup:
	response = requests.get(url)
	return BeautifulSoup(response.content, 'html.parser')

def england():
	soup = get_soup("https://es.wikipedia.org/wiki/Anexo:Ciudades_del_Reino_Unido_por_poblaci%C3%B3n")
	tr= soup.table.find_all('tr')
	file = open("/Users/usuario/Desktop/england.txt", "w")
	for row in tr:
		columns = row.find_all('td')
		t = [ele.text.strip() for ele in columns]
		print(f"{t}")
		file.write(str(t) + os.linesep)
	file.write("Posicion - Ciudad - Nacion - Poblacion" + os.linesep + os.linesep)
	file.write("--- Datos sobre las ciudades existentes en el Reino Unido ---" + os.linesep)

england()
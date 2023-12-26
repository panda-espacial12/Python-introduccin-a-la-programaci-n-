import re 

text = "este es un ejemplo de una pagina web: https://wwww.exanole.com y tambien podemos visitanos en  https://wwww.jhon.com"

pattern = "https?://[a-zA-z0-9.-]+\.[a-zA-z]{2,}"

result = re.findall(pattern, text)

print(result)

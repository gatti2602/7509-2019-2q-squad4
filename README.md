# Repositorio del Squad 4 - Año 2019 - 2Q

 Links utiles
 ------------

[Google Drive](https://drive.google.com/drive/folders/1_zad5GPKZTT3MjO10yBQzh6H7INMRInk)
[Slack](https://app.slack.com/client/T2YH923SQ/GN1GHTK8X/details/info)

 Integrantes
 -----------

- Nicolas Gatti
- Facundo Bravo
- Julian Quino
- Nicolas Sallis

---
Instalacion
-----------
Correr: 
```sh
	pip3 install -r requirements.txt
```
---
Django
------
### Helloworld 

Iniciar server e ir a: http://127.0.0.1:8000/helloworld/

---
Cucumber (Behave en Python)
--------
[Tutorial](https://behave.readthedocs.io/en/latest/tutorial.html)

Comentar la linea siguiente en settings.sh:

django_heroku.settings(locals())


```sh
	python3 manage.py behave
```
---
Heroku
------

Descomentar la linea siguiente en settings.sh:

django_heroku.settings(locals())

[server](https://squad4-psa.herokuapp.com/)
# deductive-reasoning
A tool for deductive reasoning

[Deductive Reasoning Web Site](http://142.93.138.235)


## Virtualenv Kurulumu
	pip install virtualenv

## Virtualenv Kullanımı 

	virtualenv --python=python3 <klasör_ismi>

__Virtualenv aktif etme işlemi__
	
	source <klasör_ismi>/bin/activate 

## Gereksinim Kurulumu

	pip install -r requirement.txt

## Repo klonlanması
__Proje için klasör açılır ardından;__

	git clone https://github.com/lyk2018-python/deductive-reasoning.git

## *local_settings.py* eklenmesi
__Proje clone landıktan sonra *settings.py* ın bulunduğu dizine (*../deductive-reasoning/deductivereasoning*) *local_settings.py* dosyası oluşturulur. Ardından içerisine şu kod bloğu eklenir__
```python
	SECRET_KEY = 'SECRET-KEY-BURAYA'
	ALLOWED_HOSTS = []
	DEBUG = True
	import os
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	   }
	}
```
__Daha sonra *SECRET-KEY-BURAYA* yazan alana şu linkten alınan Django Secret Keyi tırnak içerisine eklenir;__
[Django Secret Key Generator](https://www.miniwebtool.com/django-secret-key-generator/)

## Database İşlemleri

__Bu işlemleri yapmak için manage.py dosyası ile aynı dosyada olmanız gerekiyor.__

	cd deductive-reasoning/deductivereasoning
	python manage.py makemigrations
	python manage.py migrate

## Uygulamayı Çalıştırma

	python manage.py runserver

__127.0.0.1:8000 adresi ile web browserdan kullanabilirsiniz.__

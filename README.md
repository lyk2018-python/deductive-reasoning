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

## Database İşlemleri

__Bu işlemleri yapmak için manage.py dosyası ile aynı dosyada olmanız gerekiyor.__

	cd deductive-reasoning/deductivereasoning
	python manage.py makemigrations
	python manage.py migrate

## Uygulamayı Çalıştırma

	python manage.py runserver

__127.0.0.1:8000 adresi ile web browserdan kullanabilirsiniz.__

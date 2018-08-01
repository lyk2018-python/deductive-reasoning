# deductive-reasoning
A tool for deductive reasoning

[Deductive Reasoning Web Site](http://sx511w.srv.plusclouds.net/)



## Virtualenv Kurulumu
pip install virtualenv

## Virtualenv Kullanımı 

virtualenv <klasör_ismi> --python=python3\n

source <klasör_ismi>/bin/activate __Virtualenv aktif etme işlemi__

## Gereksinim Kurulumu

pip install -r requirement.txt

## Database İşlemleri

*Bu işlemleri yapmak için manage.py dosyası ile aynı dosyada olmanız gerekiyor.* 

python manage.py makemigrations

python manage.py migrate

## Uygulamayı Çalıştırma

python manage.py runserver

*127.0.0.1:8000 adresi ile web browserdan kullanabilirsiniz.*

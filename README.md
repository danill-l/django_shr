# MyShroom - справочник грибной тематики
<pre>
        ___..._
    _,--'       "`-.
  ,'.  .            \
,/:. .     .       .'
|;..  .      _..--'
`--:...-,-'""\
        |:.  `.
        l;.   l
        `|:.   |
         |:.   `.,
        .l;.    j, ,
     `. \`;:.   //,/
      .\\)`;,|\'/(
       ` `itz `(,
</pre>
Сайт-каталог, содержащий в себе информацию о грибах на территории России и СНГ, а также статьи на грибную и окологрибную тематику.
Для установки вам необходимо:
-склонировать данный репозиторий ( git clone https://github.com/danill-l/django_shr.git)
-активировать виртуальное окружение venv (venv\Scripts\activate), убедитесь, что при этом у вас установлена версия Python 3.12 (Python 3.12.5 64-bit v.)
-выполните миграцию базы данных (python manage.py makemigrations и python.manage.py migrate)
-возможно восстановление данных базы с помощью фикстур (к двум вышеупомянутым шагам запустить команду python manage.py loaddata fixtures/<директория>/file.json)
-запуск сервера осуществляется с помощью команды python manage.py runserver
-перейти по адресу, указаному в терминальном окне (http://127.0.0.1:8000 - стартовая страница)
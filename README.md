# BeatX_ADC5
BeatX is a music streaming platfrom where a user can upload their music and listen from any device as per their wish.

Requirement as a editor:
python3 installed
and pip:
        asgiref           3.2.3
        deprecation       2.0.7
        Django            3.0.2
        django-filter     2.2.0
        eyeD3             0.9
        filetype          1.0.5
        mutagen           1.43.0
        packaging         20.1
        Pillow            7.0.0
        pip               19.3.1
        pydub             0.23.1
        pyparsing         2.4.6
        python-vlc        3.0.7110
        pytz              2019.3
        setuptools        41.2.0
        six               1.14.0
        SpeechRecognition 3.8.1
        sqlparse          0.3.0
        stagger           1.0.0
        style             1.1.0
        tinytag           1.2.2


Api Documentation:
     for get/post request: use the root/path/songs
     for put/delete/get by id: use root/path/songs/<int:pk>
     for pagination:
     pagenumber=refers to the page number 
     pagesize = refers to page size
        and the url: root/path/songs/pagenumber=<int:pk>/pagezie=<int:size>

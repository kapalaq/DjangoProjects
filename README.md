Hello! I hope this file finds you well, so you will be able to check a site I created in five days. 
To launch my site you have to:
1. Open DjangoProject repo as a root directory
2. Open Console and write: myvenv\Scripts\activate
3. In Console with (myvenv) prefix, write following command: py -3 -m pip install -r requirements.txt
4. When it runs successfully, write following command to run server: py -3 manage.py runserver
5. Copy this link and paste it in your browser : localhost:8000/blog
6. Enjoy

Этот проект от начала и до конца спроектирован мной. Как вдохновение я выбрал сайт Sxodim.com, так как у нас похожие тематики. Весь мой труд можно увидеть по commitments, но в общем описывая, я следовал данному тех заданию, по немного реализуя требуемый функционал. Проблемы возникали на всех уровнях, о них я напишу ниже, но что стоит отметить, так это подход к работе. Для мероприятий я создал отдельную модель, так как сиситема моделей Django просто и удобна в использовании. Тоже самое для личных аккаунтов, я использовал встроенную систему регистрации и аккаунтов Django.contrib.auth. Зачастую оно решало всю логику за меня, а я пользовался её плодами. Сам сайт сделан проще некуда:
Если есть мероприятия, они появятся на главной странице, нажав на них вы можете прочитать детальнее и зарегистрироваться. Зарегистрированные мероприятия можно увидеть в разделе My Page. Регистрация обязательна, без неё вас не пропустит на My page и не даст зарегистрироваться на Мероприятие. Знаю, что в тех задании точно не указывается, можно ли регистрироваться без аккаунта, но я решил сделать так, потому что не хватало времени на тяжелую для реализации логику безпрофильной (non-account) регистрации. Дизайн не продумывался вовсе, я сосредоточился только на функционале, сделав сайт лишь базового вида, учитывая за что будет цепляться человеческий глаз и какие цвета ему приятны. Здесь можно переходить к ограничениям, так как в виду отсутствия времени по личным причинам, я не смог уделить сайту все 24*7 часов.

Ограничения:
Есть всего два ключевых ограничение и несколько маленьких, доставляющих только неудобство. Первым Ключевым Огрничением является тот факт, что забронировав место на мероприятие, оно не удаляется из возможности регистрации, что в теории дает вам шанс купить билет на 7ое место концерта 100 раз из 100 свободных мест. Данная дыра вызвана тем, что я впервые работал с ManyToMany(through) отношениями, включающими медианный объект. Это взаимосвязь ManyToMany, которая не напрямую связывает объекты, а через посредника. В моем случае класс EventUser. Пусть я и разобрался как реализовать unique_fields, зпрещающий регистрировать одно и то же место, я не смог удалить его из списка выборов, так как не смог достать эти данные. Поэтому и не реализовал unique_fields. Вторым ключевым ограничением, вызванным все той же проблемой незнания ManyToMany(through) была отсутсвие функционала работы с регистрациями на My page. Однако, тут скорее играет фактор времени, потому что в целом я разобрался как удалять/добавлять регистрацию через EventUser модель, но мне не хватило времени, так как это сложная логика, требующая коллосального времени. Далее пойдут мелкие проблемы, большую часть из которых можно описать отговоркой: "нехватка времени", так как они не явялись ключевыми и я не видел смысла тратить на них время.
1. Добавление и удаление мероприятий происходит только через консоль разработчика, отдельной страницы для редакторов (staff) нет, хотя весь функционал имеется и изначально планировал
2. Загрузка постера мероприятия в консоле разработчика должна производится дважды, так как урезанная версия постера, появляющаяся на главной странице, требовала использование Pillow модуля и создания страницы редактора, что отправляет к пункту 1
3. Непривликательный дизайн
4. Отсутствие полной оплаты
5. Отсутствие взаимосвязи с внешними календарями
6. Отсутствие кнопки Logout
Последний пункт скорее проблемы привередливости. Django имеет функционал для Log Out, но мне не нравится как он реализован, ибо конкретно в моем случае он требует заметных доработок, буквально костылей. В отсутсвии времени я не смог доделать свою модел Log Out, поэтому просто решил без неё. Если вы захотите сделать Login в несколько аккаунтов сразу, убедитесь что открыли сайт через режим Инкогнито. Ведь там ваши данные хранятся в пределах одной сессии и не записываются в кеш браузера, что происходит в обычном. 

Спасибо что уделили время моему скромному проекту! Буду ждать ответа от вас!

# -*- coding: utf-8 -*-
import subprocess
subprocess.call("clear")

# Парсинг – это процесс сбора данных с последующей их обработкой и анализом. 
# К этому способу прибегают, когда предстоит обработать большой массив информации, 
# с которым сложно справиться вручную. 
# Программа, которая производит сбор и синтаксический анализ, – это парсер. 
# С ее помощью можно упростить работу по поиску контента 
# для собственного ресурса и проводить ее в сжатые сроки.
#
# Разновидности парсинга:
# Parsing позволяет осуществлять работу с данными любой тематики. 
# Среди основных сфер применения такой технологии можно выделить:
# 
# - поиск и наполнение ресурсов текстовым и мультимедийным контентом;
# - товары и цены в интернет-магазинах;
# - данные из объявлений, размещенных на специальных ресурсах;
# - поиск и сбор контактных данных пользователей;
# - в рамках социальных сетей (например, отзывы и комментарии);
# - сайты, специализирующиеся на публикации спортивных результатов.
# 
# Этапы парсинга:
# - Поиск данных. 
#   В программу-парсер загружается исходный HTML-код страницы сайта. 
#   С кодом начинает работать скрипт, который разбивает весь текст на лексемы, 
#   выделяя необходимую информацию.# 
# - Извлечение информации. 
#   Поиск данных происходит благодаря определенному набору знаков, описывающих цель поиска. 
#   Этот набор также называется регулярными выражениями. 
#   Они позволяют выделить из всего массива только интересующие фрагменты.# 
# - Сохранение данных. 
#   После получения информация сохраняется в виде таблиц или вносится в базу данных.
# 
# Парсинг не является противозаконной операцией, 
# но осуществлять его можно только при соблюдении соответствующих условий:
# - исследуемая информация должна находиться в открытом доступе 
#   и не быть под защитой закона об авторских и смежных правах;# 
# - сбор данных не должен приводить к сбоям в работе сети интернет и проблемам с ресурсами, 
#   являющимися источниками информации (слишком активная работа парсера может быть принята за DOS-атаку);
# - сбор должен проводиться только законными способами;
# - парсинг не должен ограничивать конкуренцию.
#
# Защита от парсинга
# - Разграничение прав доступа. 
#   Информация о структуре сайта скрывается от роботов и остается доступной только для администрации. 
#   Это наиболее простой способ защиты информации.
# - Черные и белые списки. 
#   Пользователи, которые пытаются украсть контент, отправляются в списки нежелательных, 
#   в соответствии с чем к ним применяются установленные санкции.
# - Временная задержка между запросами. 
#   Парсинг отличается направлением постоянных хаотических запросов. 
#   Установка временной задержки для обращений, отправляемых с одного компьютера, 
#   позволит ограничить доступ к информации.\
# - Различные методы защиты от роботов. 
#   Установка на сайте авторизации, которую может пройти только человек (ввод капчи, подтверждение регистрации и другие способы).
# #

#from urllib.request import urlopen
#from bs4 import BeautifulSoup

#####################################################################################################################
import re # using Regex
import requests
from lxml import html

url = 'https://www.rusprofile.ru/codes/11100'
response = requests.get(url)
parser_tree = html.fromstring(response.content)
response = parser_tree.xpath('//*[@id="main"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/text()')


# convert a list to string
listToStr = ' '.join([str(elem) for elem in response]) #.replace('\n','')

# use a regular expression to match whitespace and remove them using re.sub() function.
# strip() - remove spaces from both side

print(re.sub(r"\s+", " ", listToStr.strip()))
#>> Производство кухонной мебели, кроме изготовленной по индивидуальному заказу населения (12)
#####################################################################################################################

# XPath - это язык выражений, предназначенный главным образом для доступа к узлам в документе XML. 
# XPath - это технология, которая использует выражения пути для выбора узлов или наборов узлов в документе XML 
# (или в нашем случае в документе HTML). 
# Даже если XPath не является языком программирования сам по себе, 
# он позволяет вам писать выражения, которые могут напрямую обращаться к определенному элементу HTML 
# без необходимости проходить через все дерево HTML.
#
# XPath может найти элемент по идентификатору, например так: [@attribute = 'value'] or ex.//*[@id="main"]

# THE BIG EXAMPLE OF XPATH - Child of Element ID
# //*[@id="dhContent"]/pre[4]/font[3]/font/text()
# <div id="dhContent">
#     <h1><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Примеры локатора XPath</font></font></h1>
#     <div class="landing-page-7mh">
#         <link href="/css/how-many-users.css" rel="stylesheet">
#         <div class="page-title grid">
#             <h2 class="unit"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Консалтинг веб-производительности</font></font></h2>
#             <div class="product-actions var--footer">
#                 <span><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
#         Наши специалисты узнают, сколько пользователей </font><font style="vertical-align: inherit;">может обработать </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ваш сайт</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> ! </font></font><br>
#       </span>
#                 <br> &nbsp;
#                 <br>
#                 <a href="/load-testing-consulting-services/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Учить больше</font></font></a>
#             </div>
#             <p></p>
#         </div>
#         <p></p>
#     </div>
#     <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Если вы новичок в XPath, мощь и гибкость XPath могут немного сбить с толку. </font><font style="vertical-align: inherit;">Эта страница содержит несколько примеров, с которых можно начать. </font><font style="vertical-align: inherit;">После этого я рекомендую ресурсы XPath, указанные на нашей </font><font style="vertical-align: inherit;">странице </font></font><a href="https://www.webperformance.com/load-testing-tools/blog/?page_id=4623"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Типы локаторов элементов</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> .</font></font>
#     </p>
#     <h2><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">«Сырой» XPath</font></font></h2>
#     <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Чтобы найти ссылку на этой странице:</font></font>
#     </p>
#     <pre><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&lt;HTML&gt; &lt;тело&gt;</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
#     &lt;p&gt; Лиса перепрыгнула через ленивую коричневую &lt;a href="dogs.html"&gt; собаку &lt;/a&gt;. &lt;/ p&gt;</font></font><font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
#     &lt;/ Body&gt; &lt;/ html&gt;</font></font></pre>
#     <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Необработанный XPath пересекает иерархию от корневого элемента документа (страницы) до нужного элемента:</font></font>
#     </p>
#     <pre><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">/ HTML / тело / р / а</font></font></pre>
#     <p>&nbsp;</p>
#     <h2><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ID дочернего элемента</font></font></h2>
#     <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">XPath может найти элемент по идентификатору, например так:</font></font>
#     </p>
#     <pre><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">// * [@ ид = "ELEMENT_ID"]</font></font></pre>
#     <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Так что, если вам нужно найти элемент, который находится рядом с другим элементом с идентификатором, как ссылка в этом примере:</font></font>
#     </p>
#
########### EXAMPLE XPATH ###########
# /pre[4]/font[3]/font
#     <pre>
#         <font style="vertical-align: inherit;">
#             <font style="vertical-align: inherit;">&lt;HTML&gt; &lt;тело&gt;</font>
#         </font>
#         <font></font>
#         <font style="vertical-align: inherit;">
#             <font style="vertical-align: inherit;">
#                 &lt;p id = "fox"&gt; Лиса перепрыгнула через ленивую коричневую &lt;a href="dogs.html"&gt; собаку &lt;/a&gt;. &lt;/ p&gt;
#             </font>
#         </font>
#         <font></font>
#         <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
#             &lt;/ Body&gt; &lt;/ html&gt;
#         </font>
#         </font>
#     </pre>


# //*[@id="main"]/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/a
# //*[@id="main"]/div/div[2]/div[3]/div/div[1]/div[2]/div[3]/div[1]/div[2]/a
# //*[@id="main"]/div/div[2]/div[3]/div/div[1]/div[2]/div[4]/div/div[2]/a
# //*[@id="main"]/div/div[2]/div[3]/div/div[1]/div[2]/div[5]/div[1]/div[2]/a
# //*[@id="main"]/div/div[2]/div[3]/div/div[1]/div[2]/div[6]/div/div[2]/a
# //*[@id="main"]/div/div[2]/div[3]/div/div[1]/div[2]/div[7]/div[1]/div[2]/a
#//*[@id="main"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/text()
#//*[@id="main"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/text()
#//*[@id="main"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[2]/a/text()
#//*[@id="main"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/div/div[2]/a/text()

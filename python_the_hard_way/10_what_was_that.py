#_*_coding:utf-8_*_
#escapes(экранирование) - вывод символов, что используются в коде, для 
#   написания программ на экран ("", \,...)
#formats - форматирование текста это, внедрение в текст специальных
#   символов и ключей, для определенного изменения содержания.
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#New format in python 3.X
print "Hello, i love {0}, and {1}". format("smart investing",
        "body, like a best fighter")

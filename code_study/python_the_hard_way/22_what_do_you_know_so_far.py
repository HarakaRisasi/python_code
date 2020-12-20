# -*- coding: utf-8 -*-

# Задача:
#   -Просмотреть все упражнения с самого начала
#   -Выписать ключевые слова и символы используемые в
#       синтаксисе Python для составления программ
#   -Составить таблицу
#
# Keyword\symbol   |   Name     |           Meaning\Explanation
#
#   print()        |print       |The print function. Used to
#                  |            |output text to the console.
#                  |            |
#   '              |Single quote|Used to encapsulate a single line
#                  |            |string.
#                  |            |
#   "              |Double quote|Used to encapsulate a single line
#                  |            |string.
#                  |            |
#   '''            |Triple quote|Used to encapsulate a multi-line
#                  |            |string.
#                  |            |
#   #              |Hash\       |Used to denote a comment.
#                  |Octothorpe\ |
#                  |Pound       |
#                  |            |
#   +              |Plus sign   |Used as an addition sing during
#                  |            |mathematical operations.
#                  |            |Also used in loops as an iterator.
#                  |            |Also used in shorthand such as +=
#                  |            |meaning 'equal to plus'.
#                  |            |e.g. a += b which can be written
#                  |            |     a = a + b
#                  |            |
#   -              |Hyphen      |Used as minus sign when performing
#                  |            |substraction in mathematical
#                  |            |operation.
#                  |            |
#   *              |Asterisk    |Used for multiplication during
#                  |            |mathematical operations.
#                  |            |Also used when using *args in
#                  |            |functions where you are not sure
#                  |            |how many arguments you are passing
#                  |            |to the function.
#                  |            |Specifically, the * allows you to
#                  |            |accept an arbitrary number of
#                  |            |arguments.
#                  |            |
#   /              |Forward     |Used as a division sign when
#                  |slash       |performing mathematical
#                  |            |operations.
#                  |            |
#   =              |Equals sign |Used to create variables or to set
#                  |            |one value to equal another.
#                  |            |Can be paried with other operators
#                  |            |like +
#                  |            | e.g.a += b
#                  |            |
#   %              |Modulo sign\|Used as modulo in mathematical
#                  |formatter   |operations(returns remainder after
#                  |            |division).
#                  |            |Also used as a formatter when using
#                  |            |format strings(only used in
#                  |            |python 2.x)
#                  |            |
#   <              |Less than   |Return TRUE if value on the left
#                  | sign       |is less than that on the right,
#                  |            |else return FALSE.
#                  |            |
#   >              |Greater than|Return TRUE if value on the left,
#                  | sign       |is greater than that on the right,
#                  |            |else return FALSE.
#                  |            |
#   <=             |Less than   |Return TRUE if value on the left,
#                  | or equal   |is less or equal than on the right,
#                  |   to sign  |else return FALSE.
#                  |            |
#   >=             |Greater than|Return TRUE if value on the left,
#                  | or equal   |is greater or equal than that
#                  |  to sign   |on the right, else return FALSE.
#                  |            |
#   ===            |Comparison  |Returns TRUE if the value on the
#                  | operator   |left is exactly same as the value
#                  |            |on the right. Else returns FALSE.
#                  |            |Can be used to campare strings,
#                  |            |boolean operators, integers etc.
#                  |            |Concerned with 'equality' and not
#                  |            |'sameness'.
#                  |            |Concomitantly,distinct from is which
#                  |            |checks if the values are literally
#                  |            |refering to the same instance of a
#                  |            |value.
#                  |            |
#   {}             |Curly       |Used in positional formatting when
#                  | brackets   |using format strings.
#                  |            |
#   .format()      |Function    |Replacement for the % used in format
#                  |            |strings. Has form '.format(a, b)'.
#                  |            |
#   input()        |Function    |Receives an input from user via the
#                  |            |keyboard.
#                  |            |
#   from           |Part of an  |Used to import external modules into
#                  | import     |a script.
#                  |  statement |
#                  |            |
#   import         |Import      |Another import statement. Similar
#                  | statement  |to from.
#                  |            |
#   argv           |Attribute   |Accept a list of command line
#                  | of (sys)   |arguments passed to it when
#                  |  module    |running a script.
#                  |            |Must be imported from the (SYS)
#                  |            |module.
#                  |            |
#   open()         |Function    |Opens a file and returns the
#                  |            |corresponding file object.
#                  |            |
#   read()         |Function    |Reads the contents of a file object.
#                  |            |
#   write()        |Function    |Writes the contents of a string to
#                  |            |a file
#                  |            |
#   close()        |Function    |Closes an open file object.
#                  |            |
#   def            |Function    |Used to create user defined
#                  | defenition |function object.This allows you to
#                  |            |create your own function.
#                  |            |
#   *args          |Arbitrary   |Allows a function to accept an
#                  | argument   |arbitrary argument list. Used for
#                  |            |when you don't know how many
#                  |            |arguments are going to be passed
#                  |            |to a function.
#                  |            |
#   seek()         |Method      |Sets the file's current position at
#                  |            |the offset. Default position is 0
#                  |            |so starts at the start of the file.
#                  |            |
#   readline()     |Method      |Reads a single line from a file.
#                  |            |A neline character is left at the
#                  |            |end of the string so will
#                  |            |automatically read the next line
#                  |            |until the end of the file each time
#                  |            |it's called.
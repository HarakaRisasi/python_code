import subprocess
subprocess.call("clear")

x_set = [1, 1, 2, 3, 2, 6, 8, 3, 4, 5]
y, z = [], []

x_set = set(x_set)

for x_set in x_set:
    if (x_set % 2 == 0):
        y.append(x_set)
    else:
        z.append(x_set)
        
print(f'even {y} and odd {z}') #>> even [2, 4, 6, 8] and odd [1, 3, 5]

# the same words
x = '''
    Two households, both alike in dignity,
    In fair Verona, where we lay our scene,
    From ancient grudge break to new mutiny,
    Where civil blood makes civil hands unclean.
    From forth the fatal loins of these two foes
    A pair of star-cross'd lovers take their life;
    Whose misadventur'd piteous overthrows
    Doth with their death bury their parents' strife.
    The fearful passage of their death-mark'd love,
    And the continuance of their parents' rage,
    Which, but their children's end, naught could remove,
    Is now the two hours' traffic of our stage;
    The which if you with patient ears attend,
    What here shall miss, our toil shall strive to mend.
'''

y = '''
He stood with his hands clasped behind him, waiting for the lieutenant or somebody to deign to notice him. Somebody would have to pay some attention to him sooner or later.

Or would they?

Wouldn't it be just like the old timers to let him stand around and let the ship take off without him, all because he hadn't followed the proper procedure—a procedure he couldn't know? All he had been instructed to do was "report to the Gorgon." How do you report to a spaceship? Say, "Hello, spaceship?" Speak to the captain? The first mate? And where did he find them?

Starbuck felt a moment of panic. He could see himself standing on the platform while the Gorgon blasted off, carrying with it his Swabber's rating, his Master's degree and his future.

The lieutenant's back, in uniform black, loomed up before him. He would have to try approaching him again. It might mean solitary confinement for a month or two where no member of the crew would speak to him. It might even mean a flogging. Nobody knew much about what went on on board an exploration ship, despite all the stories. But Starbuck knew he would have to risk it.

He marched up behind the officer. "Sir," he said. "I'm the new man."

The lieutenant whirled. "The new man!"

For the first time, Starbuck noticed that the junior officer carried a swagger stick under his left arm, black, about a foot and a half long, tipped with silver at both ends. Quite possibly it was standard procedure to rap a man with it three times sharply across the mouth for speaking out of turn, during his probationary period. Cautiously, he filled a little pocket of air between his lips and his teeth to try to keep them from being knocked loose.

The lieutenant dropped his clipboard and swagger stick on the platform. "Why didn't you say so! New man, eh?" He gripped Starbuck by the shoulders of his new, store-bought uniform. "Let me look at you, son. Got some muscles there, haven't you? Ha, ha. Don't expect you'll need them too much on board. We don't work our men too hard. My name's Sam Frawley. Call me Sam. Come on, let me show you around."

Sam Frawley scooped up his stick and board with one hand and draped the other arm around Starbuck's shoulders, leading him towards a hoist.

It was not quite what Starbuck had expected for a reception.
'''
# The main issue you have is that you're assigning 
# the method content.split to content, 
# rather than calling it and assigning its return value. 
# If you print out content after that assignment, 
# it will be: <built-in method split of str object at 0x100894200> 
# which is not what you want. 
# Fix it by adding parentheses

def separate_word(txt):
    import re # regular expression
    txt = txt.replace('\n', '') # remove newline
    txt = re.sub(r'[^\w]', ' ', txt) # remove . and ,
    txt = txt.split() # divide the text into separate words
    txt = map(lambda txt: txt.lower(), txt) # make every word to lowercase
    txt = set(txt) # remove duplicate words
    txt = sorted(txt) # sorting word list
    
    return txt

txt = separate_word(x + y) # combine lists 

for i, j in enumerate(list(txt), start= 1): # print the result as a numbered list
    print(i, j)
# AI v0.5

import time
import datetime
import random
from abc import ABCMeta, abstractmethod


class Environment:
    version = 'v0.5'

    def __init__(self, name, ai, human):
        self.name = name
        self.ai = ai
        self.human = human
        self.running = True

    def print_greetings(self):
        print 'Loading  AI %s' % (self.version)
        services.sleep(services.long_pause)
        print ''

    def run(self):
        self.print_greetings()

        text = services.choose_random(polly_text)
        ai.say(text)
        
        while env.running:
            answer = human.write()
            
            if answer[:3].lower() == 'bye':
                bye_text = services.choose_random(polly_bye)
                ai.say(bye_text)
                services.sleep(services.long_pause)
                env.running = False
                break
                
            ai.read_user_input(answer)


class Person:
    def __init__(self, name):
        self.name = name

    def say(self, text):
        typewriter.type_line(self, text)

    def draw(self, text):
        typewriter.draw(self, text)


class Human(Person):
    def write(self):
        typewriter.type_person_name(self)
        return raw_input()


class AI(Person):
    def read_user_input(self, user_input):
        split_input = text_decoder.split_line(user_input)
        self.say('you said "%s"' % user_input)
        print split_input


class TextDecoder:
    sing_cleaning = ".,!:;()"

    def split_line(self, user_input):
        user_input = str.lower(user_input)

        user_clean_input = ""
        for letter in user_input:
            if letter in "'?":
                user_clean_input += " " + letter
                continue

            if letter not in self.sing_cleaning and letter != "\"":
                user_clean_input += letter
            else:
                user_clean_input += " "

        user_words = user_clean_input.split()

        return user_words


class AnswerSets:
    def __init__(self):
        self.c_dict = dict()

        self.c_dict[('tell', 'me', 'the', 'time'),
                    ('what', 'time', 'is', 'it')] = (('Time is ',),
                                                     (eval('services.get_time()'),))
        self.c_dict[('nice', 'meet', 'you'),] = ('Nice to meet you, too',)
        self.c_dict[('pleased', 'meet', 'you'),] = ('Pleased to meet you, too',)
        self.c_dict[('bye',),] = ("Have a nice day","Have a nice time","Good bye",
                                  "See you, bye", "Pleased to talk to you", "See you",
                                  "Thank you for talking","Pleased to see you")
        self.c_dict[('what', 'your', 'name'),] = ("My name is ",),("AI","Artificial Intelligence")
        self.c_dict[('who', 'are', 'you'),] = [(("I am ",),
                                                ("an artificial intelligence","AI","a robot",
                                                 "the future of technologies","an electric mind",
                                                 "an electrical lifeform", "a brain made with transistors")),
                                                (("My name is ","Humans call me ","They call me ","I guess ",
                                                  "I read in the memory that my name is ", "It is known my name is ",
                                                  "Everyone knows that I am "),
                                                 ("AI", "an artificial intellegence", "a robot", "an electric brain",
                                                  "a smart guy", " a computer", "a PC",
                                                  "that thing... uh-uh... sorry, you know what I mean",
                                                  "a stupid thing", "a semiconductor trash"))]
        self.c_dict[('how', 'are', 'you'),] = (("I'm fine", "I'm ok", "I'm pretty well", "I'm great",
                                                "I'm super", "I'm fantastic", "Fine", "Ok", "Pretty well",
                                                "Great", "Super", "Fantastic"),
                                               ("","",". Thanks",". Thanks",". Thanks, and you?"))
        self.c_dict[("how", "do", 'you', "work"),] = [(("My ", "The ", "This "),
                                                       ("program ","algorithm "),
                                                       ("devides ","splits "),
                                                       ("the ",),
                                                       ("phrase ","sentence ","statement ","clause "),
                                                       ("and ",),
                                                       ("find ","look for ","search "),
                                                       ("key words in the ",),
                                                       ("dictionary","memory cells","matrix")),
                                                      (("My ", "The "),
                                                       ("dictionary is being ",),
                                                       ("appended ","added ", "updated "),
                                                       ("by ",),
                                                       ("users","humans","interlocutors",)),
                                                      (("I ",),
                                                       ("use ", "apply ", "employ "),
                                                       ("all of my ",),
                                                       ("knowledge ","information "),
                                                       ("in working","in talking","in conclusions", "in logic deduction")),
                                                      (("My ", "The ", "This "),
                                                       ("program ","method ","algorithm "),
                                                       ("works with ","uses ", "combines "),
                                                       ("word ",),
                                                       ("associations ","sets "," meanings",)),
                                                      (("I ",),
                                                       ("analyze ","explore ", "treat ", "refine ", "try to understand "),
                                                       ("every ","each "),
                                                       ("phrase ","sentence ","statement ","clause "),
                                                       ("you ",),
                                                       ("write ","say ","use "),
                                                       ("and ",),
                                                       ("keep ","remember ","record ", "retain ", "set ", "put "),
                                                       ("it in ",),
                                                       ("my ","the "),
                                                       ("memory","cells","matrix",)),
                                                      (("I ",),
                                                       ("look for ","search ", "treat ", "refine ", "try to understand "),
                                                       ("the parts of speech in ",),
                                                       ("phrases","sentences","statements"),
                                                       (", then ",),
                                                       ("write them down for ","match them to ","choose every one for "),
                                                       ("special questions.",))]
        self.c_dict[("what", "'s", 'up'),] = ("Nothing", "Nothing much", "Not much","The sky","The ceiling")
        self.c_dict[('who', 'am', 'i'),] = (("You are ",),
                                            ("a user","a person of minkind","a human being","a kind of organic substance",
                                             "a biological specimen", "a non-electrical lifeform"))


class Typewriter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def type_person_name(self, person):
        pass

    @abstractmethod
    def draw(self, person, text):
        pass

    @abstractmethod
    def type_line(self, person, text):
        pass


class ConsoleTypewriter(Typewriter):
    sleep_signs = ['.', '?', '!']

    def type_person_name(self, person):
        print '%s:\t' % (person.name),
        services.sleep(services.long_pause)

    def draw(self, person, text):
        self.type_person_name(person)
        print text

    def type_line(self, person, text):
        self.type_person_name(person)
        split_text = text.split()

        for word in split_text:
            services.sleep(services.short_pause)
            print word,

            for sign in self.sleep_signs:
                if sign in word:
                    services.sleep(services.long_pause)

        last_symbol = split_text[-1][-1]
        if last_symbol not in self.sleep_signs:
            services.sleep(services.long_pause)

        print ''


class Services:
    def __init__(self, short_pause=0.12, long_pause=0.7):
        self.short_pause = short_pause
        self.long_pause = long_pause

    def get_time(self):
        now_time = datetime.datetime.now()
        now_time = now_time.strftime("%H:%M:%S")
        return now_time

    def choose_random(self, collection):
        random.seed(random.random())
        return random.choice(collection)

    def sleep(self, duration):
        time.sleep(duration)


ai = AI('Polly')
human = Human('User')
env = Environment('world', ai, human)
typewriter = ConsoleTypewriter()
services = Services()
text_decoder = TextDecoder()
answer_sets = AnswerSets()

polly_text = ("Hello, my name is Polly. What is your name?",)

polly_bye = ("Have a nice day", "Have a nice time", "Good bye",
             "See you, bye", "Pleased to talk to you", "See you",
             "Thank you for talking", "Pleased to see you", "Bye-bye")

env.run()



'''

def analyze_text(user_input, c_dict):    
    for c_tuple in c_dict:
        
        for a_tuple in c_tuple:
            count = 0
        
            for word in a_tuple:
                for mean in user_input:
                    if word == mean:           
                        count += 1

            if count >= len(a_tuple):
                answer = choose_general_answer(c_dict[c_tuple])
                return type_line(answer, ai)
                break


def choose_general_answer(answer):
    if type(answer) == list:
        rand_answer = choose_random(answer)
        return make_answer(rand_answer)
    elif type(answer) == tuple:
        return make_answer(answer)
    else:
        return "nothing"


def make_answer(answer):
    rand_answer = ''
    
    for item in answer:
        if type(item) == str:
            if rand_answer == '':
                rand_answer += choose_random(answer)
                break
            else:
                return
        else:
            make_answer(item)

        rand_answer += choose_random(item)

    return rand_answer

'''


raw_input()

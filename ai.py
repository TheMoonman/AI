# AI v0.5

import time
import datetime
import random
import traceback
import math
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

        text = services.choose_random(polly_hello)
        ai.say(text)
        answer = human.write()
        if answer == '':
            answer = 'Anonymous'
        ai.say('Hello, %s' % (answer))

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
        typewriter.type_person_line(self, text)

    def draw(self, text):
        typewriter.draw(self, text)


class Human(Person):
    def write(self):
        typewriter.type_person_name(self)
        return raw_input()


class AI(Person):
    def read_user_input(self, user_input):
        split_input = text_decoder.split_line(user_input)
        answer = text_analyzer.analyze(split_input)
        self.say(answer)


class TextDecoder:
    sing_cleaning = ".,!:;()"

    def split_line(self, user_input):
        user_input = str.lower(user_input)

        user_clean_input = ""
        for letter in user_input:
            if letter in "'" and letter in "'?":
                user_clean_input += " " + letter
                continue

            if letter not in self.sing_cleaning and letter != "\"":
                user_clean_input += letter
            else:
                user_clean_input += " "

        user_words = user_clean_input.split()

        return user_words


class TextAnalyzer:
    def analyze(self, split_input):
        for key in answer_sets.answer_dict:
            key_iter = iter(key)
            cur_key_word = services.try_next(key_iter)

            for user_word in split_input:
                if user_word == cur_key_word:
                    cur_key_word = services.try_next(key_iter)

                    if cur_key_word is None:
                        answer = answer_sets.answer_dict[key]
                        if answer.strip() == 'calc':
                            return str(calc())
                        return answer_synth.synth_answer(answer)
        return "What?"


class AnswerSynth:
    def synth_answer(self, answer):
        return self.choose_general_answer(answer)

    def choose_general_answer(self, answer):
        if type(answer) == list:
            rand_answer = services.choose_random(answer)
            return self.make_answer(rand_answer)
        elif type(answer) == tuple:
            return self.make_answer(answer)
        else:
            return answer

    def make_answer(self, answer_set):
        rand_answer = ''

        for item in answer_set:
            if type(item) == str:
                rand_answer += services.choose_random(answer_set)
                break
            else:
                rand_answer += self.make_answer(item)

        return rand_answer


class AnswerSets:
    def __init__(self):
        self.answer_dict = dict()
        self.splitter = '>>>'

        f = open('dict.txt')
        for line in f:
            if self.splitter not in line:
                continue
            split_line = line.split(self.splitter)
            key, value = split_line
            split_key = tuple(key.split())
            self.answer_dict[split_key] = value


class Typewriter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def type_person_name(self, person):
        pass

    @abstractmethod
    def draw(self, person, text):
        pass

    @abstractmethod
    def type_line(self, text):
        pass

    @abstractmethod
    def type_person_line(self, person, text):
        pass


class ConsoleTypewriter(Typewriter):
    sleep_signs = ['.', '?', '!']

    def type_person_name(self, person):
        print '%s:\t' % (person.name),
        services.sleep(services.long_pause)

    def draw(self, person, text):
        self.type_person_name(person)
        print text

    def type_line(self, text):
        print text

    def type_person_line(self, person, text):
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
        now_time = now_time.strftime("%H:%M")
        return now_time

    def choose_random(self, collection):
        random.seed(random.random())
        return random.choice(collection)

    def sleep(self, duration):
        time.sleep(duration)

    def try_next(self, iterator):
        try:
            return iterator.next()
        except StopIteration:
            return None


class Calc:
    def __init__(self, a=0.0, b=0.0,
                 func_string='a + b', round=3,
                 phrase='The result for a and b is'):
        (filename, line_number, function_name, text) = \
            traceback.extract_stack()[-2]
        self.name = text[:text.find('=')].strip()
        self.func_string = func_string
        self.func = None
        self.round = round
        self.a = a
        self.b = b
        self.phrase = phrase

    def set_func(self, func_string):
        exec('%s.func = lambda a,b: %s' % (self.name, func_string))
        self.func_string = func_string

    def get_func(self):
        return self.func_string

    def func(self, a, b):
        return self.func(a, b), 3

    def __call__(self):
        try:
            if self.func is None:
                self.set_func(self.func_string)
            result = round(self.func(float(self.a),
                           float(self.b)), self.round)
            return '%s %s' % (self.phrase, result)
        except Exception, message:
            return 'error: %s' % message


ai = AI('Polly')
human = Human('User')
env = Environment('world', ai, human)
typewriter = ConsoleTypewriter()
services = Services()
text_decoder = TextDecoder()
text_analyzer = TextAnalyzer()
answer_synth = AnswerSynth()
answer_sets = AnswerSets()
calc = Calc(7, 12, 'a*a + b*b', round=3, phrase='7*7 + 12*12 is equal')


polly_hello = ("Hello, my name is Polly. What is your name?",)

polly_bye = ("Have a nice day", "Have a nice time", "Good bye",
             "See you, bye", "Pleased to talk to you", "See you",
             "Thank you for talking", "Pleased to see you", "Bye-bye")

env.run()


raw_input()

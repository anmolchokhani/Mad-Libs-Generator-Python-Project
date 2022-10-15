#mad libs template
import os
import json

class MadLibs:
    def __init__(self, word_description, template):
        self.template= template
        self.word_description= word_description
        self.user_input = []
        self.story= None

    @classmethod
    def from_json(cls,name,path='./Templates'):
        fpath= os.path.join (path,name)
        with open(fpath,'r') as read_file:
            data=json.load(read_file)
        mad_lib= cls(**data)
        return mad_lib

    def get_words_from_user(self):
        for word in self.word_description:
            u_input=input(word+ " ")
            self.user_input.append(u_input)
        return self.user_input

    def build_story(self):
        self.story= self.template.format(*self.user_input)
        return self.story



template_name='day_at_the_zoo.json'
     
mad_lib= MadLibs.from_json(template_name)

words = mad_lib.get_words_from_user()

story= mad_lib.build_story()

print(story)

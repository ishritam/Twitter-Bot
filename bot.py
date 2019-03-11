import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import tweepy
import time
import re

print("hello i'm a twitter bot")


class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        
        
        self.lbl1 = Label(text="CONSUMER_KEY")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(hint_text = 'Enter CONSUMER_KEY Key', multiline=False)
        layout.add_widget(self.txt1)

        self.lbl2 = Label(text="CONSUMER_SECRET")
        layout.add_widget(self.lbl2)
        self.txt2 = TextInput(hint_text = 'Enter CONSUMER_SECRET Key', multiline=False)
        layout.add_widget(self.txt2)
        
        self.lbl3 = Label(text="ACCESS_KEY")
        layout.add_widget(self.lbl3)
        self.txt3 = TextInput(hint_text = 'Enter ACCESS_KEY ', multiline=False)
        layout.add_widget(self.txt3)
        
        self.lbl4 = Label(text="ACCESS_SECRET")
        layout.add_widget(self.lbl4)
        self.txt4 = TextInput(hint_text = 'Enter ACCESS_SECRET Key', multiline=False)
        layout.add_widget(self.txt4)
        
        btn1 = Button(text="Enter")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        return layout

    # button click function
    def buttonClicked(self,btn):
        
        self.lbl1.text = "You CONSUMER_KEY :  " + self.txt1.text
        self.lbl2.text = "You CONSUMER_SECRET :  " + self.txt2.text
        self.lbl3.text = "You ACCESS_KEY :  " + self.txt3.text
        self.lbl4.text = "You ACCESS_SECRET : " + self.txt4.text

   # def save(self):
        fob = open('test.txt','w')
        fob.write('CONSUMER_KEY:'+ self.txt1.text)
        fob.write("\n")
        fob.write('CONSUMER_SECRET:' +self.txt2.text)
        fob.write("\n")
        fob.write('ACCESS_KEY:' + self.txt3.text)
        fob.write("\n")
        fob.write('ACCESS_SECRET:' +self.txt4.text)
        fob.write("\n")

#red = open('test.txt','r')
#result = red.read()

#check_key = re.findall(r'(?<=:)\w+.*', result)

        CONSUMER_KEY = self.txt1.text
        CONSUMER_SECRET = self.txt2.text
        ACCESS_KEY = self.txt3.text
        ACCESS_SECRET = self.txt4.text

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)

        FILE_NAME = 'last_seen_id.txt'

        def retrieve_last_seen_id(file_name):
            f_read = open(file_name, 'r')
            last_seen_id = int(f_read.read().strip())
            f_read.close()
            return last_seen_id

        def store_last_seen_id(last_seen_id, file_name):
            f_write = open(file_name, 'w')
            f_write.write(str(last_seen_id))
            f_write.close()
            return
        dic = {'helloworld': ' HelloWorld we are back to you!','happybirthday': ' Thank You so much', 'happynewyear': ' Wish you a blissful and vibrant new year! May you accomplish and surmount all the hurdles of your life and pursue a good career','canteen': ' Hello! we will try to sort out your concern as soon as possible for further assistance please contact to our FIC canteen','registration': ' Hello! the registration for the semester will begin from August 2019 for any further query contact please to our Examination cell','library': ' Hey! we hope you are enjoying our volumes and references for any queries please contact to our library department','placement': ' Hey! we hope you are doing fine. this year about 20 students have 20+ job offers. to know about upcoming campus  drives and interviews please contact to our placement cell','informationcell': ' Hello! for any management related query and complaints we request you to visit our Information cell', 'hostel': ' a good accomodation gives a feeling of sweet home! if any problem befalls you can contact to our respective wardens','accountsection': '  thank you for bringing up your concern we request all of you to clear your dues for smooth regulation and functioning of the management for any other queries contact to our account section department','happyindependenceday': 'wish you the same !it will be very grateful if all the students come and witness the morning parade followed by speech and functions','happyrepublicday': 'wish you the same !it will be very grateful if all the students come and witness the morning parade followed by speech and functions','happydurgapuja': ' wish you the same','happyholi': ' let us celebrate the colour of love and spread joy wish you all happy holi','happydiwali': ' wish you a happy and prosperous diwali too! it will be a great honor for us to invite all the siliconites to celebrate the evening pooja followed by Dj night for any queries please contact to our respective secretaries'}

        def reply_to_tweets():
            print('retrieving and replying to tweets...', flush=True)
            last_seen_id = retrieve_last_seen_id(FILE_NAME)
     #NOTE: We need to use tweet_mode='extended' below to show
     #all full tweets (with full_text). Without it, long tweets
     #would be cut off. '''
            mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')

            for mention in reversed(mentions):
                 #mention.favorite()

                 print(str(mention.id) + ' - ' + mention.full_text)
                 last_seen_id = mention.id
                 store_last_seen_id(last_seen_id, FILE_NAME)
                 text = mention.full_text.lower()
                 items = re.search(r'(?<=#)\w+', text)
                 
         #for i in dic:
                 if items[0] in dic:
                     print(f'found {items[0]}', flush=True)
                     print('responding back...', flush=True)
                     api.update_status('@' + mention.user.screen_name + dic[items[0]], mention.id)
                     mention.favorite()
                 else:
                     print("Not found!")
        def follow_people():
            user = api.me()
            print (user.name)

            for follower in tweepy.Cursor(api.followers).items():
                    follower.follow()
            print("Followed everyone that is following " + user.name)


        while True:
        #MyApp().run()
            reply_to_tweets()
            follow_people()
            time.sleep(5)


if __name__ == "__main__":
    MyApp().run()


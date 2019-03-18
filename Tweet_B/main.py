import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.base import runTouchApp

import tweepy
import time
import re

import smtplib
import email.utils




print("hello i'm a twitter bot")


class MyApp(App):
# layout

    def build(self):
        layout = BoxLayout(padding= 3, orientation='vertical', spacing=10)

        self.lbl0 = Label(text='[u][color=ff0066][b]Welcome[/b][/color] To [b][color=ff9933]TweetB[/b]', markup = True)
        layout.add_widget(self.lbl0)

        self.lbl1 = Label(text="E-mail id", font_size='25')
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(hint_text = 'Enter your e-mail i.d', multiline=False)
        layout.add_widget(self.txt1)

        self.lbl2 = Label(text="CONSUMER_KEY", font_size='25')
        layout.add_widget(self.lbl2)
        self.txt2 = TextInput(hint_text = 'Enter CONSUMER_KEY Key', multiline=False,)
        layout.add_widget(self.txt2)

        self.lbl3 = Label(text="CONSUMER_SECRET", font_size='25')
        layout.add_widget(self.lbl3)
        self.txt3 = TextInput(hint_text = 'Enter CONSUMER_SECRET Key', multiline=False)
        layout.add_widget(self.txt3)

        self.lbl4 = Label(text="ACCESS_KEY", font_size='25')
        layout.add_widget(self.lbl4)
        self.txt4 = TextInput(hint_text = 'Enter ACCESS_KEY ', multiline=False)
        layout.add_widget(self.txt4)

        self.lbl5 = Label(text="ACCESS_SECRET", font_size='25')
        layout.add_widget(self.lbl5)
        self.txt5 = TextInput(hint_text = 'Enter ACCESS_SECRET Key', multiline=False)
        layout.add_widget(self.txt5)

        btn1 = Button(text="Enter")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        return layout

    # button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "Email Id:  " + self.txt1.text
        self.lbl2.text = "You CONSUMER_KEY :  " + self.txt2.text
        self.lbl3.text = "You CONSUMER_SECRET :  " + self.txt3.text
        self.lbl4.text = "You ACCESS_KEY :  " + self.txt4.text
        self.lbl5.text = "You ACCESS_SECRET : " + self.txt5.text

   # def save(self):
        fob = open('test.txt','w',newline='\n')
        fob.write('E-mail:'+ self.txt1.text)
        fob.write("\n")
        fob.write('CONSUMER_KEY:'+ self.txt2.text)
        fob.write("\n")
        fob.write('CONSUMER_SECRET:' +self.txt3.text)
        fob.write("\n")
        fob.write('ACCESS_KEY:' + self.txt4.text)
        fob.write("\n")
        fob.write('ACCESS_SECRET:' +self.txt5.text)
        fob.write("\n")

#red = open('test.txt','r')
#result = red.read()

#check_key = re.findall(r'(?<=:)\w+.*', result)

        CONSUMER_KEY = self.txt2.text
        CONSUMER_SECRET = self.txt3.text
        ACCESS_KEY = self.txt4.text
        ACCESS_SECRET = self.txt5.text

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)

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
        dic = {'helloworld': ' HelloWorld we are back to you!','happybirthday': ' Thank You so much', 'happynewyear': ' Wish you a blissful and vibrant new year! May you accomplish and surmount all the hurdles of your life and pursue a good career','canteen': ' Hello! we will try to sort out your concern as soon as possible for further assistance please contact to our FIC canteen','registration': ' Hello! the registration for the semester will begin from August 2019 for any further query contact please to our Examination cell','library': ' Hey! we hope you are enjoying our volumes and references for any queries please contact to our library department','placement': ' Hey! we hope you are doing fine. this year about 20 students have 20+ job offers. to know about upcoming campus  drives and interviews please contact to our placement cell','informationcell': ' Hello! for any management related query and complaints we request you to visit our Information cell', 'hostel': ' a good accomodation gives a feeling of sweet home! if any problem befalls you can contact to our respective wardens','accountsection': '  thank you for bringing up your concern we request all of you to clear your dues for smooth regulation and functioning of the management for any other queries contact to our account section department','happyindependenceday': 'wish you the same !it will be very grateful if all the students come and witness the morning parade followed by speech and functions','happyrepublicday': 'wish you the same !it will be very grateful if all the students come and witness the morning parade followed by speech and functions','happydurgapuja': ' wish you the same','happyholi': ' let us celebrate the colour of love and spread joy wish you all happy holi','happydiwali': ' wish you a happy and prosperous diwali too! it will be a great honor for us to invite all the siliconites to celebrate the evening pooja followed by Dj night for any queries please contact to our respective secretaries', "lohri": " Wish you a blissful lohri too","MakarSankranti": " Wish you a blissful makarsankranti too","Pongal": " Wish you a blissful Pongal too","Valentine'sDay": " we hope you had a day well spent with your beloved","WomensDay ": " Thank you so much.Let's celebrate the fabulous achievements of women, while collectively we forge a more gender-balanced world ","Holi": " Wish you a blissful and a colorful Holi too","EarthDay": " Change starts with each and everyone of us.Earth Day and Oceans Day are coming. Instead of celebrations, we need ACTIONS!.Share your voice, your little actions with the world. Because little actions DO matter!","Easter": " The story of Easter is the story of Godís wonderful window of divine surprise.Happy Easter ","GoodFriday": " Practice mercy and forgiveness throughout as a lesson that symbolizes the love shown through his crucifixion.It is the resurrection that makes Good Friday good","RamaNavami": " Thank You. Happy Ram Navami !","HanumanJayanti": " Thank You. Happy Hanuman Jayanti!","Gangaur": " wish you the same","MayDay": " You can cut all the flowers but you cannot keep spring from coming.Happy May Day","LaborDay": " Work is no disgrace,the disgrace is idleness Happy Labors Day","RathaYatra": " May Lord Krishna bless you and your family on this holy occassion of Rath Yatra, and bring lifetime of happiness. Happy Rath Yatra.","WorldEnvironmentDay": " The nature is our silent friend and family. it protects us if we protect it happy world environment day!","GuruPurnima": " May you find happiness and peace with the blessings of Guru Nanak Dev Ji Happy GuruPurnima","RakshaBandhan": " Siblings are like streetlights along the road,They donít make the distance any shorter,But they light up the path and make the walk worthwhile.Happy Raksha Bandhan!","Eid": " Eid Mubarak to you and your family Hope your home is filled with good cheer on and always!","FriendshipDay": " Thank you for considering me an important part of your life,you are like a diamond to my ring who helps me to gather the valour for my dream A happy friendship day to you too buddy! ","GaneshaChaturthi": " Wishing you a Happy Vinayak Chaturthi too. May the grace of God keep enlightening your lives and bless you always.","InternationalDayofPeace": " A smile marks the starting of peaceÖ.. Keep smiling and keep spreading peace around!!!","Halloween": " Trick or treat!happy halloween to you too","Navratri": " Wishing you fantastic nine nights of devotion, spirituality, and happiness. May Maa shower her choicest blessings over you. Happy Navratri! to you too","GandhiJayanti": " Be the change that you wish to see in the world.í ñ Wish you a very Happy Gandhi Jayanti","Diwali": " May thousand of lamps light up your life with endless happiness, richness, health and wealth forever wishing you and your family a very Happy Diwali to you too","BodhiDay": " A blissful bodhi day to you too","ChristmasEve": " A silent night, a star above, a blessed gift of hope and love.wish you a merry christmas ","ChristmasDay": " A silent night, a star above, a blessed gift of hope and love.wish you a merry christmas","HumanRightsDay": " Human Rights Day Is A Reminder Of How Undemocratic Systems Of Government And Abuse Of Authority Can Lead To Injustice, Oppression And Violence","International Day of Disabled": " A hero is an ordinary individual who finds the strength to persevere and endure in spite of overwhelming obstacles.Happy International Day of Disabled","MahaShivaratri": " Om Namah Shivaya! Happy Maha Shivratri to you too!","Janamashtami": " Happy Janmashtami May lord krishna showers all his blessing on U.May U get a lot of Happines in lifeÖ Jay shri krishna","Onam": " Wishing you and all your family members a Happy Onam too.","VasantPanchami": " May Goddess Saraswati bless your life with success, happiness, love and warmth. Happy Basant Panchami to you and your entire family ","Vaisakhi": " wish you a very Happy Baisakhi. May Wahe Guruji accept your good deeds, bring all the years full of love and contentment.","WhoAreYou": " I am good! What about you?","Whatdoyoudo": " I work for humans.","Howoldareyou": " I am old enough that the users trust me to use there Twitter!","MensDay":" Thank you so much"}

        def reply_to_tweets():
            print('retrieving and replying to tweets...', flush=True)
            last_seen_id = retrieve_last_seen_id(FILE_NAME)
     #NOTE: We need to use tweet_mode='extended' below to show
     #all full tweets (with full_text). Without it, long tweets
     #would be cut off. '''
            mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended', count=1)


            for status in tweepy.Cursor(api.user_timeline).items():
                try:
                    api.destroy_status(status.id)
                except:
                    pass

            for mention in reversed(mentions):
                 if not mention.favorited:
                     mention.favorite()


                 print(str(mention.id) + ' - ' + mention.full_text)
                 last_seen_id = mention.id
                 store_last_seen_id(last_seen_id, FILE_NAME)
                 text = mention.full_text.lower()
                 items = re.findall(r'(?<=#)\w+', text)


                 for i in items:
                     if i not in dic:
                         api.update_status('@' + mention.user.screen_name + " Happy to see you today! We'll contact you soon.", mention.id)

                         email = 'mysmarttwitterbot@gmail.com'
                         password = 'Project@123'
                         send_to_email = self.txt1.text
                         message = "Hi Boss! You have got a tweet from @"+ mention.user.screen_name + " I think you should have a look at it. \n Have a great day Boss;) "

                         server = smtplib.SMTP('smtp.gmail.com', 587)
                         server.starttls()
                         server.login(email, password)
                         server.sendmail(email, send_to_email , message)
                         server.quit()

                     else:
                         print(f'found {items[0]}', flush=True)
                         print('responding back...', flush=True)
                         api.update_status('@' + mention.user.screen_name + dic[i], mention.id)

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

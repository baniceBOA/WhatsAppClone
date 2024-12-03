import kivy
from kivymd.app import MDApp, App
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty, ListProperty, StringProperty, BooleanProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDIcon
from kivy.graphics import Color, Line
from kivy.lang import Builder
import random
print(kivy.__version__)

kv = '''
#: import Window kivy.core.window.Window
<CustomIcon>:
<StatusCard>:
    size_hint:(None,None)
    size:(250,450)
    MDCard:
        size_hint:(None, None)
        size: self.parent.size
        radius:self.width*0.1
        FitImage:
            source:root.status_image
            radius:self.parent.radius
    FitImage:
        canvas.after:
            Color:
                rgba:(0,0.9, 0,1)
            Line:
                width:dp(1.5)
                ellipse:(self.x-dp(4),self.y-dp(4), self.width+dp(8),self.height+dp(8))
        source:root.avatar
        size_hint:(None, None)
        size:(dp(40), dp(40))
        radius:self.width/2
        pos_hint:{'top':0.95,'center_x':0.20}
    
<UpdatesScreen>:
    MDBoxLayout:
        pos_hint:{'top':0.7}
        MDBoxLayout:
            orientation:'vertical'
            size_hint_y:None
            height:Window.size[1] + dp(100)
            
            
            MDBoxLayout:
                orientation:'vertical'
                height:(self.parent.height)*0.3
                #md_bg_color:app.theme_cls.primary_color
                MDLabel:
                    text:'Status'
                    bold:True
                    font_size:dp(14)
                    font_style:'Body1'
                    padding:dp(8)
                    size_hint_y:None
                    height:self.texture_size[1]+dp(4)
                    valign:'center'
                MDScrollView:
                    size_hint_y:None
                    height:self.parent.height-dp(18)
                    do_scroll_y:False
                    do_scroll_x:True
                    
                    MDBoxLayout:
                        id: status_card_box
                        orientation:'horizontal'
                        size_hint_x:None
                        width:self.minimum_width
                        padding:dp(2)
                        spacing:dp(5)
                        
                        
            MDScrollView:
                size_hint_y:None
                height:(self.parent.height)*0.7
                MDBoxLayout:
                    orientation:'vertical'
                    adaptive_height:True
                    MDRelativeLayout:
                        size_hint_y:None
                        height:dp(50)
                        MDLabel:
                            text:'Channels'
                            bold:True
                            font_style:'Caption'
                            font_size:dp(20)
                            valign:'center'
                            padding:dp(15)
                            pos_hint:{'left':1}
                        MDRoundFlatButton:
                            text:'Explore'
                            pos_hint:{'right':0.9}
                        
                    MDList:
                        id:channel_box
                    MDRoundFlatButton:
                        text:'Explore more'
    MDIconButton:
        pos_hint:{'top':0.2, 'right':0.95}
        icon:'pencil'
        radius:self.width*0.2
        md_bg_color:app.theme_cls.primary_light
    MDFloatingActionButton:
        pos_hint:{'top':0.1, 'right':0.95}
        icon:'camera'
                
                
                    
                    
                        
    
    
<ChatItem>:
    size_hint_y:None
    height:self.children[0].height
    TwoLineAvatarListItem:
        text:root.name
        secondary_text:root.message
        _no_ripple_effect:True
        ImageLeftWidget:
            canvas.after:
                Color:
                    rgba:(1,1,1,0.5) #if not root.status else app.theme_cls.primary_color
                Line:
                    width:dp(1.5)
                    ellipse:(self.x-dp(4),self.y-dp(4), self.width+dp(8),self.height+dp(8))
            source:root.avatar
            radius:self.width
    
    MDLabel:
        text:root.date
        font_size:dp(8)
        size_hint_y:None
        height:self.texture_size[1]+dp(8)
        padding:dp(5)
        pos_hint:{'top':0.1, 'center_x':1.3}
    CustomIcon:
        icon:'numeric-1' if root.status else ''
        pos_hint:{'center_y':.5, 'center_x':0.90}
        font_size:dp(12)
        theme_text_color:'Custom'
        text_color:'white'
        canvas.before:
            Color:
                rgb:app.theme_cls.primary_color
            Line:
                width:dp(10)
                ellipse:(self.x+dp(5),self.y+dp(5), self.width-dp(10),self.height-dp(10))
                
        
<ChatScreen>:
    chats:chats
    size_hint_y:.92
   
    MDScrollView:
        MDBoxLayout:
            orientation:'vertical'
            adaptive_height:True
            
            MDScrollView:
                size_hint_y:None
                height:dp(60)
                do_scroll_y:False
                do_scroll_x:True
                MDBoxLayout:
                    orientation:'horizontal'
                    size_hint_y:None
                    height:self.parent.height
                    adaptive_width:True
                    padding:dp(10)
                    spacing:dp(12)
                    MDChip:
                        text:'All'
                        icon:'plus'
                        theme_text_color:'Custom'
                        text_color:(1,0,0,1)
                    MDChip:
                        text:'Groups'
                    MDChip:
                        text:'Unread'
                    MDChip:
                        text:'Favourite'
                    MDChip:
                        icon:'plus'
                        
                    
            MDList:
                id:chats
    MDFloatingActionButton:
        pos_hint:{'right':0.95,'top':0.1}
        icon:'plus'
    
MDScreen:
      
    MDBottomNavigation:
        on_switch_tabs:app.change_app_bar(*args)
        MDBottomNavigationItem:
            name:'screen 1'
            text:'Chats'
            icon:'message'
            #on_tab_press:app.theme_cls.theme_style='Light'
            ChatScreen:
                
                id:chats_screen
                
        MDBottomNavigationItem:
            name:'screen 2'
            text:'updates'
            icon:'whatsapp'
            UpdatesScreen:
                id:update_screen
             
        MDBottomNavigationItem:
            name:'screen 3'
            text:'communities'
            icon:'group'
            MDScreen:
                size_hint_y:.92
                md_bg_color:app.theme_cls.primary_dark
                MDLabel:
                    text:'Comminties'
                    font_size:dp(40)
        MDBottomNavigationItem:
            name:'screen 4'
            text:'Calls'
            icon:'phone'
            MDScreen:
                size_hint_y:.92
                md_bg_color:app.theme_cls.primary_dark
                MDLabel:
                    text:'calls'
                    font_size:dp(40)
    MDTopAppBar:
        id:app_bar
        title:'WhatsApp'
        anchor_title:'left'
        pos_hint:{'top':1}
        right_action_items:[['camera-outline', lambda x:x],['magnify',lambda x:x], ['dots-vertical', lambda x:x]]
           
'''
class StatusCard(MDRelativeLayout):
    status_image = StringProperty()
    avatar = StringProperty()
    
    
class UpdatesScreen(MDScreen):
    pass
    
class CustomIcon(MDIcon):
    status = BooleanProperty()
    
    def on_status(self, instance, value ):
        app = App.get_running_app()
        if value:
            with self.canvas.before:
                Color(app.them_cls.primary_color)
                Line(ellipse=(self.x+dp(5),self.y+dp(5), self.width-dp(10),self.height-dp(10)))
class ChatItem(MDRelativeLayout):
    name = StringProperty()
    avatar = StringProperty()
    message = StringProperty()
    time = StringProperty()
    date = StringProperty()
    status = BooleanProperty(False)
    
    
class ChatScreen(MDScreen):
    chats = ObjectProperty()
    
class WhatsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.material_style = 'M3'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(kv)
    def on_switch_tabs(*args):
        print(args)
    def on_start(self):
        chats = [{
        'name':'Lilo',
        'avatar':'lilo.jpeg',
        'message':'Life is a very interesting jounery',
        'time':'12:12',
        'date':'12/10/2024',
        'status':False
 
        }]
        for i in range(10):
            self.root.ids.chats_screen.ids.chats.add_widget(ChatItem(
            name=chats[0]['name'],
            avatar=f'img{i}.jpg',
            message = chats[0]['message'],
            time = chats[0]['time'],
            date = chats[0]['date'],
            status = True, #random.choice([True, False])
            ))
        status_box = self.root.ids.update_screen.ids.status_card_box
        for i in range(10):
            status_box.add_widget(StatusCard(status_image=f'img{i}.jpg', avatar='mine2.jpg'))
        channel_box = self.root.ids.update_screen.ids.channel_box
        for i in range(5):
            channel_box.add_widget(ChatItem(name='Channel', avatar=f'img{i}.jpg', message='This is nice'))
            
        print(status_box.children[:])
            
            
    def change_app_bar(self, instance_bottom_navigation, name_tab, name):
      
       
        self.root.ids.app_bar.title ='WhatsApp' if name_tab.text == 'Chats' else name_tab.text
        self.root.ids.app_bar.right_action_items =[['camera-outline', lambda x:x],['magnify',lambda x:x], ['dots-vertical', lambda x:x]]  if name_tab.text == 'Chats' else [ ['magnify',lambda x:x], ['dots-vertical', lambda x:x]]
        
            
if __name__ == '__main__':
        WhatsApp().run()
        
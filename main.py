from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.modalview import ModalView
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout









import sqlite3


class SearchView(Screen):
    pass


class FoodItems(Screen):
    pass


class MainUI(Screen):
    def __abs__(self, **kwargs):
        super().__init__(**kwargs)


    def card_fire(self):
        print("card fired !!")



class CalorieProMD(MDApp):

    def build(self):

        # set the UI themes and colors.
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lime"

        # set the Android Material design style.
        self.theme_cls.material_style = "M3"

        # initialize screen manager for the screens.
        screen_manager = ScreenManager()

        # add the 3 screens.
        screen_manager.add_widget(MainUI(name="main_ui"))
        screen_manager.add_widget(FoodItems(name="food_items"))
        screen_manager.add_widget(SearchView(name="search_view"))
        return screen_manager

    def card_fire(self):
        print("card fired !!")


CalorieProMD().run()




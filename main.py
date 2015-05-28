from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from api.endpoints import AllegroEndpoints
from credentials import API_KEY, LOGIN, PASSWORD

Window.size = (600 * 2/3, 1024 * 2/3)


class BaseLayout(BoxLayout):
    pass


class ItemsWidget(BoxLayout):
    pass


class MenuWidget(BoxLayout):
    def __init__(self, sm, screens, **kwargs):
        super(MenuWidget, self).__init__(**kwargs)
        self.menu_items = screens
        self.screen_manager = sm

    def load_home(self):
        print 'home!'
        self.screen_manager.current = 'items'

    def load_categories(self):
        print 'categories!'
        self.screen_manager.current = 'categories'

    def load_favourites(self):
        print 'favourites!'
        self.screen_manager.current = 'favourites'

    def load_settings(self):
        print 'settings!'
        self.screen_manager.current = 'settings'


class ItemsScreen(Screen):
    pass


class CategoriesScreen(Screen):
    pass


class FavouritesScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class NotificationApp(App):
    def build(self):
        base = BaseLayout()

        screens = {}
        sm = ScreenManager()

        screens['items'] = ItemsScreen(name='items')
        screens['categories'] = CategoriesScreen(name='categories')
        screens['favourites'] = FavouritesScreen(name='favourites')
        screens['settings'] = SettingsScreen(name='settings')

        sm.add_widget(screens['items'])
        sm.add_widget(screens['categories'])
        sm.add_widget(screens['favourites'])
        sm.add_widget(screens['settings'])

        sm.current = 'items'
        menu = MenuWidget(sm, screens)

        base.add_widget(sm)
        base.add_widget(menu)

        return base


if __name__ == '__main__':
    api = AllegroEndpoints(API_KEY, LOGIN, PASSWORD)
    NotificationApp().run()

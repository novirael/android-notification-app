from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from api.endpoints import AllegroEndpoints
from credentials import API_KEY, LOGIN, PASSWORD

Window.size = (600 * 2/3, 1024 * 2/3)


class BaseLayout(BoxLayout):
    pass


class ItemsWidget(BoxLayout):
    pass


class MenuWidget(BoxLayout):
    def load_home(self):
        print 'home!'

    def load_categories(self):
        print 'categories!'

    def load_favourites(self):
        print 'favourites!'

    def load_settings(self):
        print 'settings!'


class NotificationApp(App):
    def build(self):
        return BaseLayout()


if __name__ == '__main__':
    api = AllegroEndpoints(API_KEY, LOGIN, PASSWORD)
    NotificationApp().run()


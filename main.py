from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

from api.endpoints import AllegroEndpoints
from credentials import API_KEY, LOGIN, PASSWORD

Window.size = (600 * 2/3, 1024 * 2/3)


class BaseLayout(BoxLayout):
    pass


class ItemsWidget(GridLayout):
    items = []

    def __init__(self, **kwargs):
        super(ItemsWidget, self).__init__(**kwargs)
        self.api = AllegroEndpoints(API_KEY, LOGIN, PASSWORD)
        self._load_newest_items()

    def refresh(self):
        self._remove_item_widgets()
        self._load_newest_items()
        print 'refreshed'

    def _load_newest_items(self):
        for item in self.api.get_all_car_items()[:30]:
            item = Button(text=item['name'], size_hint_y=None, height=40)
            self.items.append(item)
            self.add_widget(item)

    def _remove_item_widgets(self):
        for item in self.items:
            self.remove_widget(item)


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
    def __init__(self, **kwargs):
        super(ItemsScreen, self).__init__(**kwargs)

        self.items_widget = ItemsWidget(cols=1, spacing=10, size_hint_y=None)
        self.items_widget.bind(minimum_height=self.items_widget.setter('height'))

        scroll_view = ScrollView()
        scroll_view.add_widget(self.items_widget)

        self.children[0].add_widget(scroll_view)

    def refresh_items(self):
        self.items_widget.refresh()


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
    NotificationApp().run()

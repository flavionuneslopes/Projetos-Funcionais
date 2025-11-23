from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img = AsyncImage(
            source='https://static.wikia.nocookie.net/mario/images/7/75/Mario.png/revision/latest/scale-to-width-down/1000?cb=20241120011831&path-prefix=pt-br',
            anim_delay=1,
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return img

if __name__ == '__main__':
    MainApp().run()
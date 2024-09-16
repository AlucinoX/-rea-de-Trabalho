import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner

class HashingApp(App):
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Campo para inserir senhas
        self.password_input = TextInput(hint_text='Digite uma senha', size_hint_y=None, height=40, multiline=False)
        self.layout.add_widget(self.password_input)

        # Lista de senhas inseridas
        self.password_list = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.scroll.add_widget(self.password_list)
        self.layout.add_widget(self.scroll)

        # Dropdown para escolher o algoritmo de hash
        self.algorithm_spinner = Spinner(
            text='Escolha o algoritmo',
            values=('md5', 'sha1', 'sha256'),
            size_hint_y=None,
            height=44
        )
        self.layout.add_widget(self.algorithm_spinner)

        # Botões
        self.add_button = Button(text='Adicionar Senha', size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.2, 1))
        self.add_button.bind(on_press=self.add_password)
        self.layout.add_widget(self.add_button)
        
        self.hash_button = Button(text='Gerar Hashes', size_hint_y=None, height=50, background_color=(0.6, 0.2, 0.2, 1))
        self.hash_button.bind(on_press=self.generate_hashes)
        self.layout.add_widget(self.hash_button)

        return self.layout

    def add_password(self, instance):
        password = self.password_input.text.strip()
        if password:
            self.password_list.add_widget(Label(text=password, size_hint_y=None, height=40))
            self.password_input.text = ''

    def generate_hashes(self, instance):
        algorithm = self.algorithm_spinner.text
        if algorithm == 'Escolha o algoritmo':
            self.show_popup('Erro', 'Por favor, escolha um algoritmo de hash.')
            return

        passwords = [child.text for child in self.password_list.children[::-1]]
        if not passwords:
            self.show_popup('Erro', 'Nenhuma senha foi adicionada.')
            return

        hashes = []
        for password in passwords:
            hashed_password = self.hash_password(password, algorithm)
            if hashed_password:
                hashes.append(f"Senha: {password} -> Hash: {hashed_password}")

        self.save_hashes_to_file(hashes, algorithm)
        self.show_popup('Hashes Gerados', '\n'.join(hashes))

    def hash_password(self, password, algorithm='sha256'):
        """Aplica a função de hash na senha usando o algoritmo especificado."""
        try:
            hash_object = hashlib.new(algorithm)
            hash_object.update(password.encode())
            hash_hex = hash_object.hexdigest()
            return hash_hex
        except ValueError:
            self.show_popup('Erro', f"Algoritmo de hash '{algorithm}' não é suportado.")
            return None

    def save_hashes_to_file(self, hashes, algorithm):
        """Salva os hashes em um arquivo com um formato seguro."""
        filename = f"hashed_passwords_{algorithm}.txt"
        with open(filename, "w") as file:
            file.write(f"Hash das senhas usando {algorithm.upper()}:\n")
            for line in hashes:
                file.write(f"{line}\n")

    def show_popup(self, title, message):
        """Exibe uma janela popup com a mensagem fornecida."""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

if __name__ == '__main__':
    HashingApp().run()

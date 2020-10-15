class Menu(object):

    def __init__(self, available_options):

        self.available_options = available_options

        self.options_messages = {
            0: "Log-out"
            }

    def display_menu(self):
        print('Select an option:\n')
        options = self.available_options.copy()
        last = options.pop(0)
        options.append(last)
        for key in options:
            print("[{option}]: {message}, ".format(option=key,message=self.options_messages[key]))
        print(" ")

    def get_input(self):
        message = 'Indicate an option ({}): '
        options = list(map(str, self.available_options.copy()))
        last = options.pop(-1)

        prompt = message.format(', '.join(options)+' or '+last)

        action = self._receive_numeric_input(prompt=prompt, interval=self.available_options)
        return int(action)

    def _receive_numeric_input(self, prompt, interval):
        action = input(prompt)
        while self._not_valid(action, interval):
            print("Option is not numeric or out of range. Write a new option...")
            action = input(prompt)
        return action

    def _not_valid(self, action, interval):
        return (not action.isdigit()) or (not int(action) in interval)


class BeginMenu(Menu):
    def __init__(self, available_options):

        super().__init__(available_options)
        self.options_messages = {
            1: "Create New Game.",
            2: "Load Game.",
            3: "See Ranking.",
            0: "Log-out."
            }

        #assert set(self.available_options).issubset(set(self.options_messages.keys()))


class GameMenu(Menu):


    def __init__(self, available_options):

        super().__init__(available_options)


        self.options_messages = {
            1: "Discover Square.",
            2: "Save Game.",
            0: "Exit."
            }


    def discover_square(self):
        prompt_x = 'Write the X coordinate of the square to be discovered: '
        square_x = self._receive_numeric_input(prompt_x, range(10))
        prompt_y = 'Write the Y coordinate of the square to be discovered: '
        square_y = self._receive_numeric_input(prompt_y, range(10))

        return int(square_x), int(square_y)






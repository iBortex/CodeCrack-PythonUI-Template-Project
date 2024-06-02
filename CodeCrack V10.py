import tkinter as tk
from tkinter import * 
from pygame import mixer
import random
import math
import tkinter.scrolledtext as scrolledtext
import io
import sys
import time
from tkvideo import tkvideo

class CodeCrackApp:
    username = 'JohnDoe42069'
    level = 32
    rank = 'A'
    mmr = 1000

    def __init__(self, root):
        self.root = root
        self.root.title("CodeCrack App")

        # Initialize an empty stack to store screens
        self.screen_stack = []
        self.squares = []

        mixer.init()
        # Load the MP3 file
        self.button_click_sound = mixer.Sound(r"C:\Users\Daniel\Downloads\click-button-app-147358.mp3")

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Maximize the window
        self.root.state('zoomed')

        # Set background color to black
        self.root.configure(bg='black')

        # Set initial volume and store it as an attribute
        self.volume = 50  # Set an initial volume (0-100)
        mixer.music.set_volume(self.volume / 100.0)

        # Create and pack widgets
        self.create_home_screen()


    def play_music(self):

        # Play the MP3 when entering ranked matchmaking
        mp3_path = r"C:\Users\Daniel\Downloads\rankedmusic.mp3"  # Replace with the actual path to your MP3 file
        mixer.init()

        mixer.music.load(mp3_path)
        mixer.music.play(-1)
        

    def clear_screen(self):
        # Destroy all widgets in the root window except for set_volume method
        mixer.music.stop()
        self.button_click_sound.play()
        for widget in self.root.winfo_children():
            if widget != self.set_volume:
                widget.destroy()
                


    def clear_screenwithmusic(self):
        # Destroy all widgets in the root window except for set_volume method
        self.button_click_sound.play()
        for widget in self.root.winfo_children():
            if widget != self.set_volume:
                widget.destroy()

    def create_white_box(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set canvas dimensions
        canvas_width = 800
        canvas_height = 400

        # Calculate x and y coordinates to center the canvas
        x_coordinate = (screen_width - canvas_width) // 2
        y_coordinate = (screen_height - canvas_height) // 2

        # Create a Canvas widget
        canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg='white')

        # Place the Canvas widget
        canvas.place(x=x_coordinate, y=y_coordinate)  # Use x_coordinate and y_coordinate
 
    def title_label_box(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set canvas dimensions
        canvas_width = screen_width
        canvas_height = screen_height // 5  # 1/5th of the screen height

        # Create a Canvas widget with a dark grey background
        self.title_canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg='#333333', highlightthickness=0)  # Use a dark grey color code
        player_info = tk.Canvas(self.root, width=500, height=(canvas_height/2), bg='#23284a', highlightthickness=0)  # Use a dark grey color code
        self.title = tk.Label(self.root, text="CodeCrack", font=('Lilita One', 60), bg='#333333', fg='white')
        self.player_info_label = tk.Label(self.root, text=f"{self.username}\nlvl {self.level} Rank: {self.rank}", font=('Lilita One', 30), bg='#23284a', fg='white')
        self.title_play_button = tk.Button(self.root, text="Play", command=self.play, font=('Lilita One', 30), bg='#333333', fg='white', bd=0, relief=tk.FLAT, highlightthickness=0)
        self.title_help_button = tk.Button(self.root, text="Help", command=self.help, font=('Lilita One', 30), bg='#333333', fg='white', bd=0, relief=tk.FLAT, highlightthickness=0)
        self.title_subscription_button = tk.Button(self.root, text="Subscription", font=('Lilita One', 30), bg='#333333', fg='white', bd=0, relief=tk.FLAT, highlightthickness=0)
        self.underline = tk.Canvas(self.root, width=264, height=10, bg='white')

        # Place the Canvas widget at the top of the screen
        self.title_canvas.place(x=0, y=0)
        player_info.place(x=canvas_width-550, y=canvas_height/4)
        self.title.place(x=10, y=canvas_height/3)
        self.title_play_button.place(x=canvas_width/3, y=canvas_height-75)
        self.title_help_button.place(x=(canvas_width/3)+400, y=canvas_height-75)
        self.title_subscription_button.place(x=(canvas_width/3)+800, y=canvas_height-75)
        self.underline.place(x=(canvas_width/3)-80, y=canvas_height-15)
        self.player_info_label.place(x=(canvas_width - 480), y=(canvas_height / 4 + (canvas_height / 2 - self.player_info_label.winfo_reqheight()) // 2))


    def create_home_screen(self):
        # Clear home screen widgets
        self.clear_screen()

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Create and pack widgets
        self.create_white_box()
        self.title_label_box()

        # Home screen widgets
        self.welcome_label = tk.Label(self.root, text=f"Welcome back to CodeCrack!\n\n{self.username}!", font=('Lilita One', 30), bg='white')
        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout, font=('Lilita One', 20), bg='red', fg='white')
        self.join_button = tk.Button(self.root, text="Join", command=self.show_join_menu, font=('Lilita One', 20), bg='dark blue', fg='white')
        
        # Calculate x and y coordinates to center the canvas
        label_x_coordinate = (screen_width - self.welcome_label.winfo_reqwidth()) // 2
        label_y_coordinate = (screen_height - self.welcome_label.winfo_reqheight()) // 2
        # Calculate x and y coordinates to center the canvas
        logout_x_coordinate = (screen_width - self.logout_button.winfo_reqwidth()) // 2
        logout_y_coordinate = (screen_height - self.logout_button.winfo_reqheight()) // 2
        # Calculate x and y coordinates to center the canvas
        join_x_coordinate = (screen_width - self.join_button.winfo_reqwidth()) // 2
        join_y_coordinate = (screen_height - self.join_button.winfo_reqheight()) // 2
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Place widgets
        self.welcome_label.place(x=label_x_coordinate-152, y=label_y_coordinate-128)
        self.logout_button.place(x=logout_x_coordinate-275, y=logout_y_coordinate+128)
        self.join_button.place(x=join_x_coordinate+275, y=join_y_coordinate+128)

    def show_join_menu(self):
        # Clear the current screen
        self.clear_screen()
        self.title_label_box()

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        menu_width = 40
        menu_height = 2


        # Join menu widgets
        self.multiplayer_button = tk.Button(self.root, text="Multiplayer", command=self.join_multiplayer, font=('Lilita One', 30), bg='orange', fg='white', width=menu_width, height=menu_height)
        self.solo_practice_button = tk.Button(self.root, text="Solo Practice with Step-by-Step Solutions", command=lambda: self.show_screen(self.solo_practice), font=('Lilita One', 30), bg='#2596be', fg='white', width=menu_width, height=menu_height)
        self.settings_button = tk.Button(self.root, text="Settings", command=self.show_settings, font=('Lilita One', 30), bg='grey', fg='white', width=menu_width, height=menu_height)
        # Back Button
        self.back_button = tk.Button(self.root, text='Back', command=self.create_home_screen, font=('Lilita One', 30), bg='white', width=menu_width, height=menu_height)

        # Calculate x and y coordinates to center the canvas
        label_x_coordinate = (screen_width - self.multiplayer_button.winfo_reqwidth()) // 2
        label_y_coordinate = (screen_height - self.multiplayer_button.winfo_reqheight()) // 2

        # Pack join menu widgets

        self.multiplayer_button.place(x=label_x_coordinate, y=label_y_coordinate-200)
        self.solo_practice_button.place(x=label_x_coordinate, y=label_y_coordinate-50)
        self.settings_button.place(x=label_x_coordinate, y=label_y_coordinate+100)
        self.back_button.place(x=label_x_coordinate, y=label_y_coordinate+250)

    def join_multiplayer(self):

        # Clear the current screen
        self.clear_screen()
        self.title_label_box()

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        menu_width = 40
        menu_height = 2

        # Join menu widgets
        self.ranked_button = tk.Button(self.root, text="Ranked", command=self.join_ranked, font=('Lilita One', 30), bg='orange', fg='white', width=menu_width, height=menu_height)
        self.quickplay_button = tk.Button(self.root, text="Quickplay", command=self.join_quickplay, font=('Lilita One', 30), bg='#2596be', fg='white', width=menu_width, height=menu_height)
        self.customgame_button = tk.Button(self.root, text="Custom Game", command=self.join_customgame, font=('Lilita One', 30), bg='grey', fg='white', width=menu_width, height=menu_height)
        # Back Button
        self.back_button = tk.Button(self.root, text='Back', command=self.show_join_menu, font=('Lilita One', 30), bg='white', width=menu_width, height=menu_height)

        # Calculate x and y coordinates to center the canvas
        label_x_coordinate = (screen_width - self.ranked_button.winfo_reqwidth()) // 2
        label_y_coordinate = (screen_height - self.ranked_button.winfo_reqheight()) // 2

        # Pack join menu widgets

        self.ranked_button.place(x=label_x_coordinate, y=label_y_coordinate-200)
        self.quickplay_button.place(x=label_x_coordinate, y=label_y_coordinate-50)
        self.customgame_button.place(x=label_x_coordinate, y=label_y_coordinate+100)
        self.back_button.place(x=label_x_coordinate, y=label_y_coordinate+250)


    def create_ranked_title_screen(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set canvas dimensions
        canvas_width = screen_width
        canvas_height = self.title_canvas.winfo_reqheight() // 2  # 1/2 of the title height

        self.ranked_title_canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg='#3e4243', highlightthickness=0)
        self.mmr_label = tk.Label(self.root, text=f"MMR: {self.mmr}", font=('Lilita One', 60), bg='#3e4243', fg='white')
        self.rank_label = tk.Label(self.root, text=f"Rank: {self.rank}", font=('Lilita One', 60), bg='#3e4243', fg='white')
        

        self.ranked_title_canvas.place(x=0, y=self.title_canvas.winfo_reqheight())
        self.mmr_label.place(x=100, y=self.title_canvas.winfo_reqheight()+(self.ranked_title_canvas.winfo_reqheight() // 8))
        self.rank_label.place(x=screen_width-750, y=self.title_canvas.winfo_reqheight()+(self.ranked_title_canvas.winfo_reqheight() // 8))
        



    def help(self):


        self.clear_screen()
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Set canvas dimensions
        canvas_width = screen_width
        canvas_height = screen_height // 5  # 1/5th of the screen height
        self.title_label_box()

        self.contact_label = tk.Label(self.root, text="Contact:\n954-937-9837", font=('Lilita One', 60), bg='black', fg='white')
        
        self.underline.place(x=(canvas_width/3)+320, y=canvas_height-15)
        self.contact_label.place(x=(screen_width - self.contact_label.winfo_reqwidth()) // 2, y=(screen_height - self.contact_label.winfo_reqheight()) // 2)
        

    def play(self):
        self.clear_screen()
        self.create_home_screen()
        


    def solo_practice(self):
        # Add logic for solo practice
        pass

    def show_settings(self):
        # Clear the current screen
        self.clear_screen()
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.title_label_box()

         # Volume slider
        self.volume_var = tk.StringVar(value=self.volume)
        self.volume_label = tk.Label(self.root, text="Volume", font=('Lilita One', 30), bg='black', fg='white')
        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, length=600, sliderlength=30, bg='white', fg='black', font=('Lilita One', 20), variable=self.volume_var)

        self.back_button = tk.Button(self.root, text='Back', command=self.show_join_menu, font=('Lilita One', 30), bg='white', width=20, height=2)


        # Place volume slider widgets
        self.volume_label.place(x=((screen_width - self.volume_label.winfo_reqwidth()) // 2) - 400, y=screen_height // 2)
        self.volume_slider.place(x=(screen_width - self.volume_slider.winfo_reqwidth()) // 2, y=screen_height // 2)
        self.back_button.place(x=(screen_width - self.back_button.winfo_reqwidth()) // 2, y=(screen_height - self.back_button.winfo_reqheight()) // 2+250)
    
    def set_volume(self, value):
        self.volume = float(value)
        mixer.music.set_volume(self.volume)

    def join_quickplay(self):

        pass


    def join_ranked(self):

        self.clear_screen()
        self.play_music()
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.title_label_box()
        self.create_ranked_title_screen()

        self.create_moving_squares()

        self.entermatchmaking_button = tk.Button(self.root, text="Enter Matchmaking", command=self.join_entermatchmaking, font=('Lilita One', 30), bg='green', fg='white', width=40, height=2)
        self.back_button = tk.Button(self.root, text='Back', command=self.join_multiplayer, font=('Lilita One', 20), bg='white', width=15, height=2)

        self.entermatchmaking_button.place(x=(screen_width - self.entermatchmaking_button.winfo_reqwidth()) // 2, y=((screen_height - self.entermatchmaking_button.winfo_reqheight()) // 2)+100)
        self.back_button.place(x=(screen_width - self.back_button.winfo_reqwidth()) // 2, y=(screen_height - self.back_button.winfo_reqheight()) // 2+250)


    def create_moving_squares(self):
        # Create a canvas to draw on
        canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight() - (self.title_canvas.winfo_reqheight() + self.ranked_title_canvas.winfo_reqheight()), bg='black', highlightthickness=0)
        canvas.place(x=0, y=self.title_canvas.winfo_reqheight() + self.ranked_title_canvas.winfo_reqheight())

        # Create multiple MovingSquare instances
        num_squares = 100
        squares = [MovingSquare(canvas, size=30, speed=2, alpha=0.7) for _ in range(num_squares)]

        # Start the update loop for each square
        for square in squares:
            square.update()

    def join_customgame(self):
        
        pass

    def logout(self):
        self.root.destroy()
        pass

    def join_entermatchmaking(self):
        self.clear_screenwithmusic()

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.title_label_box()

        # Get a random problem from the problem set
        self.random_problem_index = random.randint(0, len(problem_set.problems) - 1)
        random_problem = problem_set.get_problem(self.random_problem_index)
        

        # Create button to execute code
        self.execute_button = tk.Button(self.root, text="Run Code", command=self.run_code, font=('Lilita One', 30), bg='blue', fg='white', width=10, height=1)
        self.execute_button.place(x=700, y=screen_height-150)

        # Create button to submit code
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_button, font=('Lilita One', 30), bg='green', fg='white', width=10, height=1)
        self.submit_button.place(x=950, y=screen_height-150)

        # Create text editor for code input
        self.text_editor = scrolledtext.ScrolledText(self.root, width=(screen_width//20), height=20, font=('Consolas', 12), bg='#282828', fg='white', insertbackground='white')
        self.text_editor.place(x=50, y=(screen_height-350)-(self.text_editor.winfo_reqheight()))

        # Create output widget
        self.output = scrolledtext.ScrolledText(self.root, width=(screen_width//20), height=10, state='disabled', font=('Consolas', 12), bg='#282828', fg='white', insertbackground='white')
        self.output.place(x=50, y=screen_height-350)

        # Calculate the length of the text in the label
        text_length = len(f"Problem: {random_problem['problem']}\nDescription: {random_problem['description']}")
        # Calculate the wrap length based on text length
        wrap_length = text_length * 5
        # Create a label for the problem and description
        self.problem_label = tk.Label(self.root, text=f"Problem: {random_problem['problem']}\n\n\nDescription: {random_problem['description']}", font=('Consolas', 20), bg='#282828', fg='white', width=78, height=10, wraplength=wrap_length)
        self.problem_label.place(x=50, y=(screen_height-350)-(self.text_editor.winfo_reqheight())-(self.problem_label.winfo_reqheight()))
        

        # Create a label for the problem and description
        videolabel = tk.Label(self.root, bd=0)
        videolabel.place(x=1350, y=555)

        # Create the canvas
        canvas = tk.Canvas(self.root, width=1250, height=180, bg='black', highlightthickness=0)
        canvas.place(x=1350, y=510)

        OpponentLabel = tk.Label(self.root, text="Opponent: JaneDoe123\nRank: A", font=('Lilita One', 50), bg='black', fg='white')
        OpponentLabel.place(x=1650, y=450)


        # Add a video to the right side of the screen
        video_player = tkvideo(path=r"C:\Users\Daniel\Downloads\Untitled video - Made with Clipchamp (1).mp4", label=videolabel, size = (1280,720))
        video_player.play()

        # Redirect stdout to capture output
        self.stdout = io.StringIO()
        sys.stdout = self.stdout


        

                        
    def run_code(self):
        # Clear previous output
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        
        # Get code from text editor
        code = self.text_editor.get('1.0', tk.END)
        
        try:
            # Execute the code
            exec(code)
        except Exception as e:
            # Display any errors in the output
            print(e)
        
        # Display output
        output_text = self.stdout.getvalue()
        self.outputcheck = output_text
        self.output.insert(tk.END, output_text)
        self.stdout.truncate(0)
        self.stdout.seek(0)
        self.output.config(state='disabled')

    def submit_button(self):
        
        
        self.run_code()
        self.Validation()
        self.check_solution()



    def Validation(self):
        self.clear_screen()

        self.title_label_box()

        # Create a label for the loading text
        loading_label = tk.Label(self.root, text="Validating", font=('Lilita One', 50), bg='black', fg='white')
        loading_label.place(relx=0.5, rely=0.5, anchor='center')

        # Loop to simulate loading with periods
        for _ in range(5):  # Loop for 5 seconds
            self.root.update()
            loading_label.config(text="Validating")
            time.sleep(0.5)
            self.root.update()  # Update the GUI to show changes
            loading_label.config(text="Validating.")
            time.sleep(0.5)
            self.root.update()
            loading_label.config(text="Validating..")
            time.sleep(0.5)
            self.root.update()
            loading_label.config(text="Validating...")
            time.sleep(0.5)

        # Clear the loading label after the loop
        loading_label.destroy()


    def Victory(self):
        self.clear_screen()
        self.title_label_box()
        self.Victory_label = tk.Label(self.root, text='Victory!', font=('Lilita One', 10), fg='blue', bg='black')
        self.Victory_label.place(relx=0.5, rely=0.5, anchor='center')  # Center the label initially

        # Define a function to gradually increase font size
        def grow_text(font_size):
            new_font_size = font_size + 1
            self.Victory_label.config(font=('Lilita One', new_font_size))
            if new_font_size <= 200:  # Adjust the maximum font size as needed
                self.root.after(5, grow_text, new_font_size)  # Call grow_text after 50 milliseconds with new_font_size
            else:
                # After finishing the text growth, update MMR and display it
                old_mmr = self.mmr
                self.mmr += 25
                mmr_text = f'MMR {old_mmr} + 25 \n New MMR: {self.mmr}'
                display_mmr_label = tk.Label(self.root, text=mmr_text, font=('Lilita One', 25), fg='white', bg='black')
                display_mmr_label.place(relx=0.5, rely=0.8, anchor='center')  # Place the MMR label below Victory

        # Start growing the text after a delay (e.g., 500 milliseconds)
        self.root.after(500, grow_text, 10)  # Start with a font size of 10


        

    def Defeat(self):
        self.clear_screen()
        self.title_label_box()
        self.Defeat_label = tk.Label(self.root, text='Defeat.', font=('Lilita One', 10), fg='red', bg='black')
        self.Defeat_label.place(relx=0.5, rely=0.5, anchor='center')  # Center the label initially

        # Define a function to gradually increase font size
        def grow_text(font_size):
            new_font_size = font_size + 1
            self.Defeat_label.config(font=('Lilita One', new_font_size))
            if new_font_size <= 200:  # Adjust the maximum font size as needed
                self.root.after(5, grow_text, new_font_size)  # Call grow_text after 50 milliseconds with new_font_size
            else:
                # After finishing the text growth, update MMR and display it
                old_mmr = self.mmr
                self.mmr -= 25
                mmr_text = f'MMR {old_mmr} - 25 \n New MMR: {self.mmr}'
                display_mmr_label = tk.Label(self.root, text=mmr_text, font=('Lilita One', 25), fg='white', bg='black')
                display_mmr_label.place(relx=0.5, rely=0.8, anchor='center')  # Place the MMR label below Defeat

        # Start growing the text after a delay (e.g., 500 milliseconds)
        self.root.after(500, grow_text, 10)  # Start with a font size of 10
        

    def check_solution(self):
        problem_info = problem_set.get_problem(self.random_problem_index)
        solution_list = problem_info.get('solution')
        for solution in solution_list:
            if self.outputcheck.strip() == solution.strip():  # Compare as strings after stripping whitespace
                self.Victory()
            else:
                self.Defeat()


class CodingProblemSet:
    def __init__(self):
        self.problems = []

    def add_problem(self, problem, description, solution):
        self.problems.append({
            'problem': problem,
            'description': description,
            'solution': solution
        })

    def get_problem(self, index):
        if 0 <= index < len(self.problems):
            return self.problems[index]
        else:
            return None
    
        

# Usage:
problem_set = CodingProblemSet()

# # Adding coding problems to the problem set
# problem_set.add_problem(
#     problem="Two Sum",
#     description="Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
#     solution= ['[0, 1]', '[1, 0]']
# )

# # Adding coding problems to the problem set
# problem_set.add_problem(
#     problem="Sum Two Numbers",
#     description="Write a program to calculate the sum of 5 and 1324.",
#     solution=['1329']
# )


problem_set.add_problem(
    problem="Reverse String",
    description="Write a function that reverses the string 'hello'. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.",
    solution=['olleh']
)



class MovingSquare:
    def __init__(self, canvas, size=50, speed=2, alpha=0.7):  # Added alpha for transparency
        self.canvas = canvas
        self.size = size
        self.speed = speed
        self.alpha = alpha

        # Create a translucent square on the canvas
        self.square = canvas.create_rectangle(0, 0, size, size, fill=f'#ECF3F9')

        # Set initial position and direction
        self.x = random.randint(0, canvas.winfo_reqwidth() - size)
        self.y = random.randint(0, canvas.winfo_reqheight() - size)
        self.direction = random.uniform(0, 2 * 3.14159)  # Random angle in radians

    def move(self):
        # Move the square in the chosen direction
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

        # Check if the square is within the canvas boundaries
        if self.x < 0:
            self.x = self.canvas.winfo_reqwidth()  # Move to the right edge
        elif self.x > self.canvas.winfo_reqwidth():
            self.x = 0  # Move to the left edge
        if self.y < 0:
            self.y = self.canvas.winfo_reqheight()  # Move to the bottom edge
        elif self.y > self.canvas.winfo_reqheight():
            self.y = 0  # Move to the top edge

        # Move the square on the canvas
        self.canvas.coords(self.square, self.x, self.y, self.x + self.size, self.y + self.size)

    def update(self):
        # Update the movement of the square
        self.move()
        # Schedule the update function to be called again after a delay (milliseconds)
        self.canvas.after(33, self.update)  # Adjusted for approximately 30 fps




# Create the main window
root = tk.Tk()

# Initialize the CodeCrackApp class
app = CodeCrackApp(root)

# Run the Tkinter event loop
root.mainloop()

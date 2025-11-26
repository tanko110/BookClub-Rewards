import tkinter as tk
from tkinter import messagebox


class RewardsCalculator:
    #Create the main window
    def __init__(self, main):
        self.main = main
        self.main.title('Serendipity Booksellers - Points Calculator')
        self.main.geometry("400x500")
        self.main.resizable(True, True)

        # Configure style
        self.main.configure(bg='#f0f0f0')

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.main, text='Serendipity Booksellers Club Rewards',
                               font=('Arial', 16), bg='#EEFCF8', fg='black')
        title_label.pack(pady=10)

        # Instructions Label
        instruction_label = tk.Label(self.main, text='Enter Number of Books Purchased this Month',
                                     font=('Arial', 14), bg='#EEFCF8', fg='black')
        instruction_label.pack(pady=5)

        # Entry widget for user input
        self.books_entry = tk.Entry(self.main, font=('Arial', 12), width=10, justify='center',
                                    bg='#ffffff', fg='#2c3e50', bd=1)
        self.books_entry.pack(pady=10)

        # Compute Button
        compute_button = tk.Button(self.main, text='Compute Points', font=('Arial', 11, 'bold'),
                                   bg='#77B3EE', fg='black', bd=2,
                                   command=self.compute_points)
        compute_button.pack(pady=5)

        # Display Result Button
        display_button = tk.Button(self.main, text='Display Result', font=('Arial', 11, 'bold'),
                                   bg='#77B3EE', fg='black', bd=2,
                                   command=self.display_result)
        display_button.pack(pady=5)

        # Clear Button
        clear_button = tk.Button(self.main, text='Clear', font=('Arial', 11, 'bold'),
                                 bg='#84EA81', fg='black', bd=2,
                                 command=self.clear_result)
        clear_button.pack(pady=5)

        # Quit button to quit the program
        quit_button = tk.Button(self.main, text='Quit', font=('Arial', 11, 'bold'),
                                bg='#CC444A', fg='black', bd=2,
                                command=self.quit_application)
        quit_button.pack(pady=15)


        #Label to display result
        self.result_label = tk.Label(self.main, text="", font=('Arial', 14, 'bold'),
                                     bg='#E7EEFD', fg='#e67e22', wraplength=350)
        self.result_label.pack(pady=10)

        #Label for points information
        info_text = ('Points System:\n 0 books=0 pts\n 2 books=5 pts \n 4 books=15 pts'
                     '\n 6 books=30 pts \n 8 books=60 pts')
        info_label = tk.Label(self.main, text=info_text, font=('Arial', 9), bg='#f0f8ff',
                              fg='black', justify='left')
        info_label.pack(pady=5)

    #Calculate points per # of books purchased
    def calculate_points(self, books):
        books = int(books)

        if books == 0:
            return 0
        elif books == 2:
            return 5
        elif books == 4:
            return 15
        elif books == 6:
            return 30
        elif books >= 8:
            return 60
        else:
            return 0

    def compute_points(self):#Compute the points and store result
        try:
            books = self.books_entry.get().strip()

            if not books:
                messagebox.showwarning('Input Error',
                                       'Please Enter the Number of Books Purchased.')
                return

            books = int(books)

            if books < 0:
                messagebox.showwarning('Input Error',
                                       'Number of books cannot be negative.')
                return

            self.points = self.calculate_points(books)
            messagebox.showinfo('Computation Complete',
                                f"Points calculated successfully!\nClick 'Display Result' "
                                f'to see the points.')

        except ValueError:
            messagebox.showerror("Input Error",
                                 'Please enter a valid number for books purchased.')

    def display_result(self): #Display the computed result
        try:
            books = int(self.books_entry.get().strip())
            points = self.calculate_points(books)

            result_text = f'Books Purchased: {books}\nPoints Awarded: {points}'
            self.result_label.config(text=result_text)

        except (ValueError, AttributeError):
            messagebox.showerror('Error',
                                 'Please compute points first or check your input.')
    #Clear the entry and result
    def clear_result(self):
        self.books_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.books_entry.focus()

    #Quit Application
    def quit_application(self):
        self.main.destroy()


def main():
    main = tk.Tk()
    RewardsCalculator(main)

    # Start the GUI loop
    main.mainloop()

if __name__ == "__main__":
    main()
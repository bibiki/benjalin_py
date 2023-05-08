# Odin gave his eye to acquire knowledge, but I'd give far more
import db
import tkinter as tk
from datetime import datetime

virtues_english = {
    "temperance": {"key": 'Temperance', "description": 'Eat not to dullness; drink not to elevation'},
    "silence": {"key": 'Silence', "description": 'Speak not but what may benefit others or yourself; avoid trifling conversations'},
    "order": {"key": 'Order', "description": 'Let all your things have thier place; let each part of your business have its time'},
    "resolution": {"key": 'Resolution', "description": 'Resolve to perform what you ought; perform without fail what you resolve'},
    "frugality": {"key": 'Frugality', "description": 'Make no expense but to do good to others or yourself; waste nothing'},
    "industry": {"key": 'Industry', "description": 'Lose no time; be always employed in something useful; cut off all unnecessary actions'},
    "sincerity": {"key": 'Sincerity', "description": 'Use no hurtful deceit; think innocently and justly; and, if you speak, speak accordingly'},
    "justice": {"key": 'Justice', "description": 'Wrong none by doing injuries, or omitting the benefits that are your duty'},
    "moderation": {"key": 'Moderation', "description": 'Avoid extremes; forbear resenting injuries so much as you think they deserve'},
    "cleanliness": {"key": 'Cleanliness', "description": 'Tolerate no unclieanliness in body, clothes, or habitation'},
    "tranquility": {"key": 'Tranquility', "description": 'Be not disturbed at trifles, or at accidents common or unavoidable'},
    "chastity": {"key": 'Chastity', "description": 'Rarely use venery but for Health or Offspring; Never to Dulness, Weakness, or the Injury of your own or another\'s Peace or Reputation'},
    "humility": {"key": 'Humility', "description": 'Imitate Jesus and Socrates'}}

# used when user selects a virtue
virtue = None

date_today = datetime.today().strftime('%Y-%m-%d')

#used when user selects a score for the already selected virtue
score = None
def set_score(s):
    print('score', s)
    global score
    score = s
    save_button.configure(state="active")

window = tk.Tk()
window.title('Benjalin')

right_frame = tk.Frame(master=window, width=800, height=100)
right_frame.grid_propagate(0)

# possible scores
scores_list = [1,2,3,4,5,6,7,8,9,10]
  
# Variable to keep track of the score selected
value_inside = tk.StringVar(window)
  
# Set the default value of the variable
value_inside.set('---')
  
score_menu = tk.OptionMenu(right_frame, value_inside, *scores_list, command=set_score)
score_menu.configure(state="disabled")

selected_virtue = tk.Label(master=right_frame, text="")
selected_virtue_description = tk.Message(master=right_frame, text='', justify=tk.LEFT, width=450)

initial_greeting = tk.Label(master=right_frame, text='Please select one of the virtues you\'d like to score yourself on')
note = tk.Text(master=right_frame, height=15, width=60)

virtue_notes = ()

journals = tk.Variable(value=virtue_notes)

journal_dates = tk.Listbox(
    master=right_frame,
    listvariable=journals,
    height=6,
    selectmode=1
)

average_score_label = tk.Label(master=right_frame)
average_score_label.grid(sticky='W', column=3, row=2)

def journal_item_selected(item):
    selection = journal_dates.curselection()
    date = virtue_notes[selection[0]]
    journal = db.journal(virtue["key"], date)
    print('journal', journal)
    popup_window = tk.Toplevel(master=window)
    popup_window.title("Daily note")

    # Create a label with the message text and pack it into the popup windo
    note_text = tk.Text(popup_window, height=15, width=60)
    note_text.insert("1.0", journal)
    note_text.configure(state="disabled")
    note_text.pack(padx=20, pady=20)

    # Create a button to close the popup window and pack it into the popup window
    close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
    close_button.pack(padx=20, pady=10)


journal_dates.bind('<<ListboxSelect>>', journal_item_selected)

def save_button_handler():
    global score
    s = score
    score = None
    n = note.get("1.0", tk.END)
    note.delete("1.0", tk.END)
    print('saving score', virtue, score, s)
    db.save_score(date_today, s, virtue["key"], n)
    virtue_selected()

save_button = tk.Button(master=right_frame, text='Save', command=save_button_handler)
save_button.configure(state="disabled")

def virtue_selected():
    save_button.configure(state="disabled")
#    score_menu.configure(state="disabled") needs to reset the value selected to ---
    initial_greeting.configure(text='')
    score_label = tk.Label(master=right_frame, text='Score for today')
    score_label.grid(sticky='W', column=0, row=2)
    average = db.average(virtue["key"])
    if average is not None:
        average_text = 'Your average score here is ' + str(average)
        average_score_label.configure(text=average_text)
    else:
        average_score_label.configure(text='')
    score_menu.grid(sticky='W', column=1, row=2)
    selected_virtue.grid(sticky='W', column=0, row=0)
    selected_virtue.propagate(0)
    selected_virtue_description.grid(sticky='W', column=0, row=1, columnspan=3)
    selected_virtue_description.propagate(0)
    note.grid(sticky= 'W', column=0, row=5, columnspan=2)
    global virtue_notes
    virtue_notes = db.journals_by_virtue(virtue["key"])
    journals.set(virtue_notes)
    journal_dates.grid(sticky='NW', column=3, row=5)
    save_button.grid(sticky='W', column=0, row=4)


def virtue_selection_handler(v):
    def h():
        global virtue
        virtue = v
        virtue_selected()
        selected_virtue.configure(text=v["key"])
        selected_virtue_description.configure(text=v["description"])
        score_menu.configure(state="active")
    return h

def button(virtue, f, tk):
    """t is text, f is master frame, tk is the window"""
    t = virtue["key"]
    return tk.Button(master=f, text=t, command=virtue_selection_handler(virtue), width=12)

# this is the left frame containing the button representing the virtues
left_frame = tk.Frame(master=window, width=200, height=100)
left_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# this puts the buttons representing virtues on the frame on the left
for k, v in virtues_english.items():
    b = button(v, left_frame, tk)
    b.pack()

right_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
right_frame.propagate(0)
right_frame.grid_rowconfigure(0, minsize=25)
right_frame.grid_rowconfigure(1, minsize=34)
right_frame.grid_rowconfigure(2, minsize=25)


initial_greeting.grid(sticky = 'W', column=0, row=0, columnspan=3)

window.mainloop()

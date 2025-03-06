import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,messagebox,filedialog
import os

application = tk.Tk()
application.geometry('800x600')

application.title('PyText')
application.wm_iconbitmap('icon.ico')
# -----------------------------Main menu---------------------------------

main_menu = tk.Menu(application)

# File Menu

file = tk.Menu(main_menu,tearoff=0)

# File Icons

new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

# Edit Menu

edit = tk.Menu(main_menu,tearoff = 0)

#Edit Icons

undo_icon=tk.PhotoImage(file = 'icons2/undo.png')
redo_icon=tk.PhotoImage(file = 'icons2/redo.png')
copy_icon = tk.PhotoImage(file = 'icons2/copy.png')
paste_icon = tk.PhotoImage(file = 'icons2/paste.png')
cut_icon = tk.PhotoImage(file = 'icons2/cut.png')
clear_all_icon = tk.PhotoImage(file = 'icons2/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons2/find.png')

# View Menu

view = tk.Menu(main_menu,tearoff = 0)

# View icons

toolbar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_icon =  tk.PhotoImage(file='icons2/status_bar.png')

# Color Menu

colortheme = tk.Menu(main_menu,tearoff = 0)

# Color icons

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
skin_icon = tk.PhotoImage(file='icons2/red.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')

theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,monokai_icon,night_blue_icon,skin_icon,dark_icon)

color_dict={
    'light_default' : ('#000000','#ffffff'),
    'light_plus' : ('#474747','#e0e0e0'),
    'monokai' : ('#d3b774', '#474747'),
    'night_blue' : ('#ededed','#6b9dc2'),
    'skin' : ('#2d2d2d','#ffe8e8'),
    'dark' : ('#c4c4c4','#2d2d2d')
}

# ---Cascade----

main_menu.add_cascade(label='File',menu = file)
main_menu.add_cascade(label='Edit',menu = edit)
main_menu.add_cascade(label='View',menu = view)
main_menu.add_cascade(label='Color Theme',menu = colortheme)

# -----------------------------End Main menu-----------------------------

# -----------------------------Tool bar---------------------------------

toolbar=ttk.Label(application)
toolbar.pack(side=tk.TOP,fill=tk.X)

# Font box

font_tuple=font.families()
font_store=tk.StringVar()
font_box=ttk.Combobox(toolbar, width=30, textvariable=font_store, state='readonly')
font_box['value']=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5)

# Size box

size_store=tk.IntVar()
size_box=ttk.Combobox(toolbar, width=18, textvariable=size_store, state='readonly')
size_box['values']=tuple(range(8,81,2))
size_box.current(0)
size_box.grid(row=0, column=1, padx=5)

#Bold, italic and underline button

bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(toolbar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(toolbar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(toolbar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# Font color

font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
color_btn=tk.Button(toolbar, image=font_color_icon)
color_btn.grid(row=0, column=5, padx=5)

# Alignment

# --Left--

align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
left_btn=ttk.Button(toolbar, image=align_left_icon)
left_btn.grid(row=0, column=6, padx=5)

# --Center--

align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
center_btn=ttk.Button(toolbar, image=align_center_icon)
center_btn.grid(row=0, column=7, padx=5)

# --Right--

align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
right_btn=ttk.Button(toolbar, image=align_right_icon)
right_btn.grid(row=0, column=8, padx=5)

# -----------------------------End tool bar-----------------------------

# -----------------------------text editor and status bar---------------------------------

# Main frame to hold everything
main_frame = ttk.Frame(application)
main_frame.pack(expand=True, fill=tk.BOTH)

# Editor Frame (Holds Text Editor + Scrollbar)
editor_frame = ttk.Frame(main_frame)
editor_frame.grid(row=0, column=0, sticky="nsew")

# Text Editor
text_editor = tk.Text(editor_frame, wrap='word', relief=tk.FLAT, pady=5, padx=5, undo=True)
text_editor.grid(row=0, column=0, sticky="nsew")
text_editor.focus_set()

# Scrollbar
scroll_bar = ttk.Scrollbar(editor_frame, command=text_editor.yview)
scroll_bar.grid(row=0, column=1, sticky="ns")
text_editor.config(yscrollcommand=scroll_bar.set)

# Status Bar (Fixed at Bottom)
status_bar = ttk.Label(main_frame, text="Characters: 0 Words: 0",  anchor="center")
status_bar.grid(row=1, column=0, sticky="ew")

# Configure Resizing Behavior

main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=0)
editor_frame.rowconfigure(0, weight=1)
editor_frame.columnconfigure(0, weight=1)

## --Status Bar functionality--

def count(event=None):
    global text_change
    if text_editor.edit_modified():
        content=text_editor.get(1.0, 'end-1c')
        words = len(content.split())
        characters = len(content.replace(" ","").replace("\n",""))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', count)

# def test(event=None):
#     print("Modified event fired!")
# text_editor.bind('<<Modified>>', test)

#### Font family and font size functionality

text_editor.config(font=('Arial', 12))
current_font_family="Arial"
current_font_size=12

def font_change(application):
    global current_font_family
    current_font_family=font_store.get()
    text_property = tk.font.Font(font=text_editor['font'])
    new_font=font.Font(family=current_font_family,
                             size=current_font_size,
                             weight=text_property['weight'], slant= text_property['slant'], underline=text_property['underline'])
    text_editor.configure(font=new_font)
        # text_editor.tag_configure(tag_name,font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", font_change)

def size_change(application):
    global current_font_size
    current_font_size=size_store.get()
    text_property = tk.font.Font(font=text_editor['font'])
    new_font=font.Font(family=current_font_family,
                            size=current_font_size,
                            weight=text_property['weight'], slant= text_property['slant'], underline=text_property['underline'])
    text_editor.configure(font=new_font)
    # text_editor.tag_config(tag_name,font=(current_font_family, current_font_size))

size_box.bind("<<ComboboxSelected>>", size_change)

#### Buttons functionality

def bold():
        text_property = tk.font.Font(font=text_editor['font'])
        new_weight = 'bold' if text_property['weight'] == 'normal' else 'normal'
        new_font=font.Font(family=current_font_family,
                        size=current_font_size,
                         weight=new_weight, slant= text_property['slant'], underline=text_property['underline'])
        text_editor.configure(font=new_font)
    # text_editor.configure(font=(current_font_family, current_font_size, new_weight, text_property['slant'], ('normal' if text_property['underline']==0 else 'underline')))

bold_btn.configure(command=bold)

def italic():
        text_property = tk.font.Font(font=text_editor['font'])
        new_slant = 'italic' if text_property['slant'] == 'roman' else 'roman'
        new_font=font.Font(family=current_font_family,
                        size=current_font_size,
                        weight=text_property['weight'], slant= new_slant, underline=text_property['underline'])
        text_editor.configure(font=new_font)
    # text_editor.configure(font=(current_font_family, current_font_size, text_property['weight'], new_slant, text_property['underline']))

italic_btn.configure(command=italic)

def underline():
        text_property = tk.font.Font(font=text_editor['font'])
        new_underline = 1 if text_property['underline'] == 0 else 0
        new_font=font.Font(family=current_font_family,
                                size=current_font_size,
                                weight=text_property['weight'], slant= text_property['slant'], underline=new_underline)
        text_editor.configure(font=new_font)
    # text_editor.configure(font=(current_font_family, current_font_size, text_property['weight'], text_property['slant'],new_underline))

underline_btn.configure(command=underline)

# ----color chooser----

def font_color():
    global color_count
    text_color=tk.colorchooser.askcolor()
    text_editor.config(foreground=text_color[1]) #((255, 87, 51), '#ff5733'-)-->1


color_btn.config(command=font_color)

# ----alignment----

def clear_alignment():
    text_editor.tag_remove("left", "1.0", "end")
    text_editor.tag_remove("center", "1.0", "end")
    text_editor.tag_remove("right", "1.0", "end")

def align_left():
    clear_alignment()
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.tag_add('left', '1.0', 'end')

left_btn.config(command=align_left)

def align_center():
    clear_alignment()
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.tag_add('center', '1.0', 'end')

center_btn.config(command=align_center)

def align_right():
    clear_alignment()
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.tag_add('right', '1.0', 'end')

right_btn.config(command=align_right)

# -----------------------------end text editor and status bar----------------------------

# -----------------------------main menu functionality---------------------------------

## Variable

url=''

## File commands

# Open functionality
original_content=''

def open_file(event=None):
    global url, original_content
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            original_content=fr.read()
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, original_content)
    except FileNotFoundError:
        return 
    except:
        return
    application.title(os.path.basename(url))

file.add_command(label = 'Open', image = open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

## New functionality

def new_file(event=None):
    global url, original_content
    try:
        current_content=text_editor.get(1.0,tk.END).strip()
        if current_content != original_content:
            mbox=messagebox.askyesnocancel("Warning","Do you want to save the changes?")
            if mbox is True:
                if url:
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(current_content)
                else:
                    url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(("Text",".txt"),("All files","*.*")))
                    url.write(current_content)
                    url.close()
                url=''
                text_editor.delete(1.0, tk.END)
                application.title('My Text Editor')                
            elif mbox is False:
                url=''
                text_editor.delete(1.0, tk.END)
                application.title('My Text Editor')
        else:
            url=''
            text_editor.delete(1.0, tk.END)
            application.title('My Text Editor')
    except:
        return
    

file.add_command(label = 'New', image = new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)


# Save functionality

def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0, tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w', defaultextension=".txt" ,filetypes=(("Text File",".txt"),("All Files","*.*")))
            content2=str(text_editor.get(1.0, tk.END))
            url.write(content2)
            application.title(os.path.basename(url.name))
            url.close()
    except:
        return

file.add_command(label = 'Save', image = save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)

# Save as functionality

def save_as_file(event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(("Text file",".txt"),("All files","*.*")))
        content=str(text_editor.get(1.0, tk.END))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label = 'Save as', image = save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as_file)

# Exit functionality

def exit(event=None):
    global url, original_content
    try:
        current_content=text_editor.get(1.0,tk.END).strip()
        if current_content != original_content:
            mbox=messagebox.askyesnocancel("Warning","Do you want to save the changes?")
            if mbox is True:
                if url:
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(current_content)
                        application.destroy()
                else:
                    url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(("Text",".txt"),("All files","*.*")))
                    url.write(current_content)
                    url.close()
                    application.destroy()
            elif mbox is False:
                application.destroy()
        else:
            application.destroy()
    except:
        return    

file.add_command(label = 'Exit', image = exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit)

def undo_action(event=None):
    try:
        text_editor.edit_undo()  # Undo last change
    except tk.TclError:
        pass  # No more actions to undo

def redo_action(event=None):
    try:
        text_editor.edit_redo()  # Redo last undone change
    except tk.TclError:
        pass 

## Edit commands

edit.add_command(label='Undo', image=undo_icon, compound=tk.LEFT ,accelerator='Ctrl+Z', command=undo_action)
edit.add_command(label='Redo', image=redo_icon, compound=tk.LEFT ,accelerator='Ctrl+Y', command=redo_action)
edit.add_command(label = 'Copy', image=copy_icon, compound = tk.LEFT, accelerator = 'Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label = 'Paste', image=paste_icon, compound = tk.LEFT, accelerator = 'Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label = 'Cut', image=cut_icon, compound = tk.LEFT, accelerator = 'Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label = 'Clear all', image=clear_all_icon, compound = tk.LEFT, accelerator ='Ctrl+Alt+X', command=lambda:text_editor.delete(1.0, tk.END))
application.bind_all("<Control-Alt-x>", lambda event: text_editor.delete(1.0, tk.END))


# Find functionality

def find(event=None):

    def find_func():
        word=find_entry.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        match=0

        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match', start_pos, end_pos)
                match+=1
                start_pos=end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
        else:
            messagebox.showwarning("Not Found", "No word to find")
        find_dialogue.lift()

    def replace_func():
        word=find_entry.get()
        new_word=replace_entry.get()

        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.delete(start_pos, end_pos)
                text_editor.insert(start_pos, new_word)
                start_pos=end_pos
        else:
            messagebox.showwarning("Not Found","No word to replace")
        find_dialogue.lift()

        # content=text_editor.get(1.0, tk.END)
        # content1=content.replace(word, new_word)
        # text_editor.delete(1.0, tk.END)
        # text_editor.insert(1.0, content1)

    find_dialogue=tk.Toplevel()
    find_dialogue.geometry("400x150+500+200")
    find_dialogue.title('Find')
    find_dialogue.grab_set()
    find_dialogue.resizable(0,0)
    # find_dialogue.attributes('-topmost', 1)

    # Label Frame
    frame=ttk.LabelFrame(find_dialogue, text='Find/Replace')
    frame.pack(pady=20, padx=10, fill="both")

    inner_frame=tk.Frame(frame, width=400, height=500, bg ="lightgray")
    inner_frame.pack(fill="both", expand=True)
    inner_frame.grid_propagate(False)

    # Labels
    find_label=ttk.Label(inner_frame, text='Find: ')
    replace_label=ttk.Label(inner_frame, text='Replace: ')

    # Entry Box
    find_entry=ttk.Entry(inner_frame, width=40)
    replace_entry=ttk.Entry(inner_frame, width=40)

    #Find/Replace Button
    find_btn=ttk.Button(inner_frame, text='Find', command=find_func)
    replace_btn=ttk.Button(inner_frame, text='Replace', command=replace_func)

    # Button grid
    find_btn.grid(row=2, column=0, columnspan=2)
    replace_btn.grid(row=2, column=1, columnspan=2, sticky="e")

    #Entry grid
    find_entry.grid(row=0, column=1, padx=5,pady=5)
    replace_entry.grid(row=1, column=1,padx=5,pady=5)

    # Label grid
    find_label.grid(row=0, column=0,padx=5,pady=5)
    replace_label.grid(row=1, column=0,padx=5,pady=5)

edit.add_command(label = 'Find', image=find_icon, compound =tk.LEFT, accelerator='Ctrl+F', command=find)

## View commands

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False 
    else :
        main_frame.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        main_frame.pack(expand=True, fill=tk.BOTH)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.grid_forget()
        show_statusbar = False
    else :
        status_bar.grid(row=1, column=0,sticky='ew')
        show_statusbar = True 

view.add_checkbutton(label = 'Tool bar', onvalue=True, offvalue=False , variable = show_toolbar ,image = toolbar_icon, compound = tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label = 'Status bar', onvalue=True, offvalue=False , variable = show_statusbar ,image = status_icon, compound = tk.LEFT, command=hide_statusbar)

## Color Commands

def change_theme():
    theme=theme_choice.get()
    color_tuple=color_dict.get(theme)
    fg_color,bg_color=color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, foreground=fg_color)

count=0
for i in color_dict:
    colortheme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count+=1
# -----------------------------End Main menu functionality-----------------------------

## Bind shortcut keys

application.bind('<Control-n>', new_file)
application.bind('<Control-s>', save_file)
application.bind('<Control-Alt-s>', save_as_file)
application.bind('<Control-q>', exit)
application.bind('<Control-o>', open_file)
application.bind('<Control-f>', find)
text_editor.bind("<Control-z>", undo_action)
text_editor.bind("<Control-y>", redo_action)


application.config(menu = main_menu)

application.mainloop()
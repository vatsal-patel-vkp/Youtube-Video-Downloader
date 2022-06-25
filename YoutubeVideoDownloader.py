'''Importing libraries'''
from tkinter import *
from tkinter import filedialog
from pytube import YouTube


foldername = ""

'''Defining Functions Starts here'''
'''Function to Save the file'''
def openlocation():
    global foldername
    foldername = filedialog.askdirectory()
    if(len(foldername) > 1):
        location.config(text= foldername, fg= 'green')
    else:
        location.config(text= 'Please choose appropriate path!', fg= 'red')


def Download_video():
    try:
        message.set('Downloading...')
        #root.update()
        vid = YouTube(link.get())
        '''for stream in vid.streams:
            print(stream)
        '''
        vid.streams.filter(progressive=True, res="720p").first().download()
        #vid.streams.filter(progressive=True, file_extension="mp4", resolution="360p")
        success_msg.set('Video Downloaded Successfully')
    except Exception as e:
        message.set("Error!")
        root.update()
        success_msg.set('Error has occurred!\nCheck the link!')
        

'''Creating Reset Function'''
def Reset():
    link.set("")
    message.set("")
    location.config(text= "")
    success_msg.set('')
    
    
'''Creating exit function'''
def Exit():
    root.destroy()

'''Defining Functions Ends here'''


'''Creating Display Window'''
root = Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root, text= 'YouTube Video Downloader', font= 'arial 20 bold').pack()


'''Create field to Enter Link'''
link=  StringVar()
Label(root, text= "Paste the YouTube video link here:- ", font= 'timesnewroman 15 bold').place(x=140, y=60)
link_enter = Entry(root, width= 50, textvariable= link, font= 'timesnewroman 15').place(x=32, y=100)

'''Error Message'''
message = StringVar()
message.set('')
Label(root, textvariable= message, fg= 'red', font= 'arial 15').place(x=32, y= 150)

'''Choose the path'''
Button(root, text= 'Choose location', font= 'arial 15 bold', bg= 'pale violet red', padx= 1, command= openlocation, width= '15', borderwidth= '5').place(x= 50, y=200)

'''Location Error Message'''
location = Label(root, text="", fg= 'red', font= 'arial 10 bold')
location.place(x=32, y= 300)

'''Downloaded successfully message'''
success_msg = StringVar()
success_msg.set('')
Label(root, textvariable= success_msg, fg= 'green', font= 'timesnewroman 15 bold').place(x=32, y= 350)
    

'''Defining buttons'''
Button(root, text= 'Download', font= 'arial 15 bold', bg= 'pale violet red', padx= 1, command= Download_video, width= '10', borderwidth= '5').place(x= 10, y=450)
Button(root, text= 'Reset', font= 'arial 15 bold', bg= 'pale violet red', padx= 1, command= Reset, width= '10', borderwidth= '5').place(x= 300, y=450)
Button(root, text= 'Exit', font= 'arial 15 bold', bg= 'pale violet red', padx= 1, command= Exit, width= '10', borderwidth= '5').place(x= 600, y=450)


'''Run the code'''
root.mainloop()
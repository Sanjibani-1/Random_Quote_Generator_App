# Random_Quote_Generator_App
#CodeAlpha

This Python code is a simple GUI-based Random Quote Generator built using the tkinter library. It provides functionality to display random motivational quotes and allows users to share the quotes on Twitter.

Breakdown of the Code:
Imports:

tkinter and messagebox are used to create the graphical user interface and display messages.
random is used to randomly select a quote from a list.
webbrowser is used to open a browser for sharing the quote on Twitter.
Quotes List:

The list quotes contains five motivational quotes. These quotes are used in the application to randomly display on the screen.
Functions:

get_random_quote(): This function selects and returns a random quote from the quotes list using random.choice().
display_new_quote(): This function updates the label (quote_label) to display a new random quote fetched from get_random_quote(). The quote_label.config() method is used to change the text of the label.
share_on_twitter(): This function shares the current quote displayed on the label via Twitter. It gets the text from quote_label using quote_label.cget("text"). If a quote exists, it opens Twitter's "share" URL in the browser with the quote pre-filled as the tweet. If no quote is displayed, a warning message is shown using messagebox.showwarning().
GUI Setup:

Main Window (root): The root window is created using tk.Tk(). The title is set to "Random Quote Generator", and the window's size is set to 400x300 pixels using root.geometry().
Label (quote_label): This label is used to display the random quote. The text is initially empty, with a wrap length of 300 pixels and the font set to Helvetica with size 14. The pady=30 adds padding around the label.
Buttons:
New Quote Button: This button calls display_new_quote() when clicked to generate a new random quote.
Share on Twitter Button: This button calls share_on_twitter() to share the displayed quote on Twitter.
The buttons are styled with background (bg) and foreground (fg) colors, along with a font specification.
Main Event Loop:

The GUI enters its main event loop with root.mainloop(), which keeps the window open, listening for user interactions (like button clicks).
Functionality Summary:
Generate Random Quote: The user can click "New Quote" to display a random motivational quote from the predefined list.
Share on Twitter: After generating a quote, the user can click "Share on Twitter" to post the quote directly on Twitter via the browser.

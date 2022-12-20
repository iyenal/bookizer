# bookizer
Utility (Python) to reconstitute a PDF book from automated screen captures (eg. kiosk readers)

As an avid reader (my current read: Thinking Fast and Slow, by Economics Nobel Prize Daniel Kahneman), it's painful to have sometimes only available online kiosk readers to be able to read your acquired books, as you'll not be able to access them offline, read them on a device such as a Kindle, archive them and most importantly, you're at the mercy of the platform hosting it.

This utility can merge screens taken by an automated manner such as a macro (recommending Macro Recorder), operate some modifications, and export it in PDF.

## Procedure

Make sure your screen has enough resolution to be able to take qualitative screen captures of your book's pages.
Record a macro (with a visual tool such as Macro Recorder, takes few mins) that click on the next page every X seconds, and fires a key that will be recognized by a tool like ShareX to print screen automatically to an image (normal printscreen only saves the image in clipboard).
When your macro has finished, change in script the zone's coordinates to fit exactly the book's page/pages, and run the Python script.

## Possible improvements

This utility is quite basic and simple, leaving many possible improvements:
- OCR detection of characters
- Automatic detection of page zone
- Integrated macro playing

Please be welcome to contribute.

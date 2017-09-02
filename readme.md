# Mailipy - Mailing to suscribers
This program use [Markdown](https://en.wikipedia.org/wiki/Markdown) a lightweight markup language with plain text formatting syntax. You can check a [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for learn it.

credits to [python-Markdown2](https://github.com/trentm/python-markdown2) a python library to parse markdown to html.

## How this program can help you?
If you are an event organizer, teacher or someone who needs to send one mail to multiple contacts or subscribers, this will serve exactly for that purpose.

## Prerequisites
* python 2.7

## How to use it?
Well first let see what do you normally need to send an email.

* Subject
* Body
* Attachments
* Destinataries

### Body
Edit the body.md file and change with your content. Remenber you can use headings, images, links, etc. Thank to Markdown.

### Attachments
Copy all your attachments on the *attachments* folder.   
The program will attach all files on this folder.

### Destinataries
Open the data.csv file with Excel or LibreOffice Calc and write all your destinataries on the column "A".

### Subject
Run the next command.

``` bash
python maili.py -s "<email subject>" -e "<your email>" -p "<your email password>"
```
or
``` bash
python maili.py --subject="<email subject>" --email="<your email>" --password="<your email password>"
```

Remenber replace <> and anything inside them.

## License

[MIT License](https://github.com/GudarJs/Mailipy/blob/master/LICENSE)

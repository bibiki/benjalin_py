Benjalin
========

This is a personal develoment application based on Benjamin Franklin's plan for 'arriving at moral perfection.' Benjalin is a small application that you can run locally. It is based on Benjamin Franklin's plan for personal development as described in his autobiography. In his pursuit for personal development, he identified 13 virtues he wanted to improve on. His decision was to focus every week on one of the virtues and evaluate himself daily on it. I devised this scoring system where the user can chose to score themselves on a virtue daily. I have also made available a small message input that is intended to serve as a note for the selected virtue for the selected day.

In this process of self-improvement, mister Franklin realized that an infallible life is impossible, but deliberate improvement should be pursued. Here are his own words:
"But, on the whole, tho' I never arrived at the perfection I had been so ambitious of obtaining, but fell far short of it, yet I was, by the endeavour, a better and a happier man than I otherwise should have been if I had not attempted it"

If this piqued your curiosity, you can always find Benjamin Franklin's autobiography freely available on gutenberg.org or you can buy it elsewhere online.


The code for this application
=============================

You may find the code here.

This is written in Python and makes use of an sqlite database. The file for the sqlite database may be found in user_home/benjalin/ directory, and the file will be named benjalin.db

If, however, you have any questions, please feel invited to reach out to me either via gumroad, my twitter [benjalin_](https://twitter.com/benjalin_), or my [github](https://github.com/bibiki)

If you want to build the executable from the code:

Make sure you have python installed in your system. Once you have python in your system, you can run the following command to install pyinstaller

```
pip install pyinstaller
```

With pyinstaller in your system you may run the following command to build the executable for this application. Your current working directory must contain the files benjalin.py and db.py for this to work.

```
pyinstaller --onefile benjalin.py
```

The result of this command is that at least a dist/ directory will be created containing the benjalin executable. You may double click or run some other way that file to start the application.

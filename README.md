# README
Demo code for how to use Camelot to extract data from tables in PDFs. Examples are taken from this [article](https://medium.com/@marizu_makozi/extracting-tables-in-pdf-using-python-d520b6d8a66).

These are instructions for macOS.  Linux would be somewhat similar.  Your milage may vary on Windows.

## Dependencies 
Camelot depends on TKinter and ghostscript.  (See [docs](https://camelot-py.readthedocs.io/en/master/user/install.html#install)).  The official documentation states that you will need to install TKinter separately, however when going through this demo using Python 3.8 I found that step was not necessary.  You will need to install ghostscript though.  That is easily done with Brew.

`brew install ghostscript`

Once ghostscript is installed all you will need to do is install camelot.  

`pip install "camelot-py[cv]"`
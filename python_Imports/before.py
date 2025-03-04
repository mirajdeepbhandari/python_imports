#________________________________________________________________________________
############################  utils/Mail.py #####################################

"""
def giveMail():
    return "hello you got mail, " + "Miraj Bhandari"

"""


#________________________________________________________________________________
############################  routes/state.py #####################################

"""
from utils.mail import giveMail

mail = giveMail()

"""

#________________________________________________________________________________
############################  routes/test.py #####################################

"""
from state import testmail

mail = testmail()

print(mail)

"""


# ________________________________________________________________________________
# utils and routes dont have ___init__.py


#_________________________________if i run  python routes\test.py______________________________________

"""
C:\Users\mirajD\Desktop\python_Imports>python routes\test.py
Traceback (most recent call last):
  File "C:\Users\mirajD\Desktop\python_Imports\routes\test.py", line 1, in <module>
    from state import testmail
  File "C:\Users\mirajD\Desktop\python_Imports\routes\state.py", line 1, in <module>
    from utils.mail import giveMail
ModuleNotFoundError: No module named 'utils'
"""
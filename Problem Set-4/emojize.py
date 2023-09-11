#I made this program in Google Colab so i need to install the library first.
!pip install emoji  # This section of code is only for Colab notebook for installing a library
from emoji import emojize

User_input= input("Input: ")
print("Output:",emojize(input, language='alias'))

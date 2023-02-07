# ASCII Translator
A simple GUI that allows the user to convert ASCII codes in their corresponding chars and also to do the inverse operation

The GUI presents a texbox to input ascii codes and chars to convert them in the corresponding counterpart, and a single button to send the input to the function below.

For a better UX a double click in the textbox allows the user to clear the content of both input and output. Moreover the user can press "ENTER" directly by the input textbox to display the output instead of clicking the "Convert" button.

## Compile the program
First thing first, to run and compile the program you need to have Python installed in your computer.

To compile the program install `pyinstaller` from the terminal with the command -> `pip install pyinstaller`
After that you can compile the program to generate an exe file running in the terminal in the same directory as the project the command:
`pyinstaller --onefile --noconsole -w -F --add-binary ".\resources\ascii.png;." --icon=resources\ascii.ico ascii_translator.py`.

In the end remember to copy the entyre `\resources` folder in the neo-generated `dist` folder. Here you will find the .exe file **ascii_translator.exe**, to use it on every computer you have to copy the full `dist` directory (that could be renamed as you want, for example 'ascii_translator'). Remember to have python installed to run the program.

|![image](https://user-images.githubusercontent.com/45337472/216968715-fb68403c-e607-4836-93f3-c85a9c3f5b48.png)|![image](https://user-images.githubusercontent.com/45337472/216968886-4a75879e-29ab-4212-af5b-843aad188336.png)|
|![image](https://user-images.githubusercontent.com/45337472/216969001-5772195b-774d-4ac9-9351-a799e984e85f.png)|![image](https://user-images.githubusercontent.com/45337472/216968819-518633bf-5c97-4e94-a16a-3ae4d0d78aea.png)|

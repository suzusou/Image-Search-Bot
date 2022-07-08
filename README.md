# How to create an ImageSearchBot
development environment :python3, venv, flask, ngrok  
Enter the letters you want to search for and the bot will return an image!  
### First, create your own linebot.  
For instructions on how to make them, please refer to this site.  
https://udemy.benesse.co.jp/development/app/line-bot-making.html  

### How to use venv  
Please enter this sentence in the command  
python3(py) -m venv environment Name  ← anything is OK  
environment Name\Scripts\activate.bat  
Now you are ready for venv!  
Reference Site↓  
https://www.python.jp/install/windows/venv.html

### Next,install the necessary libraries.  
Please enter this sentence in the command  
pip install line-bot-sdk  
pip install flask  
pip install beautifulsoup4  
The library installation is now complete.  

### Next, install ngrok.  
You can download it here.↓  
https://ngrok.com/download     　
Select the OS you are using.  
Extract the installed zip file.  
Please enter this sentence in the command  
cd  Path of the file you just extracted  
ngrok http 5000  
Paste the https URL into your own linedevelopers webhook settings  
This completes the ngrok setup.  

#### execution method: flask run  
Enter the letters of the image you wish to search for and the image will be returned.
#### If you found this helpful, please give us a star.

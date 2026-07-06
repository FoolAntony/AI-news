# AI News Digest 

This app is designed to gather and analyze news by AI model, generate the short review of them. The app sends it by email.

### How to setup?

1) First you need to install *Python 3.13* on your device. Next download the required packages via terminal:

    <code>pip install -r requirements.txt</code>
2) Go to *<a ref="https://newsapi.org/">News API</a>* page, create an account and get API key there.
3) Go to *<a ref="https://aistudio.google.com/">Google AI Studio</a>* and generate your API key for it.
4) To send and receive message via email, you will need to generate password for your app. You may create it for gmail on <a ref="https://myaccount.google.com/apppasswords">this page</a>.
5) Create *.env* file in the project directory and add the following variables to it:
    
    <code>GOOGLE_API_KEY="Add your Google AI Studio Key here"</code>

    <code>NEWS_API_KEY="Add your News API Key here"</code>

    <code>SENDER_EMAIL=Add-your-email-address-here</code>
    
    <code>SENDER_EMAIL_PWD=Add-your-email-app-password-here</code>
6) Register and create an API key for your application on *<a ref="https://newsapi.org/">NewsAPI</a>* page.
7) Copy the key and change <code>api_key</code> variable in <a ref="https://github.com/FoolAntony/email-news/blob/master/send_email.py">send_email.py</a> file.
   
 <code>NEWS_API_KEY=Add-your-news-api-key-here</code>

   * *NOTE: you may also update the <code>url</code>* variable in <code>main.py</code> file with other URLs. By using different options, these URLs may be modified with required country, language, content, etc. For more information, please refer to *<a ref="https://newsapi.org/">NewsAPI</a> page*.

8) Run the program from the terminal: <code>python ./main.py</code>

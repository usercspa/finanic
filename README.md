# Finanic

**Introduction**
Due to the outbreak of covid-19, many businesses and services have switched online. Traditional banks have also adapted to the new normal and offer online and mobile banking.  

Opening a bank account is becoming much easier, individuals can fill in the online form, and upload their identification documents for verification. However, not everyone has access to the internet or smart devices.  

To tackle the digital divide, we are building a banking SMS chatbot to help individuals who are less tech-savvy/ without access to the internet/ smart devices to open a bank account.  
  
  
The system allows a personal bank account to be applied for, maintained and used with just using voice commands  
Commands supported:  
- sign up for account  
- check balance  
-  transfer money  
- change password/passphrase
- get account details as a text

the main functionality is in voicebank.py  
there is a helper function in twiliogenericsmssender.py  
this requires credentials in a file (not included, available on request) that contains twilio credentials for usage
  
  
to run the file just run voicebank with python3 and make sure the required libraries are installed.  
because we cannot connect tp a real bank account, we use cryptocurrency to emulate the account. the transfer made actually moves bitcoin (satoshis) and the balance is a true value
  
  
to use with your own wallet, please replace where it says redacted with your private keys
  
 







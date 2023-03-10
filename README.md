# RasaChatGptIntegration
An integration project for those who are interested to connect Rasa to ChatGpt in minimal efforts.


To use it: 

1. Install the prerequisites: 


  a. OpenAI

  b. Rasa[FULL]
  
  c. Rasa-SDK 
  
2. Go to project root directory 

3. Update your OpenAI API key in constant of action.py 

4. From project root directory, run 

    rasa train 

5. From a terminal window, run actions 
    
    rasa run actions --actions actions 

6. From another terminal window, run rasa server shell 
    
    rasa shell 








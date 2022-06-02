# AssemblyAI-Flask-Heroku

This uses the AssemblyAI Speech to text API's to transcribe from audio url sources hosted
on S3 bucket and twilio.
S3 and twilio are tested. Some external links might also work. 
Also demonstrates some common bootstrap elements like Page loading , Cards etc

Deployed using Heroku
steps to deploy 
1. git clone 
2. cd repo
( edit files if needed otherwise skip step (3-5)  ) 
3. git add .
4. git commit 
5. git push 
6. heroku login ( need heroku account and cli tool)
7. heroku create app_name 
8. git push heroku main/master

for deployments errors run
$ heroku logs --tail




Read more about the AssemblyAI API from here - https://docs.assemblyai.com/#introduction
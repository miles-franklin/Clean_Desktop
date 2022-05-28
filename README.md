# Clean_Desktop
This moves all of my image files from my Desktop to a specified folder. I have this running as a cronjob every day at every 10th minute  between 12:00pm and 1:00pm to try to catch me when I'm actually on the laptop. To set this up, open up crontab using 
`crontab -e` or `EDITOR=sublime crontab -e` if you have an editor of choice (i.e. sublime), and then add the following :
<br><br>
`MAILTO = ""`<br>
`# Clean Desktop every 10th minute  between 12:00pm and 1:00pm every day`<br>
`*/10 12 * * * ~/Clean_Desktop/organize_desktop.sh`<br>

Notes:
- `MAILTO = ""` will keep your terminal clean from messages everytime the cron job runs.
- The path may be different depending on where you save this directory to.
- If organize_desktop.sh does not have the permissions it needs, then run `chmod +X organize_desktop.sh` first.


Reference : https://apple.stackexchange.com/questions/378553/crontab-operation-not-permitted

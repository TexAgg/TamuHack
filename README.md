# Hackr
Help hackers find fellow hackers for hackathons.

![Hackr](static/hackr.png)

---

## Inspiration
Many people come to hackathons without a team, 
and must spend valuable time searching for other hackers with similar intrests and skills.
We at Hackr hope to make this a thing of the past.

## What it does
Once you submit your information to us, 
our algorithms will match you with potential teammates at the same hackathon who have similar skills and send you an email to inform you and your match.
Matches can then contact eachother and begin hacking!

## How we built it
Hackr is built using python and flask, and uses Google's [Firebase](https://firebase.google.com/) for a database.

## Challenges we ran into
Finding the best match for teammates and handling all the data in the database.
In addition, MLH has no official API for upcoming hackathons, so we had to scrape their [website](https://mlh.io/seasons/na-2017/events) using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

## Accomplishments that we're proud of
Making something that could be useful for people in future hackathons.

## What's next for Hackr
Adding a login system and profiles, and improving the matching algorithm.

---

Check us out on [DevPost](http://devpost.com/software/hackr-57zcwj)!
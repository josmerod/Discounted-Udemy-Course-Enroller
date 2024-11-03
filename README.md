<p align="center">
    <img src="https://raw.githubusercontent.com/techtanic/Discounted-Udemy-Course-Enroller/refs/heads/master/extra/promo.gif">
    <br/>
    <img src="https://forthebadge.com/images/badges/made-with-python.svg">
    <br/>
    <a href="https://github.com/techtanic/Discounted-Udemy-Course-Enroller/graphs/commit-activity"><img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge"></a>
    <a target="_blank" href="https://discord.gg/wFsfhJh4Rh"><img alt="Discord" src="https://img.shields.io/discord/703266580846346361.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge"></a>
    <br/>
    <a href="https://github.com/techtanic/Discounted-Udemy-Course-Enroller"><img src="https://cdn.discordapp.com/attachments/823472016999972884/841661124410736710/standard_13.gif"></a>
</p>

# Motivation and justification of this fork

This repository is a fork of the original repository in order to make some enhancements and fixes to the original code. I'm doing this to practice and get more confortable improving existing projects, refining my Python skills and to contribute back to the community. techtanic has done a great job with the original project and I'm just trying to make it better. 

 I've added the following features:
- Fixed the program getting stuck when retrieving the list of courses from the websites, by adding a timeout to the requests and a retry mechanism.
- Added total number of courses count on the CLI version after the process has been completed
- Modified the original cli-settings file to use the credentials from Google Chrome and to filter to specific requirements. 
- Added Course Joiner as a source for courses (in draft version, needs to improve performance).
- Added Cursos Dev as a source for courses (in draft version, testing and tuning up the number of pages, performance is OK)

This is a work in progress and will add more features in the future. If you have any suggestions, please let me know.

My next objectives are:
- Remove Tutorial Bar from the list of websites, has been causing some issues with the program. Target: improve the general reliability of the program.
- Add new websites to get coupons from that might be interesting. Target: get more profficiency with BS4 and requests.
  - Added Course Joiner, suggestions are welcome!
- Create a trigger to notify when the original repository has been updated. Target: automate the process of updating the forked repository.
- Notify a custom Telegram chatbot of new course
- Speedup codebase for joining courses
# Discounted Udemy Course Enroller



> Software to enroll in available Udemy Paid/Free courses having coupons automatically to your Udemy account.

Everything you need can be on the website.: [duce.techtanic.space](https://duce.techtanic.space)

## Key Features

- Beautiful GUI
- One click login using Browser cookies.(Supports major browsers)
- One click to add all available courses with coupons to your udemy account
- Uses popular sites for coupons
- Many more features
- CLI version available for automation
- Advanced filters

# Installation steps (this repository)

1. Clone the repository
2. Install the requirements via `pip3 install -r requirements.txt`
3. (Optional) Enter on Google Chrome and log in to your Udemy account.
4. Modify if you want the `duce-cli-settings.json` file. By default, it will use the credentials from Google Chrome
5. Run ./cli.py or ./gui.py (first one is more recommended for resource friendly)

# Downloads (original repository)

<table>
<thead >
  <tr>
    <th style="text-align: center">GUI</th>
    <th style="text-align: center">CLI</th>
  </tr>
</thead>
<tbody>
  <tr align="center">
    <td><a href="https://github.com/techtanic/Discounted-Udemy-Course-Enroller/releases/latest/download/DUCE-GUI-windows.exe">
         <img alt="GUI Windows exe" src="https://img.shields.io/static/v1?message=Download&logo=windows&labelColor=5c5c5c&color=1182c3&label=%20&style=for-the-badge"
         >
      </a></td>
    <td><a href="https://github.com/techtanic/Discounted-Udemy-Course-Enroller/releases/latest/download/DUCE-CLI-windows.exe">
         <img alt="CLI Windows exe" src="https://img.shields.io/static/v1?message=Download&logo=windows&labelColor=5c5c5c&color=1182c3&label=%20&style=for-the-badge">
      </a></td>
    
  </tr>
</tbody>
</table>

<h2><details>
<summary>Screenshots of GUI</summary>

![Login](https://cdn.discordapp.com/attachments/823472016999972884/834051177792274452/unknown.png)

![Cookie Login](https://cdn.discordapp.com/attachments/823472016999972884/834051201342373888/unknown.png)

![Discounted Udemy Course Enroller](https://cdn.discordapp.com/attachments/823472016999972884/834051568554737674/unknown.png)

![Coupon Scraping](https://cdn.discordapp.com/attachments/823472016999972884/834051762255560704/unknown.png)

![Enrolling](https://cdn.discordapp.com/attachments/823472016999972884/824187751075282974/unknown.png)

</details>

## Disclaimer

This is not the official repository, just a set of changes I've made to ensure more reliability. I'll try to keep up to date to the original repository.

## Donate (from the original creator)

BTC `bc1qdyjwj0eqxjk5hxejah4gyclrumwtqs3hqp63uz`

BTC `14JNjiNoiKcbCHcxcqUxgJcVgyDfhGbxQF`


<center>
Made with ❤️
</center>
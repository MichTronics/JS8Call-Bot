# JS8Call-Bot
This program is a BOT voor JS8CALL. You can use custom commands to send info to remote user in JS8Call. Also you can make QSO in telegram from out of a Telegram channel. The messages from JS8Call wil als be posted in Telegram Channel.


### INSTALLATION:
---

#### JS8Call-Bot

Change the Locator in config.ini
Change Host and Port in config.ini if use other pc where JS8CALL is runningc than JS8Call-Bot.
Change Callsign in config.ini

#### Telegram

You need a Telegram group channel.
Then you need to make a telegram bot with a chat @BotFather.
@BotFather will ask name for your bot and give you a token that you need to change in the config.ini file.
Also you need chatid of the group you have made, you can do that on special way search on google at the moment, more info will follow on that.
The chatid you need to change in config.ini.

##### More detailed info follow soon.


#### OpenWeatherAPI

Register a account on OpenWeatherMap page.
Get API token and change it in the config.ini file.
And change the loction to get the weather of your location

###### More detailed info follow soon.


#### JS8CALL 

Settings in JS8CALL for using the JS8Call-Bot.
Goto settings in JS8CALL and then goto the Reporting Tab, enable this settings below in the API window.

- [x] Allow setting station information from the API
- [x] Enable TCP Server API
- [x] Accept TCP Requests

See picture below for setting in JS8CALL.

![js8call-settings-js8call-bot](https://user-images.githubusercontent.com/60797474/199588064-5dd681f6-984e-4e30-874b-0bb7659e6045.png)


### TODO:
---

If you want options or commands request them in issues.

#### JS8Call

- [x] Add **/HELP** command, give help of what commands u can use in JS8CALL. 
- [x] Add **/WEATHER** command, get weather from your location on OpenWeatherApi and send it to user.
- [x] Need to add better message capture structure for posting messages in Telegram.
- [ ] Add **/QSL** command, for capturing callsign when there is a contest.

#### Telegram

- [x] Add **/help** command, give help of what commands u can use in Telegram.
- [x] Add **/hb** command, send a HeartBeat in JS8CALL
- [x] Add **/cq** command, send a standard CQ in JS8CALL
- [x] Add **/ccq** *message* command, send a custom @ALLCALL CQ CQ *message* JO22 in JS8Call
- [x] Add **/rc** *callsign* *message* command, send a *callsign*>*message* in JS8Call
- [ ] Add **/snr** *callsign* command, send a message to ask *callsign* SNR? in JS8Call




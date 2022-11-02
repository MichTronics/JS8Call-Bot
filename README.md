# JS8Call-Bot
This program is a BOT voor JS8CALL.<br> 
You can use it to send custom commands to JS8CALL.<br>
Also you can make QSO in telegram from out of a Telegram Channel.<br>
The messages from JS8CALL will also be posted in Telegram Channel.<br>


### INSTALLATION:
---

#### Installation instructions Windows

Download latest release on the right under releases, and extract<br>
it with winzip,winrar,7zip in a folder you have created.<br>
Change the config.ini file inside de JS8Call-Bot/config folder more info about de config.ini below.<br>
Run the JS8Call-Bot.exe in the JS8Call-Bot map that was created with extracting.<br>

###### More detailed info follow soon.


#### Installation instructions Linux

###### More detailed info follow soon.


#### Config JS8Call-Bot

Change the Locator in config.ini<br>
Change Host and Port in config.ini if use other pc where JS8CALL is running than JS8Call-Bot.<br>
Change Callsign in config.ini.<br>


#### Config Telegram-Bot

You need a Telegram group channel.<br>
Then you need to make a telegram bot with a chat @BotFather read this<br> 
page https://docs.influxdata.com/kapacitor/v1.6/event_handlers/telegram/ the Telegram Setup section.<br>
@BotFather will ask name for your bot and give you a token that you need to change in the config.ini file.<br>
Then add the bot to the telegram group channel invite him as<br>
user @**BotName**(name of bot you created in step before).<br>
Also you need the chatid of the group you have created, you can do that on special way, use this page for<br> 
it https://docs.influxdata.com/kapacitor/v1.6/event_handlers/telegram/ , more detailed info will follow.<br>
The chatid you need to change in config.ini.<br>

###### More detailed info follow soon.


#### Config OpenWeatherAPI

Register a account on OpenWeatherMap page.<br>
Get API token and change it in the config.ini file.<br>
And change the loction in config.ini so that remote user get the weather of your location when the remote user send a /WEATHER.<br>

###### More detailed info follow soon.


#### JS8CALL 

Settings in JS8CALL for using the JS8Call-Bot.<br>
Goto settings in JS8CALL and then goto the Reporting Tab, enable this settings below in the API window.<br>

- [x] Allow setting station information from the API
- [x] Enable TCP Server API
- [x] Accept TCP Requests

See picture below for setting in JS8CALL.<br>

![js8call-settings-js8call-bot](https://user-images.githubusercontent.com/60797474/199588064-5dd681f6-984e-4e30-874b-0bb7659e6045.png)


### TODO:
---

If you like to see new features or commands request them in issues.<br>


#### JS8Call-Bot

- [x] Add **/HELP** command, give help of what commands u can use in JS8CALL. 
- [x] Add **/WEATHER** command, get weather from your location on OpenWeatherApi and send it to user.
- [x] Need to add better message capture structure for posting messages in Telegram.
- [ ] Add **/QSL** command, for capturing callsign when there is a contest.
- [x] Add detailed installation instructions how to config JS8CALL for JS8Call-Bot.
- [ ] Add detailed Telegram installation instructions.
- [ ] Add detailed OpenWheaterApi installation instructions.
- [ ] Add detailed Linux/Raspberry installation instructions.
- [ ] Add detailed Windows installation instructions.

#### Telegram-Bot

- [x] Add **/help** command, give help of what commands u can use in Telegram.
- [x] Add **/hb** command, send a HeartBeat in JS8CALL
- [x] Add **/cq** command, send a standard CQ in JS8CALL
- [x] Add **/ccq** *message* command, send a custom @ALLCALL CQ CQ *message* JO22 in JS8CALL
- [x] Add **/rc** *callsign* *message* command, send a *callsign*>*message* in JS8CALL
- [ ] Add **/snr** *callsign* command, send a message to ask *callsign* SNR? in JS8CALL




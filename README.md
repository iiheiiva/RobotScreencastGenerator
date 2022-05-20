# READ ME

* Project requires installation of chromedriver that matches your Chrome browser version
* requirements.txt contains all the current packages from `pip freeze` command
* Hiding passwords is achieved with https://github.com/Snooz82/robotframework-crypto 
  * TODO: Place the keys and the password hash outside the project folder and refer to the location as a variable inside  a robot resource file to avoid accidental git commit inclusion

## Example contents of NarrationRecord.js
* Actual file would be all in one line
```json
[
  {
    "suite": "Hello",
    "tests": [
      {
        "name": "Sovellusasetusten muuttaminen",
        "records": [
          {
            "type": "narration",
            "time": 2.18302,
            "message": "Verkkosovelluksen käyttäminen vaatii kirjautumistiedot."
          },
          {
            "type": "narration",
            "time": 14.210219,
            "message": "Vasemmasta valikosta löytyy sovelluksen asetukset."
          },
          {
            "type": "narration",
            "time": 22.930231,
            "message": "Lisätään sovellusprofiiliin halutut tiedot."
          }
        ]
      }
    ]
  },
  {
    "suite": "Hello2",
    "tests": [
      {
        "name": "Google-haun tekeminen Chrome-selaimella",
        "records": [
          {
            "type": "narration",
            "time": 2.156134,
            "message": "Klikataan ensin huomio ikkuna pois."
          },
          {
            "type": "narration",
            "time": 4.219646,
            "message": "Kirjoita haluamasi hakusana ja paina \"enter\"."
          }
        ]
      },
      {
        "name": "Bing-haun tekeminen",
        "records": [
          {
            "type": "narration",
            "time": 3.146503,
            "message": "Kirjoita haluamasi hakusana ja paina \"enter\"."
          }
        ]
      }
    ]
  }
]
```

## RecordedClips contents

The individual recorded clips from the previous `.json` would be named:
* Hello_Sovellusasetusten muuttaminen_1.webm
* Hello2_Google-haun tekeminen Chrome-selaimella_1.webm
* Hello2-Bing-haun tekeminen_1.webm

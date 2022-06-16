# READ ME

## Prerequisites

* Project requires installation of chromedriver that matches your Chrome browser version
`requirements.txt` contains all the current packages from `pip freeze` command
* In addition to this MoviePy requires ImageMagick to be separately installed (this might need some configuration on  Windows)
* Hiding passwords is achieved with https://github.com/Snooz82/robotframework-crypto 
  * TODO: Place the keys and the password hash outside the project folder and refer to the location as a variable inside  a robot resource file to avoid accidental git commit inclusion
``
## Example usage
* TestDispatcher takes any number of `.robot` files as argument
* Robot files `NarrationRecorder.py` library for recording timestamps and narration of the tutorial videos into `NarrationRecord.js`
* Custom keywords for the robot tests are located in ``Resources/Screencast.resource``

```commandline
py .\TestDispatcher.py .\Tests\Hello.robot .\Tests\Hello2.robot
```

### Example contents of NarrationRecord.js
* Actual file would be all in one line
* 
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
            "time": 3.011473,
            "message": "Verkkosovelluksen käyttäminen vaatii kirjautumistiedot."
          },
          {
            "type": "narration",
            "time": 17.078676,
            "message": "Vasemmasta valikosta löytyy sovelluksen asetukset."
          },
          {
            "type": "narration",
            "time": 22.743502,
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
            "time": 3.013192,
            "message": "Klikataan ensin huomioikkuna pois."
          },
          {
            "type": "narration",
            "time": 7.064643,
            "message": "Kirjoita haluamasi hakusana ja paina \"enter\"."
          }
        ],
      }
      {
        "name": "Bing-haun tekeminen",
        "records": [
          {
            "type": "narration",
            "time": 3.016025,
            "message": "Kirjoita haluamasi hakusana ja paina \"enter\"."
          }
        ]
      }
    ]
  }
]
```

### RecordedClips contents

The individual recorded clips from the previous `.json` would be named:
* `Hello_Sovellusasetusten muuttaminen_1.webm`
* `Hello2_Google-haun tekeminen Chrome-selaimella_1.webm`
* `Hello2-Bing-haun tekeminen_1.webm`

### Contents of Results folder
* Raw video without subtitles
* Video with hard coded subtitles
* Subtitles in a format similar to moviePy
  * TODO: include a more commonly used format such as `srt` of `vtt` 
* Timestamps of different test cases

```text
00:00: Sovellusasetusten muuttaminen
00:33: Google-haun tekeminen Chrome-selaimella
00:48: Bing-haun tekeminen
```
from app import app #from our app folder, we need to import instance from app



@app.route('/home')
def homePage():
    return{
        "Oh Hello there" : "CLUTCH!"
    }

@app.route('/')
def landingPage():
    return{
        "You/'ve landed!" : "hope it was a good flight"
    }

@app.route('/test')
def testPage():
    return{
        "TESTINGTESTING" : "123"
    }
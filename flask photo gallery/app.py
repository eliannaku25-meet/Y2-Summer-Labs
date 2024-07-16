from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''
        <html>
            <head>
                <title>Welcome to the Photo Gallery</title>
            </head>
            <body>
                <a href='/pets1'>Pets Gallery</a>
                </br> 
                <a href='/outerspace1'>Outerspace Gallery</a>
                </br> 
                <a href='/food1'>Food Gallery</a>
            </body>
        </html>
    '''

@app.route('/food1')
def food1():
    return '''
        <html>
            <head>
                <title>Welcome to the First Food Page!</title>
            </head>
            <body>
                <h1>Food Gallery</h1>
                <img src="https://media.istockphoto.com/id/1191080960/photo/traditional-turkish-breakfast-and-people-taking-various-food-wide-composition.jpg?s=612x612&w=0&k=20&c=PP5ejMisEwzcLWrNmJ8iPPm_u-4P6rOWHEDpBPL2n7Q=">
                <a href='/food2'>Next Food Gallery</a>
            </body>
        </html>
    '''

@app.route('/food2')
def food2():
    return '''
        <html>
            <head>
                <title>Welcome to the Second Food Page!</title>
            </head>
            <body>
                <h1>Food Gallery</h1>
                <img src="https://media.istockphoto.com/id/1457979959/photo/snack-junk-fast-food-on-table-in-restaurant-soup-sauce-ornament-grill-hamburger-french-fries.webp?b=1&s=170667a&w=0&k=20&c=A_MdmsSdkTspk9Mum_bDVB2ko0RKoyjB7ZXQUnSOHl0=">
                <a href='/food3'>Next Food Gallery</a>
            </body>
        </html>
    '''

@app.route('/food3')
def food3():
    return '''
        <html>
            <head>
                <title>Welcome to the Third Food Page!</title>
            </head>
            <body>
                <h1>Food Gallery</h1>
                <img src="https://starwalk.space/gallery/images/what-is-space/1920x1080.jpg">
                <a href='/home'>Back to Home</a>
            </body>
        </html>
    '''

@app.route('/pets1')
def pets1():
    return '''
        <html>
            <head>
                <title>Welcome to the First Pets Page!</title>
            </head>
            <body>
                <h1>Pets Gallery</h1>
                <img src="https://media.wired.com/photos/593261cab8eb31692072f129/master/pass/85120553.jpg">
                <a href='/pets2'>Next Pets Gallery</a>
            </body>
        </html>
    '''

@app.route('/pets2')
def pets2():
    return '''
        <html>
            <head>
                <title>Welcome to the Second Pets Page!</title>
            </head>
            <body>
                <h1>Pets Gallery</h1>
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3HTgKkm-tBcNbiLG5eCL12nOngY_fEta2BA&s">
                <a href='/pets3'>Next Pets Gallery</a>
            </body>
        </html>
    '''

@app.route('/pets3')
def pets3():
    return '''
        <html>
            <head>
                <title>Welcome to the Last Pets Page!</title>
            </head>
            <body>
                <h1>Pets Gallery</h1>
                <img src="https://prd-sc102-cdn.rtx.com/-/media/ca/product-assets/marketing/s/space/space-symposium-graphic_1920x1080.jpg?rev=2a22f490c9c644a5bf69ef3cce59813d">
                <a href='/home'>Back to Home</a>
            </body>
        </html>
    '''

@app.route('/outerspace1')
def outerspace1():
    return '''
        <html>
            <head>
                <title>Welcome to the First Space Page!</title>
            </head>
            <body>
                <h1>Outer Space Gallery</h1>
                <img src="https://live-production.wcms.abc-cdn.net.au/8393f16b3a14cd32d0d5d75c1c05d56b?impolicy=wcms_crop_resize&cropH=1080&cropW=1918&xPos=1&yPos=0&width=862&height=485">
                <a href='/outerspace2'>Next</a>
            </body>
        </html>
    '''

@app.route('/outerspace2')
def outerspace2():
    return '''
        <html>
            <head>
                <title>Welcome to the Second Space Page!</title>
            </head>
            <body>
                <h1>Outer Space Gallery</h1>
                <img src="https://c02.purpledshub.com/uploads/sites/48/2020/04/Things-never-knew-astronomy-e454e5d.jpg">
                <a href='/outerspace3'>Next</a>
            </body>
        </html>
    '''

@app.route('/outerspace3')
def outerspace3():
    return '''
        <html>
            <head>
                <title>Welcome to the Last Space Page!</title>
            </head>
            <body>
                <h1>Outer Space Gallery</h1>
                <img src="https://cdn.mos.cms.futurecdn.net/2oNNWzMiyntgoVjmedmpdn.jpg">
                <a href='/home'>Back to Home</a>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

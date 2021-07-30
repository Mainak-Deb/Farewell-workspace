import os


content='''
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
            <title>Zenlan Scrapbook Example</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="//code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
            <link rel='stylesheet' href="lib/isotope.css"/>
        <style>
            @import url("https://fonts.googleapis.com/css?family=Indie+Flower");
        @import url("https://fonts.googleapis.com/css?family=Zilla+Slab+Highlight");
        body {
        font-family: "Indie Flower", cursive;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/seamless_paper_texture.png);
        }

        .scrapbook {
        width: 590px;
        height: 790px;
        }

        .l {
        border-top-left-radius: 80px 5px;
        border-bottom-left-radius: 80px 5px;
        }

        .r {
        border-top-right-radius: 80px 5px;
        border-bottom-right-radius: 80px 5px;
        }

        .hard {
        font-size: 150%;
        font-family: "Zilla Slab Highlight", cursive;
        color: gold !important;
        box-shadow: 0 0 10px #999;
        border-top-left-radius: 0px !important;
        background-color: red !important;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/black_paper.png) !important;
        text-align: center;
        color: white;
        height: 610px;
        }
        .hard h4 {
        font-family: "Indie Flower", cursive;
        color: white;
        }

        #magazine {
        margin: auto;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/seamless_paper_texture.png) !important;
        }
        #magazine .page {
        z-index: 1000 !important;
        background-color: grey;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/linedpaper.png);
        border: solid 1px grey;
        }
        #magazine .page .top-margin {
        height: 14px;
        }
        #magazine .page p {
        margin: 0px;
        margin-top: 1px;
        margin-left: 10px;
        }

        #magazine .turn-page {
        background-color: #ccc;
        }

        #magazine .shadow {
        position: relative;
        box-shadow: 0 4px 10px #666;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/black_paper.png);
        z-index: -1000 !important;
        }

        .image-one {
        width: 300px;
        height: 199px;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/AwardsSmall.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        border: solid 4px grey;
        transform: skew(5deg, -5deg);
        }

        .doodle {
        margin-left: 18px;
        color: grey;
        font-size: 80%;
        transform: skew(35deg, -35deg);
        }

        .centered {
        color: blue;
        margin-left: 20px;
        transform: skew(5deg, -5deg);
        }

        .networking {
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/Networking.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        width: 510px;
        right: 48px;
        height: 390px;
        border: solid 15px white;
        box-shadow: 0 4px 10px lightgrey;
        transform: skew(3deg, -3deg);
        }
        .networking:after {
        content: "A bit of networking before the ceremony!";
        left: 20%;
        bottom: 0px;
        position: absolute;
        color: blue;
        }

        .vote-for-me {
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/Vote.PNG);
        background-size: contain;
        background-repeat: no-repeat;
        width: 910px;
        right: 48px;
        height: 390px;
        }

        .reading-award {
        position: absolute;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/ReadingAward.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        right: 48px;
        height: 390px;
        top: 100px;
        border: solid 15px white;
        box-shadow: 0 4px 10px lightgrey;
        width: 233px;
        transform: skew(-7deg, 7deg);
        }

        .dan-marsh {
        position: absolute;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/DanMarsh.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        height: 330px;
        width: 190px;
        top: 100px;
        left: 30px;
        border: solid 15px white;
        box-shadow: 0 4px 10px lightgrey;
        transform: skew(7deg, -7deg);
        }

        .heart-rate {
        position: absolute;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/HeartRate.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        height: 300px;
        width: 140px;
        border: solid 15px white;
        box-shadow: 0 4px 10px lightgrey;
        transform: skew(8deg, -8deg);
        right: 30px;
        bottom: 50px;
        }

        .recieving-award {
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/JustMe.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        height: 370px;
        width: 570px;
        border: solid 15px white;
        box-shadow: 0 4px 10px lightgrey;
        }

        .london-bridge-postcard {
        width: 370px;
        margin-left: 30px;
        height: 300px;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/londonbridge-620x413.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        transform: skew(-15deg, 15deg);
        }

        .glaziers-hall {
        margin: 10px;
        margin-top: 30px;
        margin-left: auto;
        margin-right: auto;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/glaziers1.jpg);
        border: solid 20px white;
        box-shadow: 0 1px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        width: 285px;
        height: 200px;
        background-size: contain;
        background-repeat: no-repeat;
        transform: skew(15deg, -15deg);
        }

        .red-marker {
        color: #990000;
        font-weight: bold;
        }

        .blue-marker {
        color: blue;
        font-weight: bold;
        }

        .skew-3 {
        color: blue;
        position: absolute;
        bottom: 220px;
        right: 250px;
        transform: skew(-15deg, 15deg);
        }

        .skew-2 {
        margin-left: 380px;
        transform: skew(-15deg, 15deg);
        }

        .pencil-sketch-award {
        position: absolute;
        left: 150px;
        top: 160px;
        width: 300px;
        height: 400px;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/PencilSketchAward.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        border: solid 1px lightgrey;
        transform: skew(-4deg, 4deg);
        }
        .pencil-sketch-award:before {
        width: 90px;
        height: 25px;
        opacity: 0.4;
        left: -20px;
        bottom: 0px;
        position: absolute;
        content: "";
        background: DarkKhaki;
        transform: skew(-45deg, 45deg);
        }
        .pencil-sketch-award:after {
        width: 90px;
        height: 25px;
        opacity: 0.4;
        right: -10px;
        top: 16px;
        position: absolute;
        content: "";
        background: DarkKhaki;
        transform: skew(-45deg, 45deg);
        }

        .image-two {
        position: absolute;
        left: 60px;
        width: 166px;
        height: 250px;
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/30843299538_794fce528e_m.jpg);
        background-size: contain;
        background-repeat: no-repeat;
        border: solid 2px lightgrey;
        transform: skew(-4deg, 4deg);
        }
        .image-two:after {
        width: 100px;
        height: 30px;
        opacity: 0.7;
        left: 97px;
        top: 10px;
        position: absolute;
        content: "";
        background: DarkKhaki;
        transform: skew(-35deg, 35deg);
        }
            </style>
        </head>
        <body>
            <div id="magazine">
                <div class="hard">
                <h1>National Apprenticeship Awards 2018</h1>
                <h2>London Region</h2>
            <h4>A Scrapbook<h4>
                <h4>Powered by Turn.JS</h4>
                <!--<h3>Book</h3>-->
                </div>
                <div class="hard">
                </div>
                <div class="own-size scrapbook l">
                <div class="top-margin"></div>
                <p><b>The Ceremony</b></p>
                <p>On the 14th September, I was invited to Glaziers Hall on the South Bank to attend the 2018 London Regional Apprenticeship Awards, the building itself is right next to London Bridge.</p>
                <div class="glaziers-hall"></div>
                <div class="london-bridge-postcard"></div>
                <p></p>
                
                </div>
                <div class="own-size scrapbook r">
                    <div class="top-margin"></div>
                    <div class="top-margin"></div>
                <div class="image-two"></div>
                <p style="margin-top: 270px;  transform: skew(-4deg, 4deg);">Picture of me taken at the awards</p>
                
                <div style="position:absolute; top:50px; right:50px; width: 250px;">
                        <p >The event started with photographs being taken, followed by an hour of drinks and networking.</p>
                </div>
            
                
                
                <div class="networking"></div>
                
                </div>
                <div class="own-size scrapbook l">
                <div class="top-margin"></div>
                    <p>
                            <b>The Lloyds Banking Group Award for the Rising Star</b>
                </p>
                <p>
            
            
                    <i>
                    "The Lloyds Banking Group Award for the Rising Star: awarded to apprentices who have made impressive progress in their career to date and who show the potential, through their apprenticeship, to make it to the very top of their chosen profession"</i>
        <br><br>            <i>
                    "The Lloyds Banking Group Award for the Rising Star: awarded to apprentices who have made impressive progress in their career to date and who show the potential, through their apprenticeship, to make it to the very top of their chosen profession"</i>
                    
                </p>
                
                <div class="doodle">
                    <p> Pencil Sketch of my Award</p>
                    <p><del>Made using an online image editor</del></p>
                </div>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <div class="centered">
                <p>This award was one of three awards new for 2018! </p>
                <p>I guess that makes me one of the first to win it ☺</p>
                </div>
                
                <div class="skew-2 red-marker">
                <p>Easily my proudest </p>
                    <p>achievement to date</p>
                </div>
                </div>
                <div class="own-size scrapbook r">
                    <div class="top-margin"></div>
                <p><b>The Announcement</b></p>
                
                <p>The Rising Star award was read out by Emily Woffenden (right) of the Lloyds Banking Group, following a truly inspirational talk from Dan Marsh (left).</p>
                    <div class="dan-marsh"></div>
                <div class="reading-award"></div>
            
                
                <div class="heart-rate"></div>
                <div class="skew-3">
                <p>Visible heart rate spike on my fitbit as </p>
                    <p>the award was being read out...</p>
            
                </div>
                
                
                </div>
                <div class="own-size scrapbook l">
                        <div class="top-margin"></div>
                <p><b>Recieving the Award</b></p>
                <p>Posing for a photograph, completely bewildered... </p><p>Not my favourite picture, but I was caught off guard!</p>
                
                
                    <div class="recieving-award"></div>
                <div class="red-marker">
                    <br/>
                        <p>Winning the London Regional award is incredible, but as if that wasn't enough, that means automatically being put forward for the national awards!</p>
                </div>
            
                
                </div>
            
                <div class="own-size scrapbook r">
                            <div class="top-margin"></div>
                    <p><b>The National Award</b></p>
                    <p>These are the candidates for the overall national award, one for each region.</p>
                    <p>If you're looking at this before the 17th October 2018 - why not vote for me? It doesn't require any sign-up and only takes a second.</p>
                    <p>
                    <a href="https://appawards.co.uk/vote">appawards.co.uk/vote</a>
                    </p>
                    <div class="vote-for-me"></div>
                    <p>Best of luck to everyone!</p>
                    </div>
                <div  class="hard"></div>
                <div  class="hard"></div>
            </div>
        </body>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/937765/turn.js"></script>


        <script>

            
        'use strict';

        $('#magazine').turn({
        display:"double",
        width: 1200,
                height: 800,
        gradients: true, acceleration: true, turnCorners: "tl,tr"});


        </script>
        </html>
'''
  
  
# Specify the pathC:\Users\hp\Documents\Farewell\python folder\
path = 'C:/Users/hp/Documents/Farewell/CSE htmls'
  
# Specify the file name
file = 'myfile2.html'
  
s='''
<html>
    <body>
        <h1>Heading</h1>
    </body>
</html>
'''
with open(os.path.join(path, file), 'w', encoding='utf-8') as fp:
    fp.write(content)
    fp.close()
  
    pass
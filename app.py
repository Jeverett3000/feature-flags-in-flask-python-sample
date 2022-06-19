from flask import Flask, render_template
import configcatclient

configcat_client = configcatclient.create_client('xVDaCOo_-UKEeY1TeoFYHw/shuqm43hLE2LZQmMbrp8nw')

isCanShowSubscriptionPageEnabled = configcat_client.get_value('canshowsubscriptionpage', False)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/subscribe')
def subscribe():
    if isCanShowSubscriptionPageEnabled:
        return render_template('subscribe.html')
    else:
        return render_template('not-available.html')

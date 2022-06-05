from flask import Flask, render_template
import configcatclient

configcat_client = configcatclient.create_client('JjfaCL3OkE-K7KlUIm5bjw/p9xZ6rbmiUiIOY-ylC4Gnw')

isMyAwesomeFeatureEnabled = configcat_client.get_value('canshowtrendingmovies', False)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/subscribe')
def subscribe():
    if isMyAwesomeFeatureEnabled:
        return render_template('subscribe.html')
    else:
        return render_template('not-available.html')

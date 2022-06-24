# feature-flags-in-flask-python-sample
A companion repo for "How to use Feature Flags with flask (python web framework)" 

## About this sample app

This app is a fictional movie app called AcmeTV Shows built with the Nuxt.js framework

Here is what it looks like:

![image](https://user-images.githubusercontent.com/74829200/174487938-e0138ed0-098a-4e2a-8522-4e6032af1a7f.png)

## How it works

The app has three (3) pages:

1. Home Page
2. Subscription Page
3. Not Available Page

The companion article discussed the use of ConfigCat's feature flag services for feature flagging. This allowed me to render the **Subscription page** if the Feature Flag is switched on and render the **Not Available** page if its off.

## How to run the App

1. Clone this repository

2. Open a terminal in the root of this repo

3. Create and activate a python virtual environment:


```bash
virtualenv venv

```

```bash
source venv/bin/activate
```

4. Install the required python packages by running:

```bash
pip install -r requirements.txt

```

5. Set the Flask environment to development:

```bash
export FLASK_ENV=development

```

6. Start the Flask app by running:

```bash
flask run

```

## Reference

**ConfigCat** also supports many other frameworks and languages. Check out the full list of supported SDKs [here](https://configcat.com/docs/sdk-reference/overview/)

Keep up with ConfigCat on [Twitter](https://twitter.com/configcat), [Facebook](https://www.facebook.com/configcat), [LinkedIn](https://www.linkedin.com/company/configcat/), and [GitHub](https://github.com/configcat).

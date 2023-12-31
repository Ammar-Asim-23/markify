# Markify

_Markify_ is a Smart Digital Marketting Platform designed to help you market your products.

### Key Features

Here are some key features of the project:
  - Save and manage leads and clients
  - Create and promote ads from products
  - Share ads on social media
  - User teams with subscription plans
  - Customized email service
  - And much more!

### Future Expansions

This project is still under development! Here is what we will do in future expansion:
  - Integrate the products with stripe payment gateway so it is possible to buy products from our website.
  - Integrate a stripe subscription gateway to buy plans.
  - Currently we are using smtp4dev to send emails in a testing enviroment but before production we have to change the EMAIL_HOST to a production grade smtp.
  - Deploy the Website!

### Acknowledgements

Special thanks to Bilal Ahmer Founder of SayabiDevs for guiding us throughout our internship program and making this project possible.

### How to Use For Development

Install Docker Desktop

First go to [replicate.com](https://replicate.com/) and register with your Github Account.

Create an API Key and insert it in markify/product/ai_models/ad_generator.py in place of os.environ["REPLICATE_API_TOKEN"]

Use this command in cli when running markify for the first time.
`docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev`

Otherwise use this command to save resources
`docker run -p 3000:80 -p 2525:25 rnwood/smtp4dev`

Setup a python enviroment and install requirements.txt .

Then run command
`python markify/manage.py runserver`

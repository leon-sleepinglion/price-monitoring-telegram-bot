# Price Monitoring Telegram Bot

## Overview

This is a side project that I built to keep track of the price for several items that I am interested in buying. Combining simple web scraping technique with Telegram Bot API and AWS services, I can get the price update for those items everyday from a Telegram bot. The tutorial can be found [here](https://codeburst.io/price-tracking-with-telegram-bot-691d66ec7a37).

## Requirements

- Python 3
- Telegram Bot API token
- AWS CLI
- Serverless framework CLI

## Usage

Add your Telegram token and chat id  in `.env` file.

Install Python dependencies using `pipenv`:

    pipenv install

Install Serverless Python Requirements plugin:

    sls plugin install -n serverless-python-requirements

Deploy the lambda function using Serverless CLI:

    sls deploy -v

After deployment, the function will be triggered by CloudWatch Event everyday at 8am UTC. It can also be invoked manually using:

    sls invoke -f send_price
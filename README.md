# Naira Watch 🇳🇬

## About
Naira Watch is a data engineering project that explores exchange-rate data involving the Nigerian Naira (NGN). It will track USD to NGN: how many Naira one US dollar buys.

## Data Source
- API: Frankfurter API
- Website: https://frankfurter.dev
- Cost: Free
- API key: Not required
- Data format: JSON

## What It Returns
The API provides exchange-rate information, including the date, base currency, quote currency, and exchange rate.

## Sample Data
`sample.json` was copied by hand from the Frankfurter NGN page. Each record has `date`, `base`, `quote` and `rate`. The `rate` is the number I need.

## API Endpoint
`https://api.frankfurter.dev/v2/rates?base=NGN`

## Technologies
- Python
- JSON
- REST API

## Project Goal
The goal is to learn how to retrieve exchange-rate data, understand JSON responses, validate data, and eventually store the data in a database.

## Project Status
🚧 Day 1: chose the API and saved a sample file.
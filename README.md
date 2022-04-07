
# DSE Data Scraper

Dhaka Stock Exchange data scraper is a experimental Django & Python project which scrap data in realtime and serve through api.




## Built With
![Logo](https://www.probytes.net/wp-content/uploads/2019/07/django-logo-big.jpg)


## Installation

- Clone DSE_Scrapper
- Create and activate python virtual environment
- Install Dependencies, run:
```bash
  pip install -r requirements.txt
```
- Run the project:
```bash
  cd dse_scrapper
  python manage.py runserver
```

    
## API Reference

#### Get Latest Share Prices

```http
  GET /api/share_prices
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `filter` | `string` | *options* - value, volume, change  |

    Here by default it will pull all the recent 
    trading data.

#### Get Top Gainer Data

```http
  GET /api/top_gainer
```

#### Get Top Loser Data

```http
  GET /api/top_loser
```

#### Get Circuit Breaker Data

```http
  GET /api/circuit_breaker
```


## Authors

- [@hossainazad](https://github.com/h-azad/)



## Support

For support or query ping me on [Linkedin](https://www.linkedin.com/in/hossain-azad-50027980//).


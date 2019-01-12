# COUNTRY

- GET: `http://localhost:5000/api/countries`

# REGION


- GET: `http://localhost:5000/api/regions/<country_id>`
- GET: `http://localhost:5000/api/regions/<region_id>/region`
- POST: `http://localhost:5000/api/regions`

Body
```
{
	"name": "Fake 2",
	"code": "F2",
	"default_timezone": "America/Sao_Paulo",
	"country_id": 1
}

```

- PUT: `http://localhost:5000/api/regions/<region_id>/region`

Body:
```
{
	"name": "Fake 2",
	"code": "F2",
	"default_timezone": "America/Sao_Paulo",
	"country_id": 1
}

```

# LOCALITY

- GET: `http://localhost:5000/api/localities/<region_id>`
- GET: `http://localhost:5000/api/localities/<locality_id>/locality`
- POST: `http://localhost:5000/api/localities`

Body:
```
{
	"name": "Fakezao City",
	"region_id": 2
}
```
- PUT: `http://localhost:5000/api/localities/<locality_id>/locality`

Body:
```
{
	"name": "Fakezao City",
	"region_id": 2
}
```

# WEATHER FORECASTING HOUR

- GET:`http://localhost:5000/api/wfhours/<locality_id>`
- GET: `http://localhost:5000/api/wfhours/<wfhour_id>/wfhour`
- POST: `http://localhost:5000/api/wfhours`

Body: 
```
{
	"atmospheric_pressure": 1503,
	"wind": 54,
	"temp": 25,
	"relative_humidity": 12,
	"weather": "TESTANDO NODE 1",
	"locality_id": 24,
	"date_time": "2018-01-07 15:00:00"
}
```
- PUT: `http://localhost:5000/api/wfhours/<wfhour_id>/wfhour`

Body:
```
{
	"atmospheric_pressure": 1503,
	"wind": 54,
	"temp": 25,
	"relative_humidity": 12,
	"weather": "TESTANDO NODE UPDATE 2",
	"locality_id": 24,
	"date_time": "2018-01-07 18:00:00"
}
```
- DELETE: `http://localhost:5000/api/wfhours/<wfhour_id>/wfhour`

# WEATHER FORECASTING DAY

- GET: `http://localhost:5000/api/wfdays/<locality_id>`
- GET: `http://localhost:5000/api/wfdays/<wfday_id>/wfday`
- POST: `http://localhost:5000/api/wfdays`

Body:
```
{
	"weather": "FAKEZAOss",
	"precipitation": 4,
	"date": "2019-01-08",
	"max": 28,
	"min": 20,
	"locality_id": 24,
	"lag": 4
}
```
- PUT: `http://localhost:5000/api/wfdays/<wfday_id>/wfday`

Body: 
```
{
	"weather": "A MIAHUAHEUEH",
	"precipitation": 4,
	"date": "2019-01-08",
	"max": 28,
	"min": 20,
	"locality_id": 24
}
```

- DELETE: `http://localhost:5000/api/wfdays/<wfday_id>/wfday`
# gdelt-downloader
This docker image downloads the [GDELT](https://www.gdeltproject.org/) data. You can specify the number of jobs that run in parallel, and the start & end dates via environment variables.

## Usage
```sh
docker run -i -e njobs=N -e start_date=YYYYMMDD -e end_date=YYYYMMDD -v $(pwd)/data:/app/data yfiua/gdelt-downloader
```

* `-e njobs=N`: Specifies the number of parallel jobs to use. Default is 1.
* `-e start_date=YYYYMMDD`: Specifies the start date for the data download in YYYYMMDD format, optional.
* `-e end_date=YYYYMMDD`: Specifies the end date for the data download in YYYYMMDD format, optional.
* `-v $(pwd)/data:/app/data`: Binds the local `data` directory to the container's `/app/data` directory to store the downloaded files.

## Build yourself

```sh
docker build -t gdelt-downloader .
```

## Changelog

* 0.1.1
  * Less verbose output
  * Use Python 3.12
* 0.1.0
  * Initial release

## Author
[yfiua](https://github.com/yfiua)

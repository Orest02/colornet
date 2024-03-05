-   [Colornet](#colornet)
    -   [Tech stack](#tech-stack)
    -   [Set up](#set-up)
        -   [Model](#model)
        -   [Pipeline Config](#pipeline-config)
        -   [New Relic configuration](#new-relic-configuration)
    -   [Installation](#installation)
        -   [Docker Compose](#docker-compose)
        -   [Harder way: run from
            Terminal](#harder-way-run-from-terminal)

Colornet
========

[![Support
Ukraine](https://img.shields.io/badge/Support-Ukraine-FFD500?style=flat&labelColor=005BBB)](https://opensource.fb.com/support-ukraine)

The project is about deploying trained colorization GAN onto Raspberry
Pi! (Or actually whatever machine at this point)

GAN trained from this
[tutorial](https://github.com/moein-shariatnia/Deep-Learning/tree/main/Image%20Colorization%20Tutorial).


Tech stack
----------

  [PyTorch](https://pytorch.org/)
  
  [FastAPI](https://fastapi.tiangolo.com)
  
  [Streamlit](https://streamlit.io/)
  
  [Hydra](https://hydra.cc/)
  
  [New Relic](https://newrelic.com/)
  
  [Docker](https://www.docker.com/)

Set up
------

### Model

Get the trained model's weights and put them in the `artifacts` folder

### Pipeline Config

In the `configs` folder create a `config.yaml` file following the
example of the `example_config.yaml`

### New Relic configuration

In the `newrelic` directory add your licence key to two files:

``` {.bash}
echo "license_key: <YOUR_LICENCE_KEY>" > newrelic-infra.yml
newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini
```

Installation
------------

### Docker Compose

`docker compose up`

### Harder way: run from Terminal

Install Poetry, then run:

``` {.commandline}
poetry install
poe force-cuda11 # run this if you encounter quantization errors
```

Run:

``` {.commandline}
poetry run uvicorn --host 0.0.0.0 --port 5005 colornet.app.api:app
poetry run streamlit run colornet/frontend/app.py --server.port 80
```

Congratulations, you have an app running at `localhost:80`!

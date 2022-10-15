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

  [![PyTorch](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi0.wp.com%2Fwww.marktechpost.com%2Fwp-content%2Fuploads%2F2020%2F11%2Fpytorch-logo-dark.png%3Fresize%3D696%252C139%26ssl%3D1&f=1&nofb=1&ipt=afbe5f00f51c5b2efbf31696c3c34e9d5e7a8e3d431110d58cd0a650f8024dd1&ipo=images)](https://pytorch.org/)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com)
  [![Streamlit](https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e181828ba9f9e92b6ebc6e7_RGB_Logomark_Color_Light_Bg.png)](https://streamlit.io/)
  [![Hydra](https://raw.githubusercontent.com/facebookresearch/hydra/master/website/static/img/Hydra-Readme-logo2.svg)](https://hydra.cc/)
  [![New Relic](https://scontent.flcj1-1.fna.fbcdn.net/v/t39.30808-6/281769690_10160125860812495_4541212653657046312_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=xSmo5sYSG4gAX-aVGUE&_nc_ht=scontent.flcj1-1.fna&oh=00_AT8ymFe-E6Ow1xEFJJMCPj0AKXvVjuL5YGlHrLyrz3r_wA&oe=634D69AC)](https://newrelic.com/)
  [![Docker - Logos Download](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-download.com%2Fwp-content%2Fuploads%2F2016%2F09%2FDocker_logo_black.png&f=1&nofb=1&ipt=553a378a8e641b2d75576f07260b0d4478630f00a1cc41ede6e0883d5704a147&ipo=images)](https://www.docker.com/)

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

`docker-compose up`

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

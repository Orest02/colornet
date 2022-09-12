# Colornet

The project is about training and deploying colorization GAN onto Raspberry Pi!

## Instalation
Install Poetry, then run:
```commandline
poetry init
poetry install
poe force-cuda11 # run this if you encounter quantization errors
```

Or just install from wheel/tar gz in the build dir

## Run
Run:
```commandline
poetry run colornet/infer.py
```
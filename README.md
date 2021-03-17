# My Teleprompter

A simple Flask app for local teleprompting adapted from https://github.com/BroadcastVision/Open-Teleprompter.


## Requirements

The text to prompt is rendered in Markdown using [flask-misaka](https://flask-misaka.readthedocs.io) package which is a python binding
to the Markdown parser [Hoedown](https://github.com/hoedown/hoedown) written in C.

To install *flask-misaka*, you need to have the python3 development package installed first.

On Ubuntu/Debian:
```
$ sudo apt install python3-dev
```

## Quick start

To setup your repository and launch the app locally, just run the following:
```
$ git clone https://gitlab.com/JCapul/my-teleprompter
$ cd my-teleprompter
$ make venv
$ make run
```
The appliaction is accessible at http://127.0.0.1:5000

## Control Keys
* Increase font size [+]
* Decrease font size [-]
* Text Scroll [UP or DOWN Works only when the prompter in on Stop mode]
* Decrease Scroll Speed [LEFT]
* Increase Scroll Speed [RIGHT]
* Play/Pause [Spacebar]
* Full Screen [F11]
* Reset [CTRL]

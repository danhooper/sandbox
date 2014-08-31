# sandbox

Playing around with the mock
[P-ROC](http://www.pinballcontrollers.com/index.php/products/p-roc)
provided by
[pyprocgame](https://github.com/preble/pyprocgame)
and friends.

## Requirements

* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
* X11, [Mac OS X](http://xquartz.macosforge.org/trac/wiki)

## Installation

Clone this repository, change to the `sandbox` directory and run:

```
vagrant up
```

## Running

Wait for Vagrant to finish building the virtual machine and return you to a
prompt. Run:

```
vagrant ssh
sandbox
```

Previous scores are displayed for the first 10 seconds. Attract mode
starts after that.

## Controls

* `s`: Start Button
* `g`: Slingshot (10 points)
* `b`: Bumper (100 points, 1000 if super jets are active)
* `j`: Super Jets (resets on drain)
* `/`: Drain

## Operator Service

Not exciting without hardware.

* `7`: Enter
* `8`: Up
* `9`: Down
* `0`: Exit

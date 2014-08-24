# pinball

I'm playing around with the mock
[P-ROC](http://www.pinballcontrollers.com/index.php/products/p-roc)
provided by
[pyprocgame](https://github.com/preble/pyprocgame)
and friends.

## Requirements

* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)

## Installation

Clone this repository, change to the `pinball` directory and run:

```
vagrant up
```

## Running

After Vagrant has finished building the virtual machine, a login box
should be displayed on console. Login as user "vagrant", password "vagrant" and
the demonstration should start.

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

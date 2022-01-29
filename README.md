# Simple-Toggle-Autoclicker :beginner:

## A simplistic toggle clicker
Realized a long time ago in order to detect the difference between real and fake clicks.

Don't use it to cheat.

## Choice of button 
``` if pressed and button==Button.middle ```

Here, it is the middle click that is used.

## Randomness of clicks

```sleep(abs((np.random.normal(48, 35, 1) * 0.001)[0]))```

We use a Gaussian distribution.

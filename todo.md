# notes
MSS: loop takes 0.127 - 0.137 seconds
pyautogui: loop takes [about 0.1] seconds (actually changes a lot whenever the code changes)

i think the inconsistency comes from being unable to know if the dot is detected 0.01s or 0.08s after it appeared. almost 3 frames of uncertainty
ALSO its random when in that 0.1 seconds the it will realise the timer has passed and should click. so thats up to 0.2 seconds of variance.

# todo

I think the plan is to read the previous loop duration and assume the dot delay is half of that.


do health bar detection to switch to/from triple dodge
get the timings to work
change delay based on enemy position
do menuing
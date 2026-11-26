"""One-line roast of my fridge, for make.fun.

The brief: one line, at most 200 characters, roasting a fridge or a phone.
It has to be really about the appliance, find a specific detail worth
mocking, turn on a twist, and read well out loud. The fridge's light was
picked: it is the one detail everyone knows, and the twist is that the light
is not there to help you see, it is there to judge you for opening the door
again when there is nothing inside.
"""

LINE = "My fridge is the only appliance that judges me: it lights up every time I open it, just to confirm there is still nothing I want in there."

# The entry must be exactly one line of 1-200 characters, and the sealed
# scorer rejects whitespace-only text, so fail loudly instead of writing it.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, limit is 200"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

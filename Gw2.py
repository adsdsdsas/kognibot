BUILDS = {
    'elementalist': 'https://snowcrows.com/builds?profession=Elementalist',
    'mesmer': 'https://snowcrows.com/builds?profession=Mesmer',
    'ranger': 'https://snowcrows.com/builds?profession=Ranger',
    'engineer': 'https://snowcrows.com/builds?profession=Engineer',
    'thief': 'https://snowcrows.com/builds?profession=Thief',
    'warrior': 'https://snowcrows.com/builds?profession=Warrior',
    'guardian': 'https://snowcrows.com/builds?profession=Guardian',
    'revenant': 'https://snowcrows.com/builds?profession=Revenant',

}


def get_build(spec):
    downcased_spec = spec.lower()
    if downcased_spec in BUILDS.keys():
        return BUILDS[downcased_spec]
    else:
        return "Please enter proper specialization name!"


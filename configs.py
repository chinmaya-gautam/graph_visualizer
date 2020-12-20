from collections import namedtuple
defaults = {
    'win_height': 600,
    'win_width': 600,
    'x_padding': 20,
    'y_padding': 20
}

def _final_configs():
    return defaults

def get_configs():

    configs = _final_configs()
    named_configs = namedtuple('configs', configs)
    return named_configs(**configs)


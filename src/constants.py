from types import SimpleNamespace
from src.utils.keyboard import create_keyboards

keys = SimpleNamespace(
    random_connect = 'Random_connect',
    settings = 'Settings :woman_facepalming_light_skin_tone:',
)

keyboards = SimpleNamespace(
    main=create_keyboards(keys.random_connect, keys.settings),
)
    

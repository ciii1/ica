__synonyms = {	
    'hi': ['hello', 'hey'],
    'hey': ['hello', 'hi'],
	'hello': ['greeting', 'hi', 'hey'],
}

def get(key):
    global __synonyms
    try:
        ret = __synonyms[key]
    except KeyError:
        ret = []
    return ret

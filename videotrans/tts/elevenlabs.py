import json
import os
from elevenlabs import generate, Voice,set_api_key
from videotrans.configure import config
from videotrans.util import tools


def get_voice(*,text=None, role=None, rate=None,language=None, filename=None,set_p=True):
    try:
        with open(os.path.join(config.rootdir,'elevenlabs.json'),'r',encoding="utf-8") as f:
            jsondata=json.loads(f.read())
        if config.params['elevenlabstts_key']:
            set_api_key(config.params['elevenlabstts_key'])
        audio = generate(
            text=text,
            voice=Voice(voice_id=jsondata[role]['voice_id']),
            model="eleven_multilingual_v2"
        )
        with open(filename,'wb') as f:
            f.write(audio)
        return True
    except Exception as e:
        error=str(e)
        if set_p:
            tools.set_process(f'elevenlabs:{error}')
        config.logger.error(f"elevenlabsTTS：request error:{error}")
        raise Exception(f"elevenlabsTTS:{error}")

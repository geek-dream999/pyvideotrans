"""
命令行使用方式
python cli.py  [-c 可选传参一个配置文件的绝对路径，如果不传参，则使用项目根目录下的 cli.ini ] [-m mp4视频的绝对地址或填写到cli.ini文件中] [-cuda 加上即启用cuda加速，如果可用]

python cli.py -m c:/Users/c1/Videos/1.mp4 使用 默认当前目录下的 cli.ini
python cli.py -cuda -m c:/Users/c1/Videos/1.mp4 使用 默认当前目录下的 cli.ini，启用CUDA加速
python cli.py -c D:/cli.ini  -m c:/Users/c1/Videos/1.mp4 使用 D:/cli.ini, 忽略当前目录下的


"""
import os
import re
import sys
from videotrans.configure import config
import argparse
from videotrans.task.trans_create import TransCreate
from videotrans.translator import LANG_CODE, is_allow_translate, BAIDU_NAME, TENCENT_NAME, CHATGPT_NAME, AZUREGPT_NAME, \
    GEMINI_NAME, DEEPLX_NAME, DEEPL_NAME
from videotrans.util.tools import set_proxy, get_edge_rolelist, get_elevenlabs_role

parser = argparse.ArgumentParser(description='cli.ini and source mp4')
parser.add_argument('-c', type=str, help='cli.ini file absolute filepath', default=os.path.join(os.getcwd(), 'cli.ini'))
parser.add_argument('-m', type=str, help='mp4 absolute filepath', default="")
parser.add_argument('-cuda', action='store_true', help='Activates the cuda option')


def set_process(text, type="logs"):
    print(f'[{type}] {text}\n')


if not os.path.exists(os.path.join(config.rootdir, 'voice_list.json')) or os.path.getsize(
        os.path.join(config.rootdir, 'voice_list.json')) == 0:
    print("正在获取 edge TTS 角色...")
    get_edge_rolelist()
if not os.path.exists(os.path.join(config.rootdir, 'elevenlabs.json')) or os.path.getsize(
        os.path.join(config.rootdir, 'elevenlabs.json')) == 0:
    print("正在获取 elevenlabs TTS 角色...")
    get_elevenlabs_role()

if __name__ == '__main__':
    config.exec_mode = 'cli'
    config.settings['countdown_sec'] = 0

    args = vars(parser.parse_args())

    cfg_file = args['c']
    if not os.path.exists(cfg_file):
        print('不存在配置文件 cli.ini' if config.defaulelang == 'zh' else "cli.ini file not exists")
        sys.exit()

    with open(cfg_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith(";"):
                continue

            line = [x.strip() for x in line.split("=", maxsplit=1)]
            if len(line) != 2:
                continue
            if line[1] == 'false':
                config.params[line[0]] = False
            elif line[1] == 'true':
                config.params[line[0]] = True
            else:
                config.params[line[0]] = int(line[1]) if re.match(r'^\d+$', line[1]) else line[1]
    if not config.params['source_language']:
        config.params['source_language']='-'
    if not config.params['target_language']:
        config.params['target_language']='-'
    if args['cuda']:
        config.params['cuda'] = True
    if args['m'] and os.path.exists(args['m']):
        config.params['source_mp4'] = args['m']
    if not config.params['source_mp4'] or not os.path.exists(config.params['source_mp4']):
        print(
            "必须在命令行或cli.ini文件设置 source_mp4(视频文件)的绝对路径" if config.defaulelang == 'zh' else "The absolute path of source_mp4 (video file) must be set on the command line or in the cli.ini file.")
        sys.exit()
    # 字幕嵌入时标记的语言，目标语言
    if config.params['target_language']!='-':
        config.params['subtitle_language'] = LANG_CODE[config.params['target_language']][1]
    # 语音识别语言
    if config.params['source_language']!='-':
        config.params['detect_language'] = LANG_CODE[config.params['source_language']][0]

    if config.params['translate_type'] == BAIDU_NAME:
        # baidu language code
        if not config.params["baidu_appid"] or not config.params["baidu_miyue"]:
            print(config.transobj['anerror'], config.transobj['baikeymust'])
            sys.exit()
    elif config.params['translate_type'] == TENCENT_NAME:
        #     腾讯翻译
        if not config.params["tencent_SecretId"] or not config.params["tencent_SecretKey"]:
            print(config.transobj['tencent_key'])
            sys.exit()
    elif config.params['translate_type'] == CHATGPT_NAME:
        # chatGPT 翻译 5 是中文语言名称，6是英文名称
        if not config.params["chatgpt_key"]:
            print(config.transobj['chatgptkeymust'])
            sys.exit()
    elif config.params['translate_type'] == AZUREGPT_NAME:
        # chatGPT 翻译
        if not config.params["azure_key"]:
            print('必须填写Azure key')
            sys.exit()
    elif config.params['translate_type'] == GEMINI_NAME:
        # chatGPT 翻译
        if not config.params["gemini_key"]:
            print(config.transobj['bixutianxie'] + ' Gemini key')
            sys.exit()
    elif config.params['translate_type'] == DEEPL_NAME or config.params['translate_type'] == DEEPLX_NAME:
        # DeepL翻译
        if config.params['translate_type'] == DEEPL_NAME and not config.params["deepl_authkey"]:
            print(config.transobj['deepl_authkey'])
            sys.exit()
        if config.params['translate_type'] == DEEPLX_NAME and not config.params["deeplx_address"]:
            print(config.transobj['setdeeplx_address'])
            sys.exit()

        if LANG_CODE[config.params['target_language']] == 'No':
            print(config.transobj['deepl_nosupport'])
            sys.exit()
    try:
        voice_rate = int(config.params['voice_rate'].strip().replace('+', '').replace('%', ''))
        config.params['voice_rate'] = f"+{voice_rate}%" if voice_rate >= 0 else f"-{voice_rate}%"
    except:
        config.params['voice_rate'] = '+0%'
    try:
        voice_silence = int(config.params['voice_silence'].strip())
        config.params['voice_silence'] = voice_silence
    except:
        config.params['voice_silence'] = '500'
    os.makedirs(os.path.join(os.getcwd(), 'tmp'), exist_ok=True)

    if config.params['proxy'].strip():
        config.proxy = config.params['proxy'].strip()
        set_proxy(config.proxy)
    config.current_status = 'ing'

    try:
        task = TransCreate({"source_mp4": config.params['source_mp4'], 'app_mode': "biaozhun","mode":"cli"})
        set_process(config.transobj['kaishichuli'])
        res = task.run()
        print(f'{"执行完成" if config.defaulelang == "zh" else "Succeed"} {task.targetdir_mp4}')
    except Exception as e:
        print(f'\nException:{str(e)}\n')

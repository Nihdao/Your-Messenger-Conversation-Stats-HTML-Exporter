
import glob, json
from typing import *

class GenerateThread:
    def generate(self, global_path: str) -> Dict[str, List[Dict[str, Union[str, int]]]]:
        thread = {}
        for json_file in sorted(glob.glob(global_path)):
            with open(json_file) as f:
                data = json.load(f)
            
                if 'messages' in thread:
                    thread['messages'].extend(data.get('messages', []))
                else:
                    thread['messages'] = data.get('messages', [])

                for key, value in data.items():
                    if key != 'messages':
                        if key == 'participants':
                            for p in value:
                                if p['name'] == "":
                                    p['name'] = "unknown"
                        elif key == 'messages':
                            for m in value:
                                if m['sender_name'] == "":
                                    m['sender_name'] = "unknown"
                        thread[key] = value
            print("File %s done +%s messages (total : %s)" % (json_file, len(data['messages']),  len(thread['messages'])))
            thread['messages'] = sorted(thread['messages'], key=lambda x: x['timestamp_ms'])
            f.close()
        return thread

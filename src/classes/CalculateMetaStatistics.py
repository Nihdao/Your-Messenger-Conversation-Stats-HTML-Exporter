
from collections import defaultdict
import datetime
import json, os
from typing import List, Dict, Union
from urllib.parse import urlsplit
from ..utils.timer_decorator import timer_decorator
from .SuperFormatter import SuperFormatter
from ..lists.badwords_french import badwords_french
from ..lists.badwords_english import badwords_english
from src.classes.GenerateThread import GenerateThread

def generate_statistics_html(config: Dict[str, str]) -> None:
    insGenerateThread = GenerateThread()
    insCalculateMetaStatistics = CalculateMetaStatistics(insGenerateThread.generate(config["path"]), config.get("language", 'en'))
    insCalculateMetaStatistics.calculate_and_exportHTML()


class CalculateMetaStatistics:

    def __init__(self, thread: Dict[str, List[Dict[str, Union[str, int]]]], language = 'en') -> None:
        """
        Initializes the GenerateMetaStatistics class with a thread dictionary.

        Parameters:
        thread (Dict[str, List[Dict[str, Union[str, int]]]]): A dictionary containing thread information.
        """
        self.thread = thread
        if language == 'en':
            self.badwords = badwords_english
        elif language == 'fr':
            self.badwords = badwords_french

    # UTILITAIRES 
    def average(self, lst: List[int]) -> float:
        return sum(lst) / len(lst) if lst else 0

    def timestampToDate(self, timestamp: int, dateformat: str) -> str:
        return datetime.datetime.fromtimestamp(timestamp//1000).strftime(dateformat)

    def latinToUtf8(self, str: str) -> str:
        return str.encode('latin-1').decode('utf-8')



    
    def msg_number_participants(self) -> str:
        occurence_Message = {self.latinToUtf8(p['name']): sum(1 for q in self.thread['messages'] if q['sender_name'] == p['name']) for p in self.thread['participants']}
        return json.dumps(occurence_Message, indent=4, sort_keys=True)
    
    def max_content(self) -> str:
        user_pave = {}
        maximum = 0
        for q in self.thread['messages']:
            if "content" in q:
                if (len(q["content"]) > maximum):
                    maximum = len(q["content"])
                    user_pave = {"Author": self.latinToUtf8(q["sender_name"]), "Length": str(maximum), "Message": self.latinToUtf8(q["content"])}
        return json.dumps(user_pave, indent=4, sort_keys=True)
    
    def frequency_msg_per_user_per_year(self) -> str:
        freq_msg = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            for p in self.thread['participants']:
                if msg['sender_name'] == p['name']:
                    date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m-%d")
                    year, _, _ = date.split('-')
                    freq_msg[year][self.latinToUtf8(p['name'])] += 1

        return json.dumps(
            {year: {user: count for user, count in users.items()} for year, users in freq_msg.items()},
            indent=4,
            sort_keys=True
        )

    def count_unsent_msg_per_user_per_month(self) -> str:
        freq_unset = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "is_unsent" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m-%d")
                        year, _, _ = date.split('-')
                        freq_unset[year][self.latinToUtf8(p['name'])] += 1

        return json.dumps(
            {year: {user: count for user, count in users.items()} for year, users in freq_unset.items()},
            indent=4,
            sort_keys=True
        ) 

    def count_msg_per_hour_of_day(self) -> str:
        freq_msg = defaultdict(int)
        for msg in self.thread['messages']:
            hour = self.timestampToDate(msg['timestamp_ms'], "%H")
            freq_msg[hour] += 1

        return json.dumps({hour: count for hour, count in freq_msg.items()}, indent=4, sort_keys=True)
    
    def count_msg_per_day_of_week(self) -> str:
        freq_msg = defaultdict(int)
        for msg in self.thread['messages']:
            day = self.timestampToDate(msg['timestamp_ms'], "%A")
            freq_msg[day] += 1

        return json.dumps({day: count for day, count in freq_msg.items()}, indent=4, sort_keys=True)

    def count_reactions(self) -> str:
        occurence_Reactions = defaultdict(int)
        for q in self.thread['messages']:
            if "reactions" in q:
                for reaction in q["reactions"]:
                    reactionDecode = reaction.get('reaction', '')
                    occurence_Reactions[reactionDecode] += 1

        return json.dumps({reaction: count for reaction, count in occurence_Reactions.items()}, indent=4, sort_keys=True) 
    
    def count_msg_per_day(self) -> str:
        freq_msg = defaultdict(int)
        for msg in self.thread['messages']:
            date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m-%d")
            freq_msg[date] += 1

        return json.dumps({date: count for date, count in freq_msg.items()}, indent=4, sort_keys=True)

    def count_photos_per_user_per_month(self) -> str:
        freq_photo = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "photos" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        for photo in msg['photos']:
                            date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m")
                            freq_photo[self.latinToUtf8(p['name'])][date] += 1

        return json.dumps(
            {user: {date: count for date, count in user_items.items()} for user, user_items in freq_photo.items()},
            indent=4,
            sort_keys=True
        )

    def count_videos_per_user_per_month(self) -> str:
        freq_video = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "videos" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        for video in msg['videos']:
                            date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m")
                            freq_video[self.latinToUtf8(p['name'])][date] += 1

        return json.dumps( {user: {date: count for date, count in user_items.items()} for user, user_items in freq_video.items()}, indent=4, sort_keys=True)

    def count_gifs_per_user_per_month(self) -> str:
        freq_gifs = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "gifs" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        for gif in msg['gifs']:
                            date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m")
                            freq_gifs[self.latinToUtf8(p['name'])][date] += 1

        return json.dumps({user: {date: count for date, count in user_items.items()} for user, user_items in  freq_gifs.items()}, indent=4, sort_keys=True)

    def count_files_per_user_per_month(self) -> str:
        freq_files = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "files" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        for file in msg['files']:
                            date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m")
                            freq_files[self.latinToUtf8(p['name'])][date] += 1
        return json.dumps({user: {date: count for date, count in user_items.items()} for user, user_items in  freq_files.items()}, indent=4, sort_keys=True)

    def count_share_per_user_per_month(self) -> str:
        freq_share = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "share" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        for sh in msg['share']:
                            date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m")
                            freq_share[self.latinToUtf8(p['name'])][date] += 1
        return json.dumps({user: {date: count for date, count in user_items.items()} for user, user_items in  freq_share.items()}, indent=4, sort_keys=True)

    def count_audiofiles_per_user_per_month(self) -> str:
        freq_audiofiles = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "audio_files" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        for af in msg['audio_files']:
                            date = self.timestampToDate(msg['timestamp_ms'], "%Y-%m")
                            freq_audiofiles[self.latinToUtf8(p['name'])][date] += 1
        return json.dumps({user: {date: count for date, count in user_items.items()} for user, user_items in  freq_audiofiles.items()}, indent=4, sort_keys=True)

    def count_link_shared_per_user(self) -> str:
        freq_share = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "share" in msg:
                for p in self.thread['participants']:
                    if msg['sender_name'] == p['name']:
                        for sh in msg['share']:
                            if 'link' in msg['share']:
                                url = urlsplit(msg['share']['link'])
                                link = f"{url.netloc}"
                                freq_share[self.latinToUtf8(p['name'])][link] +=1
        return json.dumps({user: {link: count for link, count in user_items.items()} for user, user_items in  freq_share.items()}, indent=4, sort_keys=True)

    def count_react_per_user(self) -> str:
        count_react = defaultdict(int)
        for msg in self.thread['messages']:
            if "reactions" in msg:
                for reaction in msg['reactions']: 
                    for p in self.thread['participants']:
                        if reaction['actor'] == p['name']:
                            count_react[self.latinToUtf8(p['name'])] += 1

        return json.dumps({user: count for user, count in count_react.items()}, indent=4, sort_keys=True)
    
    def count_react_per_user_per_reaction(self) -> str:
        count_react = defaultdict(lambda: defaultdict(int))
        for msg in self.thread['messages']:
            if "reactions" in msg:
                for reaction in msg['reactions']: 
                    for p in self.thread['participants']:
                        if reaction['actor'] == p['name']:
                            count_react[self.latinToUtf8(p['name'])][reaction['reaction']] += 1

        return json.dumps({user: {reaction: count for reaction, count in reaction_count.items()} for user, reaction_count in count_react.items()}, indent=4, sort_keys=True)
    
    def word_occurence_per_user(self, tab: List[str]) -> str:
        occurence_Message = defaultdict(dict)
        for q in self.thread['messages']:
            if 'content' in q:
                for p in self.thread['participants']:
                    if q['sender_name'] == p['name']:
                        for occ in tab:
                            if occ in q['content'].lower().split():
                                if occ in occurence_Message[self.latinToUtf8(p['name'])]:
                                    occurence_Message[self.latinToUtf8(p['name'])][occ] += 1
                                else:
                                    occurence_Message[self.latinToUtf8(p['name'])][occ] = 1
        return json.dumps(
            {user: {word: count for word, count in words.items() if count > 0} for user, words in occurence_Message.items()},
            indent=4,
            sort_keys=True
        )
    
    def sum_word_occurence_per_user(self, occurence: Dict[str, Dict[str, int]]) -> str:
        return json.dumps({user: sum(count for count in words.values() if count > 0) for user, words in occurence.items()}, indent=4, sort_keys=True)

    
    def most_reacted_msg(self) -> str:
        msg_pop = max(
            (q for q in self.thread['messages'] if "reactions" in q and "content" in q),
            key=lambda q: len(q["reactions"]),
            default=None
        )
        return json.dumps({
            "Author": self.latinToUtf8(msg_pop["sender_name"]),
            "Reactions": len(msg_pop["reactions"]),
            "Message": self.latinToUtf8(msg_pop["content"]),
        }, indent=4, sort_keys=True) if msg_pop else '{}'

    
    @timer_decorator
    def calculate_and_exportHTML(self) -> None:
        print("Exporting HTML...")

        data = {}

        data['title'] = self.latinToUtf8(self.thread['title'])
        data['interval_dates'] = [self.timestampToDate(self.thread['messages'][0]["timestamp_ms"], "%d-%m-%Y"), self.timestampToDate(self.thread['messages'][-1]["timestamp_ms"], "%d-%m-%Y")]
        data['participants'] = [self.latinToUtf8(p['name']) for p in self.thread['participants']]
        data['totalparticipants'] = [len(self.thread['participants'])]
        data['totalmsg'] = [len(self.thread['messages'])]

        data['count_msg_per_day'] = [self.count_msg_per_day()]
        data['msg_number_participants']=[self.msg_number_participants()]
        data['frequency_msg_per_user_per_year']=[self.frequency_msg_per_user_per_year()]
        data['count_unsent_msg_per_user_per_month']=[self.count_unsent_msg_per_user_per_month()]
        data['count_msg_per_day_of_week']=[self.count_msg_per_day_of_week()]
        data['count_msg_per_hour_of_day']=[self.count_msg_per_hour_of_day()]

        data['count_photos_per_user_per_month'] = [self.count_photos_per_user_per_month()]
        data['count_videos_per_user_per_month'] = [self.count_videos_per_user_per_month()]
        data['count_gifs_per_user_per_month'] = [self.count_gifs_per_user_per_month()]
        data['count_audiofiles_per_user_per_month'] = [self.count_audiofiles_per_user_per_month()]
        data['count_files_per_user_per_month'] = [self.count_files_per_user_per_month()]
        data['count_share_per_user_per_month'] = [self.count_share_per_user_per_month()]
        data['count_link_shared_per_user'] = [self.count_link_shared_per_user()]

        data['count_reactions']=[self.count_reactions()] 
        data['count_react_per_user_per_reaction']=[self.count_react_per_user_per_reaction()]
        data['count_react_per_user']=[self.count_react_per_user()]

        data['max_content']=[self.max_content()]
        data['most_reacted_msg']=[self.most_reacted_msg()]
        data['badwords_list']=self.word_occurence_per_user(self.badwords)


        f = open('static/template.html')
        html = f.read()
        f.close()

        if not os.path.exists('../dist'):
            os.makedirs('../dist')
        try:
            f = open('../dist/output.html', 'w')
            sf=SuperFormatter()
            f.write(sf.format(html, data=data))
            f.close()
            print("Exported to ../dist/output.html")
        except:
            print("Exportation failed")



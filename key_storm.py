import sys
import time
import random
import platform
import os
import textwrap
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from collections import namedtuple
from typing import List, Dict

class TypingTest:
    def __init__(self):
        self.console = Console()
        self.Settings = namedtuple("Settings", ["duration", "use_numbers", "use_specials"])
        self.word_bank: Dict[str, List[str]] = {
            "common": ["the", "of", "to", "and", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "I",
                      "his", "they", "be", "at", "one", "have", "this", "from", "or", "had", "by", "not", "word", "but", "what", "some",
                      "we", "can", "out", "other", "were", "all", "there", "when", "up", "use", "your", "how", "said", "an", "each", "she",
                      "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", "them", "write", "would", "like", "so",
                      "these", "her", "long", "make", "thing", "see", "him", "two", "has", "look", "more", "day", "could", "go", "come",
                      "did", "number", "sound", "no", "most", "people", "my", "over", "know", "water", "than", "call", "first", "who",
                      "may", "down", "side", "been", "now", "find", "any", "new", "work", "part", "take", "get", "place", "made", "live",
                      "where", "after", "back", "little", "only", "round", "man", "year", "came", "show", "every", "good", "me", "give",
                      "our", "under", "name", "very", "through", "just", "form", "sentence", "great", "think", "say", "help", "low", "line",
                      "differ", "turn", "cause", "much", "mean", "before", "move", "right", "boy", "old", "too", "same", "tell", "does",
                      "set", "three", "want", "air", "well", "also", "play", "small", "end", "put", "home", "read", "hand", "port", "large",
                      "spell", "add", "even", "land", "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men", "change",
                      "went", "light", "kind", "off", "need", "house", "picture", "try", "us", "again", "animal", "point", "mother", "world",
                      "near", "build", "self", "earth", "father", "head", "stand", "own", "page", "should", "country", "found", "answer",
                      "school", "grow", "study", "still", "learn", "plant", "cover", "food", "sun", "four", "between", "state", "keep",
                      "eye", "never", "last", "let", "thought", "city", "tree", "cross", "farm", "hard", "start", "might", "story", "saw",
                      "far", "sea", "draw", "left", "late", "run", "don't", "while", "press", "close", "night", "real", "life", "few",
                      "north", "open", "seem", "together", "next", "white", "children", "begin", "got", "walk", "example", "ease", "paper",
                      "group", "always", "music", "those", "both", "mark", "often", "letter", "until", "mile", "river", "car", "feet",
                      "care", "second", "book", "carry", "took", "science", "eat", "room", "friend", "began", "idea", "fish", "mountain",
                      "stop", "once", "base", "hear", "horse", "cut", "sure", "watch", "color", "face", "wood", "main", "enough", "plain",
                      "girl", "usual", "young", "ready", "above", "ever", "red", "list", "though", "feel", "talk", "bird", "soon", "body",
                      "dog", "family", "direct", "pose", "leave", "song", "measure", "door", "product", "black", "short", "numeral", "class",
                      "wind", "question", "happen", "complete", "ship", "area", "half", "rock", "order", "fire", "south", "problem", "piece",
                      "told", "knew", "pass", "since", "top", "whole", "king", "space", "heard", "best", "hour", "better", "true", "during",
                      "hundred", "five", "remember", "step", "early", "hold", "west", "ground", "interest", "reach", "fast", "verb", "sing",
                      "listen", "six", "table", "travel", "less", "morning", "ten", "simple", "several", "vowel", "toward", "war", "lay",
                      "against", "pattern", "slow", "center", "love", "person", "money", "serve", "appear", "road", "map", "rain", "rule",
                      "govern", "pull", "cold", "notice", "voice", "unit", "power", "town", "fine", "certain", "fly", "fall", "lead", "cry",
                      "dark", "machine", "note", "wait", "plan", "figure", "star", "box", "noun", "field", "rest", "correct", "able", "pound",
                      "done", "beauty", "drive", "stood", "contain", "front", "teach", "week", "final", "gave", "green", "oh", "quick",
                      "develop", "ocean", "warm", "free", "minute", "strong", "special", "mind", "behind", "clear", "tail", "produce",
                      "fact", "street", "inch", "multiply", "nothing", "course", "stay", "wheel", "full", "force", "blue", "object", "decide",
                      "surface", "deep", "moon", "island", "foot", "system", "busy", "test", "record", "boat", "common", "gold", "possible",
                      "plane", "stead", "dry", "wonder", "laugh", "thousand", "ago", "ran", "check", "game", "shape", "equate", "hot",
                      "miss", "brought", "heat", "snow", "tire", "bring", "yes", "distant", "fill", "east", "paint", "language", "among",
                      "grand", "ball", "yet", "wave", "drop", "heart", "am", "present", "heavy", "dance", "engine", "position", "arm", "wide",
                      "sail", "material", "size", "vary", "settle", "speak", "weight", "general", "ice", "matter", "circle", "pair",
                      "include", "divide", "syllable", "felt", "perhaps", "pick", "sudden", "count", "square", "reason", "length",
                      "represent", "art", "subject", "region", "energy", "hunt", "probable", "bed", "brother", "egg", "ride", "cell",
                      "believe", "fraction", "forest", "sit", "race", "window", "store", "summer", "train", "sleep", "prove", "lone", "leg",
                      "exercise", "wall", "catch", "mount", "wish", "sky", "board", "joy", "winter", "sat", "written", "wild", "instrument",
                      "kept", "glass", "grass", "cow", "job", "edge", "sign", "visit", "past", "soft", "fun", "bright", "gas", "weather",
                      "month", "million", "bear", "finish", "happy", "hope", "flower", "clothe", "strange", "gone", "jump", "baby", "eight",
                      "village", "meet", "root", "buy", "raise", "solve", "metal", "whether", "push", "seven", "paragraph", "third", "shall",
                      "held", "hair", "describe", "cook", "floor", "either", "result", "burn", "hill", "safe", "cat", "century", "consider",
                      "type", "law", "bit", "coast", "copy", "phrase", "silent", "tall", "sand", "soil", "roll", "temperature", "finger",
                      "industry", "value", "fight", "lie", "beat", "excite", "natural", "view", "sense", "ear", "else", "quite", "broke",
                      "case", "middle", "kill", "son", "lake", "moment", "scale", "loud", "spring", "observe", "child", "straight", "consonant",
                      "nation", "dictionary", "milk", "speed", "method", "organ", "pay", "age", "section", "dress", "cloud", "surprise",
                      "quiet", "stone", "tiny", "climb", "cool", "design", "poor", "lot", "experiment", "bottom", "key", "iron", "single",
                      "stick", "flat", "twenty", "skin", "smile", "crease", "hole", "trade", "melody", "trip", "office", "receive", "row",
                      "mouth", "exact", "symbol", "die", "least", "trouble", "shout", "except", "wrote", "seed", "tone", "join", "suggest",
                      "clean", "break", "lady", "yard", "rise", "bad", "blow", "oil", "blood", "touch", "grew", "cent", "mix", "team", "wire",
                      "cost", "lost", "brown", "wear", "garden", "equal", "sent", "choose", "fell", "fit", "flow", "fair", "bank", "collect",
                      "save", "control", "decimal", "gentle", "woman", "captain", "practice", "separate", "difficult", "doctor", "please",
                      "protect", "noon", "whose", "locate", "ring", "character", "insect", "caught", "period", "indicate", "radio", "spoke",
                      "atom", "human", "history", "effect", "electric", "expect", "crop", "modern", "element", "hit", "student", "corner",
                      "party", "supply", "bone", "rail", "imagine", "provide", "agree", "thus", "capital", "won't", "chair", "danger",
                      "fruit", "rich", "thick", "soldier", "process", "operate", "guess", "necessary", "sharp", "wing", "create", "neighbor",
                      "wash", "bat", "rather", "crowd", "corn", "compare", "poem", "string", "bell", "depend", "meat", "rub", "tube", "famous",
                      "dollar", "stream", "fear", "sight", "thin", "triangle", "planet", "hurry", "chief", "colony", "clock", "mine", "tie",
                      "enter", "major", "fresh", "search", "send", "yellow", "gun", "allow", "print", "dead", "spot", "desert", "suit",
                      "current", "lift", "rose", "continue", "block", "chart", "hat", "sell", "success", "company", "subtract", "event",
                      "particular", "deal", "swim", "term", "opposite", "wife", "shoe", "shoulder", "spread", "arrange", "camp", "invent",
                      "cotton", "born", "determine", "quart", "nine", "truck", "noise", "level", "chance", "gather", "shop", "stretch",
                      "throw", "shine", "property", "column", "molecule", "select", "wrong", "gray", "repeat", "require", "broad", "prepare",
                      "salt", "nose", "plural", "anger", "claim", "continent", "oxygen", "sugar", "death", "pretty", "skill", "women",
                      "season", "solution", "magnet", "silver", "thank", "branch", "match", "suffix", "especially", "fig", "afraid", "huge",
                      "sister", "steel", "discuss", "forward", "similar", "guide", "experience", "score", "apple", "bought", "led", "pitch",
                      "coat", "mass", "card", "band", "rope", "slip", "win", "dream", "evening", "condition", "feed", "tool", "total", "basic",
                      "smell", "valley", "nor", "double", "seat", "arrive", "master", "track", "parent", "shore", "division", "sheet",
                      "substance", "favor", "connect", "post", "spend", "chord", "fat", "glad", "original", "share", "station", "dad",
                      "bread", "charge", "proper", "bar", "offer", "segment", "slave", "duck", "instant", "market", "degree", "populate",
                      "chick", "dear", "enemy", "reply", "drink", "occur", "support", "speech", "nature", "range", "steam", "motion", "path",
                      "liquid", "log", "meant", "quotient", "teeth", "shell", "neck"],
            'numbers': ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            'specials': ["@", "#", "$", "%", "&", "*", "(", ")", "-", "+"]
        }
        self.display = {"timer": Text(), "text": Text(), "input": Text()}
        self._setup_input_handler()

    def _setup_input_handler(self):
        if platform.system() == "Windows":
            import msvcrt
            self._kbhit = msvcrt.kbhit
            self._getch = lambda: msvcrt.getch().decode('latin-1', 'ignore')
        else:
            import termios, tty, select
            def unix_getch():
                fd = sys.stdin.fileno()
                old = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    return sys.stdin.read(1) if select.select([fd], [], [], 0)[0] else ''
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old)
            self._kbhit = lambda: select.select([sys.stdin], [], [], 0)[0]
            self._getch = unix_getch

    def _clear_screen(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def _show_banner(self):
        banner = textwrap.dedent("""
            ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████████████▓▒░
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
            ░▒▓███████▓▒░░▒▓██████▓▒░  ░▒▓██████▓▒░        ░▒▓██████▓▒░   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░                 ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
            ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░                 ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
            ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░  ░▒▓█▓▒░          ░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
        """).strip()
        self.console.print(banner, style="dark_blue")

    def _parse_duration(self, raw: str) -> int:
        raw = raw.lower().strip()
        try:
            if "min" in raw:
                return int(raw.replace("min", "")) * 60
            return int(raw.replace("s", "") if "s" in raw else raw)
        except ValueError:
            raise ValueError("Invalid duration format")

    def _validate_yes_no(self, prompt: str) -> str:
        while True:
            ans = input(prompt).strip().lower()
            if ans in ('y', 'yes', 'n', 'no'):
                return 'y' if ans.startswith('y') else 'n'
            self.console.print("[red]Enter 'y' or 'n'[/]")

    def get_settings(self) -> namedtuple:
        while True:
            self._clear_screen()
            self._show_banner()
            self.console.print("[bold white on black] TYPING TEST SETTINGS [/]\n")
            try:
                duration = self._parse_duration(input("Test duration (30s 60s 90s 120s): "))
                use_specials = self._validate_yes_no("Include special characters? (y or n): ")
                use_numbers = self._validate_yes_no("Include numbers? (y or n): ")
                self._clear_screen()
                self._show_banner()
                return self.Settings(duration, use_numbers, use_specials)
            except ValueError:
                self.console.print("[red]Invalid input. Try again.[/]")
                time.sleep(1.5)

    def generate_text(self, use_numbers: str, use_specials: str) -> str:
        total_words = 80
        num_numbers = max(3, total_words // 10) if use_numbers == 'y' else 0
        num_specials = max(3, total_words // 10) if use_specials == 'y' else 0
        num_common = total_words - num_numbers - num_specials

        words = random.choices(self.word_bank['common'], k=num_common)
        if num_numbers:
            words.extend(random.choices(self.word_bank['numbers'], k=num_numbers))
        if num_specials:
            words.extend(random.choices(self.word_bank['specials'], k=num_specials))

        random.shuffle(words)
        return " ".join(words)

    def get_colored_input(self, typed: str, reference: str, animated_index: int = None) -> Text:
        result = Text()
        for i, char in enumerate(typed):
            ref_char = reference[i] if i < len(reference) else ""
            style = "green" if char.lower() == ref_char.lower() else "red"
            display_char = char.upper() if i == animated_index else char.lower()
            result.append(display_char, style=style)
        result.append("_", style="bold white")
        return result

    def get_display(self) -> Panel:
        return Panel(
            Text.assemble("\n", self.display['timer'], "\n\n", self.display['text'], "\n\n", self.display['input']),
            width=84, style="on black"
        )

    def show_results(self, typed: str, reference: str, duration: int):
        typed = typed[:len(reference)]
        correct = sum(t.lower() == r.lower() for t, r in zip(typed, reference))
        accuracy = (correct / max(1, len(typed))) * 100
        wpm = (correct / 5) / (duration / 60)
        self.console.print(Panel(
            f"[bold white]TEST RESULTS[/]\n\nDuration: {duration}s\nAccuracy: {accuracy:.1f}%\nSpeed: {wpm:.1f} WPM\nTyped: {len(typed)}/{len(reference)}",
            width=50, style="on black"
        ))

    def run_test(self):
        settings = self.get_settings()
        test_text = self.generate_text(settings.use_numbers, settings.use_specials)

        self.display['text'] = Text(textwrap.fill(test_text, 80), style="white")
        self.display['timer'] = Text()
        self.display['input'] = Text("_", style="bold white")

        input("\nPress Enter to start...")

        start_time = time.time()
        end_time = start_time + settings.duration
        input_buffer = []
        last_index = -1
        last_time = start_time

        with Live(self.get_display(), refresh_per_second=30, transient=True) as live:
            while time.time() < end_time:
                self.display['timer'] = Text(f"Time remaining: {int(end_time - time.time())}s", style="bold white")

                if self._kbhit():
                    char = self._getch()
                    if char == '\x1b':
                        break
                    elif char in ('\x08', '\x7f'):
                        if input_buffer:
                            input_buffer.pop()
                            last_index = len(input_buffer) - 1
                            last_time = time.time()
                    elif char.isprintable():
                        input_buffer.append(char)
                        last_index = len(input_buffer) - 1
                        last_time = time.time()

                anim_index = last_index if time.time() - last_time < 0.1 else None
                self.display['input'] = self.get_colored_input(''.join(input_buffer), test_text, anim_index)
                live.update(self.get_display())
                time.sleep(0.01)

        self.show_results(''.join(input_buffer), test_text, settings.duration)

if __name__ == "__main__":
    while True:
        TypingTest().run_test()
        again = input("\nRepeat the test? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            break
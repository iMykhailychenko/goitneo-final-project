from prompt_toolkit.completion import Completer, Completion
from core import Actions

class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor()

        completions = [
            Completion(action.value, -len(word_before_cursor),)
            for action in Actions
            if action.value.startswith(word_before_cursor)
        ]

        for completion in completions:
            yield completion
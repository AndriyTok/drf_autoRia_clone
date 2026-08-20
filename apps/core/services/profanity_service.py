# to be updated with regex later
class ProfanityService:
    PROFANITY_WORDS = set()

    @classmethod
    def contains_profanity(cls, text: str) -> bool:
        text = text.lower()

        return any(
            word in text
            for word in cls.PROFANITY_WORDS
        )
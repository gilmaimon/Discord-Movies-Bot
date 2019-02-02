# Will search thru a list of providers and will stop on the first non-None result
class MultipleSourcesProvider:
    def __init__(self, providers):
        self.providers = providers

    async def search_subtitles(self, movie):
        for provider in self.providers:
            subs = await provider.search_subtitles(movie)
            if subs: return subs
        return None
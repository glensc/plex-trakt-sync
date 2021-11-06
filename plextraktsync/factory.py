from plextraktsync.decorators.deprecated import deprecated
from plextraktsync.decorators.memoize import memoize


class Factory:
    @memoize
    def trakt_api(self, batch_size=None):
        from plextraktsync.trakt_api import TraktApi

        trakt = TraktApi(batch_size=batch_size)

        return trakt

    @memoize
    def plex_api(self):
        from plextraktsync.plex_api import PlexApi

        server = self.plex_server()
        plex = PlexApi(server)

        return plex

    @memoize
    def media_factory(self, batch_size=None):
        from plextraktsync.media import MediaFactory

        trakt = self.trakt_api(batch_size=batch_size)
        plex = self.plex_api()
        mf = MediaFactory(plex, trakt)

        return mf

    @memoize
    def plex_server(self):
        from plextraktsync.plex_server import get_plex_server

        return get_plex_server()

    @memoize
    def session(self):
        from requests_cache import CachedSession

        config = self.config()
        trakt_cache = config["cache"]["path"]
        session = CachedSession(trakt_cache)

        return session

    @memoize
    @deprecated("Use session instead")
    def requests_cache(self):
        import requests_cache

        config = self.config()
        trakt_cache = config["cache"]["path"]

        requests_cache.install_cache(trakt_cache)

        return requests_cache

    @memoize
    def sync(self):
        from plextraktsync.sync import Sync

        config = self.config()

        return Sync(config)

    @memoize
    def progressbar(self, enabled=True):
        if enabled:
            import warnings
            from tqdm import TqdmExperimentalWarning
            from tqdm.rich import tqdm

            warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)

            return tqdm

        return None

    @memoize
    def config(self):
        from plextraktsync.config import CONFIG

        return CONFIG


factory = Factory()

# sharing monitor

from share_getter import ShareGetter

class ShareMonitor(object):
    def __init__(self):
        self.links_to_check = self.get_links()
        self.run_monitor()
    def run_monitor(self):
        sh = StatsGetter(self.links_to_check)
        counts = sh.get_stats()
        self.save_results(counts)
    def save_results(self, counts):
        for result in counts:
            #save to database
            pass
    
    def get_links(self):
        return ['http://www.gazeta.pl/', 'http://www.petycje.pl']

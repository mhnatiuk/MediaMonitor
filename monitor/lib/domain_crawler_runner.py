import link_getter


#job runner
class DomainCrawlerRunner(object):
    def __init__(self):
        self.domains = self.get_domain_uris()
    def get_domain_uris(self):
        """ connect to database and retrieve monitored domains """
        pass
    def get_monitored_domains(self):
        for domain in self.domains:
            getter = link_getter.LinkGetter(domain)
            links = getter.run()
            new_links = self.get_new_links(links)
            self.save_new_links(new_links)
            self.delete_expired_links()
    def get_new_links(self, links):
        all_links = self.get_all_links()
        pass
    def get_all_links_from_db(self):
        """ gets all links that are currently in the database """
        links = set()
        pass
    def save_new_links(self, new_links):
        """ saves all new links into the database with inherited domian's TTL  """
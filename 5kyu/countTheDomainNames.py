def count_domains(domains, min_hits=0):
	#build a list of lists with domain names split by a dot
    get_domains = [domain.split('.') for domain in domains.split()[::2]]
    #join the domians back but without the text noise
    glue_the_domains = ['.'.join(domain[-3:] if domain[-2] in ['com','co'] else domain[-2:]) for domain in get_domains]
    #extract number of hits per domain
    get_hits = [int(h) for h in domains.split()[1::2]]
    
    #set up a dictionary that's going to store domains and hits
    doms_and_hits = {}
    #zip the domains with respecitve number of hits, adding them up on the fly
    for domain, hit in zip(glue_the_domains, get_hits):
        doms_and_hits[domain] = doms_and_hits.get(domain, 0) + hit

    #join a representation of the dictionary and sort it in a descending order
    return '\n'.join('{} ({})'.format(domain, abs(hit)) for hit, domain in sorted((-hit,domain) for domain,hit in doms_and_hits.items() if hit >= min_hits))
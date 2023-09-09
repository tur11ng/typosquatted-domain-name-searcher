import itertools

import homoglyphs as hg
import validators


class Generator:
    @staticmethod
    def generate(domain_name: str):
        tld = domain_name[domain_name.rfind('.'):]
        domain_name = domain_name[:domain_name.rfind('.')]

        letters_homoglyphs = []

        for letter in domain_name:
            if letter == '.':
                letters_homoglyphs += '.'
                continue
            letters_homoglyphs += [hg.Homoglyphs().get_combinations(letter)]

        for typosquatted_domain_name in itertools.product(*letters_homoglyphs):
            typosquatted_domain_name_str = ''.join(typosquatted_domain_name) + tld
            if validators.domain(typosquatted_domain_name_str):
                yield typosquatted_domain_name_str

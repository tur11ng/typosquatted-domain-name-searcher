from typing import List

from checker import Checker
from comparator import Comparator
from generator import Generator


class Searcher:
    @staticmethod
    async def search_unregistered_typosquatted_domain_names(domain_name: str,
                                                      evaluate=False):
        for typosquatted_domain_name in Generator.generate(domain_name):
            if not Checker.is_domain_name_registered(typosquatted_domain_name):
                if evaluate:
                    score = await Comparator.compare_domain_names(domain_name, typosquatted_domain_name)
                    yield {typosquatted_domain_name: score}
                else:
                    yield typosquatted_domain_name
